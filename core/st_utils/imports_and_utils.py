import os
import streamlit as st
import io, zipfile
from core.st_utils.download_video_section import download_video_section
from core.st_utils.sidebar_setting import page_setting
from translations.translations import translate as t

def download_subtitle_zip_button(text: str):
    zip_buffer = io.BytesIO()
    output_dir = "output"
    
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for file_name in os.listdir(output_dir):
            if file_name.endswith(".srt"):
                file_path = os.path.join(output_dir, file_name)
                with open(file_path, "rb") as file:
                    zip_file.writestr(file_name, file.read())
    
    zip_buffer.seek(0)
    
    st.download_button(
        label=text,
        data=zip_buffer,
        file_name="subtitles.zip",
        mime="application/zip"
    )

# st.markdown
give_star_button = """
<style>
    .github-button {
        display: block;
        width: 100%;
        padding: 8px 16px;
        color: #1f1f1f;
        background-color: #fff0c2;
        border-radius: 0px;
        text-decoration: none;
        font-weight: 400;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1.4px;
        font-size: 0.88rem;
        transition: transform 0.1s ease, background-color 0.2s ease;
        box-sizing: border-box;
        border: 1px solid #ffd06a;
    }
    .github-button:hover {
        background-color: #ffd06a;
        color: #1f1f1f;
        transform: scale(1.02);
    }
</style>
<a href="https://github.com/Huanshere/VideoLingo" target="_blank" style="text-decoration: none;">
    <div class="github-button">
        Star on GitHub
    </div>
</a>
"""

button_style = """
<style>
div.stButton > button:first-child {
    display: block;
    padding: 8px 16px;
    color: #ffffff;
    background-color: #1f1f1f;
    text-decoration: none;
    font-weight: 400;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    font-size: 0.88rem;
    transition: all 0.15s ease;
    box-sizing: border-box;
    border: none;
    border-radius: 0px;
}
div.stButton > button:hover {
    background-color: #333333;
    color: #ffffff;
}
div.stButton > button:active, div.stButton > button:focus {
    background-color: #1f1f1f !important;
    color: #ffffff !important;
    box-shadow: none !important;
}
div.stButton > button:active:hover, div.stButton > button:focus:hover {
    background-color: #333333 !important;
    color: #ffffff !important;
    box-shadow: none !important;
}
div.stButton > button[kind="primary"] {
    background-color: #fa520f;
    color: #ffffff;
    border: none;
    border-radius: 0px;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 1.4px;
}
div.stButton > button[kind="primary"]:hover {
    background-color: #fb6424;
    color: #ffffff;
    transform: scale(1.03);
}
div.stDownloadButton > button:first-child {
    display: block;
    padding: 8px 16px;
    color: #ffffff;
    background-color: #1f1f1f;
    text-decoration: none;
    font-weight: 400;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    font-size: 0.88rem;
    transition: all 0.15s ease;
    box-sizing: border-box;
    border: none;
    border-radius: 0px;
}
div.stDownloadButton > button:hover {
    background-color: #333333;
    color: #ffffff;
}
div.stDownloadButton > button:active, div.stDownloadButton > button:focus {
    background-color: #1f1f1f !important;
    color: #ffffff !important;
    box-shadow: none !important;
}
div.stDownloadButton > button:active:hover, div.stDownloadButton > button:focus:hover {
    background-color: #333333 !important;
    color: #ffffff !important;
    box-shadow: none !important;
}
</style>
"""