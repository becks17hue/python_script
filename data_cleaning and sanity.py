from ucimlrepo import fetch_ucirepo
#fetch dataset
mice_protein_expression = fetch_ucirepo(id= 342)
x = mice_protein_expression.data.features
y = mice_protein_expression.data.targets
#metadata
print(mice_protein_expression.metadata)
#variable information
print(mice_protein_expression.variables)
#basic cleaning checks
#print(x.shape)
#print(x.head)
#print(x.isna().sum().head())
#added new lines
df = x.copy()
df = df.dropna(subset=["DYRK1A_N"])
print(df.shape)