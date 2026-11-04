(function () {
  // tabs
  document.querySelectorAll('.tabs').forEach(function (t) {
    var btns = t.querySelectorAll(':scope > .tablist button'), panes = t.querySelectorAll(':scope > .pane');
    btns.forEach(function (b, i) {
      b.addEventListener('click', function () {
        btns.forEach(function (x, j) { x.setAttribute('aria-selected', String(i === j)); panes[j].hidden = i !== j; });
      });
    });
  });
  // taalkeuze onthouden
  document.querySelectorAll('a.lang').forEach(function (a) {
    a.addEventListener('click', function () { try { localStorage.setItem('cw-lang', a.getAttribute('data-lang')); } catch (e) {} });
  });
  // menu
  var menu = document.querySelector('.menu');
  if (menu) menu.addEventListener('click', function () {
    var open = document.body.classList.toggle('nav-open'); menu.setAttribute('aria-expanded', String(open));
  });
  var on = document.querySelector('.side a.on'); if (on) on.scrollIntoView({ block: 'center' });
  // zoeken
  var input = document.getElementById('s'), box = document.querySelector('.sres'), idx = null, sel = -1;
  if (!input) return;
  function norm(s) { return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function load() {
    if (idx) return Promise.resolve(idx);
    return fetch(window.PREFIX + 'search.json').then(function (r) { return r.json(); }).then(function (d) {
      idx = d.map(function (p) { return { p: p, t: norm(p.t), d: norm(p.d), x: norm(p.x) }; }); return idx;
    });
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function run() {
    var q = norm(input.value.trim());
    if (q.length < 2) { box.hidden = true; return; }
    load().then(function (I) {
      var w = q.split(/\s+/);
      var res = I.map(function (e) {
        var s = 0;
        w.forEach(function (t) { if (e.t.indexOf(t) > -1) s += 5; if (e.d.indexOf(t) > -1) s += 2; if (e.x.indexOf(t) > -1) s += 1; });
        return { e: e, s: s };
      }).filter(function (r) { return r.s > 0; }).sort(function (a, b) { return b.s - a.s; }).slice(0, 8);
      var html = res.map(function (r) { return '<a href="' + window.PREFIX + r.e.p.u + '"><strong>' + esc(r.e.p.t) + '</strong><span>' + esc(r.e.p.d) + '</span></a>'; }).join('');
      html += '<a href="' + window.PREFIX + 'adviseur/?q=' + encodeURIComponent(input.value.trim()) + '"><strong>' + esc(window.UI.ask) + '</strong><span>' + esc(window.UI.asksub) + '</span></a>';
      box.innerHTML = html; box.hidden = false; sel = -1;
    });
  }
  input.addEventListener('input', run);
  input.addEventListener('focus', function () { load(); if (input.value) run(); });
  input.addEventListener('keydown', function (e) {
    var a = box.querySelectorAll('a'); if (!a.length) return;
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault(); sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + a.length) % a.length;
      a.forEach(function (x, i) { x.classList.toggle('sel', i === sel); });
    } else if (e.key === 'Enter') { e.preventDefault(); (a[sel > -1 ? sel : 0]).click(); }
    else if (e.key === 'Escape') { box.hidden = true; }
  });
  document.querySelector('.search').addEventListener('submit', function (e) { e.preventDefault(); });
  document.addEventListener('click', function (e) { if (!e.target.closest('.search')) box.hidden = true; });
  document.addEventListener('keydown', function (e) { if ((e.metaKey || e.ctrlKey) && e.key === 'k') { e.preventDefault(); input.focus(); } });
})();

// Terminal-animatie
(function () {
  var el = document.querySelector('.term[data-scenes]');
  if (!el) return;
  var body = el.querySelector('.term-body');
  var scenes; try { scenes = JSON.parse(el.getAttribute('data-scenes')); } catch (e) { return; }
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return; // statische eindstand blijft staan
  var SPIN = ['✶', '✸', '✹', '✺', '✹', '✷'];
  function sleep(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function line(cls) { var s = document.createElement('span'); s.className = 'term-line ' + (cls || ''); body.appendChild(s); return s; }
  async function type(span, text, speed) {
    var cur = document.createElement('span'); cur.className = 'cursor'; span.appendChild(cur);
    for (var i = 0; i < text.length; i++) { cur.before(text[i]); await sleep(speed + Math.random() * speed); }
    cur.remove();
  }
  async function spin(label, ms) {
    var s = line('t-spin'), t0 = Date.now(), i = 0;
    while (Date.now() - t0 < ms) { s.textContent = SPIN[i++ % SPIN.length] + ' ' + label; await sleep(110); }
    s.remove();
  }
  async function play() {
    for (;;) {
      for (var k = 0; k < scenes.length; k++) {
        var sc = scenes[k];
        body.innerHTML = '';
        for (var j = 0; j < sc.length; j++) {
          var st = sc[j];
          if (st.type) { var l = line(st.cls); if (st.pre) { var p = document.createElement('span'); p.className = 't-acc'; p.textContent = st.pre; l.appendChild(p); } await type(l, st.type, 28); await sleep(350); }
          else if (st.spin) { await spin(st.spin, st.ms || 1200); }
          else { var o = line(st.cls); o.textContent = st.out; await sleep(st.ms || 260); }
        }
        await sleep(2600);
      }
    }
  }
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (en) { if (en[0].isIntersecting) { io.disconnect(); play(); } }) : null;
  if (io) io.observe(el); else play();
})();
