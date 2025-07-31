# 🚀 Deploy to Render - Movie Recommendation System

## 📋 Prerequisites

1. **GitHub Account**: Your code needs to be on GitHub
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **Git Repository**: Your project should be in a Git repository

## 🔧 Step-by-Step Deployment

### Step 1: Prepare Your Repository

Make sure your project has these files:
- ✅ `app.py` - Flask application
- ✅ `requirements.txt` - Python dependencies
- ✅ `render.yaml` - Render configuration
- ✅ `Procfile` - Process specification
- ✅ `runtime.txt` - Python version
- ✅ `templates/index.html` - Web interface

### Step 2: Push to GitHub

```bash
# Initialize Git repository (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit - Movie Recommendation System"

# Add GitHub remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/movie-recommendation-system.git

# Push to GitHub
git push -u origin main
```

### Step 3: Deploy on Render

1. **Go to Render Dashboard**
   - Visit [dashboard.render.com](https://dashboard.render.com)
   - Sign in with your account

2. **Create New Web Service**
   - Click "New +" button
   - Select "Web Service"

3. **Connect GitHub Repository**
   - Choose "Connect a repository"
   - Select your movie recommendation system repository
   - Click "Connect"

4. **Configure Service**
   - **Name**: `movie-recommendation-system`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or choose paid for more resources)

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app

### Step 4: Access Your App

- Your app will be available at: `https://your-app-name.onrender.com`
- The URL will be shown in your Render dashboard
- First deployment may take 5-10 minutes

## 🔧 Configuration Files Explained

### `render.yaml`
```yaml
services:
  - type: web
    name: movie-recommendation-system
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.0
```

### `requirements.txt`
```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
flask>=2.0.0
gunicorn>=20.1.0
```

### `Procfile`
```
web: gunicorn app:app
```

### `runtime.txt`
```
python-3.9.0
```

## 🌐 Environment Variables

Your app will automatically use these environment variables on Render:
- `PORT`: Automatically set by Render
- `PYTHON_VERSION`: Set to 3.9.0

## 📊 Monitoring & Logs

### View Logs
1. Go to your service dashboard on Render
2. Click "Logs" tab
3. Monitor deployment and runtime logs

### Common Issues
- **Build Failures**: Check `requirements.txt` for missing dependencies
- **Runtime Errors**: Check logs for Python errors
- **Memory Issues**: Consider upgrading to paid plan

## 🔄 Updating Your App

### Automatic Deployments
- Render automatically redeploys when you push to GitHub
- Just push changes to your main branch

### Manual Deployments
1. Go to your service dashboard
2. Click "Manual Deploy"
3. Choose "Deploy latest commit"

## 💰 Free Tier Limitations

### Render Free Tier:
- **Build Time**: 500 minutes/month
- **Runtime**: 750 hours/month
- **Sleep**: App sleeps after 15 minutes of inactivity
- **Memory**: 512 MB RAM
- **CPU**: Shared

### Recommendations:
- Perfect for development and small projects
- Consider paid plan for production use
- Monitor usage in dashboard

## 🛠️ Troubleshooting

### Build Issues
```bash
# Check if all dependencies are in requirements.txt
pip freeze > requirements.txt

# Test locally with gunicorn
pip install gunicorn
gunicorn app:app
```

### Runtime Issues
- Check logs in Render dashboard
- Ensure `app.py` has proper error handling
- Verify all imports are in `requirements.txt`

### Performance Issues
- Free tier has limited resources
- Consider optimizing ML model loading
- Use caching for similarity calculations

## 🎯 Best Practices

### Code Optimization
```python
# Cache the similarity matrix
import pickle

# Save similarity matrix
with open('similarity_matrix.pkl', 'wb') as f:
    pickle.dump(cosine_sim, f)

# Load similarity matrix
with open('similarity_matrix.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)
```

### Environment Variables
```python
# Use environment variables for configuration
import os

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
PORT = int(os.environ.get('PORT', 5000))
```

## 🚀 Advanced Features

### Custom Domain
1. Go to your service dashboard
2. Click "Settings" → "Custom Domains"
3. Add your domain and configure DNS

### Environment Variables
1. Go to "Environment" tab
2. Add custom environment variables
3. Restart service to apply changes

### Health Checks
```python
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})
```

## 📱 Mobile Optimization

Your web app is already mobile-friendly with:
- Responsive design
- Touch-friendly interface
- Fast loading times
- Progressive Web App features

## 🎉 Success!

Once deployed, your Movie Recommendation System will be:
- ✅ Accessible worldwide
- ✅ Always available (with free tier limitations)
- ✅ Automatically updated
- ✅ Monitored and logged
- ✅ Scalable for growth

### Share Your App
- Share the Render URL with friends
- Add to your portfolio
- Demonstrate your ML skills

---

**🎬 Your Movie Recommendation System is now live on the web! 🌐** 