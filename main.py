from trigger import trigger
import time
import streamlit as st
from io import BytesIO
import os
import pandas as pd

if __name__ == "__main__":
    # pdf_path = "C:\\Users\\yasha\\OneDrive\\Desktop\\kadam2015.pdf"
    # approach = "fsl"
    # start = time.time()
    # res = trigger(pdf_path, approach)
    # for i in range(5):
    #     print(res[i])
    # end = time.time()
    #
    # print(f"Time: {end-start}")

    # zsl: 15 seconds
    # osl: 20 seconds
    # fsl: 18 seconds
    UPLOAD_DIR = "researchs"


    def clear_upload_dir():
        for filename in os.listdir(UPLOAD_DIR):
            file_path = os.path.join(UPLOAD_DIR, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")


    os.makedirs(UPLOAD_DIR, exist_ok=True)  # Streamlit interface
    st.title("PDF Processor")

    # File uploader for multiple PDF files
    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    # Dropdown menu for selecting an option
    option_id = st.selectbox("Choose an option",
                             ["Zero Shot Learning", "One Shot Learning", "Few Shot Learning", "RAG"])

    # Map dropdown text to option IDs
    option_id_mapping = {"Zero Shot Learning": "zsl", "One Shot Learning": "osl", "Few Shot Learning": "fsl",
                         "RAG": "zsl"}
    selected_option_id = option_id_mapping[option_id]

    # Button to process files
    if st.button("Process"):
        if uploaded_files:
            # Process the uploaded files
            clear_upload_dir()
            df = pd.DataFrame(columns=["Year", "Authors", "Title", "Findings", "Limitations"])
            for uploaded_file in uploaded_files:
                # Save each uploaded file to the specified directory
                file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # Process the saved file
                result = trigger(file_path, selected_option_id)
                df.loc[len(df)] = result
            st.table(df)
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='processed_data.csv',
                mime='text/csv',
            )


        else:
            st.warning("Please upload at least one PDF file.")
