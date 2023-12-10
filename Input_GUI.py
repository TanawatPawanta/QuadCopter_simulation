import pygame
import sys

class MotorSpeedSliders:
    def __init__(self):
        self.startSim_press = False
        self.speedOut = [0.0, 0.0, 0.0, 0.0]
        pygame.init()

        # Constants
        self.window_width, self.window_height = 750, 600
        self.ui_scale = 1
        self.ui_width, self.ui_height = int(self.window_width * self.ui_scale), self.window_height
        self.FPS = 60
        self.ui_offset = -15

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)

        # Set up the display
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Motor Speed Sliders")

        # Font
        self.font = pygame.font.Font(None, int(36 * self.ui_scale))

        # Slider parameters
        self.slider_width = int(30 * self.ui_scale)
        self.slider_height = int(20 * self.ui_scale)
        self.slider_spacing = int(30 * self.ui_scale)

        # RPM range
        self.rpm_min = 0
        self.rpm_max = 1000

        # Sliders
        self.speeds = [0, 0, 0, 0]  # Initial speeds for four motors, all set to 0
        self.sliders = []
        self.slider_range = int(700 * self.ui_scale)
        for i in range(4):
            initial_position = int(5 * self.ui_scale)
            text = self.font.render(f"Motor {i + 1} Speed: {self.speeds[i]:.2f} RPM", True, self.BLACK)
            text_rect = text.get_rect(
                center=(int(self.ui_width // 2), int(self.window_height - 50 * self.ui_scale) - i * int(100 * self.ui_scale)))
            self.sliders.append(
                pygame.Rect(initial_position, int(self.window_height - 80 * self.ui_scale) - i * int(100 * self.ui_scale),
                            self.slider_width, self.slider_height))

        # Textbox parameters
        self.textbox_width = int(80 * self.ui_scale)
        self.textbox_height = int(30 * self.ui_scale)
        self.textbox_color = self.WHITE
        self.textbox_active_color = (255, 255, 150)
        self.textbox_font = pygame.font.Font(None, int(30 * self.ui_scale))

        # Textbox
        self.user_input_rect = pygame.Rect(int(self.ui_width // 2 - self.textbox_width - 100 // 2 - self.ui_offset),
                                           int(self.window_height - 60 * self.ui_scale), self.textbox_width, self.textbox_height)
        self.user_input = {'rect': self.user_input_rect, 'text': '', 'active': False}

        # Button parameters
        self.button_width = int(60 * self.ui_scale)
        self.button_height = int(30 * self.ui_scale)
        self.button_color = (0, 255, 0)
        self.button_font = pygame.font.Font(None, int(30 * self.ui_scale))

        # Buttons
        self.button_rect = pygame.Rect(int(self.ui_width // 2 - self.button_width - 115// 2 - self.ui_offset),
                                       int(self.window_height - 30 * self.ui_scale), self.button_width, self.button_height)
        self.button = {'rect': self.button_rect, 'text': 'Enter'}

        # Start Sim button parameters
        self.start_sim_button_rect = pygame.Rect(int(self.ui_width // 2 + 70 // 2 + self.ui_offset),
                                                 int(self.window_height - 30 * self.ui_scale),
                                                 self.button_width + 40, self.button_height)
        self.start_sim_button = {'rect': self.start_sim_button_rect, 'text': 'Start Sim'}

        # Clock
        self.clock = pygame.time.Clock()

        # Main game loop
        self.running = True
        self.dragging = None

    def handle_enter_key(self):
        try:
            new_speed = float(self.user_input['text'])
            new_speed = min(max(new_speed, 0), self.rpm_max)
            self.user_input['text'] = ' '
            print("Entered Speed:", new_speed)

            # Set all motor speeds to 0 if entered speed is 0
            if new_speed == 0:
                new_speed = 14
                for i in range(4):
                    self.sliders[i].centerx = new_speed
                    self.speeds[i] = 0
            else:
                for i in range(4):
                    self.sliders[i].centerx = int((new_speed / self.rpm_max) * self.slider_range + 20)
                    self.speeds[i] = new_speed

        except ValueError:
            pass
        self.user_input['active'] = False

    def handle_start_sim_button(self):
        print("Start Sim Button Clicked")
        self.startSim_press = True

    def run(self):
        self.screen.fill(self.WHITE)
        print("Start Sim status:", self.startSim_press)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, slider in enumerate(self.sliders):
                    if slider.collidepoint(event.pos):
                        self.dragging = i
                if self.user_input['rect'].collidepoint(event.pos):
                    self.user_input['active'] = not self.user_input['active']
                else:
                    self.user_input['active'] = False
                if self.button['rect'].collidepoint(event.pos):
                    self.handle_enter_key()
                elif self.start_sim_button['rect'].collidepoint(event.pos):
                    self.handle_start_sim_button()
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = None
            elif event.type == pygame.MOUSEMOTION:
                if self.dragging is not None:
                    self.sliders[self.dragging].centerx = max(int(20 * self.ui_scale),
                                                                min(event.pos[0], int(20 * self.ui_scale + self.slider_range)))
                    print("Dragging:", self.dragging)
                    print("Mouse Position:", event.pos)

                if self.user_input['active']:
                    if event.type == pygame.MOUSEBUTTONUP and self.button['rect'].collidepoint(event.pos):
                        if self.user_input['text']:
                            self.handle_enter_key()
                        else:
                            self.user_input['text'] = str(self.rpm_min)  # Default to rpm_min if the input is empty
            elif event.type == pygame.KEYDOWN:
                if self.user_input['active']:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.handle_enter_key()
                        
                    elif event.key == pygame.K_BACKSPACE:
                        self.user_input['text'] = self.user_input['text'][:-1]
                    elif event.unicode.isnumeric():
                        self.user_input['text'] += event.unicode

        # Update speeds
        speeds = [int((slider.centerx - 20 * self.ui_scale) / self.slider_range * self.rpm_max) for slider in
                  self.sliders]
        speeds = [max(min(speed, self.rpm_max), 0) for speed in speeds]

        self.speedOut = speeds

        # Draw sliders
        for i, slider in enumerate(self.sliders):
            pygame.draw.rect(self.screen, self.GRAY, slider)
            pygame.draw.rect(self.screen, (0, 128, 255), (slider.x, slider.y, slider.width, slider.height))

        # Draw speed text
        for i, speed in enumerate(speeds):
            text = self.font.render(f"Motor {abs(i - 4)} Speed: {int(speed)} Rad/s", True, self.BLACK)
            text_rect = text.get_rect(center=(
                int(self.ui_width // 2 - self.ui_offset), int(self.window_height - 100 * self.ui_scale) - i * int(
                    100 * self.ui_scale)))
            self.screen.blit(text, text_rect)

        # Draw user_input
        pygame.draw.rect(self.screen,
                         self.textbox_active_color if self.user_input['active'] else self.textbox_color,
                         self.user_input['rect'])
        text_surface = self.textbox_font.render(str(self.user_input['text']), True, self.BLACK)
        text_rect = text_surface.get_rect(center=self.user_input['rect'].center)
        self.screen.blit(text_surface, text_rect)

        # Draw button for Enter
        pygame.draw.rect(self.screen, self.button_color, self.button['rect'])
        text = self.button_font.render(self.button['text'], True, self.BLACK)
        text_rect = text.get_rect(center=self.button['rect'].center)
        self.screen.blit(text, text_rect)

        # Draw button for Start Sim
        pygame.draw.rect(self.screen, self.button_color, self.start_sim_button['rect'])
        text = self.button_font.render(self.start_sim_button['text'], True, self.BLACK)
        text_rect = text.get_rect(center=self.start_sim_button['rect'].center)
        self.screen.blit(text, text_rect)

        pygame.display.flip()
        self.clock.tick(self.FPS)

    def close_window(self):
        self.startSim_press = False
        pygame.quit()

    def get_speed(self):
        return self.speedOut

    def __del__(self):
        print('Destructor called, MotorSpeedSliders deleted.')

# Uncomment the following lines to run the code
# if __name__ == "__main__":
#     motor_speed_sliders = MotorSpeedSliders()
#     while True:
#         motor_speed_sliders.run()
#         print("Read Speeds:", motor_speed_sliders.get_speed())
#         if motor_speed_sliders.enter_press:
#             motor_speed_sliders.close_window()
