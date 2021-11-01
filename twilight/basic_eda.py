from wordcloud import WordCloud
from typing import List
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from dataclasses import dataclass
import io
import base64
import gensim
from gensim.utils import simple_preprocess
import nltk
import gensim.corpora as corpora

try:
    from nltk.corpus import stopwords
except:
    nltk.download('stopwords')
    from nltk.corpus import stopwords

stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])

st.set_option('deprecation.showPyplotGlobalUse', False)


class GenerateWordCloud:
    def __init__(self, dataframe: pd.DataFrame, column_name: str, max_words: int = 5):
        self.dataframe = dataframe
        self.column_name = column_name
        self.max_words = max_words

    def get_word_cloud(self):
        """
        this func, select the column name and get all the text
        later convert all that to text to generate wordcloud object
        :return: word cloud object
        """
        text_from_column = ' '.join(self.dataframe[self.column_name].values.tolist())
        wordcloud = WordCloud(max_words=self.max_words).generate(text_from_column)

        buffer = io.BytesIO()
        wordcloud.to_image().save(buffer, 'png')
        b64 = base64.b64encode(buffer.getvalue())
        return b64

def format_result(result: list)->dict:
    res = {}
    for r in result:
        temp_res = []
        for r_ in r[1].split(' + '):
            a,b = r_.split('*')
            temp_res.append({b:a})

        res[r[0]]= temp_res

    return res


@dataclass()
class Features:
    """
    this code is taken from the following blog
    https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0

    getTopics = [
    {
      0: [{ is: '* 0.92' }, { the: '*0.25' }],
      1: [{ to: '* 0.92' }, { me: '*0.25' }],
    },
     ];
    """

    data: List[str]
    num_topics: int

    def sent_to_words(self, sentences):
        for sentence in sentences:
            # deacc=True removes punctuations
            yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))

    def remove_stopwords(self, texts):
        return [[word for word in simple_preprocess(str(doc))
                 if word not in stop_words] for doc in texts]

    def get_topics(self):
        data_words = list(self.sent_to_words(self.data))
        id2word = corpora.Dictionary(data_words)
        # Create Corpus
        texts = self.remove_stopwords(data_words)
        texts = data_words
        # Term Document Frequency
        corpus = [id2word.doc2bow(text) for text in texts]

        lda_model = gensim.models.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=self.num_topics)
        topics = lda_model.print_topics()

        #df_lda = pd.DataFrame(topics)
        return [format_result(result=topics)]


"""
if __name__ == '__main__':
    # Read data
    df = pd.read_csv('../data/qa_dataset.csv')
    wd = GenerateWordCloud(dataframe=df, column_name='question')
    # wd_obj = wd.get_word_cloud()
    # show_word_cloud(wordcloud_object=wd_obj)
    ques = df.question.values.tolist()

    feat = Features(data=ques, num_topics=10)
    # print(feat.get_topics())
"""


