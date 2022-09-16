import MySQLdb

banco = MySQLdb.connect(user="root", passwd="1234", db="clientes", host="localhost", port=3306, autocommit=True)
cursor = banco.cursor()

# CRUD - MOSTRANDO DADOS
# Selecionado todos dados do banco
cursor.execute("SELECT * FROM cliente")
for cliente in cursor.fetchall():
    print(cliente)

cursor.execute("SELECT * FROM cliente")
for cliente in cursor.fetchmany(2):
    print(cliente)

# CRUD - INSERINDO DADO
cursor.execute("INSERT INTO cliente (nome, idade) VALUES ('Marcela', 24)")
# caso o autocommit la encima estava off é necessário ealizar o commit para subir para o banco banco.commit()
cursor.execute("SELECT * FROM cliente")
print(cursor.fetchall())

# CRUD - ATUALIZAR DADO
cursor.execute("UPDATE cliente SET nome='PEDRO HENRIQUE' WHERE idade=29 and idcliente=1")

# CRUD - DELETANDO DADO
cursor.execute("DELETE FROM cliente WHERE idcliente % 2 = 0")

banco.close()
print('Banco fechado.')
