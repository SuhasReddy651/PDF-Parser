import streamlit as st
import tempfile
import base64
from pdf_utils import extract_text_from_pdf, get_exported_content

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>PDF Parsing and Export Tool</h1>",
            unsafe_allow_html=True)

# Session state to track submission
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Define columns
col1, sp, col2 = st.columns([2, 0.5, 3])

with col1:
    st.markdown("### Upload & Export Options")

    # File uploader
    uploaded_file = st.file_uploader("Upload your PDF", type=".pdf")

    # Export format selector
    export_format = st.radio("Select Export Format", [
                             ".txt", ".json", ".md"], index=None)

    # Submit button
    if st.button("Submit", type='primary'):
        # Validation
        if not uploaded_file and not export_format:
            st.error("❌ Please upload a PDF and select an export format.")
            st.session_state.submitted = False
        elif not uploaded_file:
            st.error("❌ Please upload a PDF file.")
            st.session_state.submitted = False
        elif not export_format:
            st.error("❌ Please select an export format.")
            st.session_state.submitted = False
        else:
            st.session_state.submitted = True

    # Show download button only if valid submission
    if st.session_state.submitted:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        extracted_pages = extract_text_from_pdf(tmp_path)
        exported_text = get_exported_content(extracted_pages, export_format)

        # MIME type
        mime = "text/plain" if export_format in [
            ".txt", ".md"] else "application/json"

        st.download_button(
            label=f"Download as {export_format.upper()}",
            data=exported_text,
            file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}{export_format}",
            mime=mime
        )

with col2:
    st.markdown("### PDF Preview")
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        # Display PDF
        with open(tmp_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
            pdf_display = f"""
                <iframe src="data:application/pdf;base64,{base64_pdf}" 
                        width="100%" height="650px" type="application/pdf"
                        style="border:1px solid #ccc; border-radius: 6px;"></iframe>
            """
            st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.info("Upload a PDF to preview it here.")
