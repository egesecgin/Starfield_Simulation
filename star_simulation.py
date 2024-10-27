import pygame
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
NUM_STARS = 9000
MAX_DEPTH = 40
COLLISION_RADIUS = 10

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Starfield Simulation MUI")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

trail_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
trail_surface.fill((0, 0, 0, 25))

class Star:
    def __init__(self):
        self.reset()
        self.history = []

    def reset(self):
        self.x = random.randrange(-SCREEN_WIDTH, SCREEN_WIDTH)
        self.y = random.randrange(-SCREEN_HEIGHT, SCREEN_HEIGHT)
        self.z = random.uniform(MAX_DEPTH / 2, MAX_DEPTH)
        self.pz = self.z

    def update(self, speed_multiplier):
        self.pz = self.z
        self.z -= 0.2 * speed_multiplier
        if self.z <= 0:
            self.reset()
            self.z = MAX_DEPTH
            self.pz = self.z

    def draw(self, surface, ship_x, ship_y):
        k = 128 / self.z
        x = int((self.x - (ship_x - SCREEN_WIDTH / 2)) * k + SCREEN_WIDTH / 2)
        y = int((self.y - (ship_y - SCREEN_HEIGHT / 2)) * k + SCREEN_HEIGHT / 2)

        pk = 128 / self.pz
        px = int((self.x - (ship_x - SCREEN_WIDTH / 2)) * pk + SCREEN_WIDTH / 2)
        py = int((self.y - (ship_y - SCREEN_HEIGHT / 2)) * pk + SCREEN_HEIGHT / 2)

        if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
            shade = int((1 - self.z / MAX_DEPTH) * 255)
            color = (shade, shade, shade)
            pygame.draw.line(surface, color, (px, py), (x, y))

            distance = ((x - ship_x) ** 2 + (y - ship_y) ** 2) ** 0.5
            if distance < COLLISION_RADIUS:
                return True
        return False

stars = [Star() for _ in range(NUM_STARS)]

running = True
game_over = False
ship_x = SCREEN_WIDTH / 2
ship_y = SCREEN_HEIGHT / 2
ship_speed = 0.05
collision_delay = 2
collision_timer = 0
collision_detection_enabled = False
score = 0
high_score = 0
speed_multiplier = 1.0

while running:
    delta_time = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                speed_multiplier += 0.1
            if event.button == 5:
                speed_multiplier = max(0.1, speed_multiplier - 0.1)
            if game_over and event.button == 1:
                game_over = False
                collision_timer = 0
                collision_detection_enabled = False
                ship_x = SCREEN_WIDTH / 2
                ship_y = SCREEN_HEIGHT / 2
                score = 0
                speed_multiplier = 1.0
                for star in stars:
                    star.reset()
    screen.blit(trail_surface, (0, 0))
    if not game_over:
        collision_timer += delta_time
        if collision_timer >= collision_delay:
            collision_detection_enabled = True
        mouse_x, mouse_y = pygame.mouse.get_pos()
        ship_x += (mouse_x - ship_x) * ship_speed
        ship_y += (mouse_y - ship_y) * ship_speed
        for star in stars:
            star.update(speed_multiplier)
            collision = star.draw(screen, ship_x, ship_y)
            if collision and collision_detection_enabled:
                game_over = True
                collision_detection_enabled = False
                if score > high_score:
                    high_score = score
                break
        pygame.draw.circle(screen, (255, 0, 0), (int(ship_x), int(ship_y)), COLLISION_RADIUS, 1)
        score += int(1 * speed_multiplier)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 20, 20))
        screen.blit(high_score_text, (SCREEN_WIDTH - high_score_text.get_width() - 20, 60))
    else:
        game_over_text = font.render("You crashed!", True, (255, 255, 255))
        restart_text = font.render("Click to Restart", True, (255, 255, 255))
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) / 2, SCREEN_HEIGHT / 2 - 50))
        screen.blit(restart_text, ((SCREEN_WIDTH - restart_text.get_width()) / 2, SCREEN_HEIGHT / 2))
        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_text, (SCREEN_WIDTH - high_score_text.get_width() - 20, 20))
    pygame.display.flip()

pygame.quit()
