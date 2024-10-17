import pygame


# BUTTON
X_BUTTON = 0
CIRCLE_BUTTON = 1
SQUARE_BUTTON = 2
TRIANGLE_BUTTON = 3
SHARE_BUTTON = 4
PS_BUTTON = 5
OPTIONS_BUTTON = 6
L3_BUTTON = 7
R3_BUTTON = 8
L1_BUTTON = 9
R1_BUTTON = 10
UP_ARROW_BUTTON = 11
DOWN_ARROW_BUTTON = 12
LEFT_ARROW_BUTTON = 13
RIGHT_ARROW_BUTTON = 14


# AXIS
LEFT_ANALOG_X = 0
LEFT_ANALOG_Y = 1
RIGHT_ANALOG_X = 2
RIGHT_ANALOG_Y = 3
L2_ANALOG = 4
R2_ANALOG = 5


# Pygame'in başlatılması
pygame.init()

# Joystick sistemini başlatma
pygame.joystick.init()

# Bağlı joystick sayısını al
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("Joystick bulunamadı.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    # Ana oyun döngüsü
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            else:
                if event.type == pygame.JOYBUTTONDOWN:
                    button_id = event.dict['button']
                    if button_id == X_BUTTON:
                        print("X pressed")
                    elif button_id == CIRCLE_BUTTON:
                         print("Circle pressed")
                    elif button_id == SQUARE_BUTTON:
                         print("Square pressed")
                    elif button_id == TRIANGLE_BUTTON:
                         print("Triangle pressed")
                    elif button_id == SHARE_BUTTON:
                         print("Share pressed")
                    elif button_id == PS_BUTTON:
                         print("PS pressed")
                    elif button_id == OPTIONS_BUTTON:
                         print("Options pressed")
                    elif button_id == L3_BUTTON:
                         print("L3 pressed")
                    elif button_id == R3_BUTTON:
                         print("R3 pressed")
                    elif button_id == L1_BUTTON:
                         print("L1 pressed")
                    elif button_id == R1_BUTTON:
                         print("R1 pressed")
                    elif button_id == UP_ARROW_BUTTON:
                         print("Up arrow pressed")
                    elif button_id == DOWN_ARROW_BUTTON:
                         print("Down arrow pressed")
                    elif button_id == LEFT_ARROW_BUTTON:
                         print("Left arrow pressed")
                    elif button_id == RIGHT_ARROW_BUTTON:
                         print("Right arrow pressed")

                 
                elif event.type == pygame.JOYBUTTONUP:
                    button_id = event.dict['button']
                    if button_id == X_BUTTON:
                        print("X released")
                    elif button_id == CIRCLE_BUTTON:
                         print("Circle released")
                    elif button_id == SQUARE_BUTTON:
                         print("Square released")
                    elif button_id == TRIANGLE_BUTTON:
                         print("Triangle released")
                    elif button_id == SHARE_BUTTON:
                         print("Share released")
                    elif button_id == PS_BUTTON:
                         print("PS released")
                    elif button_id == OPTIONS_BUTTON:
                         print("Options released")
                    elif button_id == L3_BUTTON:
                         print("L3 released")
                    elif button_id == R3_BUTTON:
                         print("R3 released")
                    elif button_id == L1_BUTTON:
                         print("L1 released")
                    elif button_id == R1_BUTTON:
                         print("R1 released")
                    elif button_id == UP_ARROW_BUTTON:
                         print("Up arrow released")
                    elif button_id == DOWN_ARROW_BUTTON:
                         print("Down arrow released")
                    elif button_id == LEFT_ARROW_BUTTON:
                         print("Left arrow released")
                    elif button_id == RIGHT_ARROW_BUTTON:
                         print("Right arrow released")
                
                elif event.type == pygame.JOYAXISMOTION:
                    axis = event.dict['axis']
                    value = event.dict['value']
                    value = f"{value:.3f}"

                    if axis == LEFT_ANALOG_X:
                        print(f"Left Analog X, {value}")
                    elif axis == LEFT_ANALOG_Y:
                        print(f"Left Analog Y, {value}")
                    elif axis == RIGHT_ANALOG_X:
                        print(f"Right Analog X, {value}")
                    elif axis == RIGHT_ANALOG_Y:
                        print(f"Right Analog Y, {value}")
                    elif axis == L2_ANALOG:
                        print(f"L2, {value}")
                    elif axis == R2_ANALOG:
                        print(f"R2, {value}")

