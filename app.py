from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the marks data
with open('q-vercel-python(3).json', 'r') as file:
    marks_data = json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the names from query params
    names = request.args.getlist('name')
    
    # Find the marks for each name in the same order
    response_marks = []
    for name in names:
        student = next((student for student in marks_data["students"] if student["name"] == name), None)
        if student:
            response_marks.append(student["marks"])
        else:
            response_marks.append(None)  # If student not found, append None
    
    return jsonify({"marks": response_marks})

if __name__ == '__main__':
    app.run(debug=True)
