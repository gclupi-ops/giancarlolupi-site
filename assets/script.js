const btn = document.querySelector('.menu-btn');
const nav = document.querySelector('.navlinks');
if(btn && nav){
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

// Il sito è personale: i contatti di prenotazione rimandano alle sedi private,
// mentre le appartenenze istituzionali sono riportate soltanto nel profilo professionale.
const isArticle = window.location.pathname.includes('/approfondimenti/');
const sediHref = isArticle ? '../sedi.html' : 'sedi.html';
document.querySelectorAll('a[href="mailto:g.lupi@ao-pisa.toscana.it"]').forEach(a => {
  const p = a.closest('p');
  if (p) p.innerHTML = `<a href="${sediHref}">Sedi e prenotazioni</a><br>Pisa · Ponsacco · Massa`;
});

document.querySelectorAll('.article-author span, .editorial-byline span, .editorial-signature small').forEach(el => {
  if (el.textContent.includes('AOUP')) el.textContent = 'Neurochirurgo';
});

document.querySelectorAll('.footer-bottom').forEach(el => {
  const spans = el.querySelectorAll('span');
  if (spans.length > 1) spans[spans.length - 1].textContent = 'Sito professionale personale · indipendente dalle strutture presso cui viene svolta attività clinica';
});
