import pandas as pd 
import pandera as pa 
import numpy as np

from pandera import Column, DataFrameSchema

df = pd.read_csv("pandera\moveis.csv")

df.loc[len(df)] = ["Almost Famous","R",2000,122]
df.loc[len(df)] = ["","",2000,122]
df.loc[len(df)] = ["Almost Famous","R",np.nan,np.nan]

rating_list = list(df.rating.unique())

schema = pa.DataFrameSchema(
    {
        "title": Column(str, checks=pa.Check(lambda x: x.strip() != "", element_wise=True, error = "title can't be empty")), # checkagem de string vazia
        "rating": Column(str, checks=pa.Check(lambda x: x.strip() != "", element_wise=True, error = "rating can't be empty")), # empty string check
                         #checks=pa.Check.isin(rating_list, error = "rating should be in the given list")), # checkagem de string vazia
        "year": Column(int, checks=[pa.Check(lambda x: x > 0), pa.Check.in_range(1900, 2024)]),  # checkagem de null e checkagem de datas especificas
        "runtime": Column(int, checks=pa.Check(lambda x: x > 0)) # checkagem de nulos
    },
    unique = ["title", "year"] # nome e ando combinados devem se runicos
)

try:
    schema.validate(df, lazy=True)
except pa.errors.SchemaErrors as err:
    print("Schema errors and failure cases:")
    print(err)