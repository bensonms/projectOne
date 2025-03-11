#!/bin/bash

# Navigate to the project directory
cd /Users/bensonlin/test/projectOne

# Initialize git repository if not already initialized
if [ ! -d .git ]; then
    echo "Initializing git repository..."
    git init
fi

# Add all files to git
echo "Adding files to git..."
git add .

# Commit the changes
echo "Committing changes..."
git commit -m "Initial commit"

echo "Enter your GitHub username:"
read username

echo "Enter the name for your new GitHub repository:"
read repo_name

echo "Create a new repository named '$repo_name' on GitHub now."
echo "Once created, press Enter to continue..."
read

# Add the remote repository
echo "Adding GitHub remote repository..."
git remote add origin https://github.com/$username/$repo_name.git

# Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main || git push -u origin master

echo "Repository has been pushed to GitHub successfully!"
