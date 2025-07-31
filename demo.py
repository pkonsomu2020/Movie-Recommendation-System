#!/usr/bin/env python3
"""
🎬 Movie Recommendation System - Demo Script
This script demonstrates the capabilities of our recommendation system.
"""

from movie_recommendation_system import MovieRecommendationSystem
import time

def print_separator(title=""):
    """Print a formatted separator."""
    if title:
        print(f"\n{'='*60}")
        print(f"🎬 {title}")
        print(f"{'='*60}")
    else:
        print(f"\n{'-'*60}")

def demo_basic_recommendations(recommender):
    """Demonstrate basic movie recommendations."""
    print_separator("BASIC RECOMMENDATION EXAMPLES")
    
    test_movies = ["Inception", "The Dark Knight", "The Notebook", "The Matrix"]
    
    for movie in test_movies:
        print(f"\n🎯 Because you liked '{movie}', you might also enjoy:")
        print("-" * 50)
        
        recommendations = recommender.recommend_movies(movie, 3)
        
        for rec in recommendations:
            print(f"🏆 {rec['rank']}. {rec['title']} ({rec['year']})")
            print(f"   Genre: {rec['genre']}")
            print(f"   Rating: {rec['rating']}/10")
            print(f"   Similarity: {rec['similarity_score']:.3f}")
            print()

def demo_genre_analysis(recommender):
    """Demonstrate genre-based analysis."""
    print_separator("GENRE-BASED ANALYSIS")
    
    genres = ["Sci-Fi", "Action", "Romance", "Thriller", "Drama"]
    
    for genre in genres:
        print(f"\n🎭 Movies similar to '{genre}' genre:")
        print("-" * 40)
        
        recommendations = recommender.find_similar_movies_by_genre(genre, 3)
        
        if 'error' not in recommendations[0]:
            for rec in recommendations:
                print(f"🏆 {rec['rank']}. {rec['title']} ({rec['year']})")
                print(f"   Genre: {rec['genre']}")
                print(f"   Similarity: {rec['similarity_score']:.3f}")
                print()

def demo_popular_movies(recommender):
    """Demonstrate popular movies feature."""
    print_separator("TOP RATED MOVIES")
    
    popular_movies = recommender.get_popular_movies(10)
    
    print("🏆 TOP 10 HIGHEST RATED MOVIES:")
    print("-" * 40)
    
    for i, movie in enumerate(popular_movies, 1):
        print(f"{i:2d}. {movie['title']} ({movie['year']})")
        print(f"    Genre: {movie['genre']}")
        print(f"    Rating: {movie['rating']}/10")
        print()

def demo_year_analysis(recommender):
    """Demonstrate year-based analysis."""
    print_separator("YEAR-BASED ANALYSIS")
    
    year_ranges = [
        (1990, 1999, "1990s"),
        (2000, 2009, "2000s"),
        (2010, 2019, "2010s"),
        (2020, 2023, "2020s")
    ]
    
    for start_year, end_year, decade in year_ranges:
        movies = recommender.get_movies_by_year_range(start_year, end_year)
        
        if movies:
            print(f"\n📅 Movies from {decade} ({start_year}-{end_year}):")
            print("-" * 40)
            
            for movie in movies[:5]:  # Show first 5
                print(f"• {movie['title']} ({movie['year']}) - {movie['genre']}")
            
            if len(movies) > 5:
                print(f"  ... and {len(movies) - 5} more movies")

def demo_similarity_analysis(recommender):
    """Demonstrate similarity analysis."""
    print_separator("SIMILARITY ANALYSIS")
    
    # Find most similar movie pairs
    print("🔍 Most Similar Movie Pairs:")
    print("-" * 40)
    
    # Get similarity matrix
    similarity_matrix = recommender.cosine_sim
    
    # Find top similarities (excluding self-similarity)
    similarities = []
    for i in range(len(similarity_matrix)):
        for j in range(i+1, len(similarity_matrix)):
            similarities.append((i, j, similarity_matrix[i][j]))
    
    # Sort by similarity score
    similarities.sort(key=lambda x: x[2], reverse=True)
    
    # Show top 5 most similar pairs
    for i, (idx1, idx2, score) in enumerate(similarities[:5], 1):
        movie1 = recommender.df.iloc[idx1]['title']
        movie2 = recommender.df.iloc[idx2]['title']
        print(f"{i}. {movie1} ↔ {movie2}")
        print(f"   Similarity: {score:.3f}")
        print()

def demo_dataset_statistics(recommender):
    """Demonstrate dataset statistics."""
    print_separator("DATASET STATISTICS")
    
    df = recommender.df
    
    print("📊 DATASET OVERVIEW:")
    print("-" * 30)
    print(f"Total Movies: {len(df)}")
    print(f"Year Range: {df['year'].min()} - {df['year'].max()}")
    print(f"Average Rating: {df['rating'].mean():.2f}")
    print(f"Rating Range: {df['rating'].min():.1f} - {df['rating'].max():.1f}")
    
    # Genre analysis
    print(f"\n🎭 GENRE DISTRIBUTION:")
    print("-" * 30)
    all_genres = []
    for genres in df['genre']:
        all_genres.extend([g.strip() for g in genres.split(',')])
    
    genre_counts = pd.Series(all_genres).value_counts()
    for genre, count in genre_counts.head(10).items():
        print(f"{genre}: {count} movies")
    
    # Decade analysis
    print(f"\n📅 MOVIES BY DECADE:")
    print("-" * 30)
    decade_counts = df['year'].apply(lambda x: f"{x//10*10}s").value_counts().sort_index()
    for decade, count in decade_counts.items():
        print(f"{decade}: {count} movies")

def main():
    """Main demo function."""
    print("🎬 MOVIE RECOMMENDATION SYSTEM - DEMO")
    print("=" * 60)
    print("🚀 Initializing system...")
    
    # Initialize the recommendation system
    start_time = time.time()
    recommender = MovieRecommendationSystem()
    recommender.create_enhanced_dataset()
    recommender.vectorize_descriptions()
    recommender.compute_similarity()
    
    init_time = time.time() - start_time
    print(f"✅ System initialized in {init_time:.2f} seconds!")
    
    # Run all demos
    demo_basic_recommendations(recommender)
    demo_genre_analysis(recommender)
    demo_popular_movies(recommender)
    demo_year_analysis(recommender)
    demo_similarity_analysis(recommender)
    demo_dataset_statistics(recommender)
    
    print_separator("DEMO COMPLETE")
    print("🎉 Thank you for exploring the Movie Recommendation System!")
    print("💡 Try running 'python interactive_interface.py' for an interactive experience!")

if __name__ == "__main__":
    import pandas as pd
    main() 