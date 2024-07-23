import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(fun=player.go_up, key="Up")

update_time = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # if update_time % 10 == 0:
    #     car.create_car()
    #     update_time += 1

    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

# #     detect if reach goal 这也行
#     if player.ycor() == 280:
#         player.goto(0, -280)
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()




screen.exitonclick()







