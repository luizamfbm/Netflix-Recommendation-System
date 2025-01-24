from flask import Flask, request, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Inicializar a aplicação Flask
app = Flask(__name__)


data = pd.read_csv('netflix_processed.csv')


tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['content'])


cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend(title):
    indices = pd.Series(data.index, index=data['title'].str.lower()).drop_duplicates()
    title = title.lower().strip()

    if title not in indices:
        return f"Title '{title}' not found. Please try typing another one"

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    recommended_indices = [i[0] for i in sim_scores]
    return data['title'].iloc[recommended_indices].tolist()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def get_recommendations():
    title = request.form['title']  #Obtém o título do formulário
    recommendations = recommend(title)

    # Verifica se houve um erro na recomendação
    if isinstance(recommendations, str):
        return render_template('index.html', error=recommendations)
    else:
        return render_template('index.html', title=title, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
