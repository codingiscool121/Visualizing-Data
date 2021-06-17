import pandas as pd
from pandas.io.pytables import attribute_conflict_doc
import plotly.express as px

data=pd.read_csv("c106 data.csv")
group = data.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
graph = px.scatter(group,x="student_id", y="level", color="attempt")
print("Opening your graph...")
graph.show()