const CommunityForm = document.getElementById('joinForm');
console.log("This is the community", CommunityForm);

// Function to close the form
function closeJoinForm() {
    console.log('closeJoinForm() called'); // Debugging
    if (CommunityForm) {
        CommunityForm.style.display = 'none'; // Hide the form container
    } else {
        console.error('Form container not found!'); // Debugging
    }
}

// Form submission handler
document.getElementById('sheinternet-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const formData = {
        name: document.getElementById('fname').value,
        email: document.getElementById('femail').value,
        country: document.getElementById('country').value,
        description: document.querySelector('input[name="description"]:checked')?.value || '',
        interested: document.querySelector('input[name="interested"]:checked')?.value || '',
        about: document.querySelector('input[name="about"]:checked')?.value || '',
    };

    console.log("Form Data:", formData); // Debugging

    // Get CSRF token
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Send data via AJAX
    fetch('/submit-form/', { // Replace with your Django URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('sheinternet-message');
        messageDiv.style.display = 'block';

        if (data.status === 'success') {
            messageDiv.innerHTML = `
                <div class="sheinternet-alert sheinternet-alert-success">
                    ${data.message}
                    <button type="button" class="sheinternet-close" data-dismiss="alert">&times;</button>
                </div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="sheinternet-alert sheinternet-alert-error">
                    ${data.message}
                    <button type="button" class="sheinternet-close" data-dismiss="alert">&times;</button>
                </div>
            `;
        }

        // Clear form fields and close the form after 3 seconds
        setTimeout(() => {
            document.getElementById('sheinternet-form').reset(); // Reset form fields
            closeJoinForm(); // Close the form
            
        }, 3000); // 3000 milliseconds = 3 seconds

        setTimeout(() => {
            // Close the form
            messageDiv.style.display = 'none';
        }, 7000); 
        
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Add event listener to dismiss messages
document.addEventListener('click', function (event) {
    if (event.target.classList.contains('sheinternet-close')) {
        event.target.parentElement.style.display = 'none';
    }
});