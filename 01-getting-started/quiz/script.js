// Utilize 'const' and 'let' for variable declarations.
const getLetterGrade = (percentage) => {
    // Simplify the if-else chain using ternary operators.
    return percentage >= 90 ? 'A' : 
           percentage >= 80 ? 'B' : 
           percentage >= 70 ? 'C' : 
           percentage >= 60 ? 'D' : 'F';
}

// Extract HTML elements once and use them throughout the script.
const questionContainerElement = document.getElementById('question-container');
const questionElement = document.getElementById('question');
const answerButtonsElement = document.getElementById('answer-buttons');
const nextButtonElement = document.getElementById('next-button');
const resultContainerElement = document.getElementById('result-container');
const finalScoreElement = document.getElementById('final-score');
const progressBarContainer = document.getElementById('progress-bar-container');
const progressBar = document.getElementById('progress-bar');
const answerFeedback = document.getElementById('answer-feedback');

let shuffledQuestions, currentQuestionIndex, score;

// Utilize async/await syntax for asynchronous operations.
const startQuiz = async () => {
    try {
        const response = await fetch('questions.json');
        if (!response.ok) throw new Error('Network response was not ok' + response.statusText);
        const questions = await response.json();

        score = 0;
        shuffledQuestions = questions.sort(() => Math.random() - 0.5);
        currentQuestionIndex = 0;
        questionContainerElement.classList.remove('hide');
        progressBarContainer.classList.remove('hide');
        setNextQuestion();
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
}

const setNextQuestion = () => {
    answerFeedback.classList.add('hide');
    resetState();
    showQuestion(shuffledQuestions[currentQuestionIndex]);
    updateProgressBar();
}

const resetState = () => {
    nextButtonElement.classList.add('hide');
    // Re-enable buttons and remove them.
    Array.from(answerButtonsElement.children).forEach(button => {
        button.disabled = false;
        button.remove();
    });
}

const updateProgressBar = () => {
    const progressPercentage = ((currentQuestionIndex + 1) / shuffledQuestions.length) * 100;
    progressBar.style.width = progressPercentage + '%';
}

const showQuestion = (question) => {
    // Utilize template literals for string concatenation.
    questionElement.innerHTML = question.code ? 
        `${question.question}<br><br><pre><code>${question.code}</code></pre>` : 
        question.question;
    
    const shuffledAnswers = question.answers.sort(() => Math.random() - 0.5);
    const labels = ['a)', 'b)', 'c)', 'd)'];
    
    shuffledAnswers.forEach((answer, index) => {
        const button = document.createElement('button');
        // Use destructuring for better readability.
        const {code, text, correct} = answer;
        button.innerHTML = `${labels[index]} ${code ? `<pre><code>${code}</code></pre>` : text}`;
        button.classList.add('btn');
        // Utilize dataset properties directly instead of conditionally.
        button.dataset.correct = correct;
        button.addEventListener('click', selectAnswer);
        answerButtonsElement.appendChild(button);
    });
}

const setStatusClass = (element, correct) => {
    // Simplify class manipulation by using classList methods and conditional (ternary) operator.
    element.classList.add(correct ? 'correct' : 'wrong');
}

const clearStatusClass = (element) => {
    element.classList.remove('correct', 'wrong');
}

const selectAnswer = (e) => {
    const selectedButton = e.target;
    const correct = selectedButton.dataset.correct;
    const currentQuestion = shuffledQuestions[currentQuestionIndex];

    answerFeedback.classList.remove('hide');
    answerFeedback.innerHTML = `<span style="color: ${correct ? 'green' : 'red'};">${correct ? '&#10004;' : '&#10008;'} ${correct ? 'Correct!' : 'Incorrect:'}</span> ${currentQuestion.reason}`;
    setStatusClass(selectedButton, correct);

    Array.from(answerButtonsElement.children).forEach(button => {
        button.disabled = true;
        if (button.dataset.correct) setStatusClass(button, true);
    });

    // Simplify next button setup.
    nextButtonElement.innerText = shuffledQuestions.length > currentQuestionIndex + 1 ? 'Next' : 'Finish';
    nextButtonElement.classList.remove('hide');
}

const finishQuiz = () => {
    showScore();
    nextButtonElement.innerText = 'Next'; 
    nextButtonElement.removeEventListener('click', finishQuiz);
}

const showScore = () => {
    questionContainerElement.classList.add('hide');
    resultContainerElement.classList.remove('hide');
    const percentage = (score / shuffledQuestions.length) * 100;
    const grade = getLetterGrade(percentage);
    progressBarContainer.classList.add('hide');
    finalScoreElement.textContent = `Your score: ${score}/${shuffledQuestions.length} (${percentage}% - Grade: ${grade})`;  
}

// Event listener for the 'Next' button.
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
    startQuiz();
});

// Start the quiz when the script loads.
startQuiz();
