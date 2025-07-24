import os
from pdf_utils import extract_text_from_pdf, get_exported_content, save_exported_file


def main():
    print("📄 PDF to Text Exporter\n")

    # Get PDF file path
    while True:
        pdf_path = input("Enter the path to the PDF file: ").strip()
        if not os.path.isfile(pdf_path):
            print("❌ File not found. Please try again.\n")
        elif not pdf_path.lower().endswith(".pdf"):
            print("❌ The selected file is not a PDF.\n")
        else:
            break

    # Choose export format
    formats = {1: ".txt", 2: ".json", 3: ".md"}
    print("\nChoose export format:")
    for k, v in formats.items():
        print(f"{k}. {v}")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): ").strip())
            if choice in formats:
                export_format = formats[choice]
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("❌ Please enter a number (1, 2, or 3).")

    # Extract and convert
    print("\n🔍 Extracting text from PDF...")
    extracted_pages = extract_text_from_pdf(pdf_path)
    if not extracted_pages:
        print("⚠️ No extractable text found in the PDF.")
        return

    content = get_exported_content(extracted_pages, export_format)

    # Define output path
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(os.path.dirname(
        pdf_path), base_name + export_format)

    # Save output
    save_exported_file(output_path, content)
    print(f"✅ Exported successfully to: {output_path}")


if __name__ == "__main__":
    main()
