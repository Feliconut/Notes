import re
import os
import sys

#!/usr/bin/env python3

def truncate_authors(bibtex_file, max_authors=20):
    """
    Truncates the number of authors in a BibTeX file to a maximum count.
    
    Args:
        bibtex_file (str): Path to the BibTeX file.
        max_authors (int): Maximum number of authors to keep.
    """
    # Read the entire file
    with open(bibtex_file, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    # content = content.replace(r'{CMS}', r'CMS')
    # Regular expression to find author fields
    author_pattern = r'(author\s*=\s*\{)(.+)(\},)'
    
    def process_authors(match):
        prefix = match.group(1)
        authors = match.group(2)
        suffix = match.group(3)
        
        # Split authors by " and " (BibTeX author separator)
        author_list = authors.split(' and ')
        
        # Check if we need to truncate
        if len(author_list) > max_authors:
            print(f"Entry has {len(author_list)} authors")
            print(f"Truncating entry from {len(author_list)} authors to {max_authors} authors")
            author_list = author_list[:max_authors]
            # Add "others" as the last entry
            author_list.append("others")
        
        # Join the authors back
        new_authors = ' and '.join(author_list)
        
        return prefix + new_authors + suffix
    
    # Replace author fields with truncated versions where needed
    # new_content = re.sub(author_pattern, process_authors, content, flags=re.DOTALL)
    new_content = []
    for line in content:
        new_line = re.sub(author_pattern, process_authors, line)
        new_content.append(new_line)
    
    # Write the modified content to a new file
    output_file = bibtex_file.replace('.bib', '_truncated.bib')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(new_content))
    
    print(f"Processed file saved as {output_file}")

if __name__ == "__main__":
    # Default parameters
    bibtex_file = "./reading-note/cms/zotero.bib"
    max_authors = 20
    
    # Parse command-line arguments if provided
    if len(sys.argv) > 1:
        bibtex_file = sys.argv[1]
    if len(sys.argv) > 2:
        max_authors = int(sys.argv[2])
    
    if not os.path.exists(bibtex_file):
        print(f"Error: File {bibtex_file} not found.")
        sys.exit(1)
    
    truncate_authors(bibtex_file, max_authors)