const input = document.querySelector(".container > input:nth-child(1)");
const button = document.querySelector(".container > button:nth-child(2)");
const results = document.querySelector(".results");


button.addEventListener("click", e => {
    let text = input.value;
    // Define the API URL
    const apiUrl = `http://localhost:5000/verse?text=${encodeURIComponent(text)}`;


    // Make a GET request
    fetch(apiUrl)
    .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
    })
    .then(data => {
        results.textContent = "";
        const fragment = document.createDocumentFragment();

        data.forEach(element => {
            const div = document.createElement('div');
            const br = document.createElement('br');
            div.textContent = `${element.reference} ${element.text}`;
            fragment.appendChild(div);
            fragment.appendChild(br);
            fragment.appendChild(br);
        });
        
        results.appendChild(fragment);



    })
    .catch(error => {
    console.error('Error:', error);
    });
    


})