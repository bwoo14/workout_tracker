import sqlite3
from datetime import datetime

class WorkoutDatabase:
    def __init__(self, db_name = 'mydatabase.db'):
        self.db_name = db_name

    def add_exercise(self, exercise_name, muscle_groups, exercise_type, image_path):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = 'INSERT INTO exercises (exercise_name, muscle_groups, exercise_type, image_path) VALUES (?, ?, ?, ?)'
        cursor.execute(query, (exercise_name, muscle_groups, exercise_type, image_path))
        conn.commit()
        cursor.close()

    def add_workout(self, date_time, duration, protein_taken, creatine_taken, exercises, reps, weights):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query1 = 'INSERT INTO workouts (date_time, duration, protein_taken, creatine_taken) VALUES (?, ?, ?, ?)'
        query2 = 'INSERT INTO exercises_per_workout (workout_id, exercise_id, reps, weight) VALUES (?, ?, ?, ?)'
        workout_id = cursor.execute('SELECT MAX(workout_id) FROM workouts').fetchone()[0]
        
        if workout_id is None:
            workout_id = 1
        
        cursor.execute(query1, (date_time, duration, protein_taken, creatine_taken))
        for i in range(len(exercises)):
            exercise_lookup = 'SELECT exercise_id FROM exercises WHERE exercise_name = ?'
            exercise_id = cursor.execute(exercise_lookup, (exercises[i],)).fetchone()[0]

            cursor.execute(query2, (workout_id, exercise_id, reps[i], weights[i]))
        conn.commit()
        cursor.close()

    def get_exercises(self, just_names = True, normalize = True):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        if just_names:
            cursor.execute('SELECT exercise_name FROM exercises')
        else:
            cursor.execute('SELECT * FROM exercises')
        results = cursor.fetchall()
        
        if normalize:
            results = [row[0] for row in results]
        cursor.close()
        return results
    
    def add_measurement(self, weight, bicep, thigh, waist, body_fat, date):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = 'INSERT INTO weekly_measurements (weight, bicep_measure, thigh_measure, waist_measure, body_fat, date) VALUES (?, ?, ?, ?, ?, ?)'
        cursor.execute(query, (weight, bicep, thigh, waist, body_fat, date))
        conn.commit()
        cursor.close()

    # def get_measurements(self, *specifics, normalize = True):
    #     conn = sqlite3.connect(self.db_name)
    #     cursor = conn.cursor()
    #     if len(specifics) == 0:
    #         cursor.execute('SELECT * FROM weekly_measurements')
    #     else:
    #         query = 'SELECT ' + ', '.join(specifics) + ' FROM weekly_measurements'
    #         cursor.execute(query)
    #     results = cursor.fetchall()
    #     if normalize:
    #         results = [row[0] for row in results]
    #     cursor.close()
    #     return results

    # def get_measurements(self, normalize=True):
    #     conn = sqlite3.connect(self.db_name)
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT * FROM weekly_measurements')
    #     rows = cursor.fetchall()
    #     cursor.close()

    #     # Extract column names
    #     col_names = [description[0] for description in cursor.description]

    #     # Create empty dictionary with keys being column names
    #     measurements = {col_name: [] for col_name in col_names}

    #     dates = []
    #     for row in rows:
    #         date_str = row[-1]
    #         date_str = date_str.split(' ')[0]
    #         date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    #         formatted_date = date_obj.strftime('%b. %d')
    #         dates.append(formatted_date)
    #         for i in range(len(col_names)):
    #             measurements[col_names[i]].append(row[i])

    #     if normalize:
    #         for col_name in measurements.keys():
    #             if col_name != 'id' and col_name != 'date':
    #                 col_data = measurements[col_name]
    #                 min_val = min(col_data)
    #                 max_val = max(col_data)
    #                 if min_val != max_val:
    #                     normalized_data = [(val - min_val) / (max_val - min_val) for val in col_data]
    #                     measurements[col_name] = normalized_data

    #     # Remove 'id' and 'date' keys from dictionary
    #     measurements.pop('id', None)
    #     measurements.pop('date', None)

    #     return dates, measurements
    def get_measurements(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM weekly_measurements')
        rows = cursor.fetchall()
        cursor.close()

        # Extract column names
        col_names = [description[0] for description in cursor.description]

        # Create empty dictionary with keys being column names
        measurements = {col_name: [] for col_name in col_names}

        dates = []
        for row in rows:
            date_str = row[-1]
            date_str = date_str.split(' ')[0]
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            formatted_date = date_obj.strftime('%b. %d')
            dates.append(formatted_date)
            for i in range(len(col_names)):
                measurements[col_names[i]].append(row[i])

        # Remove 'id' and 'date' keys from dictionary
        measurements.pop('id', None)
        measurements.pop('date', None)

        return dates, measurements