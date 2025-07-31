# 🌐 Web Application Guide

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start the Web Application
```bash
python start_web_app.py
```

### Step 3: Open Your Browser
Go to: **http://localhost:5000**

The web interface will open automatically in your default browser!

## 🎯 How to Use the Web Interface

### 1. **Get Movie Recommendations**
- Select a movie from the dropdown menu
- Choose the number of recommendations (1-10)
- Click "🎬 Get Recommendations"
- View your personalized recommendations with similarity scores

### 2. **View Statistics**
- See dataset overview on the right panel
- View total movies, year range, average ratings
- Browse top-rated movies

### 3. **Browse All Movies**
- Scroll down to see all available movies
- Each movie card shows title, year, genre, and rating

## 🎨 Features

### ✨ **Modern Design**
- Beautiful gradient background
- Responsive layout (works on mobile!)
- Smooth animations and hover effects
- Professional movie card design

### ⚡ **Real-time Results**
- Instant recommendations
- Live similarity scoring
- Dynamic statistics
- No page refreshes needed

### 📊 **Comprehensive Data**
- Movie details (title, year, genre, rating)
- Similarity scores (0-1 scale)
- Dataset statistics
- Top-rated movies list

## 🔧 Technical Details

### **Backend**
- Flask web framework
- RESTful API endpoints
- TF-IDF vectorization
- Cosine similarity calculation

### **Frontend**
- Modern HTML5/CSS3
- Vanilla JavaScript
- Responsive design
- AJAX for dynamic content

### **API Endpoints**
- `GET /` - Main page
- `POST /recommend` - Get recommendations
- `GET /movies` - Get all movies
- `GET /stats` - Get statistics

## 🛠️ Troubleshooting

### **Port Already in Use**
If you see "Address already in use" error:
```bash
# Find and kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### **Browser Doesn't Open Automatically**
- Manually open: http://localhost:5000
- Or try: http://127.0.0.1:5000

### **Flask Not Found**
```bash
pip install flask
```

## 📱 Mobile Support

The web interface is fully responsive and works great on:
- 📱 Smartphones
- 📱 Tablets
- 💻 Laptops
- 🖥️ Desktop computers

## 🎬 Sample Usage

1. **Select "Inception"** from the dropdown
2. **Choose 5 recommendations**
3. **Click "Get Recommendations"**
4. **See results like:**
   - Tenet (2020) - Similarity: 0.847
   - The Matrix (1999) - Similarity: 0.689
   - Interstellar (2014) - Similarity: 0.567

## 🚀 Next Steps

After using the web interface, you can:
- Try the command-line version: `python interactive_demo.py`
- Run the simple demo: `python simple_demo.py`
- Explore the code to understand the algorithms
- Add more movies to the dataset

---

**🎉 Enjoy your personalized movie recommendations! 🍿** 