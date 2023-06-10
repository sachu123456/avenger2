from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# Quiz questions
questions = [
    {
        'id': 1,
        'question': 'Who is the leader of the Avengers?',
        'options': ['Iron Man', 'Captain America', 'Thor', 'Black Widow'],
        'answer': 'Captain America'
    },
    {
        'id': 2,
        'question': 'What is the real name of Black Widow?',
        'options': ['Natasha Romanoff', 'Wanda Maximoff', 'Carol Danvers', 'Hope van Dyne'],
        'answer': 'Natasha Romanoff'
    },
    {
        'id': 3,
        'question': 'Which Infinity Stone was embedded in Vision\'s forehead?',
        'options': ['Time Stone', 'Mind Stone', 'Soul Stone', 'Power Stone'],
        'answer': 'Mind Stone'
    }
]

# Global variables
current_question = 0
score = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_quiz():
    global current_question, score
    current_question = 0
    score = 0
    return redirect('/quiz')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global current_question, score

    if request.method == 'POST':
        answer = request.form.get('answer')

        # Check if the answer is correct
        if answer == questions[current_question]['answer']:
            score += 1

        # Move to the next question
        current_question += 1

        # If all questions are answered, redirect to the result page
        if current_question >= len(questions):
            return redirect('/result')

    # Check if there are more questions available
    if current_question < len(questions):
        question = questions[current_question]
        return render_template('quiz.html', question=question)
    else:
        # If there are no more questions, redirect to the result page
        return redirect('/result')

@app.route('/result')
def result():
    global score
    return render_template('result.html', score=score, total_questions=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
