document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    // Normally, you would check credentials here
    window.location.href = '/dashboard';
});

document.getElementById('sign-up-link').addEventListener('click', function(event) {
    event.preventDefault();
    alert('Sign-up functionality is not implemented in this example.');
});
