function initRegisterForm() {
  const form = document.getElementById('register-form');
  const summarySection = document.getElementById('register-summary');
  const summaryContent = document.getElementById('summary-content');
  const summaryActions = document.getElementById('summary-actions');

  if (!form || !summarySection || !summaryContent) return;

  function setFieldError(fieldId, message) {
    const errorEl = document.querySelector(`.field-error[data-for="${fieldId}"]`);
    if (errorEl) {
      errorEl.textContent = message || '';
    }
  }

  function clearAllErrors() {
    document.querySelectorAll('.field-error').forEach((el) => {
      el.textContent = '';
    });
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    clearAllErrors();

    let hasError = false;

    const firstName = form.firstName.value.trim();
    const lastName = form.lastName.value.trim();
    const email = form.email.value.trim();
    const password = form.password.value;
    const passwordConfirm = form.passwordConfirm.value;
    const level = form.level.value;

    const pwHint = document.getElementById('password-hint');

    if (!firstName) {
      setFieldError('first-name', 'Συμπλήρωσε το όνομά σου.');
      hasError = true;
    }

    if (!lastName) {
      setFieldError('last-name', 'Συμπλήρωσε το επώνυμό σου.');
      hasError = true;
    }

    if (!email) {
      setFieldError('email', 'Συμπλήρωσε το email.');
      hasError = true;
    } else if (!email.includes('@')) {
      setFieldError('email', 'Το email δεν είναι έγκυρο.');
      hasError = true;
    }

    if (!password) {
      setFieldError('password', 'Συμπλήρωσε έναν κωδικό.');
      if (pwHint) pwHint.style.display = 'none';
      hasError = true;
    } else if (password.length < 8) {
      setFieldError('password', 'Ο κωδικός πρέπει να έχει τουλάχιστον 8 χαρακτήρες.');
      if (pwHint) pwHint.style.display = 'block';
      hasError = true;
    } else {
      // έγκυρος κωδικός
      if (pwHint) pwHint.style.display = 'none';
    }

    // Επιβεβαίωση κωδικού
    if (!passwordConfirm) {
      setFieldError('password-confirm', 'Επιβεβαίωσε τον κωδικό σου.');
      hasError = true;
    } else if (passwordConfirm !== password) {
      setFieldError('password-confirm', 'Οι κωδικοί δεν ταιριάζουν.');
      hasError = true;
    }

    // Επίπεδο γνώσεων (radio)
    if (!level) {
      const levelError = document.querySelector('.field-error[data-for="level"]');
      if (levelError) {
        levelError.textContent = 'Επίλεξε επίπεδο γνώσεων.';
      }
      hasError = true;
    }

    if (hasError) {
      summarySection.hidden = true;
      if (summaryActions) summaryActions.hidden = true;
      return;
    }

    // Αν όλα είναι εντάξει προχωράμε σην προεπισκόπηση

    const categories = Array.from(
      form.querySelectorAll('input[name="categories"]:checked')
    ).map((el) => el.nextSibling.textContent.trim());

    const preferredCourses = Array.from(
      form.querySelectorAll('input[name="courses[]"]:checked')
    ).map((el) => el.nextSibling.textContent.trim());

    summaryContent.innerHTML = `
      <p><strong>Όνομα:</strong> ${firstName} ${lastName}</p>
      <p><strong>Email:</strong> ${email}</p>
      <p><strong>Επίπεδο γνώσεων:</strong> ${level === 'beginner'
        ? 'Αρχάριος'
        : level === 'intermediate'
          ? 'Μέσο'
          : 'Προχωρημένο'
      }</p>
      <p><strong>Κατηγορίες ενδιαφέροντος:</strong> ${categories.length ? categories.join(', ') : 'Καμία επιλογή'
      }</p>
      <p><strong>Επιθυμητά μαθήματα:</strong> ${preferredCourses.length ? preferredCourses.join(', ') : 'Καμία επιλογή'
      }</p>
      <p>Παρακαλώ έλεγξε τα στοιχεία σου πριν την τελική υποβολή.</p>
    `;

    summarySection.hidden = false;
    summarySection.scrollIntoView({ behavior: 'smooth' });

    // Κουμπιά Υποβολή / Καθαρισμός
    if (summaryActions) {
      summaryActions.innerHTML = `
        <button type="button" id="final-submit" class="btn btn-primary">
          Υποβολή
        </button>
        <button type="button" id="reset-form" class="btn btn-secondary">
          Καθαρισμός
        </button>
      `;
      summaryActions.hidden = false;

      const finalSubmitBtn = document.getElementById('final-submit');
      const resetBtn = document.getElementById('reset-form');

      if (finalSubmitBtn) {
        finalSubmitBtn.addEventListener('click', () => {
          alert('Η εγγραφή ολοκληρώθηκε επιτυχώς!');
          form.reset();
          clearAllErrors();
          summarySection.hidden = true;
          summaryActions.hidden = true;
        });
      }

      if (resetBtn) {
        resetBtn.addEventListener('click', () => {
          form.reset();
          clearAllErrors();
          summarySection.hidden = true;
          summaryActions.hidden = true;
        });
      }
    }
  });
}

// κάνουμε τη συνάρτηση διαθέσιμη
window.initRegisterForm = initRegisterForm;
