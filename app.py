import streamlit as st


st.title("Welcome to twilight")

st.write(
    "Twilight is a python package to work with text data efficiently. It's a no code tool to quickly understand any text-based document and it provides an intuitive UI to explore insights from text."
)

st.subheader("Document Files")
docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])

def main():
	menu = ["Home","Dataset","Document Files","About"]
	choice = st.sidebar.selectbox("Menu",menu)
    # if choice == "Document Files":
	# 	st.subheader("Document Files")
	# 	docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])

if __name__ == '__main__':
	main()