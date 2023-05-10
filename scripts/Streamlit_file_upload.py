import streamlit as st
import os

# Define a function to read the first 12 lines of a text file
def read_file(file_path):
    with open(file_path) as f:
        lines = []
        for i in range(12):
            line = f.readline()
            if not line:
                break
            lines.append(line)
    return lines

# Create the Streamlit web app
def main():
    # Set the title and description
    current_dir = os.getcwd()
    st.title("Text File Viewer")
    st.write("Upload a text file to display its first 12 lines.")
    st.write(current_dir)

    # Create a file uploader component
    file = st.file_uploader("Choose a file", type=["txt"])

    # If a file was uploaded, display its contents
    if file is not None:
        # Save the uploaded file to a temporary location
        file_path = os.path.join("temp", file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        # Read the first 12 lines of the file
        lines = read_file(file_path)

        # Display the lines in a Streamlit component
        st.write("### First 12 lines:")
        for line in lines:
            st.write(line)

        # Remove the temporary file
        os.remove(file_path)

if __name__ == "__main__":
    main()
