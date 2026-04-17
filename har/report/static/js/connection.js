function onClickEyeIcon() {
    var password = document.getElementById("password");
    var eyebox = document.getElementById("eye-box");
    // Optional: if you want to change the icon image specifically
    var eyeIcon = document.querySelector(".eye");

    if (password.type === "password") {
        password.type = "text";
        eyebox.style.opacity = "0.5"; // Dim it slightly to indicate state
        if (eyeIcon) {
            // When password becomes visible, show the plain eye (no slash)
            if (eyeIcon.src && eyeIcon.src.indexOf('ic_eye_slash.png') !== -1) {
                eyeIcon.src = eyeIcon.src.replace('ic_eye_slash.png', 'ic_eye.png');
            } else if (eyeIcon.getAttribute('data-eye')) {
                eyeIcon.src = eyeIcon.getAttribute('data-eye');
            }
            eyeIcon.setAttribute('aria-pressed','true');
        }
    } else {
        password.type = "password";
        eyebox.style.opacity = "1"; // Standard full opacity
        if (eyeIcon) {
            // When password is hidden, show the slashed eye
            if (eyeIcon.src && eyeIcon.src.indexOf('ic_eye.png') !== -1) {
                eyeIcon.src = eyeIcon.src.replace('ic_eye.png', 'ic_eye_slash.png');
            } else if (eyeIcon.getAttribute('data-eye-slash')) {
                eyeIcon.src = eyeIcon.getAttribute('data-eye-slash');
            }
            eyeIcon.setAttribute('aria-pressed','false');
        }
    }
}

function forgotPass() {
    alert("Please contact the administrator to reset your password.");
}
