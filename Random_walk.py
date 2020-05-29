from random import choice
from matplotlib import pyplot as plt
class Randomwalk():
    '''A class to generate random walks'''

    def __init__(self,num_points=5000):

        self.num_points=num_points

        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):

        while(len(self.x_values)<=(self.num_points)):
                x_direction=choice([-1,1])
                x_step=choice([0,1,2,3,4,5,6,7,8])
                x_movement=x_direction*x_step

                y_direction = choice([-1,1])
                y_step = choice([0, 1, 2, 3, 4,5,6,7,8])
                y_movement = x_direction *y_step


                if x_movement==0 and y_movement==0:
                    continue

                else:
                    self.x_values.append(self.x_values[-1]+x_movement)
                    self.y_values.append(self.y_values[-1]+y_movement)

    def plot(self):


                num=[y for y in range(self.num_points+1)]
                plt.figure(figsize=(10, 6))
                plt.scatter(self.x_values,self.y_values,s=30,c=num,cmap=plt.cm.Blues,edgecolors=None)
                plt.scatter(self.x_values[0],self.y_values[0],s=60,c='Red')
                plt.scatter(self.x_values[-1],self.y_values[-1],s=60,c='Green')
                plt.axes().get_xaxis().set_visible(False)
                plt.axes().get_yaxis().set_visible(False)
                plt.savefig('test3.png',bbox_inches='tight')
                plt.show()

while True:

    c=Randomwalk(50000)
    c.fill_walk()
    c.plot()
    q=input()
    if q=='q':
        break
    elif q=='c':
        continue