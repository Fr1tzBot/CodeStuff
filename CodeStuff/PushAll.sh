#!/bin/bash

git pull
sh JavaStuff/CleanClass.sh
git add --all
git status
read -p "Commit Name: " commit
git commit -m "$commit"
git push origin master
