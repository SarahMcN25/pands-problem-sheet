# this program displays a plot of functions f(x)=x, g(x)=x² and h(x)=x³ in range [0, 4]
# on one set of axes
# Author: Sarah McNelis

# https://www.kite.com/python/answers/how-to-make-multiple-plots-on-the-same-figure-in-matplotlib-in-python
# https://matplotlib.org/stable/gallery/color/named_colors.html
# https://www.w3schools.com/python/matplotlib_line.asp #linestyle, thickness, color
# https://www.w3schools.com/python/matplotlib_labels.asp
# https://www.tutorialexample.com/understand-matplotlib-fontdict-a-beginner-guide-matplotlib-tutorial/ #fontdict stuff
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html # legend loc, size etc

import numpy as np 
import matplotlib.pyplot as plt 

xpoints = np.array(range(0,4))
ypoints1 = xpoints
ypoints2 = xpoints * xpoints
ypoints3 = ypoints2 * xpoints


font1 = {'family':'times new roman','color':'tab:red','size':30, 'weight':'bold', 'style':'oblique'}
font2 = {'family': 'times new roman', 'color':'indianred', 'size':20, 'weight':'semibold'}
font3 = {'family': 'times new roman', 'color':'slategrey', 'size':20, 'weight':'semibold'}

plt.plot(xpoints, ypoints1, color='tab:blue',  linestyle='dashed', linewidth='2.5', label = 'f(x)=x') #ls='--'
plt.plot(xpoints, ypoints2, color='orangered', linestyle='dotted', linewidth='2.5', label = 'g(x)=x²') #ls=#:' #lw
plt.plot(xpoints, ypoints3, color='tab:green', linestyle='solid', linewidth='2.5', label = 'h(x)=x³') #c='g' etc
plt.xlabel('Range', fontdict=font2)
plt.ylabel('Functions', fontdict=font3)
plt.title('Plot of Functions', fontdict=font1, loc='center')
plt.legend(loc='best', fontsize='large')
plt.show()
