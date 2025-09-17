from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pypdf import PdfReader
from pdf.parser import GeminiAPI
from pdf.converter import PDFer
from dotenv import load_dotenv
import os
class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Application Tools')
        self.setGeometry(150, 100, 1600, 700)

        self.layout = QtWidgets.QVBoxLayout()

        self.upload_button = QtWidgets.QPushButton('Upload PDF')
        self.upload_button.clicked.connect(self.upload_pdf)
        self.layout.addWidget(self.upload_button)

        # Job Description label and input
        self.jobdesc_label = QtWidgets.QLabel('Job Description')
        self.layout.addWidget(self.jobdesc_label)
        self.input_area = QtWidgets.QTextEdit()
        self.layout.addWidget(self.input_area)

        # CV and Cover Letter labels and fields side-by-side
        self.fields_layout = QtWidgets.QHBoxLayout()

        self.cv_layout = QtWidgets.QVBoxLayout()
        self.cv_label = QtWidgets.QLabel('CV')
        self.cv_layout.addWidget(self.cv_label)
        self.text_area = QtWidgets.QTextEdit()
        self.text_area.setReadOnly(True)
        self.cv_layout.addWidget(self.text_area)

        self.cover_layout = QtWidgets.QVBoxLayout()
        self.cover_label = QtWidgets.QLabel('Cover Letter')
        self.cover_layout.addWidget(self.cover_label)
        self.cover_area = QtWidgets.QTextEdit()
        self.cover_area.setReadOnly(True)
        self.cover_layout.addWidget(self.cover_area)

        self.fields_layout.addLayout(self.cv_layout)
        self.fields_layout.addLayout(self.cover_layout)
        self.layout.addLayout(self.fields_layout)

        # Add Generate button at the bottom
        self.generate_button = QtWidgets.QPushButton('Generate')
        self.generate_button.clicked.connect(self.generate_text)
        self.layout.addWidget(self.generate_button)

        self.setLayout(self.layout)
        try:
            importtext = open("prev.txt", "r", encoding="utf-8").read()
            self.text_area.setPlainText(importtext)
        except:
            pass

    def upload_pdf(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if file_name:
            self.parse_pdf(file_name)

    def parse_pdf(self, file_path):
        try:
            reader = PdfReader(file_path)
            self.pdf_text = ""
            for page in reader.pages:
                self.pdf_text += page.extract_text(extraction_mode="layout") or ""
            self.text_area.setPlainText(self.pdf_text)
            with open("prev.txt", "w", encoding="utf-8") as f:
                f.write(self.pdf_text)
            QMessageBox.information(self, 'Success', 'PDF parsed successfully!')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed! {str(e)}')
            print(f"Error: {str(e)}")

    def generate_text(self):
        try:
            jobdesc = self.input_area.toPlainText()
            text = self.text_area.toPlainText()
            if not text or not jobdesc:
                QMessageBox.warning(self, 'Warning', 'Please upload a PDF and enter a job description.')
                return
            load_dotenv()
            api_key = os.environ["API_KEY"]
            api = GeminiAPI()
            cvresult = api.cv_call(api_key, text, jobdesc)
            self.text_area.setPlainText(cvresult)
            coverresult = api.cover_call(api_key, text, jobdesc)
            self.cover_area.setPlainText(coverresult)


        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed! {str(e)}')
            print(f"Error: {str(e)}")