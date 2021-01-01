import pandas as pd
from matplotlib import pyplot as plt

train_save_path = "train_set.csv"
file_open_obj = open(train_save_path, "a+", newline='')

df = pd.read_csv(train_save_path, names=['process', 'threads', 'memory_usage'], sep=",")

_train_process = df["process"].to_numpy()
_train_threads = df["threads"].to_numpy()
_train_memory = df["memory_usage"].to_numpy()

# sorting
print(df.sort_values(by=['memory_usage'],axis=0,ascending=True))

# Data Visualize Duplicate Remove
_duplicate_data = df.drop_duplicates(['process'])
x_process = _duplicate_data['process']
y = _duplicate_data['memory_usage']

plot_process = sorted(x_process.to_numpy())
plot_y = sorted(y.to_numpy())

plt.xlabel("Total Process Number")
plt.ylabel("Total Memory Usage")

plt.plot(plot_process,plot_y)
plt.show()
