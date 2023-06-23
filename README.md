# Instruções para importação do banco de dados no MySQL

Este arquivo contém instruções sobre como importar um banco de dados no servidor MySQL usando o MySQL Workbench.

## Pré-requisitos

- Certifique-se de ter o MySQL Workbench instalado em seu computador.
- Tenha acesso ao arquivo de banco de dados que deseja importar.
- Verifique se você tem as permissões adequadas para importar bancos de dados no servidor MySQL.

## Passos para importação

1. Abra o MySQL Workbench.
2. Clique em "Administrador" no menu.
3. Selecione "Data Import/Restore" na seção "Management" no painel esquerdo.
4. Na guia "Import Options", escolha "Import from Self-Contained File".
5. Clique nos três pontos ("...") ao lado do campo de arquivo para selecionar o arquivo de banco de dados que deseja importar.
6. Na guia "Default Schema to be Imported To", selecione o esquema de banco de dados no qual deseja importar os dados. Se necessário, você também pode criar um novo esquema.
7. Verifique as opções de importação disponíveis e faça ajustes, se necessário.
8. Clique em "Start Import" para iniciar o processo de importação.
9. Aguarde até que o MySQL Workbench conclua a importação do banco de dados.
10. Após a conclusão, você poderá verificar o banco de dados importado no painel esquerdo do MySQL Workbench.

# Instruções para execução do projeto

Nesta pasta, temos dois arquivos em Python. Um deles é responsável por alimentar o banco de dados SQL, enquanto o outro executa um servidor local na porta 8080, exportando os dados em formato JSON para consultas no Next.js por meio do CORS.

## Descrição dos arquivos

- **Boot.py**: Este código é responsável por alimentar a base de dados criada no MySQL Workbench. Ele obtém os dados de uma API de deputados e os insere no banco de dados.

- **web.py**: Este código é responsável pelo servidor back-end. Ele obtém os dados do banco de dados e os expõe em um servidor local (http://localhost:8080), fornecendo os dados do banco de dados em formato JSON para consultas do front-end utilizando o Next.js.

## Configurando o ambiente

1. Abra dois VSCode: um com a pasta "DE_OLHO" e o outro com "BACK-END".
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
    npm i
    ```

3. Para iniciar o servidor front-end, execute o seguinte comando no terminal:

    ```
    npm run dev
    ```

## Executando o projeto

Certifique-se de seguir as etapas de configuração adequadas antes de executar o projeto. Aqui está como executar cada parte:

- **Front-end**: No terminal do VSCode "DE_OLHO", execute o comando `npm run dev` para iniciar o servidor front-end.

- **Back-end**: No terminal do VSCode "BACK-END", execute o comando `python web.py` para iniciar o servidor back-end.

Lembre-se de que você precisa ter o MySQL Workbench configurado corretamente, e se tem o python 3 instalado.

Ps: caso o banco de dados estaja sem informações rode antes o arqivo "boot" com o comando "python boot.py" ele ira alimentar o bano de dados com os dados da api
