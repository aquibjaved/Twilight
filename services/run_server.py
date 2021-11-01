from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, AnyStr, Any, List, Union
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import sys
sys.path.append('../')
from twilight.basic_eda import GenerateWordCloud
from twilight.basic_eda import Features
app = FastAPI()

origins = ["*"]
app.add_middleware(
            CORSMiddleware,
                allow_origins=origins,
                    allow_credentials=True,
                        allow_methods=["*"],
                            allow_headers=["*"],
                            )


JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

class GetCloud(BaseModel):
    n_count: int
    column_name: str

class GetTopics(BaseModel):
    n_topics: int

@app.post("/")
async def root(arbitrary_json: JSONStructure = None):
    global df
    df = pd.DataFrame.from_dict(arbitrary_json)
    return {"received_data": "success"}


@app.post("/get_word_cloud/")
async def word_cloud(data: GetCloud):
    global text_corpus
    text_corpus = df[data.column_name].values.tolist()
    object_wc = GenerateWordCloud(dataframe=df, column_name=data.column_name, max_words=data.n_count)
    res = object_wc.get_word_cloud()
    return res


@app.post("/get_topics/",response_model=List)
async def get_topic(data: GetTopics):
    #text_corpus = df.col_name.values.tolist()
    feat = Features(data=text_corpus, num_topics=data.n_topics)
    return feat.get_topics()
