# Importando as bibliotecas necessárias, Flask e mysql-connector
from flask import *
import PROJETOintegrador, projetointegrador2


# Iniciando a configuração da conexão com o banco de dados
PROJETOintegrador.conexao()


# Iniciando o Flask
app = Flask(__name__)


# Rota da página inicial
@app.route("/")
def index():
    return render_template("index.html")


# Rota da página inicial após o usuário realizar o cadastro
@app.route("/inicio.html")
def inicio():
    return render_template("inicio.html")


# Rota da página de cadastro
@app.route("/cadastro.html")
def cadastro():
    return render_template("cadastro.html")


# Rota da página de confirmação do cadastro
@app.route("/confirmar_cadastro", methods=["POST"])
def confirmar_cadastro():

    # Verificando se o método de requerimento é o POST
    if request.method == "POST":

        # Armazenando os valores obtidos pelo requerimento
        email = request.form['email']
        usuario = request.form['usuario']
        senha = request.form['senha']
        

        reques_cadas = PROJETOintegrador.cadastro(email, usuario, senha, 0)
        if reques_cadas == 1: 
            # Print que mostra no terminal os valores recebidos (apenas para confirmação)
            print(f"\n O email é: {email}, O usuário é: {usuario}, A senha é: {senha}\n")

            print("\nO resultado do requerimento foi: Sucesso\n")

            # Após o fim da confirmação o usuário é redirecionado para a página inicial já cadastrado
            return redirect(url_for('inicio'))
        else:
            return redirect(url_for('inicio'))
    

# Rota da página de login
@app.route("/login.html")
def login():
    return render_template("login.html")


# Rota da página de confirmação do login
@app.route("/logar_conta", methods=["POST"])
def logar_conta():

    # Verificando se o método do requerimentos é o POST
    if request.method == "POST":
        
        # Armazenando os valores obtidos pelo requerimento
        usuario = request.form['usuario']
        senha = request.form['senha']

        reques_log = PROJETOintegrador.entrar(usuario, senha)
        
        if reques_log == 1:
            # Print que mostra no terminal os valores recebidos (apenas para confirmação)
            print(f"\n O usuário: {usuario}, A senha é: {senha}\n")

            print("\nO resultado do requerimento foi: Sucesso\n")

            # Após o fim da confirmação o usuário é redirecionado para a página inicial com o login já feito
            return redirect(url_for('inicio'))
        else:
            return redirect(url_for('inicio'))

# Rota da página de empréstimo
@app.route('/emprestimo.html')
def emprestimo():
    return render_template('emprestimo.html')


# Rota da página de confirmação do empréstimo
@app.route("/emprestar_livro", methods=["POST"])
def emprestar_livro():
 
    # Verificando se o método do requerimentos é o POST
    if request.method == "POST":
       
        # Armazenando os valores obtidos pelo requerimento
        nome_do_livro = request.method['nome_do_livro']
        nome_do_autor = request.method['nome_do_autor']

        reques_emprest = PROJETOintegrador.emprestimo(nome_do_livro, nome_do_autor)
        # Print que mostra no terminal os valores recebidos (apenas para confirmação)
        print(f"\nO nome do livro é: {nome_do_livro}, O nome do autor é: {nome_do_autor}\n")
        
        print(f"\nO resultado do requerimento foi: {reques_emprest} \n")


        # Após o fim da confirmação o usuário é redirecionado para a página inicial
        return redirect(url_for('inicio'))
    else:
        return redirect(url_for('inicio'))

# Modo debug ativado
if __name__ == "__main__":
    app.run(debug=True)
