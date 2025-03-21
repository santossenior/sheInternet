document.getElementById('volunteer-form').addEventListener('submit', function (event) {
    event.preventDefault();  // Prevent default form submission

    // Get form data
    const formData = {
        name: document.getElementById('lname').value,
        phone: document.getElementById('lphone').value,
        email: document.getElementById('lemail').value,
        contribution: document.querySelector('input[name="contribution"]:checked')?.value || '',
        time_commitment: document.querySelector('input[name="time_commitment"]:checked')?.value || '',
        message: document.getElementById('message').value,
    };

    console.log("Form Data:", formData);  // Debugging

    // Get CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send data via AJAX
    fetch('/submit-volunteer-form/', {  // Replace with your Django URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('volunteer-message');
        messageDiv.style.display = 'block';

        if (data.status === 'success') {
            messageDiv.innerHTML = `
                <div class="volunteer-alert volunteer-alert-success">
                    ${data.message}
                    <button type="button" class="volunteer-close" data-dismiss="alert">&times;</button>
                </div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="volunteer-alert volunteer-alert-error">
                    ${data.message}
                    <button type="button" class="volunteer-close" data-dismiss="alert">&times;</button>
                </div>
            `;
        }

        // Clear form fields
        document.getElementById('volunteer-form').reset();
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Add event listener to dismiss messages
document.addEventListener('click', function (event) {
    if (event.target.classList.contains('volunteer-close')) {
        event.target.parentElement.style.display = 'none';
    }
});