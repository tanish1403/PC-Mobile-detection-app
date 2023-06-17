import os
import sys
import streamlit as st
import subprocess

# Add custom CSS to set the app background color and navbar color
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    @keyframes slideInDown {
        0% {
            transform: translateY(-100%);
            opacity: 0;
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }

    .app-title {
        animation: slideInDown 1s;
        transition: color 0.3s;
        color: #1de995;
        font-size: 24px;
        border: 2px solid #1de995;
        padding: 5px 10px;
        display: inline-block;
        cursor: pointer;
    }

    .app-title:hover {
        color: #1de995;
        border-color: #e74c3c;
    }

    body {
        background-color: rgb(68, 70, 84);
    }
    .navbar {
        display: flex;
        align-items: center;
        background-color: rgb(68, 70, 84);
        padding: 10px;
        margin-bottom: 20px;
    }
    .navbar-option {
        padding: 5px 10px;
        margin-right: 10px;
        border-radius: 5px;
        font-weight: bold;
        color: white;
        cursor: pointer;
        transition: all 0.3s;
    }
    .navbar-option:hover {
        background-color: #555;
    }
    .active-option {
        border: 2px solid red;
        color: red;
    }
    .app-title {
        font-family: "Arial", sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: white;
        padding: 10px;
        
        background-color: #444;
        margin-bottom: 20px;
    }
    .app-data {
        display: block;
        margin-block-start: 0.67em;
        margin-block-end: 0.67em;
        margin-inline-start: 0px;
        margin-inline-end: 0px;
        font-weight: bold;
        }
    
    .section-title {
        font-size: 24px;
        font-weight: bold;
        color: #333;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .sub-section-title {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .paragraph {
        font-size: 16px;
        color: #555;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the app title
st.markdown('<div class="app-title">PC/Mobile Detection App</div>', unsafe_allow_html=True)

# Set the app title and description

# Sidebar options
sidebar_options = ["Overview","Upload Image", "History", "YOLOv7 Research Paper"]

# Selected option
selected_option = st.sidebar.selectbox("Select Option", sidebar_options)

# Navbar
st.markdown('<div class="navbar">' +
            ''.join([f'<div class="navbar-option {"active-option" if option == selected_option else ""}" onclick="location.href=\'#{option.lower()}\';">{option}</div>'
                     for option in sidebar_options]) +
            '</div>',
            unsafe_allow_html=True)
# st.markdown('<h1 class="app-data">AI Powered Tool</h1>', unsafe_allow_html=True)
st.markdown('<h1 class="app-data">Detect PC/Mobile in Your Images</h1>', unsafe_allow_html=True)


# Function for performing detection
def detect(save_directory):
    weights = "best.pt"
    
    if st.button("Start Detection"):
        path = "detect.py"

        with st.spinner("Performing detection..."):
            pyth = sys.executable
            st.write("Detection started")
            out = os.path.join(save_directory, "out")
            subprocess.run(
                [pyth, path, "--source", save_directory, "--weights", weights, "--conf", "0.25", "--name", "detect", "--exist-ok", "--no-trace"]
            )
            st.write("Detection ended")

# Upload Image section


st.markdown('<h2 class="section-title">Overview</h2>', unsafe_allow_html=True)
st.markdown('<p class="paragraph">Welcome to our AI-powered tool for detecting PC/mobile devices in your images! This innovative application utilizes the powerful YOLOv7 object detection algorithm to identify and classify various devices such as mobile/tablet, TV/monitor, keyboard, mouse, and laptop.</p>', unsafe_allow_html=True)
if selected_option == "Overview":
    st.markdown('<h2 class="sub-section-title">How it Works</h2>', unsafe_allow_html=True)
    st.markdown("<p class='paragraph'>By leveraging the state-of-the-art YOLOv7 model, our app can accurately detect and locate PC/mobile devices in any uploaded image. Whether you're a designer, developer, or simply curious about the devices present in your images, this tool provides valuable insights and saves you time.</p>", unsafe_allow_html=True)
    st.markdown('<h2 class="sub-section-title">Simple and User-Friendly</h2>', unsafe_allow_html=True)
    st.markdown("<p class='paragraph'>We understand the importance of simplicity and user-friendliness. That's why our app is designed with a clean and intuitive interface. All you need to do is upload an image, and our tool will perform the detection process in the background. You can easily navigate through different options using the sidebar and explore the detected devices in your uploaded images.</p>", unsafe_allow_html=True)
    st.markdown('<h2 class="sub-section-title">Get Started</h2>', unsafe_allow_html=True)
    st.markdown('<p class="paragraph">To begin, simply select the "Upload Image" option from the sidebar. You can either drag and drop an image file or click on the upload area to select an image from your device. Once the image is uploaded, our tool will process it using the YOLOv7 algorithm and highlight the detected PC/mobile devices.</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-section-title">Why YOLOv7?</h2>', unsafe_allow_html=True)
    st.markdown('<p class="paragraph">YOLOv7 is an advanced and trainable object detection algorithm that has achieved state-of-the-art performance in real-time object detection tasks. By leveraging the power of YOLOv7, our app is capable of accurately identifying PC/mobile devices with impressive speed and efficiency.</p>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-section-title">Summary</h2>', unsafe_allow_html=True)
    st.markdown("<p class='paragraph'>Our AI-powered tool offers a convenient and efficient way to detect PC/mobile devices in your images. Whether you're analyzing designs, conducting market research, or simply exploring the devices present in your photos, our app provides valuable insights at your fingertips. Give it a try and discover the hidden devices within your images!</p>", unsafe_allow_html=True)

if selected_option == "Upload Image":
    st.markdown(f'<h2 id="upload">Upload Image</h2>', unsafe_allow_html=True)
    image_path = st.file_uploader("Drag and drop or click here to upload image", type=["png", "jpg", "jpeg"])
    upload_button = st.button("Upload")
    # image_path = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if image_path is not None:
        save_directory = "test"
        os.makedirs(save_directory, exist_ok=True)

        saving_path = os.path.join(save_directory, image_path.name)
        with open(saving_path, "wb") as f:
            f.write(image_path.getbuffer())
        if os.path.exists(saving_path):
            st.write("File Successfully Uploaded")

        detect(save_directory)

        if os.path.exists("runs/detect"):
            for i in os.listdir("runs/detect/"):
                if os.path.exists(f"runs/detect/{i}/{image_path.name}"):
                    st.image(f"runs/detect/{i}/{image_path.name}", channels="BGR", caption="pc-detection")
                    download_path = f"runs/detect/{i}/{image_path.name}"
                    st.download_button(
                        label=f"Download Image",
                        data=download_path,
                        file_name=image_path.name,
                    )

# History section
if selected_option == "History":
    st.markdown(f'<h2 id="history">History</h2>', unsafe_allow_html=True)
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
# pdf section 
if selected_option == "YOLOv7 Research Paper":
    st.markdown(f'<h2 id="pdf">View PDF</h2>', unsafe_allow_html=True)
    st.write("PDF will be displayed below:")
    st.markdown(f'<iframe src="https://openaccess.thecvf.com/content/CVPR2023/papers/Wang_YOLOv7_Trainable_Bag-of-Freebies_Sets_New_State-of-the-Art_for_Real-Time_Object_Detectors_CVPR_2023_paper.pdf" width="800" height="600"></iframe>', unsafe_allow_html=True)