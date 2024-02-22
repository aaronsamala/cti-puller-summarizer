# This will be used to pull the feed from the server and store it in a file

# Take the argument from the command line, it will be a URL. This is the URL of the feed to pull. Store it in the variable feedURL.
import sys
import datetime
import requests
import subprocess

# feedName will be the first argument from the command line
feedName = sys.argv[1]

# Take the argument from the command line, it will be a URL. This is the URL of the feed to pull. Store it in the variable feedURL.
feedURL = sys.argv[2]

# Request the feed from the server using the feedURL
# Store the feed in the variable feedContent
# Use the requests module to make a GET request to the feedURL
# Make a GET request to the feedURL and store the response in the variable response
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(feedURL, headers=headers)

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

# Decode the feedContent from bytes to string using utf-8 encoding before writing to the file
feedFile.write(feedContent.decode('utf-8'))

# Close the file
# Close the file using the close method of the file object feedFile
feedFile.close()

# Print a message to the user indicating that the feed has been pulled and stored in the file
# Print a message to the user indicating that the feed has been pulled and stored in the file

print(f"The feed has been pulled and stored in the file {file_name}.")

# call generate-summary-from-rss-feed.py with the file_name as the argument
# This will call the generate-summary-from-rss-feed.py file with the file_name as the argument


# Call the generate-summary-from-rss-feed.py script with the file_name as the argument
subprocess.call(["python3", "generate-summary-from-rss-feed.py", file_name])

