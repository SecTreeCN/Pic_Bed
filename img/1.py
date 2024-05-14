import os

# The directory containing the Markdown files.
markdown_directory = r'E:\Blog\source\_posts'

# The image file we are looking for references to.
image_filename = '3044521-20230801142810846-198498989.png'

# A list to hold the names of files referencing the image.
referencing_files = []

# Error handling in case the directory does not exist or could not be accessed.
try:
    # Iterate over the files in the given directory.
    for md_file in os.listdir(markdown_directory):
        if md_file.endswith('.md'):
            # Construct the full path to the Markdown file
            file_path = os.path.join(markdown_directory, md_file)

            # Open and read the content of the Markdown file.
            with open(file_path, 'r', encoding='utf-8') as file:
                contents = file.read()

            # Check if the image filename is referenced in the content.
            # Specifically check for the 'assets' sub-directory reference.
            if f"{image_filename}" in contents:
                referencing_files.append(md_file)

except FileNotFoundError:
    print("Directory not found. Please check the directory path.")

except Exception as e:
    print(f"An error occurred: {e}")

# Display the list of files referencing the image.
print("Markdown files referencing the image:")
for file_name in referencing_files:
    print(file_name)