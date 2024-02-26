Este projeto foi feito para estabelecer uma base sólida usando SQLAlchemy, uma biblioteca Python que facilita a comunicação entre programas Python e bancos de dados usando SQL de uma maneira mais pythonic. O objetivo era modelar um sistema simples de banco que incluísse clientes e suas respectivas contas, refletindo as operações bancárias básicas e a relação entre as entidades.
Iniciei definindo as classes Cliente e Conta usando o paradigma ORM (Object-Relational Mapping) proporcionado pelo SQLAlchemy. Cada Cliente poderia ter várias Contas, estabelecendo uma relação um-para-muitos entre as entidades. Utilizei o SQLite como o sistema de gestão de banco de dados por sua simplicidade e facilidade de integração.
Após configurar as classes e o banco de dados, prossegui com a inserção de dados, criando um cliente de exemplo, "João Silva", e uma conta associada a ele com saldo inicial. Em seguida, implementei consultas para recuperar informações sobre clientes e suas contas, demonstrando a capacidade do sistema de gerenciar e acessar dados relacionais de maneira eficiente.
A segunda parte do projeto representou uma transição do mundo estruturado e relacional para o dinâmico e flexível mundo NoSQL, utilizando MongoDB como banco de dados e PyMongo para interagir com ele. O objetivo era fornecer uma visão agregada dos dados de clientes e contas, agrupando as informações em documentos únicos por cliente, refletindo a natureza flexível e escalável dos bancos de dados NoSQL.
Conectei-me ao MongoDB Atlas, um serviço de banco de dados como serviço (DBaaS) que oferece MongoDB hospedado na nuvem, criando um novo banco de dados e definindo uma coleção bank para armazenar os documentos dos clientes. Em seguida, inseri documentos que representavam os clientes e suas contas, mantendo a integridade e a relação entre as entidades, mas em um formato que refletia a estrutura de dados do NoSQL.
Para finalizar, desenvolvi instruções de recuperação de informações utilizando os pares chave-valor, demonstrando a flexibilidade e a eficiência do MongoDB para operações de leitura e consulta de dados.
