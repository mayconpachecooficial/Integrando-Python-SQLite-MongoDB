# Importações necessárias
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Configuração Base
Base = declarative_base()

# Definição da classe Cliente
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String)
    # Relacionamento um-para-muitos com Conta
    contas = relationship("Conta", back_populates="cliente")

# Definição da classe Conta
class Conta(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    numero_conta = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    # Relacionamento muitos-para-um com Cliente
    cliente = relationship("Cliente", back_populates="contas")

# Configuração do Engine e criação das tabelas
engine = create_engine('sqlite:///banco_de_dados.db', echo=False)
Base.metadata.create_all(engine)

# Configuração da Sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de Dados
# Criação de um cliente
novo_cliente = Cliente(nome="João Silva", cpf="12345678901")
session.add(novo_cliente)
session.commit()

# Criação de uma conta para o cliente
nova_conta = Conta(numero_conta="000123", saldo=1000, cliente_id=novo_cliente.id)
session.add(nova_conta)
session.commit()

# Recuperação de Dados
# Consulta todos os clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"Cliente: {cliente.nome}, CPF: {cliente.cpf}")

# Consulta contas de um cliente específico
contas_do_joao = session.query(Conta).filter(Conta.cliente_id == novo_cliente.id).all()
for conta in contas_do_joao:
    print(f"Conta Número: {conta.numero_conta}, Saldo: {conta.saldo}")

# Encerramento da sessão
session.close()
