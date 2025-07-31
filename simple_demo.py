import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_simple_dataset():
    """Create a simple dataset with a few movies."""
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
    
    df = pd.DataFrame(data)
    return df

def recommend_movies(df, movie_title, top_n=3):
    """Recommend similar movies based on a given movie title."""
    if movie_title not in df['title'].values:
        return f"Movie '{movie_title}' not found in dataset."
    
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
            'year': movie_data['year'],
            'rating': movie_data['rating'],
            'similarity_score': round(similarity_scores[i+1][1], 3)
        })
    
    return recommendations

def main():
    """Main function to demonstrate the movie recommendation system."""
    print("🎬 SIMPLE MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)
    
    # Create dataset
    df = create_simple_dataset()
    print(f"✅ Dataset created with {len(df)} movies!")
    
    # Show available movies
    print("\n📽️ Available movies:")
    for i, title in enumerate(df['title'], 1):
        print(f"{i:2d}. {title}")
    
    # Example recommendations
    print("\n🎯 RECOMMENDATION EXAMPLES")
    print("=" * 50)
    
    test_movies = ["Inception", "The Dark Knight", "The Notebook"]
    
    for movie in test_movies:
        print(f"\n🎬 Because you liked '{movie}', you might also enjoy:")
        print("-" * 50)
        
        recommendations = recommend_movies(df, movie, 3)
        
        if isinstance(recommendations, str):
            print(f"❌ {recommendations}")
        else:
            for rec in recommendations:
                print(f"🏆 {rec['rank']}. {rec['title']} ({rec['year']})")
                print(f"   Genre: {rec['genre']}")
                print(f"   Rating: {rec['rating']}/10")
                print(f"   Similarity: {rec['similarity_score']}")
                print()
    
    # Dataset analysis
    print("\n📊 DATASET ANALYSIS")
    print("=" * 30)
    print(f"Total movies: {len(df)}")
    print(f"Year range: {df['year'].min()} - {df['year'].max()}")
    print(f"Average rating: {df['rating'].mean():.2f}")
    print(f"Rating range: {df['rating'].min():.1f} - {df['rating'].max():.1f}")
    
    # Top rated movies
    print(f"\n🏆 TOP RATED MOVIES:")
    top_movies = df.nlargest(5, 'rating')
    for i, (_, movie) in enumerate(top_movies.iterrows(), 1):
        print(f"{i}. {movie['title']} ({movie['year']}) - Rating: {movie['rating']}")
    
    print("\n🎉 Demo completed! This demonstrates:")
    print("✅ TF-IDF vectorization of movie descriptions")
    print("✅ Cosine similarity calculation")
    print("✅ Content-based movie recommendations")
    print("✅ Similarity scoring and ranking")

if __name__ == "__main__":
    main() 