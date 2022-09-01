import simple_draw as sd

sd.set_screen_size(1200, 800)


def draw_flake(point, arm_len):
    delta_angle = sd.random_number(30, 90)
    factor_a = sd.random_number(30, 90) / 100
    for angle in range(0, 360, 60):
        arm = sd.get_vector(point, angle=angle, length=arm_len)
        arm.draw(color=sd.COLOR_WHITE)
        arm_2 = sd.get_vector(point, angle=angle, length=arm_len * .6)
        sub_arm_1 = sd.get_vector(
            start_point=arm_2.end_point,
            angle=angle + delta_angle,
            length=arm_len * factor_a
        )
        sub_arm_1.draw(color=sd.COLOR_WHITE)
        sub_arm_2 = sd.get_vector(
            start_point=arm_2.end_point,
            angle=angle - delta_angle,
            length=arm_len * factor_a
        )
        sub_arm_2.draw(color=sd.COLOR_WHITE)


for _ in range(50):
    point = sd.random_point()
    length = sd.random_number(10, 50)
    draw_flake(point=point, arm_len=length)

sd.pause()
