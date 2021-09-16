import streamlit as st
from twilight import basic_eda, file_parsing
from twilight.basic_eda import Features
import pandas as pd

# st.beta_set_page_config(layout="wide")
st.title("Welcome to Twilight")

st.write(
    "Twilight is a python package to work with text data efficiently. It's a no code tool to quickly understand any text-based document and it provides an intuitive UI to explore insights from text."
)

#* Functionality for file upload & column selection
uploaded_file = st.file_uploader("Load Sample File",type=['txt','csv','tsv','xlsx'])

if uploaded_file:
	df= file_parsing.get_file_obj(uploaded_file=uploaded_file)
	st.write(df)
	_cols = df.columns.values.tolist()
	# col1, col2 = st.beta_columns(2)
	# with col1:
	_col_selected = st.multiselect("Select column to analyze",_cols)
	if _col_selected:
		st.header("Most Frequent Words 📊")
		my_expander1 = st.beta_expander(label="Word Cloud")
		st.header("Get Topics 📚")
		my_expander2= st.beta_expander(label= "Discover Topics")
		with my_expander1:
			x = st.number_input("Enter top-n most frequent words", value=100)
			wd = basic_eda
			wd_obj = wd.get_word_cloud(max_words=x)
			st.write(wd.show_word_cloud(wordcloud_object=wd_obj))
		with my_expander2:
			x = st.number_input("Enter no of topics", value=5)
			data_collected = df[_col_selected[0]].values.tolist()
			feat = Features(data=data_collected, num_topics=x)
			df_topics = feat.get_topics()
			st.write(df_topics)

st.title("Check out a Quick Demo")
sd= st.button("Load Sample Dataset")
if sd:
	data_load_state = st.text('Loading data...')
	df = pd.read_csv('./data/qa_dataset.csv')
	data_load_state = st.text('Data Loaded!')
	x= st.number_input("Enter no of words",value=10)
	st.subheader("Most frequent words from sample text file")
	wd = basic_eda
	wd_obj = wd.get_word_cloud(max_words=x)
	try:
		st.image(wd.show_word_cloud(wordcloud_object=wd_obj))
	except:
		st.image("questions_wordcloud.png")
