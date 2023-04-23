from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import sqlite3
from database_class import WorkoutDatabase
import graph

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = '.' + os.sep + 'images'
# Create a global database connection object
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
wodb = WorkoutDatabase()

@app.route('/')
def home():
    dates, measurements = wodb.get_measurements()

    weight_graph = graph.create_line_plot(dates, measurements['weight'], 'Weight')
    body_fat_graph = graph.create_line_plot(dates, measurements['body_fat'], 'Body Fat')
    return render_template('home.html', weight_graph = weight_graph, body_fat_graph = body_fat_graph)

@app.route('/new_workout', methods=['GET', 'POST'])
def new_workout():
    if request.method == 'POST':
        workout_date = request.form['workout_date']
        workout_duration = request.form['duration']
        protein_taken = request.form['protein_taken']
        creatine_taken = request.form['creatine_taken']

        exercises = request.form.getlist('exercise_name[]')
        reps= request.form.getlist('reps[]')
        weights = request.form.getlist('weight[]')
        # Process the data as needed
        wodb.add_workout(workout_date, workout_duration, protein_taken, creatine_taken, exercises, reps, weights)
        return "Data submitted successfully!"
    
    exercises = wodb.get_exercises() # Get rid of weird formatting
    return render_template('new_workout.html', exercises = exercises)

@app.route('/add_exercise', methods=['GET', 'POST'])
def add_exercise():
    if request.method == 'POST':
        exercise_name = request.form['exercise_name']
        muscle_groups = ' '.join(request.form.getlist('muscle_groups[]'))
        exercise_type = request.form['exercise_type']
        exercise_image = request.files['exercise_image']
        
        if exercise_image and allowed_file(exercise_image.filename):
            filename = secure_filename(exercise_image.filename)
            exercise_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        exercise_image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        wodb.add_exercise(exercise_name, muscle_groups, exercise_type, exercise_image_path)

        return "Data submitted successfully!"

    return render_template('add_exercise.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/view_exercises')
def view_exercises():
    exercises = wodb.get_exercises(just_names=False, normalize=False)
    return render_template('view_exercises.html', exercises = exercises)

@app.route('/add_measurements', methods=['GET', 'POST'])
def add_measurements():
    if request.method == 'POST':
        weight = request.form['weight']
        bicep_measure = request.form['bicep_measure']
        thigh_measure = request.form['thigh_measure']
        waist_measure = request.form['waist_measure']
        body_fat = request.form['body_fat']
        date = request.form['date']
        wodb.add_measurement(weight, bicep_measure, thigh_measure, waist_measure, body_fat, date)
        return "Data submitted successfully!"
    return render_template('add_measurements.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

