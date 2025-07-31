import sys
import os
from movie_recommendation_system import MovieRecommendationSystem

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
    print("2. 🔍 Search for a specific movie")
    print("3. 🏆 View top rated movies")
    print("4. 📅 Browse movies by year range")
    print("5. 🎭 Find movies by genre")
    print("6. 📊 View dataset statistics")
    print("7. 🎲 Get random movie recommendation")
    print("8. ❌ Exit")
    print()

def get_user_choice():
    """Get user choice from menu."""
    while True:
        try:
            choice = input("Enter your choice (1-8): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                return choice
            else:
                print("❌ Invalid choice. Please enter a number between 1-8.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)

def get_movie_recommendations(recommender):
    """Handle movie recommendation requests."""
    print("\n🎯 MOVIE RECOMMENDATIONS")
    print("-" * 30)
    
    # Show available movies
    print("Available movies in our database:")
    movies = recommender.df['title'].tolist()
    for i, movie in enumerate(movies, 1):
        print(f"{i:2d}. {movie}")
    
    print("\nEnter a movie title from the list above:")
    movie_title = input("Movie title: ").strip()
    
    if not movie_title:
        print("❌ No movie title entered.")
        return
    
    # Get recommendations
    recommendations = recommender.recommend_movies(movie_title, 5)
    
    if 'error' in recommendations[0]:
        print(f"❌ {recommendations[0]['error']}")
        return
    
    # Display recommendations
    print(f"\n🎬 Because you liked '{movie_title}', you might also enjoy:")
    print("-" * 60)
    
    for rec in recommendations:
        print(f"🏆 {rec['rank']}. {rec['title']} ({rec['year']})")
        print(f"   Genre: {rec['genre']}")
        print(f"   Rating: {rec['rating']}/10")
        print(f"   Similarity: {rec['similarity_score']:.3f}")
        print()

def search_movie(recommender):
    """Search for a specific movie's details."""
    print("\n🔍 SEARCH MOVIE")
    print("-" * 20)
    
    movie_title = input("Enter movie title to search: ").strip()
    
    if not movie_title:
        print("❌ No movie title entered.")
        return
    
    movie_details = recommender.get_movie_details(movie_title)
    
    if 'error' in movie_details:
        print(f"❌ {movie_details['error']}")
        return
    
    print(f"\n📽️ MOVIE DETAILS:")
    print("-" * 30)
    print(f"Title: {movie_details['title']}")
    print(f"Genre: {movie_details['genre']}")
    print(f"Year: {movie_details['year']}")
    print(f"Rating: {movie_details['rating']}/10")
    print(f"Description: {movie_details['description']}")

def view_top_rated(recommender):
    """Display top rated movies."""
    print("\n🏆 TOP RATED MOVIES")
    print("-" * 25)
    
    try:
        top_n = int(input("How many top movies to show? (default: 10): ") or "10")
    except ValueError:
        top_n = 10
    
    popular_movies = recommender.get_popular_movies(top_n)
    
    print(f"\n🏆 TOP {len(popular_movies)} HIGHEST RATED MOVIES:")
    print("-" * 50)
    
    for i, movie in enumerate(popular_movies, 1):
        print(f"{i:2d}. {movie['title']} ({movie['year']})")
        print(f"    Genre: {movie['genre']}")
        print(f"    Rating: {movie['rating']}/10")
        print()

def browse_by_year(recommender):
    """Browse movies by year range."""
    print("\n📅 BROWSE BY YEAR RANGE")
    print("-" * 25)
    
    try:
        start_year = int(input("Enter start year: "))
        end_year = int(input("Enter end year: "))
    except ValueError:
        print("❌ Invalid year format.")
        return
    
    if start_year > end_year:
        start_year, end_year = end_year, start_year
    
    movies = recommender.get_movies_by_year_range(start_year, end_year)
    
    if not movies:
        print(f"❌ No movies found between {start_year} and {end_year}.")
        return
    
    print(f"\n📽️ MOVIES FROM {start_year} TO {end_year}:")
    print("-" * 40)
    
    for i, movie in enumerate(movies, 1):
        print(f"{i:2d}. {movie['title']} ({movie['year']})")
        print(f"    Genre: {movie['genre']}")
        print(f"    Rating: {movie['rating']}/10")
        print()

def find_by_genre(recommender):
    """Find movies by genre."""
    print("\n🎭 FIND BY GENRE")
    print("-" * 20)
    
    # Show available genres
    all_genres = []
    for genres in recommender.df['genre']:
        all_genres.extend([g.strip() for g in genres.split(',')])
    
    unique_genres = sorted(set(all_genres))
    print("Available genres:")
    for i, genre in enumerate(unique_genres, 1):
        print(f"{i:2d}. {genre}")
    
    print("\nEnter a genre name:")
    genre = input("Genre: ").strip()
    
    if not genre:
        print("❌ No genre entered.")
        return
    
    recommendations = recommender.find_similar_movies_by_genre(genre, 5)
    
    if 'error' in recommendations[0]:
        print(f"❌ {recommendations[0]['error']}")
        return
    
    print(f"\n🎬 Movies similar to '{genre}' genre:")
    print("-" * 40)
    
    for rec in recommendations:
        print(f"🏆 {rec['rank']}. {rec['title']} ({rec['year']})")
        print(f"   Genre: {rec['genre']}")
        print(f"   Rating: {rec['rating']}/10")
        print(f"   Similarity: {rec['similarity_score']:.3f}")
        print()

def view_statistics(recommender):
    """Display dataset statistics."""
    print("\n📊 DATASET STATISTICS")
    print("-" * 25)
    recommender.analyze_dataset()

def random_recommendation(recommender):
    """Get a random movie recommendation."""
    print("\n🎲 RANDOM RECOMMENDATION")
    print("-" * 25)
    
    import random
    random_movie = random.choice(recommender.df['title'].tolist())
    
    print(f"🎬 Random movie: {random_movie}")
    print("\nHere are similar movies:")
    
    recommendations = recommender.recommend_movies(random_movie, 3)
    
    for rec in recommendations:
        print(f"🏆 {rec['rank']}. {rec['title']} ({rec['year']})")
        print(f"   Genre: {rec['genre']}")
        print(f"   Rating: {rec['rating']}/10")
        print()

def main():
    """Main interactive interface function."""
    clear_screen()
    print_banner()
    
    print("🚀 Initializing Movie Recommendation System...")
    print("⏳ This may take a moment...")
    
    # Initialize the recommendation system
    recommender = MovieRecommendationSystem()
    recommender.create_enhanced_dataset()
    recommender.vectorize_descriptions()
    recommender.compute_similarity()
    
    clear_screen()
    print_banner()
    print("✅ System ready! Welcome to the Movie Recommendation System!")
    print()
    
    while True:
        print_menu()
        choice = get_user_choice()
        
        if choice == '1':
            get_movie_recommendations(recommender)
        elif choice == '2':
            search_movie(recommender)
        elif choice == '3':
            view_top_rated(recommender)
        elif choice == '4':
            browse_by_year(recommender)
        elif choice == '5':
            find_by_genre(recommender)
        elif choice == '6':
            view_statistics(recommender)
        elif choice == '7':
            random_recommendation(recommender)
        elif choice == '8':
            print("\n👋 Thank you for using the Movie Recommendation System!")
            print("🎬 Happy watching!")
            break
        
        input("\nPress Enter to continue...")
        clear_screen()
        print_banner()

if __name__ == "__main__":
    main() 