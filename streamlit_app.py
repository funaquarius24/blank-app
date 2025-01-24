import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

# Title of the app
st.title("File Downloader")

# File to be downloaded
file_path = "cell_segment_model_export.zip"  # Replace with your file path

# Read the file content
with open(file_path, "rb") as file:
    file_content = file.read()

# Create a download button with generic MIME type
st.download_button(
    label="Download File",
    data=file_content,
    file_name=file_path,
    mime="application/zip"  # Generic MIME type for unknown files
)

# Optional: Display a message
st.write("Click the button above to download the file.")
