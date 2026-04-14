function onClickEyeIcon() {
    var password = document.getElementById("password");
    var eyebox = document.getElementById("eye-box");
    // Optional: if you want to change the icon image specifically
    var eyeIcon = document.querySelector(".eye");

    if (password.type === "password") {
        password.type = "text";
        eyebox.style.opacity = "0.5"; // Dim it or change icon
    } else {
        password.type = "password";
        eyebox.style.opacity = "1"; // Standard full opacity
    }
}

function forgotPass() {
    alert("Please contact the administrator to reset your password.");
}
