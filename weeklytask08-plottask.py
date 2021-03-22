# this program displays a plot of functions f(x)=x, g(x)=x² and h(x)=x³ in range [0, 4]
# on one set of axes
# Author: Sarah McNelis

import numpy as np 
import matplotlib.pyplot as plt 

xpoints = np.array(range(0,4)) 
ypoints1 = xpoints #f(x)=x
ypoints2 = xpoints * xpoints #g(x)=x²
ypoints3 = ypoints2 * xpoints #h(x)=x³

font1 = {'family':'times new roman','color':'tab:red','size':30, 'weight':'bold', 'style':'oblique'}
font2 = {'family': 'times new roman', 'color':'indianred', 'size':20, 'weight':'semibold'}
font3 = {'family': 'times new roman', 'color':'slategrey', 'size':20, 'weight':'semibold'}
# creating fonts here for title and axis labels

plt.plot(xpoints, ypoints1, color='tab:blue',  linestyle='dashed', linewidth='2.5', label = 'f(x)=x')
plt.plot(xpoints, ypoints2, color='orangered', linestyle='dotted', linewidth='2.5', label = 'g(x)=x²') 
plt.plot(xpoints, ypoints3, color='tab:green', linestyle='solid', linewidth='2.5', label = 'h(x)=x³') 
# can also use ls for linestyle eg ls='--' for dashed line':' for dotted line 
# can also use c for color eg c='g' 
# can also use lw for linewidth
plt.xlabel('Range', fontdict=font2) #use fontdict to call fonts above
plt.ylabel('Functions', fontdict=font3)
plt.title('Plot of Functions', fontdict=font1, loc='center') #loc to plot location of title
plt.legend(loc='best', fontsize='large')
plt.show()
#plt.savefig('plottask.png')
