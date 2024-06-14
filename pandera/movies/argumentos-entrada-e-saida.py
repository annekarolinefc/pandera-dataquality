import pandas as pd
import pandera as pa
import numpy as np

from pandera import Column, DataFrameSchema, Check, check_io

df = pd.read_csv("pandera\moveis.csv")

rating_list = list(df.rating.unique())

input_schema = pa.DataFrameSchema(
    {
        "title": Column(
            str,
            checks=pa.Check(
                lambda x: x.strip() != "",
                element_wise=True,
                error="title can't be empty",
            ),
        ), 
        "rating": Column(
            str,
            checks=[pa.Check(
                lambda x: x.strip() != "",
                element_wise=True,
                error="rating can't be empty",
            ),  
            pa.Check.isin(rating_list, error="rating should be in the given list")],
        ),  
        "year": Column(
            int,
            checks=[pa.Check(lambda x: x > 0, error="year can't be empty"), pa.Check.in_range(1900, 2024, error="years should be in the given range")],
        ), 
        "runtime": Column(
            int, 
            checks=Check(lambda x: x > 0, error="runtime can't be empty")
        ),  # null check
    },
    unique=["title", "year"],
)

output_schema = pa.DataFrameSchema(
    {
        "title": Column(
            str,
            checks=[pa.Check(
                lambda x: x.strip() != "",
                element_wise=True,
                error="title can't be empty",
            ),
            pa.Check.isin(rating_list, error="rating should be in the given list")],
        ),  
        "year": Column(
            int,
            checks=[pa.Check(lambda x: x > 0, error="year can't be empty"), pa.Check.in_range(1900, 2024, error="years should be in the given range")],
        ),  
        "runtime": Column(
            int, 
            checks=Check(lambda x: x > 0, error="runtime can't be empty")
        ), 
    },
    unique=["title", "year"],
)


@check_io(df=input_schema, out=output_schema, lazy=True)
def only_R_rating(df):
    return df[df["rating"] == "R"][["title", "year", "runtime"]]


only_R_rating(df).head()