# this script will be used to clean up the articles to be processed
# it will be called by the main.py script
# it will be called with the feedName as the argument
#

import sys
import os
import subprocess
import re
import shutil
from bs4 import BeautifulSoup

# Get the feedName from the command line arguments
feedName = sys.argv[1]
# print the feedName
print(feedName)

# iterate through each file in the articles-to-process directory
# for each file, read the content and clean it up
# write the cleaned up content back to the file
# use the os module to list the files in the articles-to-process directory

# Get the path to the articles-to-process directory
articles_dir = "./articles-to-be-processed"

# Iterate through each file in the directory
for filename in os.listdir(articles_dir):
    # Construct the full path to the file
    def cleanup_content_bleeping_computer(content):
        # Add your cleanup logic here
        # keep only the content in the <div class="articleBody"> tag
        

        # Use regular expressions to extract the content within the <div class="articleBody"> tag
        soup = BeautifulSoup(content, 'html.parser')
        article_body = soup.find('div', {'class': 'articleBody'})

        if article_body is not None:
            article_content = article_body.text
        else:
            print("No div with class 'articleBody' found")
        return article_content

    file_path = os.path.join(articles_dir, filename)

    # move the file to the ../articles-processed directory
    # ...

    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Clean up the content
        cleaned_content = content
        if feedName == "BleepingComputer":
            cleaned_content = cleanup_content_bleeping_computer(content)

        # Write the cleaned up content back to the file
        with open(file_path, 'w') as file:
            if cleaned_content is not None:
                file.write(cleaned_content)
                processed_dir = "./articles-cleaned-up"
                processed_file_path = os.path.join(processed_dir, filename)
                shutil.move(file_path, processed_file_path)
            else:
                print("Warning: cleaned_content is None; not moving nothing to the processed directory.")

        # Move the file to the ../articles-processed directory
        





#if feedName == "BleepingComputer": parse the feed and only keep what's in the <div class="articleBody"> tag


