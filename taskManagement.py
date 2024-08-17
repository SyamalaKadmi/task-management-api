from flask import Flask, request, jsonify

app=Flask(__name__)


tasks = [ {"id": 1, "title": "AdminService.exe", "description": "Windows Setup API", "status": "Running", "created_at":"17-08-2024", "updated_at":"17-08-2024"},
             {"id": 2, "title": "conhost.exe", "description": "Console Windows Host", "status": "Running", "created_at":"17-08-2024", "updated_at":"17-08-2024"}, 
             {"id": 3, "title": "LockApp.exe", "description": "LockApp.exe", "status": "Suspended", "created_at":"17-08-2024", "updated_at":"17-08-2024"},
               ]

# GET /tasks: Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# GET /tasks/<id>: Retrieve a specific task
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next(task for task in tasks if task['id'] == id)
    return jsonify(task)

# PUT /tasks/<id>: Updates an existing task
@app.route('/tasks/<int:id>', methods=['PUT'])
def task_update(id):
    for task in tasks:
        if(task['id'] == (id)):
            title = request.json['title']
            description = request.json['description']
            task['title'] = title
            task['description'] = description
            return("Task has been updated")
        else:
            return 'Task does not exist'

#Endpoint for deleting a record
@app.route('/tasks/<int:id>', methods=['DELETE'])
def task_delete(id):
    for task in tasks:
        if(task['id'] == (id)):
            tasks.remove(task)
            return("Task has been removed")
        else:
            return 'Task does not exist'

  
if __name__=='__main__':

    app.run(debug=True)