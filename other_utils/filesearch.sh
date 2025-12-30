#!/bin/bash

echo "where to search..(path)?:"
directory=""
read directory
echo "enter phrase"
search=""
read search
count=0

if [ "$directory"=="~" ]; then
	directory=$(pwd)
elif [[ -z "$directory" ]]; then
	directory=$(pwd)
	echo "Using directory: $directory"
fi

if [ ! -d "$directory" ]; then
	echo "Directory "$directory" doesn't exist!"
	exit 1
fi

echo "Searching for the phrase...$search in $directory..."
echo -e "\n\033[1;31m---  Searching for the phrase...$search in $directory... ---\033[0m"

for file in "$directory"/*.*;
	do
		if grep -q "$search" "$file"; then 
			((count++))
        		echo -e "\033[1;33mFound log file: $(basename "$file") => "$directory"/"$file"\033[0m"
			echo -e "\n\033[1;32m--- Contents of $file ---\033[0m"
			cat "$file" | grep "$search"
			echo -e "\n\033[1;32m--- EOF of $file ---\033[0m"
    		else
			echo "nothing found $(basename "$file")!"
		fi
	done

echo -e "\n\033[1;31m---"$count" found---\033[0m"
