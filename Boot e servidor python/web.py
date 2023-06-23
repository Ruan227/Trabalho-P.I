import mysql.connector
import json
from decimal import Decimal
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ruanpascoal227",
    database="gastos_deputados",
)


@app.route("/")
def get_gastos_deputados():
    # select da database
    cursor = mydb.cursor()
    cursor.execute(
        """
        SELECT 
    ROW_NUMBER() OVER (ORDER BY total_gastos DESC) AS indice,
    nome,
    deputado_id,
    total_gastos
FROM
    (SELECT 
        nome,
        deputado_id,
        SUM(valor) AS total_gastos
    FROM
        gastos_deputados
    GROUP BY
        nome,
        deputado_id) AS subquery
ORDER BY
    total_gastos DESC;

    """
    )

    # o resultado
    results = cursor.fetchall()

    # pega o resultdo e transforma em JSON
    data = []
    for row in results:
        item = {
            "nu mero": row[0],
            "nome": str(row[1]),
            "deputado_id": str(row[2]),
            "valor_gasto": str(row[3]),
        }
        data.append(item)

    # Retorna os dados como resposta
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
