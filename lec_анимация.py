import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#создание пространства и подпространства для анимации
fig, ax = plt.subplots()

#объект анимации
anim_object, = plt.plot([], [], '-', lw=2)
x, y = [], [] #координатф объекта анимации
frames_interval = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi) #пределы изменения переменной x
ax.set_ylim(-1, 1) #пределы изменения переменной y

#функция подстановки параметра в объект анимации
def update(frame):
    x.append(frame) #расчет координаты x
    y.append(np.sin(frame)) #расчет координаты y

    #передача координат объекту анимации
    anim_object.set_data(x, y)

    return anim_object

ani = FuncAnimation(fig, 
                    update,
                    frames=frames_interval,
                    interval=50)

ani.save('animation_1.gif', writer="pillow")