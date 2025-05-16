#!/bin/bash

# Get the current date and time
CURRENT_DATE_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# Check if a commit message was provided
if [ -z "$1" ]; then
    # Use default message with the current date and time
    COMMIT_MESSAGE="Commit: $CURRENT_DATE_TIME"
else
    # Append the current date and time to the provided message
    COMMIT_MESSAGE="$1 - $CURRENT_DATE_TIME"
fi

# Stage all changes
echo "Staging changes..."
git add .

# Commit changes with the constructed message
echo "Committing changes..."
if git commit -m "$COMMIT_MESSAGE"; then
    echo "Commit successful!"
else
    echo "Error: Commit failed. Please check for any issues."
    exit 1
fi

# Push changes to the remote repository
echo "Pushing changes to the remote repository..."
if git push; then
    echo "Changes have been pushed successfully!"
else
    echo "Error: Unable to push changes. Please check your repository and network connection."
    exit 1
fi
