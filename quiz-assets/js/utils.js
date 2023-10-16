let startTime;

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

function startTimer() {
    startTime = new Date();
}

function resetTimer() {
    startTime = null;
}

function getElapsedTime() {
    const endTime = new Date();
    const timeDiff = endTime - startTime; // Time difference in ms
    return timeDiff;
}

function formatTime(ms) {
    const minutes = Math.floor(ms / 60000);
    const seconds = Math.floor((ms % 60000) / 1000);
    const milliseconds = ms % 1000;
    
    const formattedMinutes = String(minutes).padStart(2, '0');
    const formattedSeconds = String(seconds).padStart(2, '0');
    const formattedMilliseconds = String(milliseconds).padStart(3, '0');
    
    return `${formattedMinutes}:${formattedSeconds}.${formattedMilliseconds}`;
}

export { fetchQuizData, selectElement, updateInnerHTML, toggleClass, startTimer, resetTimer, getElapsedTime, formatTime };
