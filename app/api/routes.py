from flask import Blueprint, request, jsonify, render_template
from app.services.langchain import generate_answer

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/')
def home():
    return "Welcome to the Video QA Application!"
    
@api_blueprint.route('/answer', methods=['POST'])
def get_answer():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Placeholder for the answer generation process
    answer = generate_answer(question)

    return jsonify({"question": question, "answer": answer})
