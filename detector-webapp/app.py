from flask import Flask, render_template, request, jsonify, redirect, url_for
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<prompt>')
def displayName(prompt):

    prompt = prompt.lower()
    sample_text = [prompt]

    model = load_model('model.h5')
    
    # Load the tokenizer
    with open('tokenizer.json', 'r') as f:
        data = f.read()
    tokenizer = tokenizer_from_json(data)

    # Convert the sample text to a sequence
    sample_seq = tokenizer.texts_to_sequences(sample_text)
    
    from keras.preprocessing.sequence import pad_sequences

    sample_padded = pad_sequences(sample_seq, maxlen=1000)

    # Now you can make a prediction
    prediction = model.predict(sample_padded)
    print(prediction)

    response = ""

    if prediction[0][0] > 0.5:
        response = "AI Generated Text: Positive"
    else:
        response = "Human Generated Text: Negative"

    return render_template('index.html', name=response)


if __name__ == '__main__':
    app.run()
