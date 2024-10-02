from main import *
from dataframe import df_init
from queue_logic import CounterQueue
from tree_logic import Router



df_end = df_init.copy()
df_end[:] = np.nan
print(df_end)