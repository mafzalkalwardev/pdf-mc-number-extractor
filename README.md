\# PDF MC Number Extractor



A Python utility that extracts MC numbers from PDF files automatically.



The script scans all PDF files in the same folder, extracts MC numbers, removes duplicates, sorts them, and saves the final result into a text file.



\## Features



\- Extract MC numbers from PDF files

\- Supports patterns like `MC-123456`

\- Removes duplicate MC numbers

\- Sorts MC numbers numerically

\- Saves output to `ids.txt`

\- Processes all PDFs in the folder automatically



\## Tech Stack



\- Python

\- PyPDF2

\- Regex



\## Project Structure



```text

pdf-mc-number-extractor/

│

├── extract\_mc\_numbers.py

├── README.md

└── .gitignore

```



\## Installation



```bash

pip install PyPDF2

```



\## How to Use



1\. Put your PDF files in the same folder as the script.

2\. Run:



```bash

python extract\_mc\_numbers.py

```



3\. Output will be saved in:



```text

ids.txt

```



\## Example Output



```text

123456

789012

456789

```



\## Use Cases



\- Dispatch data processing

\- Carrier MC number extraction

\- PDF data cleaning

\- Lead processing

\- FMCSA-related document parsing



\## Security Note



Do not upload private PDF files publicly.



\## Author



Muhammad Afzal Kalwar  

GitHub: @mafzalkalwardev

