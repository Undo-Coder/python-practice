import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

plt.figure()
df.plot()
plt.savefig('plot.png')
plt.close('all')


plt.figure()
df.plot(subplots=True)
plt.savefig('plot_subplots.png')
plt.close('all')