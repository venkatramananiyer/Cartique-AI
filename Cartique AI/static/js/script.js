// Capture user voice input and send it to the Flask backend for processing
function startVoiceAssistant() {
    const audioInput = document.querySelector('#audioInput');
    const formData = new FormData();
    formData.append('audio', audioInput.files[0]);

    fetch('/process_audio', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            displayRecommendations(data.recommendations);
        } else {
            alert("Sorry, something went wrong. Please try again.");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("There was an error with the request.");
    });
}

// Display the product recommendations returned by Riva
function displayRecommendations(recommendations) {
    const recommendationsContainer = document.querySelector('#recommendations');
    recommendationsContainer.innerHTML = '';

    recommendations.forEach(item => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product-item');
        productDiv.innerHTML = `
            <h3>${item.name}</h3>
            <p>${item.description}</p>
            <p>Price: ${item.price}</p>
        `;
        recommendationsContainer.appendChild(productDiv);
    });
}
