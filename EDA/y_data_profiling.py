import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from ydata_profiling import ProfileReport

df = pd.read_csv('titanic.csv')

profile = ProfileReport(df, title='Titanic Profile Report')

profile.to_file('titanic_report.html')