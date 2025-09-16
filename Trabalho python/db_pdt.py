import sqlite3
# conexao=sqlite3.connect('catalogo.db')
# cursor=conexao.cursor()
# cursor.execute('''CREATE TABLE catalogo(
#     id INTEGER,
#     categoria TEXT NOT NULL,
#     nome TEXT NOT NULL,
#     valor REAL,
#     quantidade INTEGER NULL
#     );''')

with sqlite3.connect('catalogo.db') as conexao:
    cursor= conexao.cursor()



#Atualizar produto quantidade
def upd_qnt(q,n): 
    with sqlite3.connect('catalogo.db') as conexao:
        cursor= conexao.cursor()
        cursor.execute(f'''UPDATE catalogo SET quantidade = '{q}' WHERE nome='{n}' ''')
        print("O produto foi atualizado com sucesso")
        conexao.commit()

#Atualizar produto valor
def upd_valor(v,n): 
    with sqlite3.connect('catalogo.db') as conexao:
        cursor= conexao.cursor()
        cursor.execute(f'''UPDATE catalogo SET valor  = '{v}' WHERE nome='{n}' ''')
        conexao.commit()
        print("O produto foi atualizado com sucesso")

#Somar quantidade
def sm_qnt(q,n):
    with sqlite3.connect('catalogo.db') as conexao:
        cursor= conexao.cursor()
        cursor.execute("SELECT quantidade FROM catalogo WHERE nome = ?",(n,))
        s= cursor.fetchone()[0] + q
        cursor.execute(f"UPDATE catalogo SET quantidade  = '{s}' WHERE nome='{n}'")
        conexao.commit
        print("O produto foi atualizado com sucesso")






#Deletar produto
def dlt_prt(id):
    with sqlite3.connect('catalogo.db') as conexao:
        cursor= conexao.cursor()
        cursor.execute(f"DELETE FROM catalogo WHERE id = '{id}'" )
        conexao.commit()


#Novo produto
def new_prt(categoria,nome,valor,quantidade):
    with sqlite3.connect('catalogo.db') as conexao:  # Sem acento no nome do banco
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM catalogo WHERE nome = ?", (nome,))
        resultado= cursor.fetchone()
        if resultado:
            print("Já temos esse produto")
            print("Essa quantidade é pra somar ou mudar o quantidade:" )
            while True:
                q = input(
                "\n\033[1;31m ---------------COLOQUE APENAS OS NUMEORS------------------------\033[m"
                "\n[1]-Somar a quantidade" \
                "\n[2]-Mudar a quantidade"\
                "\n[3]-Mudar o valor" \
                "\n\033[1;31m-------------------------------------------------------\033[m" \
                "\nO que vai querer:")
                if q.strip().isdigit() == True:
                    if int(q) == 1:
                        sm_qnt(quantidade,nome)
                        break
                    elif int(q) == 2:
                        upd_qnt(quantidade,nome)
                        break
                    elif int(q)== 3:
                        upd_valor(valor,nome)
                        break
                    elif int(q)>3:
                        print("\033[1;31m Digite apenas números 1,2,3!!".upper()+"\033[m")
                        
                else:                        
                    print("\033[1;31m Digite apenas números 1,2,3!!".upper()+"\033[m")        
                                
        else:
            cursor.execute("SELECT MAX(id) FROM catalogo")
            max_id= cursor.fetchone()[0]
            if max_id is None:
                id = 1
            else:
                id = max_id + 1
            cursor.execute("INSERT INTO catalogo (id,categoria,nome,valor,quantidade) VALUES(?,?,?,?,?)", (id,categoria.upper(),nome.upper(),valor,quantidade))
            conexao.commit()
            print(f"O produto {nome} cadastrado com sucesso! ID: {id}")
            return True
    

#dlt_prt(12)
#new_prt("Higiene", "Sabonete Dove", 3.80, 80)
    

#Listas de produto pelo id
def lista_id_prt(id):
    with sqlite3.connect('catalogo.db') as conexao:
        cursor= conexao.cursor()
        cursor.execute("SELECT * FROM catalogo WHERE id= ?", (id,))
        lista=cursor.fetchall()
        for c in lista:
           print(lista)


#Listas de produto pela categoria
def lista_ct_prt(categoria):
    with sqlite3.connect('catalogo.db') as conexao:
        cursor= conexao.cursor()
                
        # Busca itens que a categoria começa com o termo
        cursor.execute("SELECT * FROM catalogo WHERE categoria LIKE ?", (f'{categoria.upper().strip()}%',))
        lista_inicio = cursor.fetchall()
        
        # Busca itens que a categoria contêm o termo (em qualquer posição)
        cursor.execute("SELECT * FROM catalogo WHERE categoria LIKE ?", (f'%{categoria.upper().strip()}%',))
        lista_contem = cursor.fetchall()
        
        # Exibe os resultados de forma organizada
        if lista_inicio:
            print(f"\n--- Categorias que COMEÇAM com '{categoria.upper().strip()}' ({len(lista_inicio)} encontrados) ---")
            for item in lista_inicio:
                print(item)
        
        else:
            # Se não encontrou itens que começam, busca itens que CONTÊM a letra
            cursor.execute("SELECT * FROM catalogo WHERE categoria LIKE ?", (f'%{categoria.upper().strip()}%',))
            lista_contem = cursor.fetchall()
            
            if lista_contem:
                print(f"\n--- Itens que CONTÊM '{categoria.upper().strip()}' ({len(lista_contem)} encontrados) ---")
                for item in lista_contem:
                    print(item)
            else:
                print(f"\nNenhum item encontrado começando com ou contendo '{categoria.upper().strip()}'.")


#Listas de produto pelo nome
def lista_nm_prt(nome):
    with sqlite3.connect('catalogo.db') as conexao:
        cursor = conexao.cursor()
        
        # Primeiro busca itens que COMEÇAM com a letra
        cursor.execute("SELECT * FROM catalogo WHERE nome LIKE ?", (f'{nome.upper().strip()}%',))
        lista_inicio = cursor.fetchall()
        
        cursor.execute("SELECT * FROM catalogo WHERE nome LIKE ?", (f'%{nome}%',))
        lista_contem = cursor.fetchall()

        if lista_inicio:
            print(f"\n--- Itens que COMEÇAM com '{nome.upper().strip()}' ({len(lista_inicio)} encontrados) ---")
            for item in lista_inicio:
                print(item)
        else:
            # Se não encontrou itens que começam, busca itens que CONTÊM a letra
            cursor.execute("SELECT * FROM catalogo WHERE nome LIKE ?", (f'%{nome.upper().strip()}%',))
            lista_contem = cursor.fetchall()
            
            if lista_contem:
                print(f"\n--- Itens que CONTÊM '{nome.upper().strip()}' ({len(lista_contem)} encontrados) ---")
                for item in lista_contem:
                    print(item)
            else:
                print(f"\nNenhum item encontrado começando com ou contendo '{nome.upper().strip()}'.")

#Listas de produto pelo valor
def lista_vl_prt(valor):
    with sqlite3.connect('catalogo.db') as conexao:
        cursor= conexao.cursor()
        cursor.execute("SELECT * FROM catalogo WHERE valor LIKE ?",(f'{valor}%',))
        lista=cursor.fetchall()
        print(f"\n--- Itens que Tem com valor '{valor}' ({len(lista)} encontrados) ---")
        for c in lista:
            print(c)



#Listas de produto pela quantidade
def lista_qt_prt(quantidade):
    with sqlite3.connect('catalogo.db') as conexao:
        cursor= conexao.cursor()
        cursor.execute("SELECT * FROM catalogo WHERE quantidade LIKE ?" , (f'{quantidade}%',))
        lista=cursor.fetchall()
        for c in lista:
            print(c)



























































































































































































































































