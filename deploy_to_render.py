#!/usr/bin/env python3
"""
🚀 Deploy to Render - Helper Script
This script helps prepare your Movie Recommendation System for deployment to Render.
"""

import os
import subprocess
import sys

def check_files():
    """Check if all required files exist."""
    required_files = [
        'app.py',
        'requirements.txt',
        'render.yaml',
        'Procfile',
        'runtime.txt',
        'templates/index.html'
    ]
    
    print("🔍 Checking required files...")
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("\n✅ All required files found!")
    return True

def check_git():
    """Check if Git is initialized."""
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Git repository initialized")
            return True
        else:
            print("❌ Git repository not initialized")
            return False
    except FileNotFoundError:
        print("❌ Git not found. Please install Git first.")
        return False

def init_git():
    """Initialize Git repository."""
    print("\n🔧 Initializing Git repository...")
    
    try:
        # Initialize Git
        subprocess.run(['git', 'init'], check=True)
        print("✅ Git repository initialized")
        
        # Add all files
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Files added to Git")
        
        # Initial commit
        subprocess.run(['git', 'commit', '-m', 'Initial commit - Movie Recommendation System'], check=True)
        print("✅ Initial commit created")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        return False

def show_next_steps():
    """Show next steps for deployment."""
    print("\n" + "="*60)
    print("🚀 NEXT STEPS FOR DEPLOYMENT")
    print("="*60)
    
    print("\n1️⃣ PUSH TO GITHUB:")
    print("   git remote add origin https://github.com/yourusername/movie-recommendation-system.git")
    print("   git push -u origin main")
    
    print("\n2️⃣ DEPLOY ON RENDER:")
    print("   - Go to: https://dashboard.render.com")
    print("   - Click 'New +' → 'Web Service'")
    print("   - Connect your GitHub repository")
    print("   - Configure:")
    print("     • Name: movie-recommendation-system")
    print("     • Environment: Python 3")
    print("     • Build Command: pip install -r requirements.txt")
    print("     • Start Command: gunicorn app:app")
    print("     • Plan: Free")
    
    print("\n3️⃣ ACCESS YOUR APP:")
    print("   - Your app will be at: https://your-app-name.onrender.com")
    print("   - First deployment takes 5-10 minutes")
    
    print("\n📚 For detailed instructions, see: DEPLOYMENT_GUIDE.md")
    print("🌐 Your Movie Recommendation System will be live on the web!")

def main():
    """Main function."""
    print("🎬" + "="*60 + "🎬")
    print("           DEPLOY TO RENDER - HELPER SCRIPT")
    print("🎬" + "="*60 + "🎬")
    print()
    
    # Check required files
    if not check_files():
        print("\n❌ Please create missing files before deploying.")
        return
    
    # Check Git
    if not check_git():
        print("\n🔧 Would you like to initialize Git repository? (y/n): ", end="")
        response = input().lower().strip()
        
        if response == 'y':
            if not init_git():
                print("\n❌ Failed to initialize Git. Please do it manually.")
                return
        else:
            print("\n❌ Git repository required for deployment.")
            return
    
    # Show next steps
    show_next_steps()

if __name__ == "__main__":
    main() 