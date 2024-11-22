import zipfile
import os

OUTPUT_FOLDER = "html_pages"

# Step 5: Optional - Zip all HTML files
def create_zipfile():
    zip_path = os.path.join(OUTPUT_FOLDER, "html_pages.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for i in range(1, 25):
            file_path = os.path.join(OUTPUT_FOLDER, f"{i}.html")
            if os.path.exists(file_path):
                zipf.write(file_path, os.path.basename(file_path))
    print(f"HTML files zipped into {zip_path}")