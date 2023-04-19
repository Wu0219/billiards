import draw
import the_ball
import data
import os
import random



def draw_a_point(x, y, r, g, b, radian):
    for i in range(-radian, radian):
        for j in range(-radian, radian):
            data.table[i + x][j + y] = r, g, b


def one_time(x, y, angle,loop_time):
    initial_x = x
    initial_y = y
    initial_angle = angle
    ball = the_ball.Ball(initial_x, initial_y, initial_angle)

    count = 0

    # data.table[:] = 255

    draw_a_point(ball.x, ball.y, 0, 255, 0, 3)

    while ball.status != "hole" and count <= loop_time:
        ball.move(1)
        ball.check_status()
        # ball.change_status()

        pixel_x = abs(int(ball.x))
        pixel_y = abs(int(ball.y))

        data.table[pixel_x][pixel_y] = 255, 255, 255

        if count % (loop_time/100) == 0:
        #     # os.system("pause")
        #     ball.display()
        #     print(count, end='  ')
        #     print(data.table[pixel_x][pixel_y], end='   ')
        #     print(str(pixel_x) + '|' + str(pixel_y))
        # print(data.table)
            print(count/loop_time)

        if ball.status == "hole":
            # print("----------the ball in hole--------")
            draw_a_point(pixel_x, pixel_y, 255, 0, 0, 3)

            break

        if count > loop_time-2:
            draw_a_point(pixel_x, pixel_y, 255, 255, 0, 10)
            print('**')
            print(initial_x)
            print(initial_y)
            print(initial_angle,end='**')


        count += 1


for i in range(1000):
    one_time(random.randint(0, 2540), random.randint(0, 1270), random.randint(1, 89),10**7)
    print(i)

# one_time(487,408,45,10**7)
draw.draw_picture()
