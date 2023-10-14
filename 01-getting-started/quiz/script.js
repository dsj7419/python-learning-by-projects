
function getLetterGrade(percentage) {
    if (percentage >= 90) return 'A';
    else if (percentage >= 80) return 'B';
    else if (percentage >= 70) return 'C';
    else if (percentage >= 60) return 'D';
    else return 'F';
}
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
    document.getElementById('question-number').innerText = `Question ${currentQuestionIndex + 1} of ${shuffledQuestions.length}`;
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
    let percentage = (score / shuffledQuestions.length) * 100;
    let grade = getLetterGrade(percentage);  // Define this function to determine letter grade
    finalScoreElement.textContent = `Your score: ${score}/${shuffledQuestions.length} (${percentage}% - Grade: ${grade})`;  
}

nextButtonElement.addEventListener('click', () => {
    currentQuestionIndex++;
    setNextQuestion();
});


document.getElementById('back-to-lesson').addEventListener('click', () => {
    window.location.href = 'https://github.com/dsj7419/python-learning-by-projects/blob/main/01-getting-started/README.md#quiz';
});


document.getElementById('restart').addEventListener('click', () => {
    resultContainerElement.classList.add('hide');
    questionContainerElement.classList.remove('hide');
    startQuiz();
});
