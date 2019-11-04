#!/bin/bash

git status
sleep 1
git add --all
git status
sleep 1
read -p "Commit Name:" commit
git commit -m $commit
git push origin master
