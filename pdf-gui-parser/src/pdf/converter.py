from spire.doc import *
from spire.doc.common import *

class PDFer:
    def __init__(self):
        pass
    def toPDF(self,filepath):
        document = Document()
        document.LoadFromFile(filepath)
        base, _ = os.path.splitext(filepath)
        output_doc = base + ".docx"
        document.SaveToFile(output_doc, FileFormat.Docx)
        print(f"Converted to PDF successfully: {output_doc}")
        document.Dispose()
    
