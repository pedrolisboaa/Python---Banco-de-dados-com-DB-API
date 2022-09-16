# Forma de evitar SQL inject

import MySQLdb

nome_ = 'Pereira'
idade_ = 15

conexao = MySQLdb.connect(user="root", passwd="1234", db="clientes", host="localhost", port=3306, autocommit=False)
cursor = conexao.cursor()

cursor.execute("INSERT INTO cliente (nome, idade) VALUES (?, ?)", (nome_, idade_))
conexao.commit()


cursor.execute("SELECT *  FROM cliente")
for _ in cursor.fetchall():
    print(_)
cursor.close()
conexao.close()