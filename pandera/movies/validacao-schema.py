import pandas as pd 
import pandera as pa 

from pandera import Column, DataFrameSchema

df = pd.read_csv("pandera\moveis.csv")
schema = pa.DataFrameSchema({
    "title": Column(str),
    "rating": Column(str),
    "year": Column(int),
    "runtime": Column(int)
})

schema.validate(df)