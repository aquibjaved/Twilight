
"""Extract file extension & return dataframe object as per file type"""

import pathlib
import pandas as pd

def get_file_obj(uploaded_file):
    x= pathlib.Path(uploaded_file.name).suffix
    # file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    if x== ".csv":
        obj= pd.read_csv(uploaded_file,sep=',')
    elif x== ".tsv":
        obj= pd.read_csv(uploaded_file,sep='\t')
    elif x== ".ssv":
        obj= pd.read_csv(uploaded_file,sep='\s+')
    elif x== ".xlsx":
        obj = pd.read_excel(uploaded_file)
    return obj