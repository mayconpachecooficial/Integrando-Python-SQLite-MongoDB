from pymongo import MongoClient

# Substitua 'your_connection_string' pela sua string de conexão do MongoDB Atlas
mongo_uri = 'your_connection_string'
client = MongoClient(mongo_uri)

# Criação de um banco de dados e uma coleção
db = client['bank_database']
collection = db['bank']

# Inserção de documentos
# Documento exemplo para um cliente com duas contas
cliente_documento = {
    "nome": "João Silva",
    "cpf": "12345678901",
    "contas": [
        {"numero_conta": "000123", "saldo": 1000},
        {"numero_conta": "000124", "saldo": 1500}
    ]
}

# Inserindo o documento na coleção
collection.insert_one(cliente_documento)

# Recuperação de Informações
# Consulta todos os clientes
for cliente in collection.find():
    print(cliente)

# Consulta um cliente específico pelo CPF
cliente_especifico = collection.find_one({"cpf": "12345678901"})
print(cliente_especifico)

# Consulta clientes com saldo maior que um valor específico em uma de suas contas
clientes_saldo_maior = collection.find({"contas.saldo": {"$gt": 1200}})
for cliente in clientes_saldo_maior:
    print(cliente)
