const questionContainerElement = document.getElementById('question-container');
const questionElement = document.getElementById('question');
const answerButtonsElement = document.getElementById('answer-buttons');
const nextButtonElement = document.getElementById('next-button');
const resultContainerElement = document.getElementById('result-container');
const finalScoreElement = document.getElementById('final-score');

let shuffledQuestions, currentQuestionIndex;
let score = 0;

// Example questions
const questions = [
    {
        question: "What is the capital of France?",
        answers: [
            { text: "Paris", correct: true },
            { text: "London", correct: false },
            { text: "Berlin", correct: false },
            { text: "Madrid", correct: false }
        ]
    },
    // Additional questions...
];

startQuiz();

function startQuiz() {
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
    questionElement.innerText = question.question;
    question.answers.forEach(answer => {
        const button = document.createElement('button');
        button.innerText = answer.text;
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
    finalScoreElement.textContent = `Your score: ${score}/${questions.length}`;
}

nextButtonElement.addEventListener('click', () => {
    currentQuestionIndex++;
    setNextQuestion();
});

document.getElementById('restart').addEventListener('click', () => {
    resultContainerElement.classList.add('hide');
    startQuiz();
});
