from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, AnyStr, Any, List, Union
import pandas as pd
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
    df = pd.DataFrame.from_dict(arbitrary_json)
    print(df)
    return {"received_data": arbitrary_json}



@app.post("/get_word_cloud/")
async def word_cloud(data: GetCloud):
    object_wc = GenerateWordCloud(dataframe=df, column_name=data.column_name)

    img = object_wc.show_word_cloud(wordcloud_object=get_w_c) #base64

    return img




