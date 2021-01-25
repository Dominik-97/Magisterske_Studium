#!/bin/bash

echo "Fetching and updating data"
git fetch && git pull

echo "Checking if there is something changed in the repository"
if ! git diff-index --quiet HEAD --; then
    read -p "Please specify what to commit the same way you would after git add." whattoCommit
    git add $whattoCommit
    read -p "What is your commit message?" commitMessage
    git commit -m "$commitMessage"
    git push
fi