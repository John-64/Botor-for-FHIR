import flask
from gpt4all import GPT4All

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/process', methods=['POST']) 
def process():
    PATH='/Users/gianni/Progetti/LLM Models/mistral-7b-instruct-v0.1.Q4_K_M.gguf'

    data = flask.request.get_json()
    question = data['value']

    model = GPT4All(PATH)

    prompt = f"The answer have to start with 'Risposta:' and have to be the same language of the question. Thi is the question: {question}"

    output = model.generate(prompt=prompt, temp=0.35)
    return flask.jsonify(result=output)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000, threaded=True)