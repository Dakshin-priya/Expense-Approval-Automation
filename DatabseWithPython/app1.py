from flask import Flask, request, jsonify
from model_utils import load_model, predict
from transformers import DistilBertTokenizer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the model
model_path = r"C:\Users\Rithika T S\OneDrive\Desktop\SAP\model.safetensors"
model = load_model(model_path)

# Initialize the tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

@app.route('/predict', methods=['POST'])
def predict_expense():
    try:
        # Get data from form
        expense_category = request.form.get('expenseCategory', '')
        amount = request.form.get('amount', '')

        if not expense_category or not amount:
            return jsonify({"error": "Missing expenseCategory or amount"}), 400

        # Prepare input text for prediction
        input_text = f"{expense_category},{amount}"

        # Make prediction
        predicted_class, probabilities = predict(model, input_text, tokenizer)

        # Output the predicted class and probabilities
        response = {
            "predicted_class": predicted_class,
            "probabilities": probabilities.tolist()
        }

        print("Prediction Result:", predicted_class)
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
