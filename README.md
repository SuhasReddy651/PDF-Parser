# 📄 PDF Parsing and Multiformat Exporter

This project provides a simple yet powerful interface to extract text from PDFs and export it into `.txt`, `.json`, or `.md` formats. It comes with both a **Streamlit GUI** and a **command-line interface** for flexibility across users and environments.

---

# 🚀 Key Features

1. **PDF Uploader**: Upload any `.pdf` file for processing.
2. **Text Extraction**: Extracts structured text content page-by-page using `pdfplumber`.
3. **Multi-format Export**: Choose between `.txt`, `.json`, or `.md` output formats.
4. **Preview Panel (UI)**: View your uploaded PDF on the left and preview export formats.
5. **Error Validation**: Ensures both file and format are selected before processing.
6. **Streamlit Theming**: UI supports custom dark/light themes via config file.
7. **CLI Mode**: Run the tool from your terminal to convert PDF files interactively.

---

# 🛠️ Tech Stack

* **Programming Language**
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

* **Frameworks & Libraries**
  ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
  ![pdfplumber](https://img.shields.io/badge/pdfplumber-003B57?style=for-the-badge\&logo=pdf\&logoColor=white)
  ![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge\&logo=json\&logoColor=white)

---

# 🏗️ Project Structure

```
pdf-parser-exporter/
├── pdf_utils.py        # Core utility for extracting and formatting text
├── app.py    # GUI app built using Streamlit
├── cli_app.py          # Command-line interface version
├── .streamlit/
│   └── config.toml     # Theme configuration for Streamlit UI
├── requirements.txt    # All required Python dependencies
└── README.md           # Project documentation
```

---

# 📊 How to Run the Project Locally

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pdf-parser-exporter.git
cd pdf-parser-exporter
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Option 1: Run the Streamlit App

```bash
streamlit run app.py
```

This will launch a web interface where you can:

* Upload PDF files
* Choose export format
* View the file and download the output

### Optional: Configure Theme

Create a `.streamlit/config.toml` file:

```toml
[theme]
base="dark"
primaryColor="#F63366"
backgroundColor="#1E1E1E"
secondaryBackgroundColor="#262730"
textColor="#FFFFFF"
```

---

## 💻 Option 2: Run the CLI App

```bash
python cli_app.py
```

You will be asked to:

* Enter the path to a `.pdf` file
* Choose output format (by number)
* Exported file will be saved inside `exports/` next to your input file

---

# 📂 Output Format Preview

### TXT Output

```
Page 1
=======
Hello world...

Page 2
=======
This is page 2.
```

### JSON Output

```json
{
  "Pages": {
    "Page 1": "Hello world...",
    "Page 2": "This is page 2."
  }
}
```

### Markdown Output

```md
## Page 1

Hello world...

## Page 2

This is page 2.
```

---

# 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
