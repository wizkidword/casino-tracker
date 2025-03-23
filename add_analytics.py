import os
import streamlit as st
from bs4 import BeautifulSoup
import shutil
import pathlib

def add_analytics_tag():
    # Your Google Analytics tag with updated Measurement ID
    analytics_js = """
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RVJVWRK9BT"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-RVJVWRK9BT');
    </script>
    <div id="G-RVJVWRK9BT"></div>
    """
    analytics_id = "G-RVJVWRK9BT"

    # Find Streamlit's index.html file
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    print(f"Editing {index_path}")

    # Parse the HTML
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")

    # Check if the tag is already added
    if not soup.find(id=analytics_id):
        # Backup the original index.html
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)  # Restore from backup if exists
        else:
            shutil.copy(index_path, bck_index)  # Create a backup

        # Inject the analytics tag into the <head>
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + analytics_js)
        index_path.write_text(new_html)

if __name__ == "__main__":
    add_analytics_tag()