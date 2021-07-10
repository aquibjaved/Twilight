import streamlit as st
from twilight import basic_eda, file_parsing
from twilight.basic_eda import Features

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
	col1, col2 =st.beta_columns(2)
	with col1:
		_col_selected = st.multiselect("Select column to analyze",_cols)

	if _col_selected:
		with col2:
			x = st.number_input("# frequent words", value=100)
			y = st.number_input("# of Topics", value=5)

		if x:
			st.button("Generate Word Cloud")
			wd = basic_eda.GenerateWordCloud(dataframe=df, column_name=_col_selected[0])
			wd_obj = wd.get_word_cloud(max_words=x)
			st.write(wd.show_word_cloud(wordcloud_object=wd_obj))

		if y:
			st.button("Get Topics 📚")
			data_collected = df[_col_selected[0]].values.tolist()
			feat = Features(data=data_collected, num_topics=10)
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
	wd = basic_eda.GenerateWordCloud(dataframe=df, column_name='question')
	wd_obj = wd.get_word_cloud(max_words=x)
	try:
		st.image(wd.show_word_cloud(wordcloud_object=wd_obj))
	except:
		st.image("questions_wordcloud.png")
