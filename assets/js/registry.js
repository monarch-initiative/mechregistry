/* Filter and search the Mech table on the home page.
   The table is rendered by Liquid from site.mechs; this only hides rows. */
(function () {
  'use strict';
  var rows = Array.prototype.slice.call(document.querySelectorAll('#mech-table tbody tr'));
  if (!rows.length) return;

  function values(attr) {
    var seen = {};
    rows.forEach(function (r) {
      (r.getAttribute(attr) || '').split('|').forEach(function (v) {
        if (v) seen[v] = true;
      });
    });
    return Object.keys(seen).sort();
  }

  function fill(selectId, attr) {
    var sel = document.getElementById(selectId);
    values(attr).forEach(function (v) {
      var opt = document.createElement('option');
      opt.value = v;
      opt.textContent = v;
      sel.appendChild(opt);
    });
    sel.addEventListener('change', apply);
    return sel;
  }

  var fDomain = fill('f-domain', 'data-domains');
  var fCollection = fill('f-collection', 'data-collections');
  var fStatus = fill('f-status', 'data-status');
  var fMaturity = fill('f-maturity', 'data-maturity');
  var fOntology = fill('f-ontology', 'data-ontologies');
  var fSearch = document.getElementById('f-search');
  fSearch.addEventListener('input', apply);
  var count = document.getElementById('mech-count');

  function has(row, attr, v) {
    if (!v) return true;
    return (row.getAttribute(attr) || '').split('|').indexOf(v) !== -1;
  }

  function apply() {
    var q = (fSearch.value || '').trim().toLowerCase();
    var shown = 0;
    rows.forEach(function (r) {
      var ok = has(r, 'data-domains', fDomain.value)
        && has(r, 'data-collections', fCollection.value)
        && has(r, 'data-status', fStatus.value)
        && has(r, 'data-maturity', fMaturity.value)
        && has(r, 'data-ontologies', fOntology.value)
        && (!q || (r.getAttribute('data-search') || '').toLowerCase().indexOf(q) !== -1);
      r.style.display = ok ? '' : 'none';
      if (ok) shown++;
    });
    count.textContent = shown + ' of ' + rows.length + ' Mechs shown';
  }

  // Allow ?collection=x-mech-suite etc. in the URL.
  var params = new URLSearchParams(window.location.search);
  [['domain', fDomain], ['collection', fCollection], ['status', fStatus], ['maturity', fMaturity], ['ontology', fOntology]]
    .forEach(function (pair) {
      var v = params.get(pair[0]);
      if (v) pair[1].value = v;
    });
  if (params.get('q')) fSearch.value = params.get('q');
  apply();
})();
