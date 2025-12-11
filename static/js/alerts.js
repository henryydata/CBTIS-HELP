document.addEventListener("DOMContentLoaded", function () {
    const djangoMessages = JSON.parse(
        document.getElementById("django-messages")?.textContent || "[]"
    );

    if (djangoMessages.length > 0) {
        djangoMessages.forEach(msg => {
            Swal.fire({
                icon: msg.tags.includes("success") ? "success" :
                      msg.tags.includes("error") ? "error" : "info",
                title: msg.message,
                timer: 2500,
                timerProgressBar: true,
                showConfirmButton: false
            });
        });
    }
});
