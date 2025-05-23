import fitz

def extract_text_from_pdf(upload_file):
    text="" 
    with fitz.open(stream=upload_file.file.read(),filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

