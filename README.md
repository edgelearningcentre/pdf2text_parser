# PDF Text Extractor

This is a **Streamlit application** that allows users to upload PDF files, extract text from them, and display the extracted text in a clean content.

## Features

- **Upload PDF Files**: Easily upload PDF documents for text extraction.
- **Text Extraction**: Extracts and processes text from PDFs using PyMuPDF (Fitz).
- **Interactive Interface**: User-friendly interface to upload files and view results instantly.

## Requirements

- Python 3.9 or higher
- Libraries:
  - `streamlit`
  - `pymupdf`
  - `unidecode`

## Installation

1. Clone this repository or download the code:
   ```bash
      https://github.com/edgelearningcentre/pdf2text_parser.git
      cd pdf2text_parser
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## How to Use

1. Open the Streamlit app in your browser (usually at `http://localhost:8501`).
2. Upload a PDF file using the file uploader.
3. Click the "Extract Text" button.
4. View the extracted and formatted text displayed in the app.

## Example Output

- **Uploaded PDF**: A research paper or document.
- **Extracted Text**: Structured content 
  ```

## Limitations

- The accuracy of heading detection relies on simple heuristics and may require adjustments for complex PDF layouts.
- Currently supports only text-based PDFs, not scanned image PDFs.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve this app.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

**Author**: edgelearningcentre
**Contact**:  edgelearning2017@gmail.com

