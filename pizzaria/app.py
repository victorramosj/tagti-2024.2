#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
# pip install python-dotenv
#pip freeze > requirements.txt
#pip install -r requirements.txt
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cardapio')
def cardapio():
    pizzas = [
        {
            "nome": "Calabresa",
            "ingredientes": "Molho de tomate, mussarela, calabresa, cebola e orégano",
            "preco": 30.00
        },
        {
            "nome": "Mussarela",
            "ingredientes": "Molho de tomate, mussarela e orégano",
            "preco": 25.00
        },
        {
            "nome": "Portuguesa",
            "ingredientes": "Molho de tomate, mussarela, presunto, ovos, cebola, azeitona e orégano",
            "preco": 35.00
        }
    ]
    return render_template("cardapio.html", pizzas=pizzas)



@app.route('/avaliacoes')
def avaliacoes():
    avaliacoes = [
        {
            "nome": "João",
            "comentario": " Muito bom",
            "nota": 4
        },
        {
            "nome": "Bia",
            "comentario": " Mais ou menos",
            "nota": 2
        },
        {
            "nome": "Anônimo",
            "comentario": "Ótima",
            "nota": 5
        }
    ]
    return render_template("avaliacoes.html", avaliacoes=avaliacoes)
app.secret_key = "123"

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None  # Variável para armazenar mensagens de feedback
    if request.method == 'POST':
        # Obter dados do formulário
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Verificar credenciais
        if email == "admin@um.com" and password == "123":
            return redirect(url_for('index'))  # Redirecionar em caso de sucesso
        else:
            message = "Credenciais inválidas. Tente novamente."
    
    # Renderizar formulário de login com mensagem (se existir)
    return render_template('login.html', message=message)

@app.route('/faleconosco', methods=['GET', 'POST'])
def faleconosco():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        mensagem = request.form.get('mensagem')

        # Aqui você pode salvar os dados no banco de dados ou processá-los
        print(f"Nome: {nome}, Email: {email}, Mensagem: {mensagem}")

        # Exibir uma página de agradecimento ou redirecionar para outra página
        return redirect(url_for('index'))  # Exemplo de redirecionamento para a página inicial
    
    return render_template('faleconosco.html')



if __name__ == '__main__':
    app.run()
