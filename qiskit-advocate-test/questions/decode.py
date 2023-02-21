import os
import sys
import json
import uuid 

class Form:
    def __init__(self):
        self.questions_data = None
        self.final_html_page = ""

    def add_questions(self, file):
        self.questions_data = json.loads(file)

    def create_questions_page(self, page_title, output_file_path):
        self.create_page_headers(page_title)
        self.add_questions_to_page()
        self.close_page()
        self.save_file(output_file_path)

    def create_page_headers(self, page_title):
        self.final_html_page = f"""
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">        
                    <link rel="stylesheet" type="text/css" href="styles.css" />
                    
                    <title>{page_title}</title>
                </head>
                <body>
                    <ul>
        """

    def add_questions_to_page(self):
        if(not self.questions_data):
            return

        for question_index, question in enumerate(self.questions_data["items"]):
            question_content = question["question"]
            question_answers = question["options"]
            self.add_question_content(question_content)
            self.add_question_answers(question_index, question_answers)

    def add_question_content(self, question_content):
        self.final_html_page += f"<li class=question_content>{question_content}"
    
    def add_question_answers(self, question_index, question_answers):
        self.final_html_page += '<ul>'
        for answer in question_answers:
            self.add_question_answer(question_index, answer)
        self.final_html_page += '</ul></li>'

    def add_question_answer(self, question_index, answer):
        answer_id = str(uuid.uuid4())
        self.final_html_page += f"""
            <li>
                <input type="radio" id="{answer_id}" value="{answer_id}" name="{question_index}" />
                <label for="{answer_id}">{answer}</label>
            </li>
        """
    
    def close_page(self):
        self.final_html_page += """
            </ul>
            </body>
            </html>
        """

    def save_file(self, output_file_path):
        with open(output_file_path, 'w') as html_file:
            html_file.write(self.final_html_page)

def get_questions_files_paths():
    files = os.listdir()
    elements_filter = lambda element: '.json' in element
    json_files = list(filter(elements_filter, files))
    return json_files

    

    return ["circuits.json", "advanced_circuits.json", "error_analysis.json"]

def get_page_title(filename):
    return filename.replace(".json", '').replace('_', ' ').capitalize()

if __name__ == '__main__':


    questions_files_paths = get_questions_files_paths()

    for questions_file_path in questions_files_paths:

        print(f"\n{questions_file_path}")

        with open(questions_file_path, 'r') as question_file:

            question_page_name = get_page_title(questions_file_path)
            question_page_output_file = f"{question_page_name}.html"

            questions_form = Form()
            questions_form.add_questions(question_file.read())
            
            print(f"creating {question_page_output_file}...")
            questions_form.create_questions_page(question_page_name, question_page_output_file)

    sys.exit(0)
