import pandas as pd
import numpy as np

def load_data(path, *args):
    data = pd.read_csv(path)
    data = data.dropna()
    lst = []
    for header in args:
        if header == "SALARY":
            data[header] = pd.to_numeric(data[header].str.replace(r"[$,]", "", regex=True).str.strip())
        lst.append(np.array(data[header].tolist()))
    return lst