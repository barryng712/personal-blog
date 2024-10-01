import os
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key in production

ARTICLES_DIR = 'articles'
if not os.path.exists(ARTICLES_DIR):
    os.makedirs(ARTICLES_DIR)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def load_articles():
    articles = []
    for filename in os.listdir(ARTICLES_DIR):
        with open(os.path.join(ARTICLES_DIR, filename), 'r') as file:
            article = json.load(file)
            articles.append(article)
    return sorted(articles, key=lambda x: x['date'], reverse=True)

@app.route('/')
def home():
    articles = load_articles()
    return render_template('home.html', articles=articles)

@app.route('/article/<int:id>')
def article(id):
    articles = load_articles()
    article = next((a for a in articles if a['id'] == id), None)
    if article:
        return render_template('article.html', article=article)
    return redirect(url_for('home'))

@app.route('/admin')
@login_required
def admin():
    articles = load_articles()
    return render_template('admin.html', articles=articles)

@app.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = request.form['date']
        articles = load_articles()
        new_id = max([a['id'] for a in articles], default=0) + 1
        article = {'id': new_id, 'title': title, 'content': content, 'date': date}
        with open(os.path.join(ARTICLES_DIR, f'{new_id}.json'), 'w') as file:
            json.dump(article, file)
        return redirect(url_for('admin'))
    return render_template('new.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    articles = load_articles()
    article = next((a for a in articles if a['id'] == id), None)
    if not article:
        return redirect(url_for('admin'))
    
    if request.method == 'POST':
        article['title'] = request.form['title']
        article['content'] = request.form['content']
        article['date'] = request.form['date']
        with open(os.path.join(ARTICLES_DIR, f'{id}.json'), 'w') as file:
            json.dump(article, file)
        return redirect(url_for('admin'))
    return render_template('edit.html', article=article)

@app.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    file_path = os.path.join(ARTICLES_DIR, f'{id}.json')
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('admin'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'password':
            session['logged_in'] = True
            return redirect(url_for('admin'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
