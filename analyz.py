import streamlit as st

# Page Configuration
st.set_page_config(page_title="Text Analyzer", page_icon="📝", layout="wide")

# Custom CSS 
st.markdown("""
    <style>
    body { 
        font-size: 14px;
    }
    .stTitle { 
        color: #1e90ff;
        text-align: center;
    }
    textarea { 
        border: 2px solid #1e90ff; 
        border-radius: 8px;
     }
    .stButton>button{
        background-color: linear-gradient(45deg, #0b5394, #351c75);
        color:white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius:10px;
        transition:0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201,255,0.4);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background-color: linear-gradient(45deg,#92fe9d, #00c9ff);
        box-shadow: 0px 8px 20px rgba(0, 201, 255, 0.6);
        color:black;
    }
    .footer{
        text-align: center;
        font-size:18px;
        margin-top: 50px;
        color:black;
    }
    </style>
    """, unsafe_allow_html=True)

# Functions
def count_vowels(text):
    return sum(1 for char in text if char.lower() in "aeiouAEIOU")

def avg_word_length(text):
    words = text.split()
    return round(sum(len(word) for word in words) / len(words), 2) if words else 0

# Title
st.title("Text Analyzer📜")

# Text Input
text_input = st.text_area("Enter text:✍️", height=120)

# Sidebar Options
option = st.sidebar.selectbox("Select Analysis:", ["Basic Stats", "Python Check", "Case Conversion", "Find & Replace"])

if option == "Find & Replace":
    search = st.text_input("Find:")
    replace = st.text_input("Replace:")

# Analyze Button
if st.button("Analyze"):
    if not text_input.strip():
        st.error("Please enter text!")
    else:
        if option == "Basic Stats":
            st.write(f"**Words:** {len(text_input.split())} | **Chars:** {len(text_input)} | **Vowels:** {count_vowels(text_input)} | **Avg Word Length:** {avg_word_length(text_input)}")
        elif option == "Python Check":
            st.write("✅ 'Python' found!" if "python" in text_input.lower() else "❌ 'Python' not found.")
        elif option == "Case Conversion":
            st.write(f"🔠 Upper: {text_input.upper()} \n 🔡 Lower: {text_input.lower()}")
        elif option == "Find & Replace" and search and replace:
            st.write(f"🔄 Modified Text: {text_input.replace(search, replace)}")

st.markdown(f"<div class='footer'>  Created by Mubashira Tanveer </div>", unsafe_allow_html=True)            
