from flask import Flask, request, jsonify
from model_utils import load_model, predict
from transformers import DistilBertTokenizer
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Load the model
model = load_model(r'"C:\Users\Ganesh Balaji\Desktop\Backend\model.safetensors"')

# Initialize the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

@app.route('/predict', methods=['POST'])
def predict_expense():
    # Get data from frontend
    expense_category = request.form.get('expenseCategory')
    amount = request.form.get('amount')
    
    # Prepare input text for prediction
    input_text = f"{expense_category},{amount}"
    
    # Make prediction
    predicted_class, probabilities = predict(model, input_text, tokenizer)
    
    # Output the predicted class and probabilities
    response = {
        "predicted_class": predicted_class,
        "probabilities": probabilities.tolist()
    }
    print("result",predicted_class)
    return jsonify(response)
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)
