import pandas as pd 
import pandera as pa 

# SCHEMA
price_check = pa.DataFrameSchema({
    "price": pa.Column(
        pa.Int,
        pa.Check.in_range(min_value = 5, max_value = 20)
    )
})

# VALIDATE FUNCTION
def price_validation(df: pd.DataFrame) -> pd.DataFrame:
    price_check.validate(df)
    return df

data = {
    "price": [10, 15, 5, 20, 25]
}

if __name__ == "__main__":
    df = pd.DataFrame(data)

    try:
        validated_df = price_validation(df)
        print("Dataframe validado com sucesso!")
        print(validated_df)
    except pa.errors.SchemaError as e:
        print("Erro de validação:")
        print(e)