import pandas as pd
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
body_part = ["hips", "ab","chest","neck","head","Lshoulder","LUarm","LFarm","Lhand","Rshoulder","RUarm","RFarm","Rhand", "Lthigh", "Lshin", "Lfoot", "Rthigh", "Rshin", "Rfoot","Ltoe","Rtoe" ]
print(len(body_part))


df_0 = pd.read_csv(".\data\Fosco chen31 mouv1.csv")
df = df_0 [df_0.Frame <= 100]


# indexes for xyz are 7i -1/0/+1
# there are 21 body parts
x = []
y = []
z = []

for t in range(len(df)):
    x_0 = []
    y_0 = []
    z_0 = []

    for i in range(1,22):
        x_0.append(df.iloc[t, 7*i-1])
        y_0.append(df.iloc[t, 7*i])
        z_0.append(df.iloc[t, 7*i+1])

    x.append(x_0)
    y.append(y_0)
    z.append(z_0)

fig = plt.figure()
ax = plt.axes(projection='3d')
t = 0
for i in range(21):
    ax.scatter3D(x[t][i], y[t][i], z[t][i], label = body_part[i], marker = 'o')

plt.legend()
plt.show()
