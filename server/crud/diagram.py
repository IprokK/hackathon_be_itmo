# Пример 11.2

from math import pi
import matplotlib.pyplot as plt
import numpy as np

lag = pi/4.
angles = np.arange(0, 2*pi , lag)

fig = plt.figure(figsize=(10,5)) # зададим явно размер полотна, чтобы графики не перекрывались

for i in range(1, 2):

    r = np.random.random(len(angles)) # для каждой розы значения будут разные

    ax = fig.add_subplot(120+i, projection='polar')
    ax.plot(angles, r, color='r', linewidth=1.)
    # Так как 0 и 2*pi - это одна и та же точка, то значение в ней должно быть одно
    # Однако, будет разрыв между последней точкой и нулевой.
    # Чтобы его убрать, искусственно соединим эти точки.

    # Замыкаем розу ветров (соединяем конец с началом)
    ax.plot((angles[-1],angles[0]),(r[-1],r[0]), color='r', linewidth=1.)

    # Изменяем направление обхода с "против часовой" на "по часовой"
    ax.set_theta_direction(-1)
    
    # Смещаем нулевую или полярную ось на 90 градусов против часовой стрелки, в положение "север"
    ax.set_theta_offset(pi/2.0)

    ax.set_title(u"Роза ветров N%d" % i, loc='center')

plt.tight_layout()

plt.show()   