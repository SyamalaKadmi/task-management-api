# #GET /tasks: Retrieve all tasks
# GET /tasks/<id>: Retrieve a specific task
# POST /tasks: Create a new task
# PUT /tasks/<id>: Update an existing task
# DELETE /tasks/<id>: Delete a task

from flask import Flask, jsonify, request

app=Flask(__name__)

tasks = [ {"id": 1, "title": "AdminService.exe", "description": "Windows Setup API", "status": "Running", "created_at":"17-08-2024", "updated_at":"17-08-2024"},
             {"id": 2, "title": "conhost.exe", "description": "Console Windows Host", "status": "Running", "created_at":"17-08-2024", "updated_at":"17-08-2024"}, 
             {"id": 3, "title": "LockApp.exe", "description": "LockApp.exe", "status": "Suspended", "created_at":"17-08-2024", "updated_at":"17-08-2024"},
               ]

@app.route("/tasks/<id>", methods=["PUT"])
def task_update(id):
    tasks = tasks.query.get(id)
    title = request.json['title']
    description = request.json['description']
    return("Task has been updated")

if __name__=='__main__':

    app.run(debug=True)