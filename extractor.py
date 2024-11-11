from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTTextLine, LTChar

import re

def extract_text_from_pdf(pdf_path, line_spacing_threshold=0.5, paragraph_spacing_threshold=20, column_divider=300):
    all_text = []

    for page_layout in extract_pages(pdf_path):
        left_column = []
        right_column = []

        for element in page_layout:
            if isinstance(element, LTTextContainer):
                for text_line in element:
                    if isinstance(text_line, LTTextLine):
                        line_text = []
                        prev_x = None

                        for char in text_line:
                            if isinstance(char, LTChar):
                                if prev_x is not None and (char.x0 - prev_x) > line_spacing_threshold * char.width:
                                    line_text.append(" ")
                                line_text.append(char.get_text())
                                prev_x = char.x1

                        if text_line.x0 < column_divider:
                            left_column.append((text_line.y0, text_line.x0, ''.join(line_text).strip()))
                        else:
                            right_column.append((text_line.y0, text_line.x0, ''.join(line_text).strip()))

        left_column.sort(key=lambda item: (-item[0], item[1]))
        right_column.sort(key=lambda item: (-item[0], item[1]))

        page_text = []
        prev_y = None

        for column in [left_column, right_column]:
            for y, x, text in column:
                if prev_y is not None and abs(prev_y - y) > paragraph_spacing_threshold:
                    page_text.append("\n")
                page_text.append(text)
                prev_y = y
            prev_y = None

        all_text.append("\n".join(page_text))

    return "\n\n".join(all_text)

def extract_specific_sections(text):
    # Pattern to capture various forms of section headers
    section_pattern = re.compile(
        r'(^[A-Z][A-Z ]+\n|^\d+\.\s+[A-Z ]+\n|^[IVXLCDM]+\.\s+[A-Z ]+\n|^Abstract|^Conclusion\n)',
        re.MULTILINE
    )

    # Find all section headers in the text
    matches = list(section_pattern.finditer(text))

    sections = {
        "Title and Authors": "",
        "Abstract and Introduction": "",
        "Conclusion": ""
    }

    # Step 1: Extract everything before the Abstract or first header into "Title and Authors"
    if matches:
        first_section_start = 0
        first_section_end = matches[0].start()
        sections["Title and Authors"] = text[first_section_start:first_section_end].strip()

    # Step 2: Iterate through headers and extract specific sections
    abstract_found = False  # Track if Abstract section has been found
    for i, match in enumerate(matches):
        section_title = match.group().strip()  # Exact match for inclusion in the output
        section_title_lower = section_title.lower()  # Lowercase for comparison

        # Define the content of this section
        section_start = match.end()
        section_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        section_content = text[section_start:section_end].strip()

        # Handle Abstract section and start appending into Abstract and Introduction
        if "abstract" in section_title_lower:
            sections["Abstract and Introduction"] = f"{section_title}\n{section_content}\n\n"
            abstract_found = True

        elif "introduction" in section_title_lower and abstract_found:
            sections["Abstract and Introduction"] += f"{section_title}\n{section_content}\n\n"

        elif "conclusion" in section_title_lower:
            sections["Conclusion"] = f"{section_title}\n{section_content}"

    return sections


def save_sections_to_files(sections):
    for section_name, content in sections.items():
        filename = section_name.replace(" ", "_").lower() + ".txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Saved {section_name} to {filename}")

if __name__=="__main__":
    ...
    # print('hi')
    # pdf_path = "C:\\Users\\yasha\\OneDrive\\Desktop\\kadam2015.pdf"
    # extracted_text = extract_text_from_pdf(pdf_path, line_spacing_threshold=0.5, paragraph_spacing_threshold=20)
    # sections = extract_specific_sections(extracted_text)
    # save_sections_to_files(sections)
