import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class SimpleMovieRecommender:
    """
    A simple movie recommendation system using content-based filtering.
    """
    
    def __init__(self):
        self.df = None
        self.vectorizer = None
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.movie_indices = None
        
    def create_dataset(self):
        """
        Create a balanced dataset with movies.
        """
        data = {
            'title': [
                'The Matrix', 'John Wick', 'Inception', 'The Notebook', 'Titanic',
                'The Avengers', 'Interstellar', 'The Dark Knight', 'Tenet',
                'Forrest Gump', 'Pulp Fiction', 'The Shawshank Redemption',
                'Fight Club', 'Goodfellas', 'The Godfather', 'Casablanca',
                'Gone with the Wind', 'The Wizard of Oz', 'Citizen Kane',
                'Star Wars: A New Hope', 'The Empire Strikes Back', 'Return of the Jedi',
                'Jurassic Park', 'E.T. the Extra-Terrestrial', 'Jaws',
                'Raiders of the Lost Ark', 'Indiana Jones and the Last Crusade',
                'Back to the Future', 'The Terminator', 'Terminator 2: Judgment Day',
                'Die Hard', 'Lethal Weapon', 'Speed', 'The Rock',
                'Mission: Impossible', 'Top Gun', 'Rain Man', 'A Beautiful Mind',
                'The Silence of the Lambs', 'Se7en', 'The Usual Suspects',
                'Memento', 'The Sixth Sense', 'The Green Mile', 'Saving Private Ryan',
                'Schindler\'s List', 'The Pianist', 'Life is Beautiful',
                'Amélie', 'La La Land', 'The Greatest Showman', 'Moulin Rouge!',
                'Chicago', 'The Lion King', 'Toy Story', 'Finding Nemo',
                'Up', 'Wall-E', 'Frozen', 'Moana', 'Coco', 'Spider-Man',
                'Iron Man', 'Black Panther', 'Wonder Woman', 'Captain America',
                'Thor', 'Guardians of the Galaxy', 'Deadpool', 'Logan',
                'X-Men', 'Batman Begins', 'Aquaman', 'Shazam!', 'Joker',
                'The Suicide Squad', 'Black Widow', 'Shang-Chi', 'Eternals',
                'Doctor Strange', 'Ant-Man'
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
                'drama prison friendship hope redemption',
                'psychological thriller violence social commentary',
                'crime gangster mafia violence drama',
                'crime mafia family drama classic',
                'romance war drama classic black white',
                'romance drama historical civil war epic',
                'fantasy adventure musical classic family',
                'drama mystery journalism classic',
                'sci-fi fantasy adventure space epic',
                'sci-fi fantasy adventure space family',
                'sci-fi fantasy adventure space redemption',
                'sci-fi adventure dinosaurs action family',
                'sci-fi family adventure alien friendship',
                'horror thriller shark survival adventure',
                'adventure action archaeology treasure hunt',
                'adventure action archaeology religious quest',
                'sci-fi comedy time travel adventure',
                'sci-fi action robot future dystopia',
                'sci-fi action robot future redemption',
                'action thriller hostage christmas',
                'action comedy buddy cop crime',
                'action thriller bus bomb speed',
                'action thriller prison escape military',
                'action spy thriller mission impossible',
                'action drama military aviation',
                'drama autism family road trip',
                'drama mathematics mental illness genius',
                'thriller horror serial killer psychological',
                'thriller crime mystery serial killer',
                'thriller crime mystery plot twist',
                'thriller mystery memory loss revenge',
                'thriller supernatural plot twist',
                'drama prison friendship execution',
                'war drama military rescue mission',
                'war drama holocaust historical',
                'war drama holocaust survival',
                'comedy romance magical realism',
                'musical romance hollywood dreams',
                'musical drama circus showman',
                'musical romance paris bohemian',
                'musical crime chicago jazz',
                'animation adventure family lions',
                'animation adventure family toys',
                'animation adventure family fish',
                'animation adventure family balloons',
                'animation adventure family robot',
                'animation musical family princess',
                'animation adventure family polynesia',
                'animation adventure family mexico',
                'superhero action spider powers',
                'superhero action iron technology',
                'superhero action africa king',
                'superhero action amazon warrior',
                'superhero action patriotic soldier',
                'superhero action thunder god',
                'superhero action space guardians',
                'superhero action antihero comedy',
                'superhero action wolverine mutant',
                'superhero action mutants x-men',
                'superhero action batman origin',
                'superhero action atlantis king',
                'superhero action magic powers',
                'superhero action clown villain',
                'superhero action team villains',
                'superhero action spy assassin',
                'superhero action martial arts',
                'superhero action cosmic beings',
                'superhero action magic doctor',
                'superhero action shrinking hero'
            ],
            'genre': [
                'Sci-Fi, Action', 'Action, Thriller', 'Sci-Fi, Thriller',
                'Romance, Drama', 'Romance, Drama', 'Action, Adventure',
                'Sci-Fi, Drama', 'Action, Drama', 'Sci-Fi, Thriller',
                'Drama, Comedy', 'Crime, Thriller', 'Drama',
                'Thriller, Drama', 'Crime, Drama', 'Crime, Drama',
                'Romance, Drama', 'Romance, Drama', 'Fantasy, Adventure',
                'Drama, Mystery', 'Sci-Fi, Adventure', 'Sci-Fi, Adventure',
                'Sci-Fi, Adventure', 'Sci-Fi, Adventure', 'Sci-Fi, Family',
                'Horror, Thriller', 'Adventure, Action', 'Adventure, Action',
                'Sci-Fi, Comedy', 'Sci-Fi, Action', 'Sci-Fi, Action',
                'Action, Thriller', 'Action, Comedy', 'Action, Thriller',
                'Action, Thriller', 'Action, Thriller', 'Action, Drama',
                'Drama', 'Drama', 'Thriller, Horror', 'Thriller, Crime',
                'Thriller, Crime', 'Thriller, Mystery', 'Thriller, Mystery',
                'Drama', 'War, Drama', 'War, Drama', 'War, Drama',
                'Comedy, Romance', 'Musical, Romance', 'Musical, Drama',
                'Musical, Romance', 'Musical, Crime', 'Animation, Adventure',
                'Animation, Adventure', 'Animation, Adventure',
                'Animation, Adventure', 'Animation, Adventure',
                'Animation, Musical', 'Animation, Adventure',
                'Animation, Adventure', 'Action, Adventure', 'Action, Adventure',
                'Action, Adventure', 'Action, Adventure', 'Action, Adventure',
                'Action, Adventure', 'Action, Comedy', 'Action, Drama',
                'Action, Adventure', 'Action, Adventure', 'Action, Adventure',
                'Action, Adventure', 'Action, Adventure', 'Action, Adventure',
                'Action, Adventure', 'Action, Adventure', 'Action, Adventure'
            ],
            'year': [
                1999, 2014, 2010, 2004, 1997, 2012, 2014, 2008, 2020,
                1994, 1994, 1994, 1999, 1990, 1972, 1942, 1939, 1939,
                1941, 1977, 1980, 1983, 1993, 1982, 1975, 1981, 1989,
                1985, 1984, 1991, 1988, 1987, 1994, 1996, 1996, 1986,
                1988, 2001, 1991, 1995, 2000, 1999, 1999, 1998, 1993,
                2002, 1991, 2001, 2003, 2016, 2017, 2001, 2002, 1994,
                1995, 2003, 2008, 2013, 2016, 2017, 2002, 2008, 2018,
                2017, 2019, 2016, 2021, 2021, 2016, 2018, 2015
            ],
            'rating': [
                8.7, 7.4, 8.8, 7.8, 7.9, 8.0, 8.6, 9.0, 7.4,
                8.8, 8.9, 9.3, 8.8, 8.7, 9.2, 8.5, 8.1, 8.0,
                8.3, 8.6, 8.7, 8.3, 8.5, 7.8, 8.0, 8.4, 8.2,
                8.5, 8.0, 8.5, 8.2, 7.6, 7.2, 7.4, 7.0, 6.9,
                8.0, 8.3, 8.6, 8.6, 8.5, 8.4, 8.1, 8.6, 8.9,
                8.9, 8.5, 8.1, 8.3, 7.4, 7.6, 7.2, 7.2, 8.5,
                8.4, 8.1, 8.9, 7.4, 7.4, 7.6, 7.3, 7.9, 7.4,
                7.3, 6.8, 7.0, 7.4, 7.5, 7.3, 7.4, 6.8, 6.3
            ]
        }
        
        self.df = pd.DataFrame(data)
        self.movie_indices = pd.Series(self.df.index, index=self.df['title'])
        print(f"✅ Dataset created with {len(self.df)} movies!")
        return self.df
    
    def vectorize_descriptions(self):
        """
        Convert movie descriptions into TF-IDF vectors.
        """
        self.vectorizer = TfidfVectorizer(
            stop_words='english',
            ngram_range=(1, 2),
            max_features=5000
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['description'])
        print(f"✅ TF-IDF matrix created with shape: {self.tfidf_matrix.shape}")
        return self.tfidf_matrix
    
    def compute_similarity(self):
        """
        Compute cosine similarity matrix between all movies.
        """
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        print(f"✅ Similarity matrix computed with shape: {self.cosine_sim.shape}")
        return self.cosine_sim
    
    def recommend_movies(self, movie_title, top_n=5):
        """
        Recommend similar movies based on a given movie title.
        """
        if movie_title not in self.df['title'].values:
            return [{"error": f"Movie '{movie_title}' not found in dataset."}]
        
        idx = self.movie_indices[movie_title]
        similarity_scores = list(enumerate(self.cosine_sim[idx]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        # Get top N similar movies (excluding the movie itself)
        top_indices = [i[0] for i in similarity_scores[1:top_n+1]]
        
        recommendations = []
        for i, movie_idx in enumerate(top_indices):
            movie_data = self.df.iloc[movie_idx]
            recommendations.append({
                'rank': i + 1,
                'title': movie_data['title'],
                'genre': movie_data['genre'],
                'year': movie_data['year'],
                'rating': movie_data['rating'],
                'similarity_score': round(similarity_scores[i+1][1], 3)
            })
        
        return recommendations
    
    def get_movie_details(self, movie_title):
        """
        Get detailed information about a specific movie.
        """
        if movie_title not in self.df['title'].values:
            return {"error": f"Movie '{movie_title}' not found in dataset."}
        
        movie_data = self.df[self.df['title'] == movie_title].iloc[0]
        return {
            'title': movie_data['title'],
            'genre': movie_data['genre'],
            'year': movie_data['year'],
            'rating': movie_data['rating'],
            'description': movie_data['description']
        }
    
    def get_popular_movies(self, top_n=10):
        """
        Get the most popular movies based on rating.
        """
        popular_movies = self.df.nlargest(top_n, 'rating')
        return popular_movies[['title', 'genre', 'year', 'rating']].to_dict('records')
    
    def analyze_dataset(self):
        """
        Perform basic analysis of the dataset.
        """
        print("\n📊 DATASET ANALYSIS")
        print("=" * 50)
        print(f"Total movies: {len(self.df)}")
        print(f"Year range: {self.df['year'].min()} - {self.df['year'].max()}")
        print(f"Average rating: {self.df['rating'].mean():.2f}")
        print(f"Rating range: {self.df['rating'].min():.1f} - {self.df['rating'].max():.1f}")
        
        # Genre analysis
        all_genres = []
        for genres in self.df['genre']:
            all_genres.extend([g.strip() for g in genres.split(',')])
        
        genre_counts = pd.Series(all_genres).value_counts()
        print(f"\nTop 10 Genres:")
        for genre, count in genre_counts.head(10).items():
            print(f"  {genre}: {count} movies")

def main():
    """
    Main function to demonstrate the movie recommendation system.
    """
    print("🎬 MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)
    
    # Initialize the system
    recommender = SimpleMovieRecommender()
    
    # Create dataset
    recommender.create_dataset()
    
    # Vectorize descriptions
    recommender.vectorize_descriptions()
    
    # Compute similarity
    recommender.compute_similarity()
    
    # Analyze dataset
    recommender.analyze_dataset()
    
    # Interactive recommendations
    print("\n🎯 RECOMMENDATION EXAMPLES")
    print("=" * 50)
    
    # Example 1: Sci-Fi recommendations
    print("\n1. Because you liked 'Inception', you might also enjoy:")
    recommendations = recommender.recommend_movies("Inception", 5)
    for rec in recommendations:
        print(f"   {rec['rank']}. {rec['title']} ({rec['year']}) - {rec['genre']} - Similarity: {rec['similarity_score']}")
    
    # Example 2: Action recommendations
    print("\n2. Because you liked 'The Dark Knight', you might also enjoy:")
    recommendations = recommender.recommend_movies("The Dark Knight", 5)
    for rec in recommendations:
        print(f"   {rec['rank']}. {rec['title']} ({rec['year']}) - {rec['genre']} - Similarity: {rec['similarity_score']}")
    
    # Example 3: Romance recommendations
    print("\n3. Because you liked 'The Notebook', you might also enjoy:")
    recommendations = recommender.recommend_movies("The Notebook", 5)
    for rec in recommendations:
        print(f"   {rec['rank']}. {rec['title']} ({rec['year']}) - {rec['genre']} - Similarity: {rec['similarity_score']}")
    
    # Popular movies
    print("\n🏆 TOP 10 HIGHEST RATED MOVIES:")
    popular = recommender.get_popular_movies(10)
    for i, movie in enumerate(popular, 1):
        print(f"   {i}. {movie['title']} ({movie['year']}) - Rating: {movie['rating']}")
    
    return recommender

if __name__ == "__main__":
    recommender = main() 