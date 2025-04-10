const newsletter = document.getElementById('newsletter-form'); 
if (newsletter) {
    newsletter.addEventListener('submit', function (event) {
        event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/subscribe/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ name, email }),
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('message');
        console.log("Response Data:", data);  // Debugging

        if (data.status === 'success') {
            messageDiv.innerHTML = `
                <div class="alert alert-success">
                    ${data.message}
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                </div>
            `;
        } else {
            messageDiv.innerHTML = `
                <div class="alert alert-danger">
                    ${data.message}
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                </div>
            `;
        }

        messageDiv.style.display = 'block';  // Make the message visible
        setTimeout(() => {
            document.getElementById('newsletter-form').reset();
            messageDiv.style.display = 'none';
        }, 3000);
        
       
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Add event listener to dismiss messages
document.addEventListener('click', function (event) {
    if (event.target.classList.contains('close')) {
        event.target.parentElement.style.display = 'none';
    }
});
}

    