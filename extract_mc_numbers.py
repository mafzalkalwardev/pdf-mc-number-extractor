import os
import re
from PyPDF2 import PdfReader

def extract_mc_numbers_from_pdf(pdf_path):
    """Extract all MC numbers from a single PDF file."""
    mc_numbers = set()  # Using a set to avoid duplicates
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    # Find all MC-XXXXXXX patterns (case insensitive)
                    matches = re.findall(r'MC[-–—]\s*(\d+)', text, re.IGNORECASE)
                    mc_numbers.update(matches)
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")
    return mc_numbers

def process_directory(directory):
    """Process all PDF files in a directory and extract MC numbers."""
    all_mc_numbers = set()
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            mc_numbers = extract_mc_numbers_from_pdf(pdf_path)
            all_mc_numbers.update(mc_numbers)
    
    # Sort the numbers numerically
    sorted_numbers = sorted(all_mc_numbers, key=lambda x: int(x))
    return sorted_numbers

def save_to_file(mc_numbers, output_file='ids.txt'):
    """Save MC numbers to a text file."""
    with open(output_file, 'w') as f:
        for number in mc_numbers:
            f.write(f"{number}\n")

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Process all PDFs in the same directory
    mc_numbers = process_directory(script_dir)
    
    # Save results
    save_to_file(mc_numbers)
    
    # Print summary
    print(f"Extracted {len(mc_numbers)} unique MC numbers.")
    print(f"Results saved to ids.txt in: {script_dir}")