# Instruções para execução do projeto

Nesta pasta, temos dois arquivos em Python. Um deles é responsável por alimentar o banco de dados SQL, enquanto o outro executa um servidor local na porta 8080, exportando os dados em formato JSON para consultas no Next.js por meio do CORS.

## Descrição dos arquivos

- **Boot.py**: Este código é responsável por alimentar a base de dados criada no MySQL Workbench. Ele obtém os dados de uma API de deputados e os insere no banco de dados.

- **web.py**: Este código é responsável pelo servidor back-end. Ele obtém os dados do banco de dados e os expõe em um servidor local (http://localhost:8080), fornecendo os dados do banco de dados em formato JSON para consultas do front-end utilizando o Next.js.

## Configurando o ambiente

1. Abra dois VSCode: um com o repositório "DE_OLHO" e o outro com o repositório "BACK-END".
2. Em cada VSCode, abra um terminal.

### Configurando o servidor back-end

No terminal do VSCode "BACK-END", siga estas etapas:

1. Verifique se o diretório em que você está é o mesmo onde o arquivo "web.py" está localizado.
2. Instale as dependências necessárias executando os seguintes comandos:

    ```
    pip install flask
    pip install flask_cors
    pip install CORS
    ```

3. Para iniciar o servidor back-end, execute o seguinte comando no terminal:

    ```
    python web.py
    ```

### Configurando o front-end

No terminal do VSCode "DE_OLHO", siga estas etapas:

1. Verifique se o diretório em que você está é o mesmo onde o arquivo "package.json" está localizado.
2. Instale as dependências necessárias executando o seguinte comando:

    ```
    npm install
    ```

3. Para iniciar o servidor front-end, execute o seguinte comando no terminal:

    ```
    npm run dev
    ```

## Executando o projeto

Certifique-se de seguir as etapas de configuração adequadas antes de executar o projeto. Aqui está como executar cada parte:

- **Front-end**: No terminal do VSCode "DE_OLHO", execute o comando `npm run dev` para iniciar o servidor front-end.

- **Back-end**: No terminal do VSCode "BACK-END", execute o comando `python web.py` para iniciar o servidor back-end.

Lembre-se de que você precisa ter o MySQL Workbench configurado corretamente e os dados do banco de dados devem ser alimentados antes de executar o servidor back-end.

Espero que essas instruções sejam úteis! Se você tiver mais dúvidas ou precisar de ajuda adicional, fique à vontade para perguntar.
