import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot Ball")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball class
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = BLACK
        self.speed_x = 5  # Horizontal speed
        self.speed_y = -10  # Vertical speed (initially zero)
        self.gravity = 0.1  # Gravity acceleration
        self.bounce_factor = 0.2  # Damping factor for bounce

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity  # Apply gravity

        # Collision with screen boundaries
        if self.y + self.radius > HEIGHT:  # If ball hits bottom
            self.y = HEIGHT - self.radius
            self.speed_y *= -self.bounce_factor  # Reverse and dampen vertical speed
            self.speed_x *= self.bounce_factor  # Dampen horizontal speed

            # Stop bouncing if speed is very low
            if abs(self.speed_y) < 0.1:
                self.speed_y = 0
                self.speed_x = 0

        if self.x + self.radius > WIDTH:  # If ball hits right side
            self.x = WIDTH - self.radius
            self.speed_x *= -self.bounce_factor  # Reverse and dampen horizontal speed

# Main function
def main():
    balls = []

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Create a new ball when mouse button is pressed
                x, y = pygame.mouse.get_pos()
                balls.append(Ball(x, y, 20))

        for ball in balls:
            ball.draw(screen)
            ball.move()

            # If ball goes out of the screen or hits bottom, remove it
            if ball.x > WIDTH + ball.radius or ball.y > HEIGHT + ball.radius:
                balls.remove(ball)

        pygame.display.flip()

if __name__ == "__main__":
    main()
