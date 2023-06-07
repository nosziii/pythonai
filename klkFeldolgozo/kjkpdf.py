import pdfplumber
import PyPDF2
import json
import re
from pdfminer.high_level import extract_text


# def extract_information(pdf_file):
#     # PDF fájl megnyitása PyPDF2.PdfFileReader(file)
#     with pdfplumber.open(pdf_file) as pdf:
#         # Információk kinyerése a PDF-ből
#         text = ''
#         for page in pdf.pages:
#             text += page.extract_text()

#     return text.encode("iso-8859-1").decode("utf-8")


# def pdf_to_text(path):
#     with pdfplumber.open(path) as pdf:
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text()
#         return text.encode("iso-8859-2").decode("utf-8")
    
def pdf_to_text(path):
    # text = extract_text(path)
    # return text
    text = ""
    with open(path, 'r') as f:
        text = f.read()
        # print(text)
    return text


def process_information(text):
    information = {}
    lines = text.split('\n')
    for line in lines:
        if line.startswith("A B C"):
            information["sequence"] = line.split()[3:]
        elif "Lapozz" in line:
            page_number_str = re.search(r"Lapozz a\s*(\d+)", line)
            if page_number_str:
                page_number = int(page_number_str.group(1))
            # page_number_str = line.split("Lapozz a")[-1].split("-")[0].strip(". ").strip()
            if  page_number_str.isdigit():
                page_number = int(page_number_str)
                information["page_number"] = page_number
            else:
                print(f"A lapozó szám értéke nem megfelelő: '{page_number_str}'")
        elif "ÜGYESSÉG" in line and "ÉLETERŐ" in line:
            stats = line.split()
            try:
                agility_index = stats.index("ÜGYESSÉG")
                if agility_index + 1 < len(stats):
                    information["agility"] = int(stats[agility_index + 1])
                else:
                    print("Az 'ÜGYESSÉG' értéke hiányzik a listából.")
            except ValueError:
                print("A 'ÜGYESSÉG' szó nem található a listában.")
            try:
                health_index = stats.index("ÉLETERŐ")
                if health_index + 1 < len(stats):
                    information["health"] = int(stats[health_index + 1])
                else:
                    print("Az 'ÉLETERŐ' értéke hiányzik a listából.")
            except ValueError:
                print("Az 'ÉLETERŐ' szó nem található a listában.")
        elif "SZERENCSÉD" in line:
            try:
                information["luck"] = int(line.split("SZERENCSÉD")[-1].strip("."))
            except ValueError:
                print("A 'SZERENCSÉD' szó nem található a listában.")
        elif "százalék" in line:
            information["percentage"] = int(line.split("százalék")[0].strip())
    return information


def save_to_json(information, json_file):
    # JSON fájlba mentés
    with open(json_file, 'w') as file:
        json.dump(information, file, ensure_ascii=False, indent=4)

def save_to_text(txt, txt_file):
    # TXT fájlba mentés
    with open(txt_file, 'w', encoding='UTF-8') as file:
        file.write(txt)


if __name__ == '__main__':
    pdf_file = 'kjkpdf.pdf'
    json_file = 'kjkpdf.json'
    test_text_file = 'testklk.txt'

    text = pdf_to_text(test_text_file)
    # print(text)
    # save_to_text(text, test_text_file)
    information = process_information(text)
    # print(information)
    save_to_json(information, json_file)
    print(f'Az információk sikeresen elmentve a {json_file} fájlba.')
