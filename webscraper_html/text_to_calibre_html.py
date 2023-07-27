from bs4 import BeautifulSoup

def convert_text_to_html(input_file, output_file, encoding='utf-8'):
    # Read the content of the text file with the specified encoding
    with open(input_file, 'r', encoding=encoding) as file:
        text_content = file.read()

    # Replace line breaks with <br> tags to preserve paragraph structure
    html_content = text_content.replace('\n', '<br>')
    html_content = html_content.replace("CHAPTER", "</div>\n<div class=chapter>\nCHAPTER")

    # Create a BeautifulSoup object with the HTML content and specify the parser
    soup = BeautifulSoup(html_content, 'html.parser')

    # Create a new HTML file and write the converted content
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

if __name__ == "__main__":
    input_file_name = "story.txt"  # Replace with the name of your input text file
    output_file_name = "output.html"  # Replace with the desired name for the output HTML file

    try:
        convert_text_to_html(input_file_name, output_file_name)
        print("Conversion successful.")
    except UnicodeDecodeError as e:
        print("Error: Unable to decode the file using the default encoding.")
        print("Try specifying a different encoding using the 'encoding' parameter in the 'convert_text_to_html' function.")
