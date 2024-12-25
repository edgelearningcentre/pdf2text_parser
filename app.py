import streamlit as st
import fitz  # PyMuPDF
from unidecode import unidecode

def extract_text_from_data(data):
    """Extract text from the block data dictionary."""
    extracted_text = []
    for page_number, items in data.items():
        for item in items:
            if item['type'] == 0:  # Type 0 indicates text blocks
                for line in item['lines']:
                    for span in line['spans']:
                        extracted_text.append(span['text'])
    return ' '.join(extracted_text)

def clean_and_format_text(text):
    """Clean and format the extracted text into Markdown."""
    text = unidecode(text)  # Normalize text
    lines = text.splitlines()  # Split text into lines
    cleaned_lines = [line.strip() for line in lines if line.strip()]  # Remove empty and whitespace-only lines

    # Format Markdown headings and content based on simple heuristics
    formatted_text = ""
    for line in cleaned_lines:
        if line.endswith(":") and len(line.split()) < 10:  # Heuristic for headings
            formatted_text += f"## {line}\n\n"
        else:
            formatted_text += f"{line}\n\n"

    return formatted_text

def extract_text_from_pdf(uploaded_file):
    """Extract text from an uploaded PDF file."""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    block_dict = {}
    page_num = 1
    for page in doc:
        file_dict = page.get_text('dict')
        block = file_dict['blocks']
        block_dict[page_num] = block
        page_num += 1
    raw_text = extract_text_from_data(block_dict)
    return clean_and_format_text(raw_text)

# Streamlit App Interface
st.title("PDF Text Extractor")
st.write("Upload a PDF file to extract its text in a clean, Markdown-formatted style with proper headings.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    if st.button("Extract Text"):
        with st.spinner("Extracting text, please wait..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
        st.success("Text extraction complete!")
        st.markdown(extracted_text)
else:
    st.info("Please upload a PDF file to proceed.")
