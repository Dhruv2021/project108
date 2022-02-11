import plotly.figure_factory as pff
import pandas as pd

df=pd.read_csv("project.csv")

graph=pff.create_distplot([df["Avg Rating"].tolist()],["result"],show_hist=True)
graph.show()
