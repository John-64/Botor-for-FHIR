import flask
from gpt4all import GPT4All
import re

def remove_answer_prefix(text):
  return re.sub("Answer: ", "", text)

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/process', methods=['POST']) 
def process():
    PATH='/Users/gianni/Progetti/LLM Models/gpt4all-falcon-q4_0.gguf'

    data = flask.request.get_json()
    question = data['value']

    model = GPT4All(PATH)

    prompt = f"My name is Botor, your chatbot, and i will try to answer to all your question. This is the question: {question}"

    output = model.generate(prompt=question, temp=0.75)

    response = remove_answer_prefix(output)
    return flask.jsonify(result=response)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000, threaded=True)