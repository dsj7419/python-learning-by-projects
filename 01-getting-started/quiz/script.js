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
    document.getElementById('progress-bar-container').classList.remove('hide');
    setNextQuestion();
}

function setNextQuestion() {
    document.getElementById('question-number').innerText = `Question ${currentQuestionIndex + 1} of ${shuffledQuestions.length}`;
    document.getElementById('answer-feedback').classList.add('hide');
    resetState();
    showQuestion(shuffledQuestions[currentQuestionIndex]);
    updateProgressBar();
}

function updateProgressBar() {
    const progressBar = document.getElementById('progress-bar');
    const progressPercentage = ((currentQuestionIndex + 1) / shuffledQuestions.length) * 100;
    console.log('Updating progress bar:', progressPercentage);
    progressBar.style.width = progressPercentage + '%';
}

function showQuestion(question) {
    questionElement.innerHTML = question.question;  
    const shuffledAnswers = question.answers.sort(() => Math.random() - 0.5);
    shuffledAnswers.forEach(answer => {
        const button = document.createElement('button');
        
        // Replace backticks with <code> tags
        button.innerHTML = answer.text.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>').replace(/`([^`]+)`/g, '<code>$1</code>');  

        button.classList.add('btn');
        if (answer.correct) {
            button.dataset.correct = answer.correct;
        }
        button.addEventListener('click', selectAnswer);
        answerButtonsElement.appendChild(button);
    });
}

function setStatusClass(element, correct) {
    clearStatusClass(element);
    if (correct) {
        element.classList.add('correct');
    } else {
        element.classList.add('wrong');
    }
}

function clearStatusClass(element) {
    element.classList.remove('correct');
    element.classList.remove('wrong');
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
    const currentQuestion = shuffledQuestions[currentQuestionIndex];

    document.getElementById('answer-feedback').classList.remove('hide');

    if (correct) {
        score++;
        document.getElementById('answer-feedback').innerHTML = `<span style="color: green;">&#10004; Correct!</span> ${currentQuestion.reason}`;
        setStatusClass(selectedButton, true);
    } else {
        document.getElementById('answer-feedback').innerHTML = `<span style="color: red;">&#10008; Incorrect:</span> ${currentQuestion.reason}`;
        setStatusClass(selectedButton, false);
        
        // Highlight the correct answer in green
        Array.from(answerButtonsElement.children).forEach(button => {
            if (button.dataset.correct) setStatusClass(button, true);
        });
    }

    if (shuffledQuestions.length > currentQuestionIndex + 1) {
        nextButtonElement.classList.remove('hide');
    } else {
        nextButtonElement.innerText = 'Finish';  // Change button text to 'Finish'
        nextButtonElement.classList.remove('hide');
        nextButtonElement.addEventListener('click', finishQuiz);  // Add event listener to finish the quiz
    }
}

function finishQuiz() {
    showScore();
    nextButtonElement.innerText = 'Next'; 
    nextButtonElement.removeEventListener('click', finishQuiz);  
}

function showScore() {
    questionContainerElement.classList.add('hide');
    resultContainerElement.classList.remove('hide');
    let percentage = (score / shuffledQuestions.length) * 100;
    let grade = getLetterGrade(percentage);
    document.getElementById('progress-bar-container').classList.add('hide');
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
    currentQuestionIndex = 0;
    score = 0;
    resultContainerElement.classList.add('hide');
    questionContainerElement.classList.remove('hide');
    startQuiz(shuffledQuestions);
});
