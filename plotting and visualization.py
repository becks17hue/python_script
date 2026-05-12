import matplotlib.pyplot as plt
import pandas as pd
from ucimlrepo import fetch_ucirepo
#load data
mice_protein_expression = fetch_ucirepo(id=342)
df = mice_protein_expression.data.features

#selecting first 10 protein columns
proteins = df.columns[1:11]
#get expression levels for first mouse
expression = df[proteins].iloc[0]
#create bar chart
plt.bar(proteins, expression)
plt.xlabel("proteins")
plt.ylabel("expression level")
plt.title("protein expression across mice(first mouse)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("protein_expression_plot.png", dpi=300)
plt.show()
import seaborn as sns
#targets = mice_protein_expression.data.targets
#df["Genotype"] = targets["Genotype"]
sns.boxplot(x="Genotype", y="DYRK1A_N", data=df)
plt.title("protein expression by Genotype")
plt.savefig("protein_expression_boxplot.svg")
plt.show()
import plotly.express as px
df_plot = df.reset_index()
print(df_plot.columns)
fig = px.scatter(df_plot, x="index", y="DYRK1A_N", color="Genotype",
                 title="Interactive protein expression plot")
fig.write_html("interactive_expression_plot.html")
fig.show()