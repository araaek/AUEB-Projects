function initMainMenu() {
  const navToggle = document.querySelector('.nav-toggle');
  const nav = document.getElementById('main-nav');

  if (!navToggle || !nav) {
    return;
  }

  // Αρχική κατάσταση
  navToggle.setAttribute('aria-expanded', 'false');

  function toggleMenu() {
    const isOpen = nav.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  }

  navToggle.addEventListener('click', toggleMenu);

  // κλείσιμο όταν πατάω κάποιο link του μενού
  const navLinks = nav.querySelectorAll('a');
  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      if (nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });
  });
}

window.initMainMenu = initMainMenu;
