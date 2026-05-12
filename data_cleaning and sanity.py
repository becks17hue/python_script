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
print(x.shape)
print(x.head)
print(x.isna().sum().head())
#added new lines
df = x.copy()
df = df.dropna(subset=["DYRK1A_N"])
print(df.shape)
#checking expected columns
expected_columns = ["DYRK1A_N", "NR1_N"]
for col in expected_columns:
    if col not in df.columns:
        raise ValueError(f"missing expected columns: {col}")
    
if len(df)< 500:
    print("warning: Dataset is smaller than expected after cleaning")

if df["DYRK1A_N"] .max() > 20:
    print("warning: expression values exceed expected biological range")
