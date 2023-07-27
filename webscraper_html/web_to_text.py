import requests
from bs4 import BeautifulSoup
import textwrap
import re
import subprocess

def extract_text_from_webpage(url):
    try:
        # Send a GET request to the URL to fetch the webpage's content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request fails

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')  # Use response.content instead of response.text

        # Find all the paragraphs or relevant elements containing the story text
        # You might need to inspect the webpage's HTML to find the specific elements containing the story
        story_paragraphs = soup.findAll('pre')  # Example: Assuming the story is written in <p> tags

        # Extract the text from each paragraph and join them with two line breaks
        story_text = '\n\n'.join(paragraph.get_text() for paragraph in story_paragraphs)

        return story_text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def save_text_to_ebook(text, filename):
    try:
        # Create an EPUB e-book using Calibre's ebook-convert command-line tool
        subprocess.run(['ebook-convert', '-', filename, '--output-profile', 'tablet'],
                       input=text.encode('utf-8').decode(),  # Convert bytes to string before passing
                       check=True,
                       text=True,  # Set text to True to indicate that the input is a string
                       capture_output=True)

        print(f"E-book saved to {filename} successfully!")
    except subprocess.CalledProcessError as e:
        # If there's an error, print the detailed error message from stderr
        print(f"Error while saving the e-book: {e.stderr.encode()}")
    except Exception as e:
        print(f"Error while saving the e-book: {e}")


def save_text_to_file(text, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Split the text into paragraphs
            paragraphs = text.split('\n\n')
            for paragraph in paragraphs:
                final_text = re.sub(r'\s+', ' ', paragraph)
                # Format each paragraph to a maximum width of 180 characters and save it to the file
                wrapped_text = textwrap.fill(final_text, width=180)
                file.write(wrapped_text + '\n\n')  # Add two line breaks to separate paragraphs
        print(f"Text saved to {filename} successfully!")
    except Exception as e:
        print(f"Error while saving the file: {e}")

# url of the webpage
if __name__ == "__main__":
    url = "https://www.bdsmlibrary.com/stories/wholestory.php?storyid=242"  # Replace this with the actual URL of the story
    story_text = extract_text_from_webpage(url)
    if story_text:
        # Save the story to a text file using utf-8 encoding and proper formatting
        save_text_to_file(story_text, "story.txt")

        # Save the story to an EPUB e-book
        #save_text_to_ebook(story_text, "story.epub")
