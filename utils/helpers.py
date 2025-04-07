import re

# Function to remove HTML tags
def remove_html_tags(text):
    return re.sub(r'<[^>]*>', '', text)