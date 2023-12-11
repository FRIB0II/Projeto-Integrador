# import tkinter as tk
import mysql.connector
# from tkinter import *
import projetointegrador2
from datetime import datetime,timedelta

def conexao():
    global meuBancoDeDados
    meuBancoDeDados = mysql.connector.connect(
        host="localhost",
        user="root",
        database="bd_projeto"
    )
    meuCursor = meuBancoDeDados.cursor()
    return meuCursor


def entrar(usuario_login, senha_login):
  log = projetointegrador2.login1(usuario_login, senha_login)
  inserir2(log)
  cont =1 
  return cont

"""
def cadastrar():
 
 root = tk.Tk()
 root.geometry("450x300")
 root.title("Fazer o cadastro")

 label1 = tk.Label(root, text="Email:" )
 label1.place(x=50, y=20)

 global entry1
 global entry2
 global entry3

 entry1 = tk.Entry(root, width=35)
 entry1.place(x=100, y=20, width=100)

 label2 = tk.Label(root, text="Usuário:")
 label2.place(x=50, y=50)

 entry2 = tk.Entry(root, width=35)
 entry2.place(x=100, y=50, width=100)

 label3 = tk.Label(root, text="Senha:")
 label3.place(x=50, y=80)

 entry3 = tk.Entry(root, width=35 )
 entry3.place(x=100, y=80, width=100)

 botao = tk.Button(root, text="CADASTRAR", bg='lightblue', command = cadastro)
 botao.place(x=110, y=110, width=75)
 """

def cadastro(email_cad, usuario_cad, senha_cad, cod):
 cad = projetointegrador2.cadastro1(email_cad, usuario_cad, senha_cad, cod)
 inserir(cad)
 cont = 1
 return cont
 

def inserir(cadastro1):
    meuCursor = conexao()
    sql = "INSERT INTO cadastro2 (email, usuario, senha) VALUES (%s, %s, %s)"
    valor = (cadastro1.email, cadastro1.usuario, cadastro1.senha)
    meuCursor.execute(sql, valor)

    meuBancoDeDados.commit()
    print(meuCursor.rowcount, "registro inserido.")
    # livro()


def inserir2(login1):
    meuCursor = conexao()
    sql = "INSERT INTO login3 (usuario, senha) VALUES (%s, %s)"
    valor = (login1.usuario, login1.senha)
    meuCursor.execute(sql, valor)

    meuBancoDeDados.commit()
    consultar()

"""
def login():

 root = tk.Tk()
 root.geometry("450x300")
 root.title("Fazer o login")

 label1 = tk.Label(root, text="Usuário:" )
 label1.place(x=130, y=20)

 global entryy1
 global entryy2

 entryy1 = tk.Entry(root, width=35)
 entryy1.place(x=100, y=50, width=100)

 label2 = tk.Label(root, text="Senha:")
 label2.place(x=130, y=80)

 entryy2 = tk.Entry(root, width=35)
 entryy2.place(x=100, y=110, width=100)

 botao = tk.Button(root, text="ENTRAR", bg='lightblue', command = entrar)
 botao.place(x=120, y=150, width=55)
"""

def consultar():
    meuCursor = conexao()
    sql = "SELECT * FROM cadastro2"
    meuCursor.execute(sql)

    meusResultados = meuCursor.fetchall()
    

    meuCursor2 = conexao()
    sql2 = "SELECT * FROM login3"
    meuCursor2.execute(sql2)

    meusResultados2 = meuCursor2.fetchall()

    aux = 0
    for resultado in meusResultados2:
       aux +=1
    
    listalog= []
    cont = 0
    
    for resultado in meusResultados2:
       loog = projetointegrador2.login1(resultado[0], resultado[1])
       listalog.append(loog)
       cont +=1
       if cont == aux:
          auxlog = loog.usuario
          auxlog2 = loog.senha 


    #listacad = []
    cont2 = 0 
    for resultado in meusResultados:
        caad = projetointegrador2.cadastro1(resultado[0], resultado[1], resultado[2], resultado[3])
        auxcad = caad.usuario
        auxcad2 = caad.senha
        global codcad
        codcad = caad.cod

        #listacad.append(caad)
        
        if auxlog == auxcad and auxlog2 == auxcad2:
           print("Login existente")
           cont2 = 1
           #livro()
    if cont2 != 1:
        print("Login não existe, faça o seu cadastro")    

"""    
def pesquisa():
   
   livro1 = entry4.get()
   livro2 = entry5.get()

   meuCursor = conexao()
   sql = "SELECT * FROM livro"
   meuCursor.execute(sql)

   meusResultados = meuCursor.fetchall()
 
   global cont 
   cont = 0

   for resultado in meusResultados: 
     liv = projetointegrador2.livro(resultado[0],resultado[1], resultado[2])
     liv1 = liv.titulo
     liv2 = liv.autor
     global liv3
     liv3 = liv.cod
     if liv1 == livro1 and liv2 == livro2:
        print("Livro encontrado")
        cont = 1

   if cont != 1:
        print("Livro nao existe")
  
def livro():
 root = tk.Tk()
 root.geometry("450x300")
 root.title("Livro")

 label1 = tk.Label(root, text="Título:" )
 label1.place(x=45, y=20)

 global entry4
 global entry5

 entry4 = tk.Entry(root, width=35)
 entry4.place(x=100, y=20, width=100)

 label2 = tk.Label(root, text="Autor:")
 label2.place(x=45, y=80)

 entry5 = tk.Entry(root, width=35)
 entry5.place(x=100, y=80, width=100)

 botao2 = tk.Button(root, text="EMPRESTAR", bg='lightblue', command = emprestimo)
 botao2.place(x=115, y=120, width=70)
 root.mainloop()"""

def emprestimo(titulo, autor):
   print('Socorro')
   livro1 = titulo
   livro2 = autor

   meuCursor = conexao()
   sql = "SELECT * FROM livro"
   meuCursor.execute(sql)

   meusResultados = meuCursor.fetchall()
   
   global cont 
   cont = 0
   print('Sucesso')
   for resultado in meusResultados: 
     print('Sucesso 2')
     liv = projetointegrador2.livro(resultado[0],resultado[1], resultado[2])
     liv1 = liv.titulo
     liv2 = liv.autor
     global liv3
     print('Sucesso 3')
     if liv1 == livro1 and liv2 == livro2:
        print("Livro encontrado")
        cont = 1
        liv3 = liv.cod

   if cont != 1:
        print("Livro nao existe")

   if cont==1:
      dataAtual = datetime.now()
      dt_emprestimo = dataAtual.date()
      
      dt_devolucao = dt_emprestimo + timedelta(weeks=3)


      meuCursor = conexao()
      sql = "INSERT INTO emprestimo (dt_emprestimo, dt_devolucao, codlivro, codcadastro) VALUES (%s, %s, %s, %s)"
      valor = (dt_emprestimo, dt_devolucao, liv3, codcad)
      meuCursor.execute(sql, valor)
 
      meuBancoDeDados.commit()
      print("Emprestimo realizado.")
      print(f"Data da devolução: {dt_devolucao}")
      cont = 1
      return dt_devolucao
    

"""
root = tk.Tk()
root.geometry("350x200")
root.title("Escolha")

botao1 = tk.Button(root, text="Login", bg='lightblue', command = login)
botao1.place(x=80, y=40, width=55)

botao2 = tk.Button(root, text = "Cadastrar", bg= 'lightblue', command=cadastrar)
botao2.place(x=155, y=40, width=55)

root.mainloop()
"""
