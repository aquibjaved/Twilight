import streamlit as st
from twilight import basic_eda
import pandas as pd

st.title("Welcome to twilight")

st.write(
    "Twilight is a python package to work with text data efficiently. It's a no code tool to quickly understand any text-based document and it provides an intuitive UI to explore insights from text."
)

st.subheader("Most frequent words from sample text file")
# docx_file = st.file_uploader("Load Sample File",type=['txt','docx','pdf'])
# if docx_file:
wc_g= st.button("Generate Wordcloud")
if wc_g:
	data_load_state = st.text('Loading data...')
	df = pd.read_csv('./data/qa_dataset.csv')
	data_load_state = st.text('Data Loaded!')
	wd = basic_eda.GenerateWordCloud(dataframe=df, column_name='question')
	x=st.slider("words",50,250)
	wd_obj = wd.get_word_cloud(max_words=x)
	try:
		st.image(wd.show_word_cloud(wordcloud_object=wd_obj).show())
	except:
		st.image("questions_wordcloud.png")
	

def main():
	menu = ["Home","Dataset","About"]
	choice = st.sidebar.selectbox("Menu",menu)
    # if choice == "Document Files":
	# 	st.subheader("Document Files")
	# 	docx_file = st.file_uploader("Upload File",type=['txt','docx','pdf'])

if __name__ == '__main__':
	main()