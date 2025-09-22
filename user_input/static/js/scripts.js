// script.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("JS Loaded ✅");

    // Confirm before removing a user
    const deleteLinks = document.querySelectorAll("a.delete-link");
    deleteLinks.forEach(link => {
        link.addEventListener("click", (event) => {
            if (!confirm("Are you sure you want to delete this user?")) {
                event.preventDefault();
            }
        });
    });
});
