document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navbarMenu = document.querySelector(".navbar-menu");

  menuToggle.addEventListener("click", function () {
    navbarMenu.classList.toggle("active");
  });

  const navbarLinks = document.querySelectorAll(".navbar-links a");
  const currentURL = window.location.pathname;

  navbarLinks.forEach(link => {
      const linkURL = link.getAttribute("href");

      if (currentURL === linkURL) {
          link.classList.add("active");
      }
  });
});
