import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Game state
game_started = False
sound_on = True

class Hero:
    def __init__(self, pos):
        self.idle_frames = ["hero_idle_1", "hero_idle_2"]
        self.walk_frames = ["hero_walk_1", "hero_walk_2"]
        self.actor = Actor(self.idle_frames[0], pos)
        self.frame = 0
        self.animation_timer = 0
        self.on_ground = True
        self.vy = 0

    def move(self):
        if keyboard.left:
            self.actor.x -= 5
            self.animate(self.walk_frames)
        elif keyboard.right:
            self.actor.x += 5
            self.animate(self.walk_frames)
        else:
            self.animate(self.idle_frames)

        if keyboard.space and self.on_ground:
            self.vy = -10
            self.on_ground = False
            # if sound_on:
                    sounds.jump.play()

        if not self.on_ground:
            self.vy += 0.5
            self.actor.y += self.vy
            if self.actor.y >= 500:
                self.actor.y = 500
                self.vy = 0
                self.on_ground = True

    def animate(self, frames):
        self.frame = (self.frame + 1) % len(frames)
        self.actor.image = frames[self.frame]

    def draw(self):
        self.actor.draw()

class Enemy:
    def __init__(self, pos, patrol_range):
        self.frames = ["enemy_idle_1", "enemy_idle_2"]
        self.actor = Actor(self.frames[0], pos)
        self.frame = 0
        self.direction = 1
        self.range = patrol_range
        self.origin_x = pos[0]

    def move(self):
        self.actor.x += self.direction * 2
        if abs(self.actor.x - self.origin_x) > self.range:
            self.direction *= -1
        self.animate()

    def animate(self):
        self.frame = (self.frame + 1) % len(self.frames)
        self.actor.image = self.frames[self.frame]

    def draw(self):
        self.actor.draw()

# Initialize hero and enemies
hero = Hero((100, 500))
enemies = [Enemy((300, 500), 100), Enemy((500, 500), 100), Enemy((700, 500), 80)]

def draw():
    screen.clear()
    if not game_started:
        draw_menu()
    else:
        draw_game()

def draw_menu():
    screen.draw.text("Hero in the Sky", center=(WIDTH // 2, 100), fontsize=60, color="white")
    screen.draw.text("Press S to Start", center=(WIDTH // 2, 200), fontsize=40, color="white")
    screen.draw.text("Press M to Toggle Sound", center=(WIDTH // 2, 260), fontsize=30, color="white")
    screen.draw.text("Press Q to Quit", center=(WIDTH // 2, 320), fontsize=30, color="white")

def draw_game():
    screen.draw.text("Use arrows to move, space to jump", (10, 10), fontsize=30, color="white")
    hero.draw()
    for enemy in enemies:
        enemy.draw()

def update(dt):
    global game_started

    if not game_started:
        return

    hero.move()
    for enemy in enemies:
        enemy.move()
        if hero.actor.colliderect(enemy.actor):
            reset_game()

def reset_game():
    global game_started
    hero.actor.x, hero.actor.y = 100, 500
    game_started = False

def on_key_down(key):
    global game_started, sound_on

    if not game_started:
        if key == keys.S:
            game_started = True
            # if sound_on:
            #     music.play("bg_music")
        elif key == keys.M:
            sound_on = not sound_on
        elif key == keys.Q:
            exit()

pgzrun.go()