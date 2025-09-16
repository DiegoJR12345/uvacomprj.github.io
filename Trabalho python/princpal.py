import Banco_de_Dados
import db_pdt

while True:
    c=0
    while True:
        mail = str( input("Email: "))
        pw = str(input("Senha: "))
        cd = Banco_de_Dados.find_usu(mail,pw)
        c += 1
        # Escreveu errado 
        if c%2==0 and cd != True:
            while True:
                try:
                    t = int(input(f"\033[1;31mNossa você errou {c} vezes \033[m"\
                             "\n \033[1;32m-------Coloque o numero------"\
                             "\n [1]-Quero tentar colocar o email e senha de novo"\
                             "\n [2]-Quero mudar a senha"\
                             "\n [3]-Quero fazer uma conta"\
                             "\n---------------------------------"
                             "\n\033[1mQual o numero:\033[m"))
                    if t == 1:
                        break
                    elif t == 2:
                        m=input("Qual o seu email? ")
                        s=input("Qual a nova senha? ")
                        Banco_de_Dados.changer_pw(m,s)
                        print("---------------------------------")
                        break
                    elif t ==3:
                        n=input( "\033[mQual o seu nome? ")
                        nm=input("\033[mQual o seu email? ")
                        ns=input("\033[mQual o sua senha? ")
                        Banco_de_Dados.new_usu(n,nm,ns)
                        print("---------------------------------")
                        break
                    elif t >3:
                        print("\033[1;31mEscolha um dos numeros")
                        print("---------------------------------\033[m")
                        continue
                except ValueError:
                    print("\033[1;31mEscolha um dos numeros")
                    print("---------------------------------\033[m")
                    continue

        # Escreveu certo
        elif cd == True:
            while True:
                q= input("----------------Oque você quer----------------------- ?\n" \
                "[1]-Quer preocura produto por id \n" \
                "[2]-Quer preocura produto por categoria \n" \
                "[3]-Quer preocura produto por nome \n" \
                "[4]-Quer preocura produto por valor\n" \
                "[5]-Quer preocura produto por quantidade\n" \
                "[6]-Sair do programa \n"
                "----------------------------------------------------\n"
                "Qual você quer : ")

                if q.strip().isdigit() == True:
                    if int(q) == 1:
                        d = str(input("Ok! Qual o id : "))
                        db_pdt.lista_id_prt(d)
                        continue

                    elif int(q) == 2:
                        d = str(input("Ok! Qual a categoria : "))
                        db_pdt.lista_ct_prt(d)
                        continue

                    elif int(q)== 3:
                        d = str(input("Ok! Qual o nome :"))
                        db_pdt.lista_nm_prt(d)
                        continue
                    
                    elif int(q)== 4:
                        d = str(input("Ok! Qual o valor : "))
                        db_pdt.lista_vl_prt(d)
                        continue

                    elif int(q)== 5:
                        d = str(input("Ok! Qual a quantidade : "))
                        db_pdt.lista_qt_prt(d)
                        continue

                    elif int(q)== 6:
                       d = print("Ok! Tchau!")
                       exit()

                    elif int(q)>6:
                        print("\033[1;31m Digite apenas números 1,2,3,4,5,6!!".upper()+"\033[m")
                    

        
                        
                else:                        
                    print("\033[1;31m Digite apenas números 1,2,3,4,5,6!!".upper()+"\033[m")        
        

        

    
        
        






