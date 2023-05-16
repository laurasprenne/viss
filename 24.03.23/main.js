const quizData = [
    {
        question: "Kas licis skolas pamatakmen?",
        a: "Auseklis",
        b: "Vērpēja",
        c: "Inese Bērziņa",
        d: "Rainis",
        correct: "d",
    }
];
const quiz= document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const text1 = document.getElementById('text1')
const text2 = document.getElementById('text2')
const text3 = document.getElementById('text3')
const text4 = document.getElementById('text4')
const submitBtn = document.getElementById('submit')
let currentQuiz = 0
loadQuiz()
function loadQuiz() {
    deselectAnswers()
    const currentQuizData = quizData[currentQuiz]
    questionEl.innerText = currentQuizData.question
    text1.innerText = currentQuizData.a
    text2.innerText = currentQuizData.b
    text3.innerText = currentQuizData.c
    text4.innerText = currentQuizData.d
}
function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}
function getSelected() {
    let answer
    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}
submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    if(answer) {
       if(answer === quizData[currentQuiz].correct) {
        quiz.innerHTML = '<h2>Atbilde ir pareiza!</h2>'
       }
       currentQuiz++
       if(currentQuiz < quizData.length) {
           loadQuiz()
       } else {
           quiz.innerHTML = "<h2>Atbilde nav pareiza!</h2>"
       }
    }
})