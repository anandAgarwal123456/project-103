import pandas as pd
import plotly.express as px

data = pd.read_csv('data.csv')
graph = px.scatter(data, x ="date", y = "cases", color = "country")
graph.show()