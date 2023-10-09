import pygame as pg
import random 
import sys

class Snake:
    def __init__(self): #  Initialize the game and set up the initial state, such as the snake's position, direction, and the game window.
        pg.init()
        self.width = 600
        self.height = 400
        self.window = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption('Snake Game')
        self.clock = pg.time.Clock()
        self.snake_segments = [(100, 100)]
        self.direction = "RIGHT"
        self.score = 0
        self.food = Food(self.width, self.height)
        self.game_over = False
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused

    def handle_events(self): # handling input events to change direction of the snake
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game_over = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP and self.direction != 'DOWN':
                    self.direction = 'UP'
                elif event.key == pg.K_DOWN and self.direction != 'UP':
                    self.direction = 'DOWN'
                elif event.key == pg.K_LEFT and self.direction != 'RIGHT':
                    self.direction = 'LEFT'
                elif event.key == pg.K_RIGHT and self.direction != 'LEFT':
                    self.direction = 'RIGHT'
                elif event.key == pg.K_ESCAPE:
                    self.toggle_pause()
            
                

    def update(self): # uppdating the state of the game
        if not self.game_over:
            self.move_snake()
            self.check_collision()
            self.check_food()

    def move_snake(self):
        new_head = list(self.snake_segments[0])

        if self.direction == 'UP':
            new_head[1] -= 10
        elif self.direction == 'DOWN':
            new_head[1] += 10
        elif self.direction == 'LEFT':
            new_head[0] -= 10
        elif self.direction == 'RIGHT':
            new_head[0] += 10

        self.snake_segments = [tuple(new_head)] + self.snake_segments[:-1]

        if self.snake_segments[0] in self.snake_segments[1:]:
            self.game_over = True

        if (
            self.snake_segments[0][0] < 0
            or self.snake_segments[0][0] >= self.width
            or self.snake_segments[0][1] < 0
            or self.snake_segments[0][1] >= self.height
        ):
            self.game_over = True

        if self.snake_segments[0] == self.food.position:
            self.score += 1
            self.food.respawn_food()
        # Add a new segment at the end of the snake
            x, y = self.snake_segments[-1]
            self.snake_segments.append((x, y))

    # Remove the last segment if the snake did not eat food
        elif not self.food.on_screen:
            self.snake_segments.pop()
            
 
    
    def check_collision(self):
        if self.snake_segments[0] == self.food.position:
            self.score += 1
            self.food.respawn_food()
        
    def check_food(self): 
            if not self.food.on_screen:
                self.food.respawn_food()
                
                x, y = self.snake_segments[-1]
                self.snake_segments.append((x, y))



    def render(self): # drawing current state in window
        self.window.fill((0, 0, 0))
        
        for i, segment in enumerate(self.snake_segments):
            if i % 2 == 0:
                pg.draw.rect(self.window, (0, 255, 0), pg.Rect(segment[0], segment[1], 10, 10))
            else:
                pg.draw.rect(self.window, (0, 128, 0), pg.Rect(segment[0], segment[1], 10, 10))
        
        pg.draw.rect(self.window, (255, 0, 0), pg.Rect(self.food.position[0], self.food.position[1], 10, 10))

        font = pg.font.SysFont(None, 30)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))

        pg.display.flip()




    def run(self): # running the game loop
        while not self.game_over:
            self.handle_events()
            
            if not self.paused:
                self.update()
                self.render()
            self.clock.tick(15)

        pg.quit()
        sys.exit()


class Food:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.position = self.generate_food_position()
        self.on_screen = True

    def generate_food_position(self):
        x = random.randrange(1, self.max_x // 10) * 10
        y = random.randrange(1, self.max_y // 10) * 10
        return x, y
    
    def respawn_food(self):
        self.position = self.generate_food_position()
        self.on_screen = True

if __name__ == "__main__":
    game = Snake()
    game.run()