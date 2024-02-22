# This will be used to pull the feed from the server and store it in a file

# Take the argument from the command line, it will be a URL. This is the URL of the feed to pull. Store it in the variable feedURL.
import sys
import datetime
import requests

# feedName will be the first argument from the command line
feedName = sys.argv[1]

# Take the argument from the command line, it will be a URL. This is the URL of the feed to pull. Store it in the variable feedURL.
feedURL = sys.argv[2]

# Request the feed from the server using the feedURL
# Store the feed in the variable feedContent
# Use the requests module to make a GET request to the feedURL
# Make a GET request to the feedURL and store the response in the variable response
response = requests.get(feedURL)

# Store the content of the response in the variable feedContent
feedContent = response.content

# Open the file "feedName-date-time.txt" in write mode and store the file object in the variable feedFile.
# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d-%H-%M-%S")

# Create the file name using the feedName and formatted_datetime
file_name = f"{feedName}-{formatted_datetime}.txt"

# Open the file with the created file name in write mode and store the file object in the variable feedFile
feedFile = open(file_name, "w")

# Write the feedContent to the file
# Write the feedContent to the file using the write method of the file object feedFile
feedFile.write(feedContent)

# Close the file
# Close the file using the close method of the file object feedFile
feedFile.close()

# Print a message to the user indicating that the feed has been pulled and stored in the file
# Print a message to the user indicating that the feed has been pulled and stored in the file

print(f"The feed has been pulled and stored in the file {file_name}.")

