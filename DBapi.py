import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent


conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()
def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()
def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", data)
    conexao.commit()
def excluir_item(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()
def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome,email) VALUES(?,?)", dados)
    conexao.commit()
def recuperar_cliente(cursor):
    cursor.execute("SELECT * FROM clientes ")
    return cursor.fetchone()

def recuperar_todos(cursor):
    cursor.execute("SELECT * FROM clientes")
    colunas = [desc[0] for desc in cursor.description]  # Obtém os nomes das colunas
    return [dict(zip(colunas, linha)) for linha in cursor.fetchall()]

cliente = recuperar_todos(cursor)
print(cliente)



#dados = [
#    ("Guilherme Jorel", "guilhermer@hot.com.br"),
#    ("Erik Jhones", "erikmer@hot.com.br"),
#    ("Jader Junio", "jadermer@hot.com.br"),
#    ("Felipe Ranaudo", "ranaudomer@hot.com.br")
#]
#inserir_muitos(conexao, cursor,dados)
#inserir_registro(conexao, cursor,"Guilherme Carvalho", 'gui@gmail.com;')
#inserir_registro(conexao, cursor, 'Giovana Nanues', 'giovana.serra@hot.com.br;')
#atualizar_registro(conexao, cursor, "Guilherme Carvalho", 'gui@gmail.com', 1)
#atualizar_registro(conexao, cursor, 'Giovana Nanues', 'giovana.serra@hot.com.br', 2)
#excluir_item(conexao, cursor, 4)

