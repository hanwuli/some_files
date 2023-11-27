"""运行环境：windows10系统，python3.9.6
   python包：numpy,matplotlib"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#x = np.linspace(0, 2*np.pi, 100)
x = np.linspace(0, 50, 1000)
#print(x[0])
#print(x)
#y = np.sin(x)
#y = np.sqrt(5**2-(x-5)**2)
y=[]
def f(x):
    #for x in np.linspace(0, 50, 1000):
    if 0<=x<=10:
        y=0
    elif 10<x<=30:
        y=np.sqrt(10**2-(x-20)**2)
    elif 30<x<=35:
        y=0
    elif 35<x<=45:
        y=x-35
    elif 45<x<=50:
        y=10
    else:
        y=0
    #y.append(y1)
    return y
    #print(y1)
#y=array(f(x))
#print(y)
#print(y=f(2))
#y.f(30)
#y=f(30)
#print(y)
for z in np.linspace(0, 50, 1000):
    y1=f(z)
    y.append(y1)
print(y[999])
print(x[0])
#画sin曲线
fig = plt.figure(tight_layout=True)

#设置坐标轴范围
# plt.xlim((-1, 7))
# plt.ylim((-2, 2)) 
plt.xlim((-1, 55))
plt.ylim((-7, 20))

#画动点
point_ani,=plt.plot(x[0], y[0], "r-")#必须有,，表示得到元组
text_pt = plt.text(3.5, 0.8, '', fontsize=16)

def update(num):
    '''更新数据点
    .set_data()的意思是将这里的(x[num], y[num])代替上面的(x[0], y[0])
    也可以.set_ydata,需要将上面的x[0]改成x,这里的x[num]去掉
    '''
    #xx = np.linspace(0, 2*np.pi*num/100, num)
    xx = np.linspace(0, 50*num/1000, num)
    #yy = np.sin(xx)
        #yy = np.sqrt(5**2-(xx-5)**2)
    yy=y[:num]
    #yy.append(f(xx))
    # yy=[]
    # yy=f(xx)

    point_ani.set_data(xx, yy)
    #text_pt.set_position([num], y[num])#更新文本位置
    text_pt.set_text("x=%.3f, y=%.3f"%(x[num], y[num]))
    return point_ani, text_pt,

#开始制作动画
ani = animation.FuncAnimation(fig=fig, func=update, frames=np.arange(0, 1000),
                              interval=80, blit=True)

#ani.save('sin.gif', writer='imagegick', fps=10)
plt.show()                       