import os
import json
import pdfplumber


def extract_text_from_pdf(pdf_path: str, x_tolerance: float = 1, y_tolerance: float = 1):
    """Extracts text from a PDF and returns a list of (Page Label, Text) tuples."""
    extracted_text = []

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages, start=1):
                try:
                    text = page.extract_text(
                        x_tolerance=x_tolerance, y_tolerance=y_tolerance)
                    if text:
                        extracted_text.append((f"Page {i}", text))
                except Exception as e:
                    print(f"Error extracting text from page {i}: {e}")
    except Exception as e:
        print(f"Failed to open PDF: {e}")
        return None

    return extracted_text


def get_exported_content(page_text_list, export_format=".txt") -> str:
    """Returns the formatted string content according to the export format."""
    if not page_text_list:
        return ""

    if export_format == ".txt":
        return "\n\n".join(
            f"{label}\n{'=' * len(label)}\n{text}" for label, text in page_text_list
        )

    elif export_format == ".json":
        json_data = {
            label: text.strip() + "\n\n"
            for label, text in page_text_list
        }
        return json.dumps({"Pages": json_data}, indent=2, ensure_ascii=False)

    elif export_format == ".md":
        return "\n\n".join(
            f"## {label}\n\n{text}" for label, text in page_text_list
        )

    else:
        raise ValueError(f"Unsupported format: {export_format}")


def save_exported_file(output_path: str, content: str):
    """Saves the content to the given file path."""
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"File saved to: {output_path}")
    except Exception as e:
        print(f"Failed to save file: {e}")
