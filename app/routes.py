from flask import Flask, render_template, request, jsonify
from app import database as db_helper

app = Flask(__name__)

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    try:
        # Uncomment and use this line to interact with your database
        # db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except Exception as e:
        result = {'success': False, 'response': str(e)}

    return jsonify(result)

@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    try:
        data = request.get_json()
        print(data)  # Print data to the console for debugging
        if "status" in data:
            # Uncomment and use this line to interact with your database
            # db_helper.update_status_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            # Uncomment and use this line to interact with your database
            # db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except Exception as e:
        result = {'success': False, 'response': str(e)}

    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    try:
        data = request.get_json()
        # Uncomment and use this line to interact with your database
        # db_helper.insert_new_task(data['description'])
        result = {'success': True, 'response': 'Done'}
    except Exception as e:
        result = {'success': False, 'response': str(e)}

    return jsonify(result)

@app.route("/")
def homepage():
    """ Returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)
