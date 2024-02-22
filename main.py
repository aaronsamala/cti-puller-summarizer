# this will be the main python application
# it will be the entry point for the application
# it will be the main file that will be run
# it will be the file that will be run by the user
# it will call the pull-feed.py, it will provide the feedName as the first argument and the feedURL as the second argument

# call pull-feed.py with the feedName and feedURL as the arguments
# This will call the pull-feed.py file with the feedName and feedURL as the arguments
#
# Call the pull-feed.py script with the feedName and feedURL as the arguments

import subprocess
import sys
import os

# Get the feedName and feedURL from the command line arguments
feedName = sys.argv[1]
feedURL = sys.argv[2]

# Call the pull-feed.py script with the feedName and feedURL as the arguments
subprocess.call(["python3", "pull-feed.py", feedName, feedURL])

# Call the cleanup-the-article.py script with the feedName as the argument
subprocess.call(["python3", "cleanup-the-article.py", feedName])

# iterate through the articles-cleaned-up directory and call the generate-summary.py script with the filename as the argument
# use the os module to list the files in the articles-cleaned-up directory
# Iterate through each file in the directory
# For each file, call the generate-summary.py script with the filename as the argument


# Get the path to the articles-cleaned-up directory
articles_dir = "./articles-cleaned-up"

# Iterate through each file in the directory
for filename in os.listdir(articles_dir):
    # Construct the full path to the file
    file_path = os.path.join(articles_dir, filename)

    # Check if the file is a regular file
    if os.path.isfile(file_path):
        # Call the generate-summary.py script with the filename as the argument
        subprocess.call(["python3", "generate-summary.py", file_path])
