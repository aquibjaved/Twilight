from wordcloud import WordCloud
from typing import List
import pandas as pd
import matplotlib.pyplot as plt



class GenerateWordCloud:
    def __init__(self, dataframe: pd.DataFrame, column_name: str):
        self.dataframe = dataframe
        self.column_name = column_name


    def get_word_cloud(self,max_words):
        '''
        this func, select the column name and get all the text
        later convert all that to text to generate wordcloud object
        :return:
        '''
        text_from_column =  ' '.join(self.dataframe[self.column_name].values.tolist())
        wordcloud = WordCloud(max_words=max_words).generate(text_from_column)
        return wordcloud

    def show_word_cloud(self, wordcloud_object):
        # Display the generated image:
        x= plt.imshow(wordcloud_object, interpolation='bilinear')
        x.axis("off")
        # x.show()
        return x

    # def controller(self):

    #     df = pd.read_csv('../data/qa_dataset.csv')
    #     wd = GenerateWordCloud(dataframe=df, column_name='question')
    #     wd_obj = wd.get_word_cloud()
    #     wd.show_word_cloud(wordcloud_object=wd_obj)


if __name__  == '__main__':

    # Read data
    df = pd.read_csv('../data/qa_dataset.csv')
    wd = GenerateWordCloud(dataframe=df, column_name='question')
    wd_obj = wd.get_word_cloud()
    wd.show_word_cloud(wordcloud_object=wd_obj)



