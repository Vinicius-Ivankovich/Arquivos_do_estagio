# %%
import pandas as pd

df = pd.read_csv('ships2.csv')
df
# %%
#Coloca condicionais nas variaveis
import pandera as pa
import numpy as np

schema = pa.DataFrameSchema({
    'name': pa.Column(pa.String),
    'lat': pa.Column(
        pa.Float,
        nullable=True,
        checks=pa.Check(
            lambda v: v >= -90 and v <= 90,
            element_wise=True,
        ),
    ),
    'lng': pa.Column(
        pa.Float,
        nullable=True,
        checks=pa.Check(
            lambda v: v >= -180 and v <= 180,
            element_wise=True,
        ),
    ),
})

schema.validate(df)
# %%
