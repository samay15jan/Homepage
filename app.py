from flask import Flask, render_template, request
import openai, random

app = Flask(__name__)
openai.api_key = "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"

def generate_response(text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        temperature=0.5,
        max_tokens=150,
    )
    return completion.choices[0].message["content"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_input():
    user_input = request.form['input']
    response = generate_response(user_input)
    with open('quotes.txt') as file:
        quotes = file.read().splitlines()
    random_quote = random.choices(quotes)
    return render_template('index.html', input=user_input, response=response, quote=random_quote)

if __name__ == '__main__':
    app.run()