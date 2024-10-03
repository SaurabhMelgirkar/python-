import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
x=[1,2,3,4,5]
y=[1,2,3,4,5]
q={"x","y"}
value=pd.DataFrame(q) 
sns.lineplot(x="x",y="y",data=value)
plt.show()