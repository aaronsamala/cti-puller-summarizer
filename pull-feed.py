# This will be used to pull the feed from the server and store it in a file

# Take the argument from the command line, it will be a URL. This is the URL of the feed to pull. Store it in the variable feedURL.
import sys
import datetime
import requests
import subprocess
import xml.etree.ElementTree as ET

# create a testing boolean to test the script

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

# the feed format schema can be viewed in BleepingComputer-2024-02-22-00-08-32.txt
# parse the feed and extract the title, pubDate, dc:creator, link and description

feedXML = ET.fromstring(feedContent)
# Do something with the extracted data
# For example, print the extracted data
# Extract the title, pubDate, dc:creator, link and description from the feedXML
# Extract the title, pubDate, dc:creator, link and description from the feedXML
# Extract the title, pubDate, dc:creator, link and description from the feedXML

# Loop through each item in the feedXML and extract the title, pubDate, dc:creator, link and description
# Create an array of the items in the feedXML


for item in feedXML.findall('.//item'):
    title = item.find('title').text
    pubDate = item.find('pubDate').text
    creator = item.find('{http://purl.org/dc/elements/1.1/}creator').text
    link = item.find('link').text
    description = item.find('description').text
    print(f"Title: {title}")
    print(f"PubDate: {pubDate}")
    print(f"Creator: {creator}")
    print(f"Link: {link}")
    print(f"Description: {description}")
    print("\n")
    # scrape the link and extract the content
    response= requests.get(link, headers=headers)
    # store the content in a file; the file name will be the title of the article (replace spaces with hyphens)
    # Replace spaces in the title with hyphens
    file_name = title.replace(" ", "-") + ".html"

    # Create the file path for the "articles-to-be-processed" folder
    folder_path = "articles-to-be-processed/" + file_name

    # Open the file with the created file path in write mode and store the file object in the variable articleFile
    articleFile = open(folder_path, "w")

    # Decode the content from bytes to string using utf-8 encoding before writing to the file
    articleFile.write(response.content.decode('utf-8'))

    # Close the file
    articleFile.close()



# Call the generate-summary-from-rss-feed.py script with the file_name as the argument
#subprocess.call(["python3", "generate-summary-from-rss-feed.py", file_name])

