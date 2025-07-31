from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

app = Flask(__name__)

def create_dataset():
    """Create the movie dataset."""
    data = {
        'title': [
            'The Matrix', 'John Wick', 'Inception', 'The Notebook', 'Titanic',
            'The Avengers', 'Interstellar', 'The Dark Knight', 'Tenet',
            'Forrest Gump', 'Pulp Fiction', 'The Shawshank Redemption'
        ],
        'description': [
            'sci-fi action dystopia virtual reality computer simulation',
            'action assassin revenge fast-paced gunfights',
            'dream reality heist sci-fi mind-bending thriller',
            'romance drama emotional love story tearjerker',
            'romantic tragedy ship iceberg love disaster',
            'superhero marvel team save world action adventure',
            'space time travel family survival emotional sci-fi',
            'dark superhero joker crime gotham psychological',
            'inverted time sci-fi mystery thriller mind-bending',
            'drama comedy historical life story inspirational',
            'crime thriller dark humor violence gangster',
            'drama prison friendship hope redemption'
        ],
        'genre': [
            'Sci-Fi, Action', 'Action, Thriller', 'Sci-Fi, Thriller',
            'Romance, Drama', 'Romance, Drama', 'Action, Adventure',
            'Sci-Fi, Drama', 'Action, Drama', 'Sci-Fi, Thriller',
            'Drama, Comedy', 'Crime, Thriller', 'Drama'
        ],
        'year': [
            1999, 2014, 2010, 2004, 1997, 2012, 2014, 2008, 2020,
            1994, 1994, 1994
        ],
        'rating': [
            8.7, 7.4, 8.8, 7.8, 7.9, 8.0, 8.6, 9.0, 7.4,
            8.8, 8.9, 9.3
        ]
    }
    return pd.DataFrame(data)

def get_recommendations(df, movie_title, top_n=5):
    """Get movie recommendations."""
    if movie_title not in df['title'].values:
        return []
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['description'])
    
    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Find movie index
    movie_idx = df[df['title'] == movie_title].index[0]
    
    # Get similarity scores
    similarity_scores = list(enumerate(cosine_sim[movie_idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Get top N similar movies (excluding the movie itself)
    top_indices = [i[0] for i in similarity_scores[1:top_n+1]]
    
    recommendations = []
    for i, idx in enumerate(top_indices):
        movie_data = df.iloc[idx]
        recommendations.append({
            'rank': i + 1,
            'title': movie_data['title'],
            'genre': movie_data['genre'],
            'year': int(movie_data['year']),  # Convert numpy.int64 to regular int
            'rating': float(movie_data['rating']),  # Convert numpy.float64 to regular float
            'similarity_score': round(similarity_scores[i+1][1], 3)
        })
    
    return recommendations

# Global variables
df = create_dataset()

@app.route('/')
def index():
    """Main page."""
    movies = []
    for _, row in df.iterrows():
        movies.append({
            'title': row['title'],
            'genre': row['genre'],
            'year': int(row['year']),
            'rating': float(row['rating']),
            'description': row['description']
        })
    return render_template('index.html', movies=movies)

@app.route('/recommend', methods=['POST'])
def recommend():
    """API endpoint for getting recommendations."""
    data = request.get_json()
    movie_title = data.get('movie_title', '')
    top_n = data.get('top_n', 5)
    
    recommendations = get_recommendations(df, movie_title, top_n)
    
    return jsonify({
        'success': True,
        'recommendations': recommendations,
        'input_movie': movie_title
    })

@app.route('/movies')
def get_movies():
    """API endpoint for getting all movies."""
    movies = []
    for _, row in df.iterrows():
        movies.append({
            'title': row['title'],
            'genre': row['genre'],
            'year': int(row['year']),
            'rating': float(row['rating']),
            'description': row['description']
        })
    return jsonify(movies)

@app.route('/stats')
def get_stats():
    """API endpoint for getting dataset statistics."""
    stats = {
        'total_movies': len(df),
        'year_range': f"{int(df['year'].min())} - {int(df['year'].max())}",
        'average_rating': round(float(df['rating'].mean()), 2),
        'rating_range': f"{float(df['rating'].min()):.1f} - {float(df['rating'].max()):.1f}",
        'top_movies': df.nlargest(5, 'rating')[['title', 'year', 'rating']].to_dict('records')
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 