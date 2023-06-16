import os
import sys
import streamlit as st
import subprocess

st.title("PC/Mobile Detection App")
option = st.sidebar.selectbox("Select Option", ("Upload Image","History"))

if option == "Upload Image":
    image_path = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if image_path is not None:
        save_directory = "test"
        os.makedirs(save_directory, exist_ok=True)

        # Remove previous images from the test directory
        for old_image in os.listdir(save_directory):
            os.remove(os.path.join(save_directory, old_image))

        saving_path = os.path.join(save_directory, image_path.name)
        with open(saving_path, "wb") as f:
            f.write(image_path.read())
        if os.path.exists(saving_path):
            st.write("File Successfully Uploaded")

        if st.button("Start Detection"):
            path = "detect_img.py"

            with st.spinner("Performing detection..."):
                subprocess.run([sys.executable, path], bufsize=0, shell=True, check=True)

        if os.path.exists("runs"):
            for i in os.listdir("runs/detect/"):
                if os.path.exists(f"runs/detect/{i}/{image_path.name}"):
                    st.image(f"runs/detect/{i}/{image_path.name}", channels="BGR", caption="pc-detection")
                    download_path = f"runs/detect/{i}/{image_path.name}"
                    st.download_button(
                        label=f"Download Image",
                        data=download_path,
                        file_name=image_path.name,
                )

elif option == "History":
    st.subheader("Detection History")

    if os.path.exists("runs/detect"):
        for folder in os.listdir("runs/detect"):
            if os.path.isdir(os.path.join("runs/detect", folder)):
                
                for image_file in os.listdir(os.path.join("runs/detect", folder)):
                    if os.path.isfile(os.path.join("runs/detect", folder, image_file)):
                        st.write(image_file)
                        st.image(os.path.join("runs/detect", folder, image_file), channels="BGR")
                        st.download_button(
                        label=f"Download Image",
                        data=os.path.join("runs/detect", folder, image_file),
                        file_name=image_file,
                )

