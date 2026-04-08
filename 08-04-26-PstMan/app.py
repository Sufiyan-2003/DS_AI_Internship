from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
employees = [
    {"id": 1, "name": "Sufiyan"},
    {"id": 2, "name": "Ahmed"},
    {"id": 3, "name": "Ali"}
]

next_id = 3

# GET all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees), 200

# POST new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    global next_id
    data = request.get_json()

    new_employee = {
        "id": next_id,
        "name": data["name"]
    }

    employees.append(new_employee)
    next_id += 1

    return jsonify(new_employee), 201

# PUT update employee
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()

    for emp in employees:
        if emp["id"] == id:
            emp["name"] = data["name"]
            return jsonify(emp), 200

    return jsonify({"error": "Employee not found"}), 404

# DELETE employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees

    employees = [emp for emp in employees if emp["id"] != id]

    return jsonify({"message": "Deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return "API is running 🚀"