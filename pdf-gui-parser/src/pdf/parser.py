class GeminiAPI:
    def __init__(self):
        pass

    def cv_call(self, apikey,cv_text,jobdesc):
        import google.generativeai as genai
        from pdf.converter import PDFer
        savehandler = PDFer()
        genai.configure(api_key=apikey)
        print("Debug: API key configured.")
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.contextdata = """instructions('''Modify this CV with for the following role, returning the full CV only.)
        Attempt to format the given input into a CV.ELSE, Reject any input that is not possible to create a CV from AND Return an error specifying that an invalid input was recieved, formatted correctly:
        error "Can't process CV"
        The resulting CV should be formatted in markdown.
        Your inputs are a CV and a job description.
        Your outputs are a modified CV to fit the job description.
        Markdown formatting should be used. Avoid using | in the CV, as it interferes with markdown formatting.
        The CV should be entirely based on the input CV, with no additional information added.
        Relevant skills and experiences should be highlighted, and the CV should be formatted in a clear and professional manner.
        Any skills mentioned in the job description that are not present in the CV should added if they are plausible based on the existing content of the CV. Try to add as many skills to meet the job description as possible, but ensure they fit the existing content of the CV. Do not state if the skill was added or not.
        Any experiences or qualifications not present in the CV should not be added, but if they are similar to existing content they can be modified to fit the job description.
        The CV should be concise and relevant to the job description, avoiding any unnecessary information.
    
        Do not annotate the CV with any additional information.
        CV: 
        """
        print("Debug: Generating response...")
        
        response = self.model.generate_content(self.contextdata+cv_text+"\n Job Description: "+jobdesc)
        with open("cv.md", "w", encoding="utf-8") as f:
            f.write(response.text)
            print("CV export complete.")
        savehandler.toPDF("cv.md")
        print("Done!")
        return(response.text)
    
    def cover_call(self, apikey,cv_text,jobdesc):
        import google.generativeai as genai
        from pdf.converter import PDFer
        savehandler = PDFer()
        genai.configure(api_key=apikey)
        print("Debug: API key configured.")
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.contextdata = """instructions('''Write a cover letter for the following role, returning the full cover letter only.)
        Begin with "Dear Hiring Manager," and end with a signature. No other formatting should be included.
        Reject any input that is not possible to create a cover letter from AND Return an error specifying that an invalid input was recieved, formatted correctly:
        error "Can't process cover letter"
        Your inputs are a CV and a job description.
        Your outputs are a cover letter tailored to the job description.
        Markdown formatting should be used.
        The cover letter should be entirely based on the input CV, but should not simply restate the CV.
        Relevant skills and experiences should be highlighted, and the cover letter should be formatted in a clear and professional manner.
        Any skills mentioned in the job description that are not present in the CV should be added if they are plausible based on the existing content of the CV. Do not state if the skill was added or not.
        Any experiences or qualifications not present in the CV should not be added, but if they are similar to existing content they can be modified to fit the job description.
        The cover letter should be concise and relevant to the job description, avoiding any unnecessary information.
        The cover letter should explain why the candidate is a good fit for the role based on their experiences and skills.
        CV: 
        """
        print("Debug: Generating response...")
        
        response = self.model.generate_content(self.contextdata+cv_text+"\n Job Description: "+jobdesc)
        with open("coverletter.md", "w", encoding="utf-8") as f:
            f.write(response.text)
            print("Cover letter export complete.")
        savehandler.toPDF("coverletter.md")
        print("Done!")
        return(response.text)
    

