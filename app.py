from flask import Flask, jsonify, request, abort, make_response, render_template
import json
from flask_sqlalchemy import SQLAlchemy
import random

with open('config.json') as c:
    params = json.load(c)['params']

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=params['username'],
    password=params['password'],
    hostname=params['hostname'],
    databasename=params['databasename'],
)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/quotebuddy" -> uncomment this when running local
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


############################################
# ROOT
############################################
@app.route('/')
def query_developer_details():
    return jsonify({
        "author": "TheBotbox",
        "author_url": "http://thebotbox.online/",
        "base_url": "thebotbox.pythonanywhere.com",
        "project_name": "QuoteBuddy",
        "project_url": "https://github.com/TheBotBox/QuoteBuddy"
    })


class Quotes(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    quote = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(30), nullable=False)


############################################
# GET RANDOM QUOTE
############################################

@app.route('/get-random-quote', methods=['GET'])
def get_random():
    try:
        all_quotes = Quotes.query.filter_by().all()
        length_of_quotes = len(all_quotes)
        quote_id = random.randint(1, length_of_quotes)
        quote = Quotes.query.filter_by(id=quote_id).first()
        return make_response(jsonify({
            'quote': quote.quote,
            'author': quote.author,
            'quote_id': quote.id
        }), 200)
    except:
        return make_response(jsonify({
            'error': 'Quote not found'
        }), 404)


############################################
# GET QUOTE BY ID
############################################

@app.route('/get-quote/<string:quote_id>', methods=['GET'])
def get_quotes_by_id(quote_id):
    try:
        quote = Quotes.query.filter_by(id=quote_id).first()
        if int(quote.id) != int(quote_id):
            abort(404)
    except:
        abort(404)
    return make_response(jsonify({'quote': quote.quote,
                                  'author': quote.author,
                                  'quote_id': quote.id}), 200)


############################################
# CREATE QUOTE
############################################


@app.route('/create-quote', methods=['POST'])
def create_quote():
    if not request.json:
        return make_response(jsonify({'error': 'Invalid request. JSON expected'}), 400)
    if 'quote' not in request.json:
        return make_response(jsonify({'error': "'quote' missing"}), 400)
    if 'author' not in request.json:
        return make_response(jsonify({'error': "'author' missing"}), 400)

    request_quote = request.json['quote']
    request_author = request.json['author']

    entry = Quotes(quote=request_quote, author=request_author)

    db.session.add(entry)
    db.session.commit()
    return make_response(jsonify({'message': 'Quote updated successfully',
                                  'quote_id': entry.id}), 200)


############################################
# CLEAR TABLE | NEEDS CREDENTIALS
############################################


@app.route('/clear-table', methods=['POST'])
def clear_table():
    if not request.json:
        return make_response(jsonify({'error': 'Invalid request. JSON expected'}), 400)
    if 'username' not in request.json:
        return make_response(jsonify({'error': "'username' missing"}), 400)
    if 'password' not in request.json:
        return make_response(jsonify({'error': "'password' missing"}), 400)

    user_name = request.json['username']
    password = request.json['password']

    if user_name == params['clear_table_user_name'] and password == params['clear_table_password']:
        db.session.query(Quotes).delete()
        db.session.commit()

        return make_response({
            'message': 'table cleared'
        }, 200)
    else:
        return make_response(jsonify({
            'error': 'Unauthorized to delete table'
        }), 401)


############################################
# 404 Handling
############################################

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Quote not found'}), 404)


############################################
# Post a quote -> GUI Panel
############################################
@app.route('/post-quote', methods=['GET', 'POST'])
def post_quote():
    if request.method == 'POST':
        request_quote = request.form.get('post_a_quote')
        request_author = request.form.get('author')

        entry = Quotes(quote=request_quote, author=request_author)

        db.session.add(entry)
        db.session.commit()
        return make_response(jsonify({'message': 'Quote updated successfully',
                                      'quote_id': entry.id}), 200)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
