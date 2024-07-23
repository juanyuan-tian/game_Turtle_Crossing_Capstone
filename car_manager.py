from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # self.objs = []
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    # 怎么产生车子，我的思路是右半边的平面，x y都random，但是要有个数限制，不然太密集

    def create_car(self):
        super().__init__()
        # 控制car的密度，可以比如random chance， 6选1再创造。
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

        # for i in range(6):
        #     self.shape("square")
        #     column.append(self)
        # for item in column:
        #     item.color(random.choice(COLORS))
        #     item.goto(0, random.randint(0, 200))
        #     颜色有了，沿着y轴也动了，但是没有每次都产生一个square,
        #     貌似每个self只产生一个turtle,  但是多个变量或者多个object肯定可以产生的。
        # self.objs = [Turtle() for i in range(6)]
        # for obj in self.objs:
        #     obj.shape("square")
        #     obj.turtlesize(stretch_wid=1, stretch_len=2)
        #     obj.color(random.choice(COLORS))
        #     obj.penup()
        #     obj.goto(x=250, y=random.randint(-250, 250))
    # 可以产生一列条带，想把移动直接放在这里，但是一旦call了函数，loop就无限了不行。
    # 但是另一个移动函数，只能控制这一条obj，产生新的obj后，老的不动了，这里要无限多的object？没做出来
    # 只产生一个car，然后在main函数中loop产生无数，产生好的放在attributes表中
    # 动作一是，只一个动，mainloop 然每一个动。
    # 这是我个人的当时没有理解的难点，产生cars



    # def car_move(self):
    #     super().__init__()
    #     for obj in self.objs:
    #         obj.backward(5)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    # 常数怎么加速度啊, 另外加一个函数,设置一个attributes

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    # self.shape("square")
    # self.shapesize(stretch_wid=1, stretch_len=2)
    # self.color(random.choice(COLORS))
    # self.goto(0, 20)

    # self.block.append(self)
