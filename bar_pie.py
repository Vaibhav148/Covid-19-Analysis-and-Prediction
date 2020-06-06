from data import *
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use('seaborn')



print("gg")
plt.figure(figsize=(32,32))
plt.barh(vis_countries,vis_cases)
plt.show()



c=random.choices(list(mcolors.CSS4_COLORS.values()),k=len(unq_countries))
plt.figure(figsize=(30,30))
plt.pie(vis_cases,colors=c)
plt.legend(vis_countries,loc='upper right')
plt.show()


