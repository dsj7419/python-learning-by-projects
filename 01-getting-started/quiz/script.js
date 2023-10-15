import { fetchQuizData, selectElement, updateInnerHTML, toggleClass } from './utils.js';

class Quiz {
    constructor() {
        this.questionContainerElement = selectElement('question-container');
        this.questionElement = selectElement('question');
        this.answerButtonsElement = selectElement('answer-buttons');
        this.nextButtonElement = selectElement('next-button');
        this.resultContainerElement = selectElement('result-container');
        this.finalScoreElement = selectElement('final-score');
        this.finishQuiz = this.finishQuiz.bind(this);
        this.selectAnswer = this.selectAnswer.bind(this);
        this.goToNextQuestion = this.goToNextQuestion.bind(this);
        this.questions = [];
        this.currentQuestionIndex = 0;
        this.score = 0;
    }

    loadAndStartQuiz() {
        fetchQuizData('questions.json')
            .then(questions => {
                this.startQuiz(questions);
            });
    }

    startQuiz(questions) {
        this.score = 0;
        this.questions = questions.sort(() => Math.random() - 0.5);
        this.currentQuestionIndex = 0;
        toggleClass('question-container', 'hide', false);
        toggleClass('progress-bar-container', 'hide', false);
        this.setNextQuestion();
    }

    setNextQuestion() {
        updateInnerHTML('question-number', `Question ${this.currentQuestionIndex + 1} of ${this.questions.length}`);
        toggleClass('answer-feedback', 'hide', true);
        this.resetState();
        this.showQuestion(this.questions[this.currentQuestionIndex]);
        this.updateProgressBar();
    }

    resetState() {
        toggleClass('next-button', 'hide', true);
        while (this.answerButtonsElement.firstChild) {
            this.answerButtonsElement.firstChild.disabled = false;
            this.answerButtonsElement.removeChild(this.answerButtonsElement.firstChild);
        }
    }

    showQuestion(question) {
        updateInnerHTML('question', question.question + (question.code ? `<pre><code>${question.code}</code></pre>` : ''));
        question.answers.forEach(answer => {
            const button = document.createElement('button');
            button.setAttribute('aria-label', answer.text);
            button.innerHTML = answer.code ? `<pre><code>${answer.code}</code></pre>` : answer.text;
            button.classList.add('btn');
            if (answer.correct) {
                button.dataset.correct = answer.correct;
            }
            button.addEventListener('click', this.selectAnswer.bind(this));
            this.answerButtonsElement.appendChild(button);
        });
    }

    // Handle answer selection
    selectAnswer(e) {
        const selectedButton = e.target;
        const correct = selectedButton.dataset.correct;
        const feedbackElement = document.getElementById('answer-feedback');
        feedbackElement.setAttribute('aria-live', 'assertive');
    
        // Ensure feedback is visible
        feedbackElement.classList.remove('hide');
        
        if (correct) {
            this.score++;
            feedbackElement.innerHTML = `<span class="correct-feedback">&#10004; Correct:</span> ${this.questions[this.currentQuestionIndex].reason}`;
        } else {
            feedbackElement.innerHTML = `<span class="incorrect-feedback">&#10008; Incorrect:</span> ${this.questions[this.currentQuestionIndex].reason}`;
        }        

        Array.from(this.answerButtonsElement.children).forEach(button => {
            const isCorrect = button.dataset.correct;
            // Ensure buttons are colored accordingly
            if (button === e.target) {
                this.setStatusClass(button, isCorrect);
            } else if (isCorrect) {
                this.setStatusClass(button, true);
            }
            button.disabled = true;
        });

        if (this.questions.length > this.currentQuestionIndex + 1) {
            this.nextButtonElement.classList.remove('hide');
            this.nextButtonElement.removeEventListener('click', this.finishQuiz);
            this.nextButtonElement.addEventListener('click', this.goToNextQuestion);
            this.nextButtonElement.setAttribute('aria-label', 'Next question');
        } else {
            this.nextButtonElement.innerText = 'Finish';
            this.nextButtonElement.classList.remove('hide');
            this.nextButtonElement.removeEventListener('click', this.goToNextQuestion);
            this.nextButtonElement.addEventListener('click', this.finishQuiz);
            this.nextButtonElement.setAttribute('aria-label', 'Finish the quiz');
        }
        this.nextButtonElement.focus();
    }

    // Finalize the quiz and show the score
    finishQuiz() {
        this.showScore();
        this.nextButtonElement.classList.add('hide');
        this.nextButtonElement.innerText = 'Next';
        this.nextButtonElement.removeEventListener('click', this.goToNextQuestion);
        this.nextButtonElement.removeEventListener('click', this.finishQuiz);
    }

    // Proceed to the next question or finish the quiz
    goToNextQuestion() {
        console.log('Going to next question, current index:', this.currentQuestionIndex);
        if (this.questions.length > this.currentQuestionIndex + 1) {
            this.currentQuestionIndex++;
            this.setNextQuestion();
        } else {
            this.finishQuiz();
        }
    }

    // Update the progress bar
    updateProgressBar() {
        const progressPercentage = ((this.currentQuestionIndex + 1) / this.questions.length) * 100;
        document.getElementById('progress-bar').style.width = ((this.currentQuestionIndex + 1) / this.questions.length) * 100 + '%';
        updateInnerHTML('progress-text', `You are on question ${this.currentQuestionIndex + 1} of ${this.questions.length}, which is ${progressPercentage.toFixed(0)}% of the quiz.`);
    }

    // Set the status of buttons (correct/incorrect)
    setStatusClass(element, correct) {
        element.classList.remove('correct', 'wrong'); 
        element.classList.add(correct ? 'correct' : 'wrong');  
    }

    // Show the score
    showScore() {
        this.questionContainerElement.classList.add('hide');
        this.resultContainerElement.classList.remove('hide');
        let percentage = (this.score / this.questions.length) * 100;
        let grade = this.getLetterGrade(percentage);
        document.getElementById('progress-bar-container').classList.add('hide');
        this.finalScoreElement.setAttribute('aria-live', 'polite');
        this.finalScoreElement.textContent = `Your score: ${this.score}/${this.questions.length} (${percentage}% - Grade: ${grade})`;
    }

    // Convert a score percentage into a letter grade
    getLetterGrade(percentage) {
        if (percentage >= 90) return 'A';
        else if (percentage >= 80) return 'B';
        else if (percentage >= 70) return 'C';
        else if (percentage >= 60) return 'D';
        else return 'F';
    }
}

// Instantiate Quiz class and manage event listeners
const quiz = new Quiz();

window.onload = () => {
    quiz.loadAndStartQuiz();
};

quiz.nextButtonElement.addEventListener('click', quiz.goToNextQuestion);

selectElement('back-to-lesson').addEventListener('click', () => {
    window.location.href = 'https://github.com/dsj7419/python-learning-by-projects/blob/main/01-getting-started/README.md#quiz';
});

selectElement('restart').addEventListener('click', () => {
    quiz.currentQuestionIndex = 0;
    quiz.score = 0;
    toggleClass('result-container', 'hide', true);
    toggleClass('question-container', 'hide', false);
    quiz.startQuiz(quiz.questions)
    updateInnerHTML('next-button', 'Next');
    quiz.nextButtonElement.removeEventListener('click', quiz.finishQuiz);
    quiz.nextButtonElement.addEventListener('click', quiz.goToNextQuestion);
});