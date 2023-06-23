import requests
import mysql.connector

# define o número máximo de deputados adicionados
max_deputados = 1000

# realiza a requisição da Câmara dos Deputados
url_base = "https://dadosabertos.camara.leg.br/api/v2/deputados"
params = {
    "ordem": "ASC",
    "ordenarPor": "nome",
    "itens": 100, 
    "pagina": 1
}

# conecta ao banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ruanpascoal227",
    database="gastos_deputados"
)

# cria o cursor para manipulação do banco de dados
mycursor = mydb.cursor()

# lista para armazenar os IDs dos deputados já adicionados
ids_adicionados = []

# loop para percorrer todas as páginas
while True:
    response = requests.get(url_base, params=params).json()
    for deputado in response["dados"]:
        # Pega os dados dos deputados
        id_deputado = deputado["id"]
        nome = deputado["nome"]
        partido = deputado["siglaPartido"]
        uf = deputado["siglaUf"]

        # verificação para não repetir
        if id_deputado in ids_adicionados:
            continue

        # realiza a requisição de gastos do deputado
        url_gastos = f"{url_base}/{id_deputado}/despesas?ordem=ASC&ordenarPor=ano"
        response_gastos = requests.get(url_gastos).json()

        # loop das despesas do deputado
        for despesa in response_gastos["dados"]:
            tipo_despesa = despesa["tipoDespesa"]
            fornecedor = despesa["nomeFornecedor"]
            data_emissao = despesa["dataDocumento"]
            valor = despesa["valorDocumento"]
            url_documento = despesa["urlDocumento"]

            # adiciona a despesa no banco
            sql = "INSERT INTO gastos_deputados (deputado_id, nome, partido, uf, tipo_despesa, fornecedor, data_emissao, valor, url_documento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (id_deputado, nome, partido, uf, tipo_despesa, fornecedor, data_emissao, valor, url_documento)
            mycursor.execute(sql, val)

        # adiciona o ID do deputado à lista de IDs adicionados
        ids_adicionados.append(id_deputado)

        # salva as mudanças no banco de dados
        mydb.commit()

        # verifica se o número máximo de deputados foi atingido
        if len(ids_adicionados) == max_deputados:
            break

    # verifica se há mais páginas para percorrer
    if "links" in response and "next" in response["links"]:
        params["pagina"] += 1
    else:
        break

# encerra a conexão com o banco de dados
mycursor.close()
mydb.close()
print("FOI, GRAÇAS A DEUS")
