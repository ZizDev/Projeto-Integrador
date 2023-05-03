from flask import Flask, request, jsonify,render_template
import openai


# Configura a API da OpenAI
openai.api_key = "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"
model_engine = "text-davinci-003"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('principal.html')
@app.route('/mediador')
def mediador():
    return render_template("index.html")                          
@app.route('/processar', methods=['POST'])
def suggest_career():
    # Obtém os dados enviados pelo cliente
    info = request.form['info']

    # Processa a solicitação usando a API da OpenAI
    prompt = f"recomende uma carreira e dê uma pequena descrição sobre ela com base nas informações, e a resposta não pode passar de 100 caracteres: {info}"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop="",
        temperature=0.6
    )
    career = response.choices[0].text.strip()
    resultado = 'De acordo com o que foi apresentado, achamos que essa área combina com você:'
    # Renderiza o template HTML com a sugestão de carreira
    return render_template('index.html', resultado=resultado,career=career)


if __name__ == '__main__':
    app.run(debug=True)
