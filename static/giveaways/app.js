document.addEventListener("DOMContentLoaded", () => {
  // Confirm irreversible or important actions before submitting.
  document.querySelectorAll("form[data-confirm]").forEach((form) => {
    form.addEventListener("submit", (event) => {
      const message = form.dataset.confirm || "Are you sure?";
      if (!window.confirm(message)) event.preventDefault();
    });
  });

  // Disable submit buttons after a valid submit to reduce accidental double-clicks.
  document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", () => {
      if (!form.checkValidity()) return;
      const button = form.querySelector('button[type="submit"], button:not([type])');
      if (button && !form.dataset.confirm) {
        button.dataset.originalText = button.textContent;
        button.textContent = "Please wait…";
        button.disabled = true;
      }
    });
  });
});
