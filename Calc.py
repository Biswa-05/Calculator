import pygame

pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
light_gray = (200, 200, 200)

# Screen dimensions
width, height = 350, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Calculator")

# Font
font = pygame.font.Font(None, 32)

# Button dimensions
button_width = 70
button_height = 50
button_margin = 10

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create button objects
buttons = []
buttons.append(Button(30, 130, button_width, button_height, "7", gray))
buttons.append(Button(110, 130, button_width, button_height, "8", gray))
buttons.append(Button(190, 130, button_width, button_height, "9", gray))
buttons.append(Button(30, 190, button_width, button_height, "4", gray))
buttons.append(Button(110, 190, button_width, button_height, "5", gray))
buttons.append(Button(190, 190, button_width, button_height, "6", gray))
buttons.append(Button(30, 250, button_width, button_height, "1", gray))
buttons.append(Button(110, 250, button_width, button_height, "2", gray))
buttons.append(Button(190, 250, button_width, button_height, "3", gray))
buttons.append(Button(30, 310, button_width, button_height, "0", gray))
buttons.append(Button(110, 310, button_width, button_height, ".", gray))
buttons.append(Button(190, 310, button_width, button_height, "=", light_gray)) 
buttons.append(Button(270, 130, button_width, button_height, "+", light_gray))
buttons.append(Button(270, 190, button_width, button_height, "-", light_gray))
buttons.append(Button(270, 250, button_width, button_height, "*", light_gray))
buttons.append(Button(270, 310, button_width, button_height, "/", light_gray))
buttons.append(Button(30, 370, button_width, button_height, "C", light_gray))

# Calculator logic
current_input = ""
operator = None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            for button in buttons:
                if button.is_clicked((mouse_x, mouse_y)):
                    if button.text.isdigit() or button.text == ".":
                        current_input += button.text
                    elif button.text in "+-*/":
                        if current_input:
                            operator = button.text
                            current_input += " " + operator + " "
                    elif button.text == "=":
                        try:
                            result = eval(current_input)
                            current_input = str(result)
                        except:
                            current_input = "Error"
                        operator = None
                    elif button.text == "C":
                        current_input = ""
                        operator = None

    # Fill the screen with white color
    screen.fill(white)

    # Draw buttons
    for button in buttons:
        button.draw()

    # Display current input
    input_surface = font.render(current_input, True, black)
    input_rect = input_surface.get_rect(center=(width // 2, 50))
    screen.blit(input_surface, input_rect)

    pygame.display.update()

pygame.quit()
