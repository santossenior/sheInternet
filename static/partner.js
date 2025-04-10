const partnerFormElement = document.getElementById('partnerForm');

function closePartnerForm() {
    console.log('closeForm() called'); // Debugging
    if (partnerFormElement) {
        partnerFormElement.style.display = 'none'; // Hide the form container
    } else {
        console.error('Form container not found!'); // Debugging
    }
}

const partnerForm = document.querySelector('.partner_form');
if (partnerForm) {
    partnerForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

    // Get form data
    const formData = {
        name: document.getElementById('pname').value,
        organization: document.getElementById('porganization').value,
        email: document.getElementById('pemail').value,
        message: document.getElementById('pmessage').value,
    };

    console.log("Form Data:", formData); // Debugging

    // Get CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send data via AJAX
    fetch('/submit-partner-form/', { // Replace with your Django URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('partner-message');
        messageDiv.style.display = 'block';

        if (data.status === 'success') {
            messageDiv.innerHTML = `
                <div class="partner-alert partner-alert-success">
                    ${data.message}
                    <button type="button" class="partner-close" data-dismiss="alert">&times;</button>
                </div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="partner-alert partner-alert-error">
                    ${data.message}
                    <button type="button" class="partner-close" data-dismiss="alert">&times;</button>
                </div>
            `;
        }

        // Clear form fields and close the form immediately
        document.getElementById('partnerFormFields').reset(); // Reset form fields
        closePartnerForm(); // Close the form

        // Hide the message after 7 seconds
        setTimeout(() => {
            messageDiv.style.display = 'none';
        }, 7000); // Hide after 7 seconds
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Add event listener to dismiss messages
document.addEventListener('click', function (event) {
    if (event.target.classList.contains('partner-close')) {
        event.target.parentElement.style.display = 'none';
    }
});
}
    