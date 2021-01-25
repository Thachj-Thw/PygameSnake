import pygame
import random
import sys
pygame.init()
pygame.display.set_caption('Snake Game')
display = pygame.display.set_mode((400, 400), 0)

# màu
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (225, 225, 225)
orange = (255, 85, 0)
dark_orange = (200, 85, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
dark_green = (0, 85, 0)

# import image
head_up = pygame.transform.scale(pygame.image.load('images/head_up.png'), (20, 20))
head_down = pygame.transform.scale(pygame.image.load('images/head_down.png'), (20, 20))
head_left = pygame.transform.scale(pygame.image.load('images/head_left.png'), (20, 20))
head_right = pygame.transform.scale(pygame.image.load('images/head_right.png'), (20, 20))
tail_up = pygame.transform.scale(pygame.image.load('images/tail_up.png'), (20, 20))
tail_down = pygame.transform.scale(pygame.image.load('images/tail_down.png'), (20, 20))
tail_left = pygame.transform.scale(pygame.image.load('images/tail_left.png'), (20, 20))
tail_right = pygame.transform.scale(pygame.image.load('images/tail_right.png'), (20, 20))
left_up = pygame.transform.scale(pygame.image.load('images/body_left_up.png'), (20, 20))
left_down = pygame.transform.scale(pygame.image.load('images/body_left_down.png'), (20, 20))
right_up = pygame.transform.scale(pygame.image.load('images/body_right_up.png'), (20, 20))
right_down = pygame.transform.scale(pygame.image.load('images/body_right_down.png'), (20, 20))
img_snake = (
	(head_up, head_down, head_left, head_right),
	(left_up, left_down, right_up, right_down),
	(tail_up, tail_down, tail_left, tail_right)
)
img_color = pygame.transform.scale(pygame.image.load('images/color.png'), (140, 60))
img_map = pygame.transform.scale(pygame.image.load('images/map.png'), (400, 400))
img_menu = pygame.transform.scale(pygame.image.load('images/menu.png'), (180, 100))
img_setting = (img_menu, img_color)


def draw_text(text, size, color, _map, x, y):
	font = pygame.font.SysFont('comicsansms', size)
	textobj = font.render(text, True, color)
	_map.blit(textobj, [x, y])


def click_mouse(button):
	x_mouse, y_mouse = pygame.mouse.get_pos()
	if button.collidepoint((x_mouse, y_mouse)):
		return True
	return False


def light_button(screen, but, color):
	x_mouse, y_mouse = pygame.mouse.get_pos()
	if but.collidepoint((x_mouse, y_mouse)):
		pygame.draw.rect(screen, color, but)


mode = 'easy'
color_1 = green
color_2 = green


class Setting:
	def __init__(self, screen, img):
		self.screen = screen
		self.img_snake = img[0]
		self.img_color = img[1]
		self.easy = pygame.Rect(45, 210, 70, 20)
		self.normal = pygame.Rect(45, 240, 70, 20)
		self.hard = pygame.Rect(45, 270, 70, 20)
		self.mode = {
			'self.easy': 'easy',
			'self.normal': 'normal',
			'self.hard': 'hard'
		}

		self.bk = pygame.Rect(150, 210, 20, 20)
		self.r = pygame.Rect(170, 210, 20, 20)
		self.b = pygame.Rect(190, 210, 20, 20)
		self.g = pygame.Rect(150, 230, 20, 20)
		self.w = pygame.Rect(170, 230, 20, 20)
		self.dg = pygame.Rect(190, 230, 20, 20)
		self.o = pygame.Rect(150, 250, 20, 20)
		self.do = pygame.Rect(170, 250, 20, 20)
		self.y = pygame.Rect(190, 250, 20, 20)
		self.col_1 = {
			'self.bk': black,
			'self.r': red,
			'self.b': blue,
			'self.g': green,
			'self.w': white,
			'self.dg': dark_green,
			'self.o': orange,
			'self.do': dark_orange,
			'self.y': yellow
		}

		self.bk2 = pygame.Rect(230, 210, 20, 20)
		self.r2 = pygame.Rect(250, 210, 20, 20)
		self.b2 = pygame.Rect(270, 210, 20, 20)
		self.g2 = pygame.Rect(230, 230, 20, 20)
		self.w2 = pygame.Rect(250, 230, 20, 20)
		self.dg2 = pygame.Rect(270, 230, 20, 20)
		self.o2 = pygame.Rect(230, 250, 20, 20)
		self.do2 = pygame.Rect(250, 250, 20, 20)
		self.y2 = pygame.Rect(270, 250, 20, 20)
		self.col_2 = {
			'self.bk2': black,
			'self.r2': red,
			'self.b2': blue,
			'self.g2': green,
			'self.w2': white,
			'self.dg2': dark_green,
			'self.o2': orange,
			'self.do2': dark_orange,
			'self.y2': yellow
		}

		self.window = pygame.Rect(45, 300, 100, 20)
		self.fullscreen = pygame.Rect(45, 330, 100, 20)
		self.save = pygame.Rect(320, 350, 40, 20)
		self.cont = True

	def draw(self):
		self.screen.fill(white)
		pygame.draw.rect(self.screen, color_1, [170, 120, 20, 20])
		pygame.draw.rect(self.screen, color_2, [190, 120, 20, 20])
		pygame.draw.rect(self.screen, color_1, [210, 120, 20, 20])
		self.screen.blit(self.img_snake, pygame.Rect(110, 80, 180, 100))
		self.screen.blit(self.img_color, pygame.Rect(150, 210, 140, 60))

		light_button(self.screen, self.easy, blue)
		light_button(self.screen, self.normal, blue)
		light_button(self.screen, self.hard, blue)
		light_button(self.screen, self.save, blue)
		light_button(self.screen, self.window, green)
		light_button(self.screen, self.fullscreen, green)

		draw_text('Setting', 30, blue, self.screen, 150, 30)
		draw_text('{}'.format(mode), 15, black, self.screen, 220, 160)
		draw_text('easy', 20, green, self.screen, 50, 205)
		draw_text('normal', 20, orange, self.screen, 50, 235)
		draw_text('hard', 20, red, self.screen, 50, 265)
		draw_text('save', 20, black, self.screen, 320, 345)
		draw_text('window', 20, blue, self.screen, 50, 295)
		draw_text('fullscreen', 20, blue, self.screen, 50, 325)
		pygame.display.update()

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for button in self.mode.keys():
					if click_mouse(eval(button)):
						globals()['mode'] = self.mode.get(button)

				for button in self.col_1.keys():
					if click_mouse(eval(button)):
						globals()['color_1'] = self.col_1.get(button)

				for button in self.col_2.keys():
					if click_mouse(eval(button)):
						globals()['color_2'] = self.col_2.get(button)

				if click_mouse(self.window):
					pygame.display.set_mode((400, 400), 0)
				if click_mouse(self.fullscreen):
					pygame.display.set_mode((400, 400), pygame.FULLSCREEN)

				if click_mouse(self.save):
					self.cont = False

	def setting_display(self):
		while self.cont:
			self.draw()
			self.update()
		self.cont = True


class MainMenu:
	def __init__(self, screen, img):
		self.screen = screen
		self.play = pygame.Rect(150, 195, 93, 30)
		self.setting = pygame.Rect(150, 235, 90, 30)
		self.exit = pygame.Rect(150, 275, 90, 30)
		self.img = img

	def draw(self):
		self.screen.fill(white)
		pygame.draw.rect(self.screen, color_1, [170, 120, 20, 20])
		pygame.draw.rect(self.screen, color_2, [190, 120, 20, 20])
		pygame.draw.rect(self.screen, color_1, [210, 120, 20, 20])
		self.screen.blit(self.img, pygame.Rect(110, 80, 180, 100))

		light_button(self.screen, self.play, green)
		light_button(self.screen, self.setting, green)
		light_button(self.screen, self.exit, green)

		draw_text('Snake Game', 30, green, self.screen, 125, 25)
		draw_text('Create by Thw', 10, red, self.screen, 250, 60)
		draw_text('Play Now', 20, black, self.screen, 155, 195)
		draw_text('{}'.format(mode), 15, black, self.screen, 220, 160)
		draw_text('Setting', 20, black, self.screen, 160, 235)
		draw_text('Exit', 20, black, self.screen, 175, 275)
		pygame.display.update()

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if click_mouse(self.play):
					start()
				if click_mouse(self.setting):
					setting.setting_display()
				if click_mouse(self.exit):
					pygame.quit()
					sys.exit()

	def menu_display(self):
		while True:
			self.draw()
			self.update()


snake = []
food = []
score = 0


class Snake:
	def __init__(self, screen, img):
		self.screen = screen
		self.size = 20
		self.snakehead = [200, 300]
		self.snakebody = [[200, 300], [200, 320], [200, 340]]
		globals()['snake'] = self.snakebody
		self.way = 'UP'

		self.img_head_up = img[0][0]
		self.img_head_down = img[0][1]
		self.img_head_left = img[0][2]
		self.img_head_right = img[0][3]

		self.img_left_up = img[1][0]
		self.img_left_down = img[1][1]
		self.img_right_up = img[1][2]
		self.img_right_down = img[1][3]

		self.img_tail_up = img[2][0]
		self.img_tail_down = img[2][1]
		self.img_tail_left = img[2][2]
		self.img_tail_right = img[2][3]

	def draw(self):
		k = 0
		for snk in self.snakebody:
			if k % 2 == 0:
				pygame.draw.rect(self.screen, color_1, [snk[0], snk[1], self.size, self.size])
			else:
				pygame.draw.rect(self.screen, color_2, [snk[0], snk[1], self.size, self.size])
			k += 1

		if self.way == 'UP':
			self.screen.blit(
				self.img_head_up,
				pygame.Rect(self.snakebody[0][0], self.snakebody[0][1], self.size, self.size)
			)
		elif self.way == 'DOWN':
			self.screen.blit(
				self.img_head_down,
				pygame.Rect(self.snakebody[0][0], self.snakebody[0][1], self.size, self.size)
			)
		elif self.way == 'LEFT':
			self.screen.blit(
				self.img_head_left,
				pygame.Rect(self.snakebody[0][0], self.snakebody[0][1], self.size, self.size)
			)
		else:
			self.screen.blit(
				self.img_head_right,
				pygame.Rect(self.snakebody[0][0], self.snakebody[0][1], self.size, self.size)
			)

		for i in range(len(self.snakebody) - 2):
			x = self.snakebody[i + 2][0] - self.snakebody[i][0]
			y = self.snakebody[i + 2][1] - self.snakebody[i][1]
			t = self.snakebody[i + 2][0] - self.snakebody[i + 1][0]
			if (x == 20 and y == 20 and t == 0) or (x == -20 and y == -20 and t != 0):
				self.screen.blit(
					self.img_left_down,
					pygame.Rect(self.snakebody[i + 1][0], self.snakebody[i + 1][1], self.size, self.size)
				)
			elif (x == -20 and y == 20 and t == 0) or (x == 20 and y == -20 and t != 0):
				self.screen.blit(
					self.img_right_down,
					pygame.Rect(self.snakebody[i + 1][0], self.snakebody[i + 1][1], self.size, self.size)
				)
			elif (x == 20 and y == -20 and t == 0) or (x == -20 and y == 20 and t != 0):
				self.screen.blit(
					self.img_left_up,
					pygame.Rect(self.snakebody[i + 1][0], self.snakebody[i + 1][1], self.size, self.size)
				)
			elif (x == -20 and y == -20 and t == 0) or (x == 20 and y == 20 and t != 0):
				self.screen.blit(
					self.img_right_up,
					pygame.Rect(self.snakebody[i + 1][0], self.snakebody[i + 1][1], self.size, self.size)
				)

		tail_x = self.snakebody[-1][0] - self.snakebody[-2][0]
		tail_y = self.snakebody[-1][1] - self.snakebody[-2][1]
		if tail_y == 20:
			self.screen.blit(
				self.img_tail_up,
				pygame.Rect(self.snakebody[-1][0], self.snakebody[-1][1], self.size, self.size)
			)
		elif tail_y == -20:
			self.screen.blit(
				self.img_tail_down,
				pygame.Rect(self.snakebody[-1][0], self.snakebody[-1][1], self.size, self.size)
			)
		elif tail_x == 20:
			self.screen.blit(
				self.img_tail_left,
				pygame.Rect(self.snakebody[-1][0], self.snakebody[-1][1], self.size, self.size)
			)
		else:
			self.screen.blit(
				self.img_tail_right,
				pygame.Rect(self.snakebody[-1][0], self.snakebody[-1][1], self.size, self.size)
			)

	def update(self, way):
		self.way = way
		if way == 'UP':
			self.snakehead[1] -= self.size
		elif way == 'DOWN':
			self.snakehead[1] += self.size
		elif way == 'LEFT':
			self.snakehead[0] -= self.size
		else:
			self.snakehead[0] += self.size

		self.snakebody.insert(0, list(self.snakehead))
		if self.snakehead[0] == food[0] and self.snakehead[1] == food[1]:
			globals()['score'] += 1
		else:
			self.snakebody.pop()
		globals()['snake'] = self.snakebody

	def die(self):
		if not (20 <= self.snakehead[0] <= 360 and 20 <= self.snakehead[1] <= 360):
			return True

		for i in self.snakebody[1:]:
			if i[0] == self.snakehead[0] and i[1] == self.snakehead[1]:
				return True
		return False


class Food:
	def __init__(self, screen):
		self.screen = screen
		self.x_food = random.randrange(1, 13) * 20
		self.y_food = random.randrange(1, 13) * 20
		globals()['food'] = [self.x_food, self.y_food]

	def draw(self):
		pygame.draw.circle(self.screen, red, [self.x_food + 10, self.y_food + 10], 7)

	def update(self):
		for i in snake:
			if i[0] == self.x_food and i[1] == self.y_food:
				self.x_food = random.randrange(1, 13) * 20
				self.y_food = random.randrange(1, 13) * 20
				globals()['food'] = [self.x_food, self.y_food]


class Map:
	def __init__(self, screen, img):
		self.screen = screen
		self.img = img

	def draw(self):
		self.screen.blit(self.img, pygame.Rect(0, 0, 400, 400))
		draw_text('Score: {}'.format(score), 15, black, self.screen, 0, -5)


class Pause:
	def __init__(self, screen):
		self.screen = screen
		self.resume = pygame.Rect(150, 155, 80, 30)
		self.menu = pygame.Rect(150, 195, 80, 30)
		self.cont = True

	def draw(self):
		self.screen.fill(white)
		light_button(self.screen, self.resume, green)
		light_button(self.screen, self.menu, green)
		draw_text('Game Pause!', 25, red, self.screen, 125, 65)
		draw_text('Resume', 20, black, self.screen, 155, 155)
		draw_text('Menu', 20, black, self.screen, 165, 195)
		pygame.display.update()

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if click_mouse(self.resume):
					self.cont = False
				if click_mouse(self.menu):
					menu.menu_display()

	def pause_display(self):
		while self.cont:
			self.draw()
			self.update()
		self.cont = True


class End:
	def __init__(self, screen):
		self.screen = screen
		self.restart = pygame.Rect(150, 155, 80, 30)
		self.menu = pygame.Rect(150, 195, 80, 30)

	def draw(self):
		self.screen.fill(white)
		light_button(self.screen, self.restart, green)
		light_button(self.screen, self.menu, green)
		draw_text('Game Over!', 25, red, self.screen, 135, 65)
		draw_text('Restart', 20, black, self.screen, 155, 155)
		draw_text('Menu', 20, black, self.screen, 165, 195)
		draw_text('Score: {}'.format(score), 20, black, self.screen, 150, 100)
		pygame.display.update()

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if click_mouse(self.restart):
					start()
				if click_mouse(self.menu):
					menu.menu_display()

	def end_display(self):
		while True:
			self.draw()
			self.update()


def start():
	if mode == 'easy':
		delay = 150
	elif mode == 'normal':
		delay = 100
	else:
		delay = 50

	_snake = Snake(display, img_snake)
	_food = Food(display)
	_map = Map(display, img_map)
	way = 'UP'
	globals()['score'] = 0

	while True:
		pygame.time.delay(delay)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause.pause_display()
				if event.key == pygame.K_UP and way != 'DOWN':
					way = 'UP'
					break
				if event.key == pygame.K_DOWN and way != 'UP':
					way = 'DOWN'
					break
				if event.key == pygame.K_RIGHT and way != 'LEFT':
					way = 'RIGHT'
					break
				if event.key == pygame.K_LEFT and way != 'RIGHT':
					way = 'LEFT'
					break

		display.fill(white)
		_map.draw()
		_food.draw()
		_snake.draw()
		pygame.display.update()
		if _snake.die():
			end.end_display()
		_snake.update(way)
		_food.update()


menu = MainMenu(display, img_menu)
setting = Setting(display, img_setting)
end = End(display)
pause = Pause(display)


if __name__ == '__main__':
	menu.menu_display()
