function fetchQuizData(url) {
    return fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok' + response.statusText);
            }
            return response.json();
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

function selectElement(id) {
    return document.getElementById(id);
}

function updateInnerHTML(elementId, html) {
    selectElement(elementId).innerHTML = html;
}

function toggleClass(elementId, className, shouldAdd) {
    const element = selectElement(elementId);
    shouldAdd ? element.classList.add(className) : element.classList.remove(className);
}

export { fetchQuizData, selectElement, updateInnerHTML, toggleClass };
