import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

with open('data_clean.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    data = list(lines)


