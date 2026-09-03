
const btn = document.querySelector('.menu-btn');
const nav = document.querySelector('.navlinks');
if(btn && nav){
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}
document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
