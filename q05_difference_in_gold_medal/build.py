import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.olympics_project.q02_rename_columns.build import q02_rename_columns

def q05_difference_in_gold_medal(path):
    "write your solution here"
    df = q02_rename_columns(path)
    df=df[:-1]
    gold_diff= df.iloc[:,2].astype(int) - df.iloc[:,7].astype(int)
    return gold_diff.max()
