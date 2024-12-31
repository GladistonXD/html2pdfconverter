# HTML EPUB to PDF Converter

This is a Python script that converts HTML files to PDF made for conversion of .html `EPUB` with markers template using the `wkhtmltopdf` tool and the `pdfkit` library. The script allows for customization of page size and file paths via command-line arguments.
PDF book formats do not work because they use SVG images

## Features

- Converts HTML files to PDF
- Supports custom page sizes (default is A4)
- Flexible options via command-line arguments
- Uses `wkhtmltopdf` for high-quality PDF rendering

## Requirements

- Python 3.x
- `wkhtmltopdf` installed on your system

### Python Libraries

The required Python libraries are listed in the `requirements.txt` file. Install them using the following command:

```bash
pip install -r requirements.txt
```
# Installation

# Clone the repository
```bash
git clone https://github.com/GladistonXD/html2pdfconverter.git
cd html2pdfconverter
```
# Install the required Python libraries
```bash
pip install -r requirements.txt
```
# Install wkhtmltopdf
-  Download and install wkhtmltopdf from the official website:
-  https://wkhtmltopdf.org/downloads.html
-  After installation, note the path to the wkhtmltopdf executable.

## Usage

# Run the script from the command line with the following options
- python html2pdfconverter.py -p <path_file> -i <input_html_file> -o <output_pdf_file> -s <page_size> 

# Example
```bash
python html2pdfconverter.py --path "C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe" --input perlego.html --output perlego.pdf --page-size A4
```
# Command-Line Options:
-  -i, --input: Path to the input HTML file (required)
-  -o, --output: Path to the output PDF file (required)
-  -s, --page-size: Page size for the PDF (default is A4)
-  -p, --path: Path to the wkhtmltopdf executable (required)

# Example of Shortened Command
```bash
python html2pdfconverter.py -p "C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe" -i perlego.html -o perlego.pdf -s A3
```
# Default Values:
-  Page size defaults to A4.
# Supported values:
- A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, B0, B1, B10, B2, B3, B4, B5, B6, B7, B8, B9, C5E, Comm10E, DLE, Executive, Folio, Ledger, Legal, Letter, Tabloid
