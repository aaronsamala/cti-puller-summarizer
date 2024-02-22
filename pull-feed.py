# This will be used to pull the feed from the server and store it in a file

# Take the argument from the command line, it will be a URL. This is the URL of the feed to pull. Store it in the variable feedURL.
import sys
import datetime

# feedName will be the first argument from the command line
feedName = sys.argv[1]

# Take the argument from the command line, it will be a URL. This is the URL of the feed to pull. Store it in the variable feedURL.
feedURL = sys.argv[2]

# Open the file "feedName-date-time.txt" in write mode and store the file object in the variable feedFile.
# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")

# Create the file name using the feedName and formatted_datetime
file_name = f"{feedName}-{formatted_datetime}.txt"

# Open the file with the created file name in write mode and store the file object in the variable feedFile
feedFile = open(file_name, "w")
