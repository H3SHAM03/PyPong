from Classes import *

def sine(speed: float, time: int, how_far: float, overall_y: int) -> int:
	t = pygame.time.get_ticks() / 2 % time
	y = math.sin(t / speed) * how_far + overall_y
	return int(y)

def get_font(size):
	return pygame.font.Font("assets\\Minecrafter.ttf",size)

def Pong():
	pygame.init()
	screen = pygame.display.set_mode((1280,720))
	# screen.fill((3, 0, 30))
	screen.fill("Black")
	running = True
	ball = Ball()
	ball.Resize(40,40)
	ball_mask = pygame.mask.from_surface(ball.image)
	mask_img = ball_mask.to_surface()

	P1 = Player()
	P2 = Player()
	P1_mask = pygame.mask.from_surface(P1.image)
	P2_mask = pygame.mask.from_surface(P2.image)
	P1_score = 0
	P2_score = 0
	clock = pygame.time.Clock()
	dt = clock.tick(240) / 1000
	ball_xspeed = 0 * dt
	ball_yspeed = 0 * dt
	Players = pygame.sprite.Group()
	Players.add(P1)
	Players.add(P2)

	P1.pos = pygame.Vector2(50, screen.get_height() / 2)
	P2.pos = pygame.Vector2(1230, screen.get_height() / 2)
	ball_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
	layers = pygame.sprite.LayeredUpdates()
	layers.add(ball)
	layers.add(P1)
	layers.add(P2)
	Up_flag = False
	Down_flag = False
	START_TEXT = get_font(45).render("PRESS SPACEBAR TO START",True, "#ffffff")
	START_TEXT.set_alpha(255)
	SCOREBOARD = get_font(40).render("0 - 0",True,"#ffffff")
	started = False

	while running:
		# poll for events
		# pygame.QUIT event means the user clicked X to close your window

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				key = pygame.key.name(event.key)
				if key == "f":
					pygame.display.toggle_fullscreen()
			keys = pygame.key.get_pressed()
			if keys[pygame.K_w]:
				P1.pos.y -= 10
			if keys[pygame.K_s]:
				P1.pos.y += 10
			if keys[pygame.K_i]:
				P2.pos.y -= 10
			if keys[pygame.K_k]:
				P2.pos.y += 10
			if keys[pygame.K_SPACE]:
				ball_xspeed = 50 * dt
				ball_yspeed = 50 * dt
				START_TEXT.set_alpha(0)
				started = True


		if (ball_pos.y+20) > 720:
			if ball_yspeed > 0:
				ball_yspeed += 5 * dt
				ball_yspeed = -ball_yspeed
			else:
				ball_yspeed -= 5 * dt
				ball_yspeed = -ball_yspeed
		elif (ball_pos.y-20) < 0:
			if ball_yspeed > 0:
				ball_yspeed += 5 * dt
				ball_yspeed = -ball_yspeed
			else:
				ball_yspeed -= 5 * dt
				ball_yspeed = -ball_yspeed


		if pygame.sprite.spritecollide(ball, Players, False, pygame.sprite.collide_mask):
			if ball_pos.x+20 > P2.pos.x-16 or ball_pos.x-20 < P1.pos.x+16:
				passed = True
				ball_yspeed = -ball_yspeed
			else:
				passed = False
			if ball_xspeed > 0 and started and not passed:
				ball_xspeed = -ball_xspeed
				ball_xspeed -= 5 * dt
			elif ball_xspeed < 0 and started and not passed:
				ball_xspeed = -ball_xspeed
				ball_xspeed += 5 * dt


		if ball_pos.x > 1280 or ball_pos.x < 0:
			if ball_pos.x > 1280:
				P1_score += 1
			elif ball_pos.x < 0:
				P2_score += 1
			SCOREBOARD = get_font(40).render(str(P1_score)+" - "+str(P2_score),True,"#ffffff")
			ball_xspeed = 0 * dt
			ball_yspeed = 0 * dt
			P1.pos = pygame.Vector2(50, screen.get_height() / 2)
			P2.pos = pygame.Vector2(1230, screen.get_height() / 2)
			ball_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
			started = False
			START_TEXT.set_alpha(255)


		


		ball_pos.x += ball_xspeed
		ball_pos.y += ball_yspeed
		P1.PlayerUpdate(P1.pos.x,P1.pos.y)
		P2.PlayerUpdate(P2.pos.x,P2.pos.y)
		ball.BallUpdate(ball_pos.x,ball_pos.y)
		screen.fill("Black")
		screen.blit(mask_img,(ball_pos.x-20,ball_pos.y-20))

		layers.draw(screen)
		screen.blit(START_TEXT,(300,360))
		screen.blit(SCOREBOARD,(575,20))
		# fill the screen with background to wipe away anything from last frame
		pygame.display.flip()

Pong()