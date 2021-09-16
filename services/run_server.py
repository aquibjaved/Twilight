from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, AnyStr, Any, List, Union
import pandas as pd
import sys

sys.path.append('../')
from twilight.basic_eda import GenerateWordCloud

app = FastAPI()

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


class GetCloud(BaseModel):
    n_count: int
    column_name: str


@app.post("/")
async def root(arbitrary_json: JSONStructure = None):
    global df
    df = pd.DataFrame.from_dict(arbitrary_json)
    return {"received_data": "success"}


@app.post("/get_word_cloud/")
async def word_cloud(data: GetCloud):
    object_wc = GenerateWordCloud(dataframe=df, column_name=data.column_name, max_words=data.n_count)
    res = object_wc.get_word_cloud()
    return res
