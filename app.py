from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize empty JSON data
assignments = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        subject_name = request.form['subject_name']
        assignment_name = request.form['assignment_name']
        question = request.form['question']
        code_block = request.form['code_block']
        if subject_name in assignments:
            if assignment_name in assignments[subject_name]:
                assignments[subject_name][assignment_name].append({'question': question, 'code_block': code_block})
            else:
                assignments[subject_name][assignment_name] = [{'question': question, 'code_block': code_block}]
        else:
            assignments[subject_name] = {assignment_name: [{'question': question, 'code_block': code_block}]}
        return redirect(url_for('admin'))

    return render_template('admin.html', assignments=assignments)


@app.route('/view_assignments/<subject_name>/<assignment_name>')
def view_assignments(subject_name, assignment_name):
    if subject_name in assignments and assignment_name in assignments[subject_name]:
        questions = assignments[subject_name][assignment_name]
    else:
        questions = []
    return render_template('view_assignments.html', subject_name=subject_name, assignment_name=assignment_name, questions=questions)


@app.route('/clear_json')
def clear_json():
    global assignments
    assignments = {}
    return redirect(url_for('admin'))


@app.route('/assignments')
def list_assignments():
    return render_template('assignments.html', assignments=assignments)


if __name__ == '__main__':
    app.run(debug=True)
