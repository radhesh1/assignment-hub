from flask import Flask, render_template, request, redirect, url_for
from flask_caching import Cache
import json
import os

app = Flask(__name__)
cache = Cache(app)

# Path to the assignments.json file
JSON_FILE_PATH = 'assignments.json'

# Function to load assignments data from assignments.json
def load_assignments():
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    else:
        return {}

# Function to save assignments data to assignments.json
def save_assignments(assignments):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(assignments, file)

# Initialize assignments dictionary from assignments.json
assignments = load_assignments()

# Cache the assignments data
@cache.cached(timeout=300)  # Cache for 5 minutes


@app.route('/')
def list_assignments():
    global assignments
    
    selected_main_category = request.args.get('main_category')

    # Extract main categories
    main_categories = list(assignments.keys())

    main_categories = list(get_cached_assignments().keys())

    if selected_main_category:
        # Filter assignments based on the selected main category
        assignments_list = get_cached_assignments().get(selected_main_category, {})
    else:
        # If no main category is selected, show all assignments
        assignments_list = get_cached_assignments()

    return render_template('assignments.html', main_categories=main_categories, assignments_list=assignments_list, selected_main_category=selected_main_category)



@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        main_category = request.form['main_category']
        subject_name = request.form['subject_name']
        assignment_name = request.form['assignment_name']
        question = request.form['question']
        code_block = request.form['code_block']
        
        # Check if the main category already exists in the assignments dictionary
        if main_category in assignments:
            # Check if the subject name already exists in the main category
            if subject_name in assignments[main_category]:
                # Check if the assignment name already exists in the subject
                if assignment_name in assignments[main_category][subject_name]:
                    # If assignment name exists, append the new question and code block
                    assignments[main_category][subject_name][assignment_name].append({'question': question, 'code_block': code_block})
                else:
                    # If assignment name doesn't exist, create a new assignment with the question and code block
                    assignments[main_category][subject_name][assignment_name] = [{'question': question, 'code_block': code_block}]
            else:
                # If subject name doesn't exist, create a new subject with the assignment and its details
                assignments[main_category][subject_name] = {assignment_name: [{'question': question, 'code_block': code_block}]}
        else:
            # If main category doesn't exist, create a new main category with the subject, assignment, and details
            assignments[main_category] = {subject_name: {assignment_name: [{'question': question, 'code_block': code_block}]}}
        save_assignments(assignments)
        # After updating the assignments dictionary, redirect to the admin page
        return redirect(url_for('admin'))

    # Render the admin template and pass the assignments dictionary to it
    return render_template('admin.html', assignments=assignments)


@app.route('/view_assignments/<main_category>/<subject_name>/<assignment_name>')
def view_assignments(main_category, subject_name, assignment_name):
    if main_category in assignments and subject_name in assignments[main_category] and assignment_name in assignments[main_category][subject_name]:
        questions = assignments[main_category][subject_name][assignment_name]
    else:
        questions = []
    return render_template('view_assignments.html', main_category=main_category, subject_name=subject_name, assignment_name=assignment_name, questions=questions)


@app.route('/clear_json')
def clear_json():
    global assignments
    assignments = {}
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)
