import sqlite3

# Create a connection to the 'mydatabase.db' file
conn = sqlite3.connect('mydatabase.db')

# # Create the exercises table
# conn.execute('''CREATE TABLE exercises (
#   exercise_id INTEGER PRIMARY KEY,
#   exercise_name TEXT NOT NULL,
#   muscle_groups TEXT,
#   exercise_type TEXT,
#   image_path TEXT
# )''')

# # Create the workouts table
# conn.execute('''CREATE TABLE workouts (
#   workout_id INTEGER PRIMARY KEY,
#   date_time DATETIME NOT NULL,
#   duration INTEGER,
#   protein_taken INTEGER,
#   creatine_taken INTEGER
# )''')

# # Create the exercises per workout table
# conn.execute('''CREATE TABLE exercises_per_workout (
#   id INTEGER PRIMARY KEY,
#   workout_id INTEGER,
#   exercise_id INTEGER,
#   reps INTEGER,
#   weight TEXT,
#   FOREIGN KEY (workout_id) REFERENCES workouts (workout_id),
#   FOREIGN KEY (exercise_id) REFERENCES exercises (exercise_id)
# )''')


conn.execute('''CREATE TABLE weekly_measurements (
  id INTEGER PRIMARY KEY,
  weight FLOAT,
  bicep_measure FLOAT,
  thigh_measure FLOAT,
  waist_meausre FLOAT,
  body_fat FLOAT,
  date DATETIME
)''')

# Commit the changes and close the connection
conn.commit()
conn.close()



# useful stuff:

