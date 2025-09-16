import sqlite3

#criando tabela
#conexao=sqlite3.connect('usuario.db') 
#cursor = conexao.cursor()
#cursor.execute('''CREATE TABLE usuario( 
#               id INTEGER , 
#               nome  TEXT NOT NULL,
#                email  TEXT NOT NULL,
#               senha TEXT NOT NULL  );''')
#
#Inseir dados na tabela 
#cursor.execute('''INSERT INTO usuario (nome,email,senha) VALUES('Ana Beatriz  ','ana.beatriz1994@example.com','A8#vR4xZ')''' )

#Nova Conta
def new_usu(nome,email,senha):
    with sqlite3.connect('usuario.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuario WHERE email = ?", (email,))
        resultado= cursor.fetchone()
        if resultado:
                print("Esse email já tem uma conta")
                return False
        cursor.execute("SELECT MAX(id) FROM usuario")
        max_id = cursor.fetchone()[0]
        if max_id is None:
             id = 1
        else:
             id = max_id + 1
        cursor.execute("INSERT INTO usuario (id,nome,email,senha) VALUES(?,?,?,?)",(id,nome.upper(),email.strip(),senha) )
        conexao.commit()
        print(f"Usuário {nome} cadastrado com sucesso! ID: {id}")
        return True


#new_usu("Caim","caim.03@example.com","Ca5$wL1m")



#Atualizar as senhas
def changer_pw(email,newpw):
    with sqlite3.connect('usuario.db') as conexao:
      cursor = conexao.cursor()
      cursor.execute(f"UPDATE usuario SET senha = '{newpw}' WHERE email = '{email}' ")
      conexao.commit()
    print("Senha mudada com sucesso")

#Buscar conta
def find_usu(email,senha):
    with sqlite3.connect('usuario.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuario WHERE email = ? and senha = ?" , (email,senha,) )
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute("SELECT nome FROM usuario WHERE email = ? and senha = ?", (email,senha,))
            nome= cursor.fetchone()
            print(f"Seja bem-vindo {nome[0]}")
            return True
        else :
            print("Senha ou email estão errados")
        conexao.commit()





#Deletar conta
def dlt_usu(email):
    with sqlite3.connect('usuario.db') as conexao:
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM usuario WHERE email = '{email}'" )
        conexao.commit()


#Imprimindo os dados
#   with sqlite3.connect('usuario.db') as conexao:
#       cursor = conexao.cursor()
#       cursor.execute('''SELECT * FROM usuario''')
#       resultado= cursor.fetchall()
#   
#   for c in resultado:
#       print(c)
#       print(c.count('caim.03@example.com'))
#       print(c.count('Ca1m4t4d0r'))

