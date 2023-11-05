document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");

  menuToggle.addEventListener("click", function () {
    navbarMenu.classList.toggle("active");
  });
});
