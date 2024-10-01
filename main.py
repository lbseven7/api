from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Rota para homepage
@app.route('/')
def homepage():
    return 'Essa é a homepage do site'

# Rota para mostrar todos os dados do CSV
@app.route('/dados', methods=['GET'])
def get_dados():
    try:
        # Lendo o arquivo CSV
        df = pd.read_csv('encomendas.csv')

        # Convertendo os dados para uma lista de dicionários
        resultado = df.to_dict(orient='records')

        # Retornando os dados em formato JSON
        return jsonify(resultado)

    except Exception as e:
        return jsonify({'erro': str(e)})

# Executando o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
