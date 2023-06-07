import re
import json

def pdf_to_text(path):
    # text = extract_text(path)
    # return text
    text = ""
    with open(path, 'r') as f:
        text = f.read()
        # print(text)
    return text

# def extract_blocks(text):
#     blocks = {}
#     block_pattern = re.compile(r"^(\d+)\.", re.MULTILINE)
#     matches = list(block_pattern.finditer(text))

#     for i in range(len(matches)):
#         start = matches[i].start()
#         if i + 1 < len(matches):
#             end = matches[i + 1].start()
#             block_content = text[start:end]
#         else:
#             block_content = text[start:]
        
#         block_key = matches[i].group(1)
#         block_content = block_content.strip()
#         blocks[block_key] = block_content

#     return blocks

# def extract_blocks_and_lap(text):
#     blocks = {}
#     block_pattern = re.compile(r"^(\d+)\.", re.MULTILINE)
#     lapozz_a_pattern = re.compile(r"lapozz a (\d+)", re.IGNORECASE)
#     matches = list(block_pattern.finditer(text))

#     for i in range(len(matches)):
#         start = matches[i].start()
#         if i + 1 < len(matches):
#             end = matches[i + 1].start()
#             block_content = text[start:end]
#         else:
#             block_content = text[start:]
        
#         block_key = matches[i].group(1)
#         block_content = block_content.strip()
#         lapozz_a_matches = lapozz_a_pattern.findall(block_content)
#         lapozz_a_numbers = [int(match) for match in lapozz_a_matches]

#         blocks[block_key] = {
#             "text": block_content,
#             "lapozz_a": lapozz_a_numbers
#         }

#     return blocks

def extract_blocks_lapozz_change(text):
    blocks = {}
    block_pattern = re.compile(r"^(\d+)\.", re.MULTILINE)
    lapozz_a_pattern = re.compile(r"(lapozz a|Ha nem, a) (\d+)", re.IGNORECASE)
    matches = list(block_pattern.finditer(text))

    for i in range(len(matches)):
        start = matches[i].start()
        if i + 1 < len(matches):
            end = matches[i + 1].start()
            block_content = text[start:end]
        else:
            block_content = text[start:]
        
        block_key = matches[i].group(1)
        block_content = block_content.strip()
        lapozz_a_matches = lapozz_a_pattern.findall(block_content)
        lapozz_a_numbers = [int(match) for match in lapozz_a_matches]

        for index, number in enumerate(lapozz_a_numbers):
            block_content = block_content.replace(f"lapozz a {number}", f"lapozz a [{index + 1}]")

        blocks[block_key] = {
            "text": block_content,
            "lapozz_a": lapozz_a_numbers
        }

    return blocks

def extract_ha_van(text):
    match = re.search(r'ha van (\w+)', text)
    if match:
        return match.group(1)
    return None

def extract_blocks(text):
    blocks = {}
    block_pattern = re.compile(r"^(\d+)\.", re.MULTILINE)
    # lapozz_a_pattern = re.compile(r"(lapozz a|Ha nem, a|lapozz  a|lapozz  a\s*|lapozz  a) *(\n? *\d+)", re.IGNORECASE)
    lapozz_a_pattern = re.compile(r"(lapozz a|Ha nem, a|lapozz  a|lapozz  a\s*|lapozz  a|akkor a) *(\n? *\d+)", re.IGNORECASE)
    szerencse_pattern = re.compile(r"Tedd\s*próbára\s*SZERENCSÉD", re.IGNORECASE)
    matches = list(block_pattern.finditer(text))

    for i in range(len(matches)):
        start = matches[i].start()
        if i + 1 < len(matches):
            end = matches[i + 1].start()
            block_content = text[start:end]
        else:
            block_content = text[start:]
        
        block_key = matches[i].group(1)
        block_content = block_content.strip()
        lapozz_a_matches = lapozz_a_pattern.findall(block_content)
        lapozz_a_numbers = [int(re.sub(r"\n", "", match[1])) for match in lapozz_a_matches]

        for index, number in enumerate(lapozz_a_numbers):
            block_content = re.sub(f"({lapozz_a_matches[index][0]})\s*{number}", f"\\1 [{index + 1}]", block_content)

        ha_van_word = extract_ha_van(block_content)

        blocks[block_key] = {
            "text": block_content,
            "lapozz_a": lapozz_a_numbers,
            "szerencse_required": bool(szerencse_pattern.search(block_content))
        }

        if ha_van_word:
            blocks[block_key]["ha_van"] = ha_van_word

    return blocks

def save_to_json(information, json_file):
    # JSON fájlba mentés
    with open(json_file, 'w') as file:
        json.dump(information, file, ensure_ascii=False, indent=4)
        

pdf_file = 'kjkpdf.pdf'
json_file = 'halallabirintus.json'
test_text_file = 'testklk.txt'
text = pdf_to_text(test_text_file)
blocks = extract_blocks(text)

save_to_json(blocks, json_file)
# print(json.dumps(blocks, ensure_ascii=False, indent=2))
    