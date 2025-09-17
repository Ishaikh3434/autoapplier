def is_pdf_file(file_path):
    return file_path.lower().endswith('.pdf')

def validate_file_selection(file_path):
    if not is_pdf_file(file_path):
        raise ValueError("Selected file is not a PDF.")
    return True

def read_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()