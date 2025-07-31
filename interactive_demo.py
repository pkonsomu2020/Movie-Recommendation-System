import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

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

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the application banner."""
    print("🎬" + "="*48 + "🎬")
    print("           MOVIE RECOMMENDATION SYSTEM")
    print("🎬" + "="*48 + "🎬")
    print()

def print_menu():
    """Print the main menu options."""
    print("📋 MAIN MENU:")
    print("1. 🎯 Get movie recommendations")
    print("2. 🔍 View all available movies")
    print("3. 🏆 View top rated movies")
    print("4. 📊 View dataset statistics")
    print("5. ❌ Exit")
    print()

def get_user_choice():
    """Get user choice from menu."""
    while True:
        try:
            choice = input("Enter your choice (1-5): ").strip()
            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("❌ Invalid choice. Please enter a number between 1-5.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            exit(0)

def get_movie_recommendations(df):
    """Handle movie recommendation requests."""
    print("\n🎯 MOVIE RECOMMENDATIONS")
    print("-" * 30)
    
    # Show available movies
    print("Available movies in our database:")
    movies = df['title'].tolist()
    for i, movie in enumerate(movies, 1):
        print(f"{i:2d}. {movie}")
    
    print("\nEnter a movie title from the list above:")
    movie_title = input("Movie title: ").strip()
    
    if not movie_title:
        print("❌ No movie title entered.")
        return
    
    # Get recommendations
    recommendations = recommend_movies(df, movie_title, 3)
    
    if isinstance(recommendations, str):
        print(f"❌ {recommendations}")
        return
    
    # Display recommendations
    print(f"\n🎬 Because you liked '{movie_title}', you might also enjoy:")
    print("-" * 60)
    
    for rec in recommendations:
        print(f"🏆 {rec['rank']}. {rec['title']} ({rec['year']})")
        print(f"   Genre: {rec['genre']}")
        print(f"   Rating: {rec['rating']}/10")
        print(f"   Similarity: {rec['similarity_score']}")
        print()

def view_all_movies(df):
    """Display all available movies."""
    print("\n📽️ ALL AVAILABLE MOVIES")
    print("-" * 30)
    
    for i, (_, movie) in enumerate(df.iterrows(), 1):
        print(f"{i:2d}. {movie['title']} ({movie['year']})")
        print(f"    Genre: {movie['genre']}")
        print(f"    Rating: {movie['rating']}/10")
        print()

def view_top_rated(df):
    """Display top rated movies."""
    print("\n🏆 TOP RATED MOVIES")
    print("-" * 25)
    
    top_movies = df.nlargest(5, 'rating')
    
    for i, (_, movie) in enumerate(top_movies.iterrows(), 1):
        print(f"{i}. {movie['title']} ({movie['year']})")
        print(f"   Genre: {movie['genre']}")
        print(f"   Rating: {movie['rating']}/10")
        print()

def view_statistics(df):
    """Display dataset statistics."""
    print("\n📊 DATASET STATISTICS")
    print("-" * 25)
    
    print(f"Total movies: {len(df)}")
    print(f"Year range: {df['year'].min()} - {df['year'].max()}")
    print(f"Average rating: {df['rating'].mean():.2f}")
    print(f"Rating range: {df['rating'].min():.1f} - {df['rating'].max():.1f}")
    
    # Genre analysis
    print(f"\n🎭 GENRE DISTRIBUTION:")
    all_genres = []
    for genres in df['genre']:
        all_genres.extend([g.strip() for g in genres.split(',')])
    
    genre_counts = pd.Series(all_genres).value_counts()
    for genre, count in genre_counts.items():
        print(f"{genre}: {count} movies")

def main():
    """Main interactive function."""
    clear_screen()
    print_banner()
    
    print("🚀 Initializing Movie Recommendation System...")
    print("⏳ This may take a moment...")
    
    # Initialize the recommendation system
    df = create_simple_dataset()
    
    clear_screen()
    print_banner()
    print("✅ System ready! Welcome to the Movie Recommendation System!")
    print()
    
    while True:
        print_menu()
        choice = get_user_choice()
        
        if choice == '1':
            get_movie_recommendations(df)
        elif choice == '2':
            view_all_movies(df)
        elif choice == '3':
            view_top_rated(df)
        elif choice == '4':
            view_statistics(df)
        elif choice == '5':
            print("\n👋 Thank you for using the Movie Recommendation System!")
            print("🎬 Happy watching!")
            break
        
        input("\nPress Enter to continue...")
        clear_screen()
        print_banner()

if __name__ == "__main__":
    main() 