function initCoursesPage() {
  const grid = document.getElementById('courses-grid');

  if (!grid || !window.courses) {
    return;
  }

  const selectCategory = document.getElementById('filter-category');
  const selectLevel = document.getElementById('filter-level');

  // διαβάζουμε το ?category=... από το URL
  const params = new URLSearchParams(window.location.search);
  const initialCategory = params.get('category') || '';

  function renderCourses() {
    const categoryFilter = selectCategory ? selectCategory.value : '';
    const levelFilter = selectLevel ? selectLevel.value : '';

    grid.innerHTML = '';

    window.courses
      .filter((course) => {
        const matchCategory =
          !categoryFilter || course.category === categoryFilter;
        const matchLevel =
          !levelFilter || course.level === levelFilter;
        return matchCategory && matchLevel;
      })
      .forEach((course) => {
        const article = document.createElement('article');
        article.className = 'card course-card';

        article.innerHTML = `
          <img src="${course.image}" alt="${course.title}" class="card-thumb">
          <h3 class="card-title">${course.title}</h3>
          <p class="card-meta">
            Κατηγορία: ${course.categoryLabel} · Επίπεδο: ${course.levelLabel}
          </p>
          <p>${course.shortDescription}</p>
          <a href="course-details.html?id=${course.id}" class="btn btn-sm">Περισσότερα</a>
        `;

        grid.appendChild(article);
      });
  }

  // αν ήρθαμε με ?category=..., ρύθμισε το select πριν το πρώτο render
  if (selectCategory && initialCategory) {
    // βεβαιώσου ότι υπάρχει τέτοια option
    const optionExists = Array.from(selectCategory.options).some(
      (opt) => opt.value === initialCategory
    );
    if (optionExists) {
      selectCategory.value = initialCategory;
    }
  }

  if (selectCategory) {
    selectCategory.addEventListener('change', renderCourses);
  }
  if (selectLevel) {
    selectLevel.addEventListener('change', renderCourses);
  }

  // αρχικό render
  renderCourses();
}


function initCourseDetailsPage() {

  if (!window.courses) return;

  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');

  const courseDetailsEl = document.getElementById('course-details');
  const notFoundEl = document.getElementById('course-not-found');

  if (!id || !courseDetailsEl) return;

  const course = window.courses.find((c) => c.id === id);

  if (!course) {
    // Δείξε μήνυμα "δεν βρέθηκε"
    if (courseDetailsEl) courseDetailsEl.hidden = true;
    if (notFoundEl) notFoundEl.hidden = false;
    return;
  }

  const titleEl = document.getElementById('course-title');
  const metaEl = document.getElementById('course-meta');
  const descEl = document.getElementById('course-description');
  const imgEl = document.getElementById('course-image');
  const booksSection = document.getElementById('course-books-section');
  const booksList = document.getElementById('course-books');
  const videosSection = document.getElementById('course-videos-section');
  const videosList = document.getElementById('course-videos');

  if (titleEl) titleEl.textContent = course.title;
  document.title = `${course.title} | CS4All Academy`;

  if (metaEl) {
    metaEl.textContent = `Κατηγορία: ${course.categoryLabel} · Επίπεδο: ${course.levelLabel}`;
  }
  if (descEl) {
    descEl.textContent = course.description || course.shortDescription || '';
  }
  if (imgEl) {
    imgEl.src = course.image;
    imgEl.alt = course.title;
  }

  // Βιβλία
  if (course.books && course.books.length && booksSection && booksList) {
    booksList.innerHTML = '';
    course.books.forEach((book) => {
      const li = document.createElement('li');

      // book.title και book.url
      li.innerHTML = `<a href="${book.url}" target="_blank" rel="noopener"> ${book.title} </a> `;

      booksList.appendChild(li);
    });

    booksSection.hidden = false;
  }

  // Video
  if (course.videos && course.videos.length && videosSection && videosList) {
    videosList.innerHTML = '';
    course.videos.forEach((video) => {
      const li = document.createElement('li');
      li.innerHTML = `<a href="${video.url}" target="_blank" rel="noopener">${video.title}</a>`;
      videosList.appendChild(li);
    });
    videosSection.hidden = false;
  }
}

function initBooksPage() {
  const container = document.getElementById('books-list');
  const allCourses = window.courses;

  if (!container || !allCourses) return;

  container.innerHTML = '';

  allCourses.forEach((course) => {
    if (!course.books || !course.books.length) return;

    const section = document.createElement('section');
    section.className = 'books-section';

    const itemsHtml = course.books
      .map((book) => {
        /* 
         if (typeof book === 'string') {
           return `<li>${book}</li>`;
         }
        */
        // Αν είναι object { title, url }
        const title = book.title || '';
        const url = book.url || '';

        if (url) {
          return `
            <li>
              <a href="${url}" target="_blank" rel="noopener">
                ${title}
              </a>
            </li>
          `;
        } else {
          return `<li>${title}</li>`;
        }
      })
      .join('');

    section.innerHTML = `
      <h2>${course.title}</h2>
      <ul class="books-list">
        ${itemsHtml}
      </ul>
    `;

    container.appendChild(section);
  });
}



document.addEventListener('DOMContentLoaded', function () {
  if (window.initMainMenu) {
    window.initMainMenu();
  }

  if (document.body.classList.contains('page-courses')) {
    initCoursesPage();
  }

  if (document.body.classList.contains('page-course-details')) {
    initCourseDetailsPage();
  }

  if (document.body.classList.contains('page-books')) {
    initBooksPage();
  }
  if (document.body.classList.contains('page-register') && window.initRegisterForm) {
    window.initRegisterForm();
  }
});


