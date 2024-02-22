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

# Get the feedName and feedURL from the command line arguments
feedName = sys.argv[1]
feedURL = sys.argv[2]

# Call the pull-feed.py script with the feedName and feedURL as the arguments
subprocess.call(["python3", "pull-feed.py", feedName, feedURL])

# Call the generate-summary-from-rss-feed.py script with the feedName as the argument
