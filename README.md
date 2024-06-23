# Resumo do Projeto
## Este projeto integra Python com bancos de dados SQLite e MongoDB utilizando SQLAlchemy para o modelo ORM e pymongo para interação com MongoDB. Abaixo estão as principais funcionalidades e bibliotecas utilizadas.

## Bibliotecas Utilizadas
SQLAlchemy: Utilizada para mapear classes Python para tabelas no banco de dados SQLite e gerenciar consultas e transações.
pymongo: Utilizada para conectar e interagir com o banco de dados MongoDB.
pprint: Usada para imprimir os dados de forma mais legível.
### Funcionalidades
### Modelo ORM com SQLAlchemy:

Definição de classes Client e Account que representam tabelas no SQLite.
Criação de tabelas no banco de dados SQLite.
### Persistência de dados no SQLite.
Consultas para recuperar dados do SQLite utilizando SQLAlchemy.
###  Conexão com SQLite:

Criação de uma engine para conectar ao banco de dados.
Sessões para adicionar e manipular registros no banco de dados.
Execução de consultas para recuperar informações específicas, ordenadas e associadas entre clientes e contas.
### Conexão com MongoDB:

###  Criação de uma conexão com o MongoDB utilizando pymongo.
Definição de documentos representando clientes e suas contas.
Inserção de múltiplos documentos no MongoDB.
Consultas para recuperar documentos específicos e realizar filtros e ordenações nos dados armazenados no MongoDB.

### Execução
Para executar a aplicação, basta rodar o script principal: python app.py

Este projeto demonstra como integrar Python com bancos de dados SQL e NoSQL, permitindo manipulação e consulta de dados de maneira eficiente e organizada.

Projeto realizado por Cibele Gomes Domingos Moraes Lima 
