#!/usr/bin/env python3
"""
🎬 Movie Recommendation System - Web Application Startup Script
This script launches the Flask web application for the movie recommendation system.
"""

import subprocess
import sys
import time
import webbrowser
import os

def install_requirements():
    """Install required packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Error installing packages. Please install manually:")
        print("   pip install -r requirements.txt")
        return False

def start_web_app():
    """Start the Flask web application."""
    print("🚀 Starting Movie Recommendation System Web App...")
    print("⏳ This may take a moment...")
    
    try:
        # Start the Flask app
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Web application stopped.")
    except Exception as e:
        print(f"❌ Error starting web application: {e}")

def main():
    """Main function."""
    print("🎬" + "="*60 + "🎬")
    print("           MOVIE RECOMMENDATION SYSTEM - WEB APP")
    print("🎬" + "="*60 + "🎬")
    print()
    
    # Check if Flask is installed
    try:
        import flask
        print("✅ Flask is already installed!")
    except ImportError:
        print("📦 Flask not found. Installing requirements...")
        if not install_requirements():
            return
    
    print("\n🌐 Starting web application...")
    print("📱 The web interface will open in your browser automatically.")
    print("🔗 If it doesn't open, go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print()
    
    # Wait a moment for user to read
    time.sleep(2)
    
    # Try to open browser automatically
    try:
        webbrowser.open('http://localhost:5000')
    except:
        pass
    
    # Start the web app
    start_web_app()

if __name__ == "__main__":
    main() 