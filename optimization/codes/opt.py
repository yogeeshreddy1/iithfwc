import numpy as np
import matplotlib.pyplot as plt
#import cvxpy  as cp

import sys, os
sys.path.insert(0,'/home/user/Desktop/optimization/CoordGeo')

#if using termux
import subprocess
import shlex
#Defining f(x)
def f(x,p,q):
  return x**3 - p * x + q
p =1
q =1
label_str = "$x^3-x+1$"

#For minima using gradient ascent
cur_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0
#min_x = -1
#max_x = 1

#Defining derivative of f(x)
df = lambda x: 3*x**2-1            

#Gradient ascent calculation
while ((previous_step_size > precision) and (iters < max_iters)) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x) 
    iters+=1
    min_val = f(cur_x,p,q)
print("Maximum value of f(x) is ", min_val, "at","x =",cur_x)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

#Gradient descent calculation/home/user/Desktop/conics/CoordGeo


def f(x,p,q):
  return x**3 - p * x + q
p =1
q =1

#For minima using gradient ascent
cur_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0
#min_x = -1
#max_x = 1

df = lambda x: 3*x**2-1            
#Defining derivative of f(x)
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x -= alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1     
max_val = f(cur_x,p,q)
print("Miniimum value of f(x) is ", max_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x,p,q)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'Q({cur_x:.4f},{max_val:.4f})')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
#plt.savefig('/home/user/Desktop/optimization/CoordGeo/figs6.pdf')
#subprocess.run(shlex.split("termux-open  /sdcard/ramesh/maths/CoordGeo/figs6.pdf"))
plt.show()
