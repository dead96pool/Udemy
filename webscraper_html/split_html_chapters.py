from bs4 import BeautifulSoup

def format_chapter_name(chapter_number):
    return f"{chapter_number:04d}"

def split_html_into_chapters(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'lxml')

    # Find all the chapter div elements (You may need to adjust the tag and class names)
    chapters = soup.find_all('div', class_='chapter')

    for index, chapter in enumerate(chapters, start=1):
        # Create a new BeautifulSoup object for each chapter
        chapter_soup = BeautifulSoup(str(chapter), 'lxml')

        # Add any necessary header, CSS, or other content to the chapter here
        # For example, you could add a title to each chapter:
        chapter_title = chapter_soup.new_tag('h2')
        formatted_chapter_number = format_chapter_name(index)
        chapter_title.string = f"Chapter {formatted_chapter_number}"
        chapter.insert(0, chapter_title)

        # Save each chapter as a separate HTML file
        chapter_filename = f"{formatted_chapter_number}.html"
        with open(chapter_filename, 'w', encoding='utf-8') as chapter_file:
            chapter_file.write(chapter_soup.prettify())

if __name__ == "__main__":
    input_html_file = "output.html"  # Replace with the path to your HTML file
    split_html_into_chapters(input_html_file)
