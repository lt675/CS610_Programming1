"""This manages all dependencies and script imports for the other files"""

import random
from queue import Queue, Empty
from treelib import Tree
from scipy.stats import truncexpon
from scipy.stats import truncnorm
import pandas as pd
import numpy as np


from dataframe import df_init
from queue_logic import CounterQueue
from tree_logic import Router

# Set random seeds for reproducibility
random.seed(42)
np.random.seed(42)
