# Import
from flask import Flask, render_template,request, redirect
# Importowanie biblioteki bazy danych
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Podłączanie SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creating a DB
db = SQLAlchemy(app)

class Card(db.Model):
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    def __repr__(self):
        return f'<Card {self.id}>'

# Uruchamianie strony z treścią
@app.route('/')
def index():
    # Wyświetlanie obiektów Bazy w index.html
    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html',cards = cards)

# Uruchomienie strony z kartą
@app.route('/card/<int:id>')
def card(id):
    #Wyświetlanie właściwej karty według jej identyfikatora
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Uruchomienie strony i utworzenie karty
@app.route('/create')
def create():
    return render_template('create_card.html')

# Formularz karty
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        date =  request.form['date']
        text =  request.form['text']

        #Sposób przechowywania danych w bazie danych
        card = Card(title=title, date=date, text=text)
        db.session.add(card)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)