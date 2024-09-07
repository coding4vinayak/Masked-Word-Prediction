from flask import Flask, render_template, request
from transformers import BertTokenizer, BertForMaskedLM
import torch

# Initialize the Flask app
app = Flask(__name__)

# Load the model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertForMaskedLM.from_pretrained('bert-base-multilingual-cased')
device = torch.device("cpu")

# Function to predict the masked word
def predict_masked_word(input_text):
    tokenized_text = tokenizer.tokenize(input_text)
    masked_index = tokenized_text.index('[MASK]')
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    tokens_tensor = torch.tensor([indexed_tokens]).to(device)

    with torch.no_grad():
        outputs = model(tokens_tensor)
        predictions = outputs.logits[0, masked_index].topk(5)

    predicted_token_ids = predictions.indices.tolist()
    predicted_tokens = tokenizer.convert_ids_to_tokens(predicted_token_ids)
    return predicted_tokens

# Define the route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['text']
        predicted_tokens = predict_masked_word(input_text)
        return render_template('index.html', input_text=input_text, predictions=predicted_tokens)
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
