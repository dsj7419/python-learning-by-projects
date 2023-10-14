const questionContainerElement = document.getElementById('question-container');
const questionElement = document.getElementById('question');
const answerButtonsElement = document.getElementById('answer-buttons');
const nextButtonElement = document.getElementById('next-button');
const resultContainerElement = document.getElementById('result-container');
const finalScoreElement = document.getElementById('final-score');

let shuffledQuestions, currentQuestionIndex;
let score = 0;

fetch('questions.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok' + response.statusText);
        }
        return response.json();
    })
    .then(questions => {
        startQuiz(questions);
    })
    .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });

function startQuiz(questions) {
    score = 0;
    shuffledQuestions = questions.sort(() => Math.random() - 0.5);
    currentQuestionIndex = 0;
    questionContainerElement.classList.remove('hide');
    setNextQuestion();
}

function setNextQuestion() {
    resetState();
    showQuestion(shuffledQuestions[currentQuestionIndex]);
}

function showQuestion(question) {
    // Use innerHTML to interpret HTML tags and entities
    questionElement.innerHTML = question.question;  
    question.answers.forEach(answer => {
        const button = document.createElement('button');
        // Use innerHTML here as well
        button.innerHTML = answer.text;  
        button.classList.add('btn');
        if (answer.correct) {
            button.dataset.correct = answer.correct;
        }
        button.addEventListener('click', selectAnswer);
        answerButtonsElement.appendChild(button);
    });
}

function resetState() {
    nextButtonElement.classList.add('hide');
    while (answerButtonsElement.firstChild) {
        answerButtonsElement.removeChild(answerButtonsElement.firstChild);
    }
}

function selectAnswer(e) {
    const selectedButton = e.target;
    const correct = selectedButton.dataset.correct;
    if (correct) score++;

    if (shuffledQuestions.length > currentQuestionIndex + 1) {
        nextButtonElement.classList.remove('hide');
    } else {
        showScore();
    }
}

function showScore() {
    questionContainerElement.classList.add('hide');
    resultContainerElement.classList.remove('hide');
    // Ensure score is displayed using total questions from shuffledQuestions
    finalScoreElement.textContent = `Your score: ${score}/${shuffledQuestions.length}`;  
}

nextButtonElement.addEventListener('click', () => {
    currentQuestionIndex++;
    setNextQuestion();
});

document.getElementById('restart').addEventListener('click', () => {
    resultContainerElement.classList.add('hide');
    startQuiz();
});
