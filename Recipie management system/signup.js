// signup.js
document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent form from submitting the default way

    const username = document.getElementById('username').value;
    const Email = document.getElementById('E-mail').value;
    const password = document.getElementById('pass').value;
    const gender = document.getElementById('gender').value;

    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'signup.php', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById('message').textContent = xhr.responseText;
        }
    };

    // Sending the form data
    xhr.send(`username=${username} & E-mail=${Email}&pass=${password}&gender=${gender}`);
});
