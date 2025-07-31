# 🎬 Movie Recommendation System

A comprehensive content-based movie recommendation system built with Python and Machine Learning using TF-IDF vectorization and cosine similarity.

## 🚀 Features

- **Content-Based Filtering**: Recommends movies based on description similarity
- **TF-IDF Vectorization**: Converts movie descriptions into numerical vectors
- **Cosine Similarity**: Measures similarity between movies
- **🌐 Web Interface**: Beautiful, modern web application
- **📱 Interactive Interface**: User-friendly command-line interface
- **Enhanced Dataset**: 12 popular movies with detailed information
- **Multiple Search Options**: By title, genre, year range, and popularity
- **Comprehensive Analysis**: Dataset statistics and insights
- **Real-time Recommendations**: Instant results with similarity scoring

## 📋 Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## 🌐 Live Demo

**🎬 Your Movie Recommendation System is now live!**

👉 **[Try it now: https://movie-recommendation-system-0u9l.onrender.com/](https://movie-recommendation-system-0u9l.onrender.com/)**

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **🌐 Start the Web Application (Local):**
   ```bash
   python start_web_app.py
   ```
   Then open your browser to: **http://localhost:5000**

4. **Run the simple demo:**
   ```bash
   python simple_demo.py
   ```

5. **For interactive interface:**
   ```bash
   python interactive_demo.py
   ```

## 🎯 How It Works

### 1. **Data Processing**
- Movie descriptions are converted into TF-IDF vectors
- TF-IDF captures the importance of words in each movie description
- Stop words are removed and n-grams are used for better context

### 2. **Similarity Calculation**
- Cosine similarity is computed between all movie vectors
- Similarity scores range from 0 (no similarity) to 1 (identical)
- Higher scores indicate more similar movies

### 3. **Recommendation Generation**
- For a given movie, find movies with highest similarity scores
- Return top N most similar movies
- Exclude the input movie from recommendations

## 📊 Dataset

The system includes 70+ movies with the following information:
- **Title**: Movie name
- **Description**: Text description of plot/genre
- **Genre**: Movie categories
- **Year**: Release year
- **Rating**: IMDb-style rating (1-10)

### Sample Movies:
- The Matrix (1999) - Sci-Fi, Action
- Inception (2010) - Sci-Fi, Thriller
- The Dark Knight (2008) - Action, Drama
- The Notebook (2004) - Romance, Drama
- And many more...

## 🎮 Usage Examples

### Basic Usage
```python
from simple_demo import create_simple_dataset, recommend_movies

# Create dataset
df = create_simple_dataset()

# Get recommendations
recommendations = recommend_movies(df, "Inception", 3)
for rec in recommendations:
    print(f"{rec['title']} - Similarity: {rec['similarity_score']}")
```

### 🌐 Web Interface
**Live Demo**: [https://movie-recommendation-system-0u9l.onrender.com/](https://movie-recommendation-system-0u9l.onrender.com/)

**Local Development**: Run `python start_web_app.py` and open your browser to **http://localhost:5000**

Features:
- 🎯 Interactive movie selection
- 📊 Real-time statistics
- 🎨 Beautiful, modern design
- 📱 Responsive layout
- ⚡ Instant recommendations

### 📱 Command Line Interface
Run `python interactive_demo.py` and choose from:
1. 🎯 Get movie recommendations
2. 🔍 View all available movies
3. 🏆 View top rated movies
4. 📊 View dataset statistics
5. ❌ Exit

## 📈 Sample Output

```
🎬 Because you liked 'Inception', you might also enjoy:
🏆 1. Tenet (2020) - Sci-Fi, Thriller - Similarity: 0.847
🏆 2. Interstellar (2014) - Sci-Fi, Drama - Similarity: 0.723
🏆 3. The Matrix (1999) - Sci-Fi, Action - Similarity: 0.689
🏆 4. Memento (2000) - Thriller, Mystery - Similarity: 0.567
🏆 5. The Sixth Sense (1999) - Thriller, Mystery - Similarity: 0.534
```

**🌐 Try it live**: [https://movie-recommendation-system-0u9l.onrender.com/](https://movie-recommendation-system-0u9l.onrender.com/)

## 🔧 Technical Details

### Algorithms Used:
- **TF-IDF (Term Frequency-Inverse Document Frequency)**
  - Converts text to numerical vectors
  - Weights words by importance
  - Handles common vs. rare words

- **Cosine Similarity**
  - Measures angle between vectors
  - Range: 0 to 1
  - Higher values = more similar

### Performance:
- **Dataset Size**: 70+ movies
- **Vector Dimensions**: ~5000 features
- **Similarity Matrix**: 70x70 matrix
- **Recommendation Speed**: Near-instantaneous

## 🎨 Customization

### Adding New Movies
```python
# Add to the data dictionary in create_enhanced_dataset()
new_movie = {
    'title': 'Your Movie',
    'description': 'sci-fi action adventure space',
    'genre': 'Sci-Fi, Action',
    'year': 2023,
    'rating': 8.5
}
```

### Modifying Parameters
```python
# Adjust TF-IDF parameters
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1, 3),  # Use 1-3 word combinations
    max_features=10000   # Increase feature count
)
```

## 📊 Analysis Features

### Dataset Statistics:
- Total movies count
- Year range analysis
- Average ratings
- Genre distribution
- Decade-wise movie counts

### Similarity Analysis:
- Movie-to-movie similarity scores
- Genre-based clustering
- Year-based patterns
- Rating correlations

## 🚀 Future Enhancements

- **Collaborative Filtering**: User-based recommendations
- **Hybrid Approach**: Combine content + collaborative
- **Web Interface**: Flask/Django web app
- **Database Integration**: SQL/NoSQL storage
- **Real-time Updates**: Dynamic movie additions
- **Advanced NLP**: Sentiment analysis, entity recognition
- **Visualization**: Interactive charts and graphs

## 🤝 Contributing

Feel free to contribute by:
- Adding more movies to the dataset
- Improving the recommendation algorithm
- Enhancing the user interface
- Adding new features
- Fixing bugs

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Scikit-learn for ML algorithms
- Pandas for data manipulation
- The movie dataset contributors
- Open source community

---

**Happy Movie Watching! 🎬🍿** 