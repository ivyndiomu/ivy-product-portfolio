(function () {
  const config = window.IVY_SITE_CONFIG || {};
  const $ = (selector, scope = document) => scope.querySelector(selector);
  const $$ = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));

  const menuButton = $('.nav-toggle');
  const nav = $('.site-nav');
  if (menuButton && nav) {
    menuButton.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      menuButton.setAttribute('aria-expanded', String(open));
    });
  }

  $$('.js-name').forEach(el => { el.textContent = config.fullName || config.name || 'Ivy'; });
  $$('.js-role').forEach(el => { el.textContent = config.role || 'Product Manager'; });

  const contactLinks = [
    ['.js-email-link', config.email ? `mailto:${config.email}` : ''],
    ['.js-linkedin-link', config.linkedin || ''],
    ['.js-github-link', config.github || ''],
    ['.js-resume-link', config.resumeUrl || '']
  ];

  contactLinks.forEach(([selector, href]) => {
    $$(selector).forEach(el => {
      if (href) {
        el.href = href;
        el.hidden = false;
      } else {
        el.hidden = true;
      }
    });
  });

  const emptyContact = $('.js-contact-empty');
  if (emptyContact) {
    emptyContact.hidden = Boolean(config.email || config.linkedin);
  }

  const year = $('.js-year');
  if (year) year.textContent = new Date().getFullYear();

  const progress = $('.reading-progress');
  if (progress) {
    const updateProgress = () => {
      const root = document.documentElement;
      const max = root.scrollHeight - root.clientHeight;
      const pct = max > 0 ? (root.scrollTop / max) * 100 : 0;
      progress.style.width = `${Math.min(100, Math.max(0, pct))}%`;
    };
    document.addEventListener('scroll', updateProgress, { passive: true });
    updateProgress();
  }

  const observer = 'IntersectionObserver' in window ? new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 }) : null;

  $$('.reveal').forEach(el => {
    if (observer) observer.observe(el);
    else el.classList.add('revealed');
  });
})();
