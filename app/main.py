from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine

engine = create_engine('sqlite:///\\flask\\flaskApp4\\app\\sqlite\\database.db')


def load_eliteBatters():
    with engine.connect() as conn:
        statsEB = conn.execute('SELECT * FROM elite_batters')
        stats_dict = []
        for stat in statsEB.all():
            stats_dict.append(dict(stat))
        return stats_dict


def load_eliteBowlers():
    with engine.connect() as conn:
        statsEBo = conn.execute('SELECT * FROM elite_bowlers')
        stats_dict = []
        for stat in statsEBo.all():
            stats_dict.append(dict(stat))
        return stats_dict


def load_eliteARs():
    with engine.connect() as conn:
        statsAR = conn.execute('SELECT * FROM elite_allrounders')
        stats_dict = []
        for stat in statsAR.all():
            stats_dict.append(dict(stat))
        return stats_dict

def load_articles():
    with engine.connect() as conn:
        articles = conn.execute('SELECT * FROM articles')
        articles_dict = []
        for article in articles.all():
            articles_dict.append(dict(article))
        return articles_dict

def load_batter(id):
    with engine.connect() as conn:
        statsEB = conn.execute(
            'SELECT * FROM elite_batters WHERE id= :val', val=id)
        row = statsEB.all()
        if row == 0:
            return None
        else:
            return dict(row[0])


def load_bowler(id):
    with engine.connect() as conn:
        statsEBo = conn.execute(
            'SELECT * FROM elite_bowlers WHERE id= :val', val=id)
        row = statsEBo.all()
        if row == 0:
            return None
        else:
            return dict(row[0])


def load_AR(id):
    with engine.connect() as conn:
        statsAR = conn.execute(
            'SELECT * FROM elite_allrounders WHERE id= :val', val=id)
        row = statsAR.all()
        if row == 0:
            return None
        else:
            return dict(row[0])


def load_article(id):
    with engine.connect() as conn:
        article = conn.execute('SELECT * FROM articles WHERE id= :val', val=id)
        row = article.all()
        if row == 0:
            return None
        else:
            return dict(row[0])

# -------------------------------------------------------------------------------------------


app = Flask(__name__)

app.config['SECRET_KEY'] = 'shamoil18babar56'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/statsEliteBatters')
def statsEB():
    stats = load_eliteBatters()
    if not stats:
        return 'Not Found', 404
    else:
        return render_template('statsEB.html', stats=stats)

@app.route('/statsEliteBowlers')
def statsEBo():
    stats = load_eliteBowlers()
    if not stats:
        return 'Not Found', 404
    else:
        return render_template('statsEBo.html', stats=stats)

@app.route('/statsEliteAllrounders')
def statsAR():
    stats = load_eliteARs()
    if not stats:
        return 'Not Found', 404
    else:
        return render_template('statsAR.html', stats=stats)

@app.route('/statsEliteBatters/<id>')
def statsEliteBatter(id):
    stats = load_batter(id)
    if not stats:
        return 'Not found', 404
    else: 
        return render_template('statsBatter.html', stats=stats)

@app.route('/statsEliteBowlers/<id>')
def statsEliteBowler(id):
    stats = load_bowler(id)
    if not stats:
        return 'Not found', 404
    else: 
        return render_template('statsBowler.html', stats=stats)

@app.route('/statsEliteAllrounders/<id>')
def statsEliteALlrounder(id):
    stats = load_AR(id)
    if not stats:
        return 'Not found', 404
    else: 
        return render_template('statsAllrounder.html', stats=stats)

@app.route('/articles')
def articles_list():
    articles = load_articles()
    if not articles:
        return 'Not found', 404
    else: 
        return render_template('articles_list.html', articles=articles)

@app.route('/articles/<id>')
def articles(id):
    article = load_article(id)
    if not article:
        return 'Not found', 404
    else: 
        return render_template('articles.html', article=article)

if (__name__ == '__main__'):
    app.run(debug=True)
