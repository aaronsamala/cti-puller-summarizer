# this script will be used to clean up the articles to be processed
# it will be called by the main.py script
# it will be called with the feedName as the argument
#

import sys
import os
import subprocess
import re
import shutil

# Get the feedName from the command line arguments
feedName = sys.argv[1]

# iterate through each file in the articles-to-process directory
# for each file, read the content and clean it up
# write the cleaned up content back to the file
# use the os module to list the files in the articles-to-process directory

# Get the path to the articles-to-process directory
articles_dir = "/articles-to-process"

# Iterate through each file in the directory
for filename in os.listdir(articles_dir):
    # Construct the full path to the file
    def cleanup_content(content):
        # Add your cleanup logic here
        # keep only the content in the <div class="articleBody"> tag
        

        # Use regular expressions to extract the content within the <div class="articleBody"> tag
        pattern = r'<div class="articleBody">(.*?)</div>'
        match = re.search(pattern, content, re.DOTALL)

        # Check if a match is found
        if match:
            # Get the content within the <div class="articleBody"> tag
            cleaned_content = match.group(1)
        else:
            # If no match is found, set cleaned_content to an empty string
            cleaned_content = ""

        # Remove any remaining HTML tags from the cleaned content
        cleaned_content = re.sub(r'<.*?>', '', cleaned_content)
        pass

    file_path = os.path.join(articles_dir, filename)

    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Clean up the content
        cleaned_content = cleanup_content(content)

        # Write the cleaned up content back to the file
        with open(file_path, 'w') as file:
            file.write(cleaned_content)

    # move the file to the ../articles-processed directory
    # ...

    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Clean up the content
        cleaned_content = cleanup_content(content)

        # Write the cleaned up content back to the file
        with open(file_path, 'w') as file:
            file.write(cleaned_content)

        # Move the file to the ../articles-processed directory
        processed_dir = "../articles-processed"
        processed_file_path = os.path.join(processed_dir, filename)
        shutil.move(file_path, processed_file_path)





#if feedName == "BleepingComputer": parse the feed and only keep what's in the <div class="articleBody"> tag


