#!/bin/bash

git pull
sh JavaStuff/CleanClass.sh
git status
sleep 1
git add --all
git status
sleep 1
read -p "Commit Name:" commit
echo commit
git commit -m "$commit"
git push origin master
