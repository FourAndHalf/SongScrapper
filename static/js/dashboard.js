document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const navbar = document.getElementById("navbar");

    let isOpen = false;

    menuIcon.addEventListener("click", function () {
        if (!isOpen) {
            gsap.to("#navbar", { right: 0, duration: 0.5, ease: "power2.out" });
        } else {
            gsap.to("#navbar", { right: "-250px", duration: 0.5, ease: "power2.in" });
        }
        isOpen = !isOpen;
    });
});
