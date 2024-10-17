# this is a UTILITY FILE - THIS IS a helper file
import os
import PyPDF2
import json
import traceback

# We need data to define two methods

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)  # Corrected assignment operator
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text  # Return statement moved outside the for loop
        except Exception as e:
            raise Exception("Error reading the PDF file") from e  # Optional: keep the original exception context

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise Exception("Unsupported file format; only PDF and text files are supported")

def get_table_data(quiz_str):
    try:
        # Convert the quiz from a str to dict
        quiz_dict = json.loads(quiz_str)  # Corrected variable name
        quiz_table_data = []
        
        # Iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [f"{option}-> {option_value}" for option, option_value in value["options"].items()]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "choices": options, "correct": correct})

        return quiz_table_data  # Return statement moved outside the for loop

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False
