#!/bin/bash
#To get all arguments
args="$@"
#get first
NAME=${args[0]}

cd 3klearnings
git stash 
git checkout main
git checkout -b $NAME
mkdir $NAME
cd $NAME
touch README.md 
git add .
git commit -m "[init] $NAME learnings"
git push --set-upstream origin $NAME