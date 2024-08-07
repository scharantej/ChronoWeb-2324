
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Sample data objects for tasks and time slots
tasks = [
    {"id": 1, "title": "Task 1", "description": "This is task 1", "duration": 60},
    {"id": 2, "title": "Task 2", "description": "This is task 2", "duration": 120},
    {"id": 3, "title": "Task 3", "description": "This is task 3", "duration": 180},
]

time_slots = [
    {"id": 1, "start_time": "08:00", "end_time": "10:00"},
    {"id": 2, "start_time": "10:00", "end_time": "12:00"},
    {"id": 3, "start_time": "13:00", "end_time": "15:00"},
    {"id": 4, "start_time": "15:00", "end_time": "17:00"},
]

# Home page route
@app.route("/")
def home():
    return render_template("index.html", tasks=tasks, time_slots=time_slots)

# Planner generation route
@app.route("/generate-planner", methods=["POST"])
def generate_planner():
    # Extract data from the form submission
    task_ids = request.form.getlist("tasks")
    time_slot_ids = request.form.getlist("time_slots")

    # Generate a personalized planner using Smart Time's algorithms
    # This part would usually connect to the database to generate the planner
    planner = {"tasks": [], "time_slots": []}
    for task_id in task_ids:
        task = next((task for task in tasks if task["id"] == int(task_id)), None)
        if task:
            planner["tasks"].append(task)

    for time_slot_id in time_slot_ids:
        time_slot = next((time_slot for time_slot in time_slots if time_slot["id"] == int(time_slot_id)), None)
        if time_slot:
            planner["time_slots"].append(time_slot)

    # Render the planner template with the generated planner
    return render_template("planner.html", planner=planner)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
