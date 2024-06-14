import pandas as pd 
import pandera as pa 

from pandera import Column, DataFrameSchema

df = pd.read_csv("pandera\moveis.csv")

schema = pa.DataFrameSchema(
    {
        "title": Column(str, checks=pa.Check(lambda x: x.strip() != "", element_wise=True)), # checkagem de string vazia
        "rating": Column(str, checks=pa.Check(lambda x: x.strip() != "", element_wise=True)), # checkagem de string vazia
        "year": Column(int, checks=[pa.Check(lambda x: x > 0), pa.Check.in_range(1900, 2024)]),  # checkagem de null e checkagem de datas especificas
        "runtime": Column(int, checks=pa.Check(lambda x: x > 0)) # checkagem de nulos
    },
    unique = ["title", "year"] # nome e ando combinados devem se runicos
)

schema.validate(df)