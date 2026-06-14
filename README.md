<div align="center">

# 🚀 Pdf MC Number Extractor

**A Python utility that extracts MC numbers from PDF files, removes duplicates, sorts them, and saves the results into a text file.**

Documented · MIT licensed · Maintained

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

</div>

---

## 🐍 Contribution graph

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/mafzalkalwardev/pdf-mc-number-extractor/output/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/mafzalkalwardev/pdf-mc-number-extractor/output/snake.svg" />
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/mafzalkalwardev/pdf-mc-number-extractor/output/snake.svg" />
</picture>

---

\# PDF MC Number Extractor

A Python utility that extracts MC numbers from PDF files automatically.

The script scans all PDF files in the same folder, extracts MC numbers, removes duplicates, sorts them, and saves the final result into a text file.

\## Screenshots

## Features

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
