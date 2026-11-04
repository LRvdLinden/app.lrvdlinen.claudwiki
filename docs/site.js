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
      html += '<a href="' + window.PREFIX + 'adviseur/?q=' + encodeURIComponent(input.value.trim()) + '"><strong>Vraag de Skill-adviseur →</strong><span>Beschrijf wat je wilt en krijg de beste skill</span></a>';
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
