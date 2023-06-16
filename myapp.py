import os
import sys
import streamlit as st
import subprocess

st.title("PC/Mobile Detection App")
def detect(save_directory):
    weights = "best.pt"
    # detectorScript = "detect.py"
    
    if st.button("Start Detection"):
            path = "detect.py"

            with st.spinner("Performing detection..."):
                pyth = sys.executable
                st.write("detection started")
                out = os.path.join(save_directory, "out")
                subprocess.run([pyth , path, '--source', save_directory, '--weights', weights, '--conf', '0.25', '--name', 'detect', '--exist-ok','--no-trace'])
                st.write("Detection ended")

option = st.sidebar.selectbox("Select Option", ("Upload Image","History"))

if option == "Upload Image":
    image_path = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if image_path is not None:
        save_directory = "test"
        os.makedirs(save_directory, exist_ok=True)

        saving_path = os.path.join(save_directory, image_path.name)
        with open(saving_path, "wb") as f:
            f.write(image_path.getbuffer())
        if os.path.exists(saving_path):
            st.write("File Successfully Uploaded")

        detect(save_directory)

        if os.path.exists("runs/detect") :
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

