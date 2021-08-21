import pandas as pd
import csv
import plotly.express as px
df = pd.read_csv("data.csv")
mean = df.groupby(["Student Id", "Level"], as_index=False)["Attempt"].mean()
fig = px.scatter(mean, x="Student Id", y="Level", size="Attempt", color="Attempt",title="Data Analysis")
fig.show()