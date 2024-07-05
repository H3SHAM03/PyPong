from Classes import *

#Colors
red = (255 , 0 , 0) # RED
green = (0, 255, 0) # GREEN
blue = (10, 60, 225) # BLUE
white = (255, 255, 255) # WHITE
black = (0, 0, 0) # BLACK
Colors = [red,green,blue,white,black]

def sine(speed: float, time: int, how_far: float, overall_y: int) -> int:
	t = pygame.time.get_ticks() / 2 % time
	y = math.sin(t / speed) * how_far + overall_y
	return int(y)

def get_font(size):
	return pygame.font.Font("assets\\Minecrafter.ttf",size)

def OpponentMovement(Player,Ball_pos,Player_speed,dt):
	if Player.pos.x > 720:
		b = 720
		coord = Ball_pos.x
	elif Player.pos.x < 720:
		b = Ball_pos.x
		coord = 720
	if Player.opponent:
		if b < coord:
			if Player.pos.y-15 > Ball_pos.y:
				if Player.pos.y-90 > 0:
					Player.pos.y -= Player_speed * dt
			elif Player.pos.y+15 < Ball_pos.y:
				if Player.pos.y+90 < 720:
					Player.pos.y += Player_speed * dt


def Pong():
	pygame.init()
	screen = pygame.display.set_mode((1280,720))
	clock = pygame.time.Clock()
	dt = clock.tick(240) / 1000
	# screen.fill((3, 0, 30))
	screen.fill("Black")
	running = True
	ball = Ball()
	ball.Resize(40,40)
	ball_mask = pygame.mask.from_surface(ball.image)
	mask_img = ball_mask.to_surface()
	passed = False
	surf = pygame.Surface((1280,720),pygame.SRCALPHA,32)
	surf.convert_alpha()
	startsurf = pygame.Surface((1280,720),pygame.SRCALPHA,32)
	startsurf.convert_alpha()
	scoresurf = pygame.Surface((1280,720),pygame.SRCALPHA,32)
	scoresurf.convert_alpha()
	settingssurf = pygame.Surface((1280,720),pygame.SRCALPHA,32)
	settingssurf.convert_alpha()


	P1 = Player(True)
	P2 = Player(True)
	P1_mask = pygame.mask.from_surface(P1.image)
	P2_mask = pygame.mask.from_surface(P2.image)
	P1_score = 0
	P2_score = 0
	AI_Speed = 200

	direction_x = random.choice([1,-1])
	direction_y = random.choice([-1,1])
	ball_xspeed = random.randint(100,200) * dt * direction_x
	ball_yspeed = random.randint(100,200) * dt * direction_y
	Players = pygame.sprite.Group()
	Players.add(P1)
	Players.add(P2)
	P1_speed = 0
	P2_speed = 0

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
	menu = 1
	sub_menu = 0
	players = 0
	START = Button(pygame.image.load("assets\\nothing.png"),(640,250),"START",get_font(70),"White","Green")
	START.update(surf)
	SETTINGS = Button(pygame.image.load("assets\\nothing.png"),(640,400),"SETTINGS",get_font(70),"White","Green")
	SETTINGS.update(surf)
	QUIT_BUTTON = Button(pygame.image.load("assets\\nothing.png"),(640,550),"QUIT",get_font(70),"White","Green")
	QUIT_BUTTON.update(surf)
	ONEPLAYER = Button(pygame.image.load("assets\\nothing.png"),(320,400),"1 Player",get_font(70),"White","Green")
	TWOPLAYERS = Button(pygame.image.load("assets\\nothing.png"),(960,400),"2 Players",get_font(70),"White","Green")
	ONEPLAYER.update(startsurf)
	TWOPLAYERS.update(startsurf)
	SCORE_TEXT = get_font(45).render("FIRST TO",True,"#ffffff")
	SCORE_TEXT.set_alpha(255)
	SEVEN = Button(pygame.image.load("assets\\nothing.png"),(960,400),"7",get_font(70),"White","Green")
	FIFTEEN = Button(pygame.image.load("assets\\nothing.png"),(960,400),"15",get_font(70),"White","Green")
	TWENTYONE = Button(pygame.image.load("assets\\nothing.png"),(960,400),"21",get_font(70),"White","Green")
	SEVEN.update(scoresurf)
	FIFTEEN.update(scoresurf)
	TWENTYONE.update(scoresurf)

	while running:
		# poll for events
		# pygame.QUIT event means the user clicked X to close your window

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_f:
					pygame.display.toggle_fullscreen()
				if menu == 0:
					if event.key == pygame.K_w:
						P1_speed -= 200
					elif event.key == pygame.K_s:
						P1_speed += 200
					if players == 2:
						if event.key == pygame.K_i:
							P2_speed -= 200
						elif event.key == pygame.K_k:
							P2_speed += 200
					if event.key == pygame.K_SPACE:
						direction_x = random.choice([1,-1])
						direction_y = random.choice([-1,1])
						ball_xspeed = random.randint(100,200) * dt * direction_x
						ball_yspeed = random.randint(100,200) * dt * direction_y
						START_TEXT.set_alpha(0)
						started = True
			elif event.type == pygame.KEYUP and menu == 0:
				if event.key == pygame.K_w:
					P1_speed += 200
				elif event.key == pygame.K_s:
					P1_speed -= 200
				if players == 2:
					if event.key == pygame.K_i:
						P2_speed += 200
					elif event.key == pygame.K_k:
						P2_speed -=200
			if event.type == pygame.MOUSEBUTTONDOWN:
				if START.checkForInput(pygame.mouse.get_pos()):
					menu = 0
					players = 0
				elif SETTINGS.checkForInput(pygame.mouse.get_pos()):
					pass
				elif QUIT_BUTTON.checkForInput(pygame.mouse.get_pos()):
					pass
				if ONEPLAYER.checkForInput(pygame.mouse.get_pos()):
					if menu == 0:
						P1.SetOpponent(False)
						P2.SetOpponent(True)
						players = 1
						P1_score = 0
						P2_score = 0
						ball_xspeed = 0
						ball_yspeed = 0
						ball_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
						SCOREBOARD = get_font(40).render(str(P1_score)+" - "+str(P2_score),True,"#ffffff")
				elif TWOPLAYERS.checkForInput(pygame.mouse.get_pos()):
					if menu == 0:
						P1.SetOpponent(False)
						P2.SetOpponent(False)
						players = 2
						P1_score = 0
						P2_score = 0
						ball_xspeed = 0
						ball_yspeed = 0
						ball_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
						SCOREBOARD = get_font(40).render(str(P1_score)+" - "+str(P2_score),True,"#ffffff")
				if SEVEN.checkForInput(pygame.mouse.get_pos()):
					pass
				elif FIFTEEN.checkForInput(pygame.mouse.get_pos()):
					pass
				elif TWENTYONE.checkForInput(pygame.mouse.get_pos()):
					pass
				
					
				
			# if keys[pygame.K_w]:
			# 	if P1.pos.y-90 > 0:
			# 		P1.pos.y -= 10
			# if keys[pygame.K_s]:
			# 	if P1.pos.y+90 < 720:
			# 		P1.pos.y += 10
			# if keys[pygame.K_i]:
			# 	if P2.pos.y-90 > 0:
			# 		P2.pos.y -= 10
			# if keys[pygame.K_k]:
			# 	if P2.pos.y+90 < 720:
			# 		P2.pos.y += 10


		if (ball_pos.y+20) > 720:
			if ball_yspeed > 0:
				ball_yspeed += 20 * dt
				ball_yspeed = -ball_yspeed
			else:
				ball_yspeed -= 20 * dt
				ball_yspeed = -ball_yspeed
		elif (ball_pos.y-20) < 0:
			if ball_yspeed > 0:
				ball_yspeed += 20 * dt
				ball_yspeed = -ball_yspeed
			else:
				ball_yspeed -= 20 * dt
				ball_yspeed = -ball_yspeed

		if pygame.sprite.spritecollide(ball, Players, False, pygame.sprite.collide_mask):
			if (ball_pos.x+19 >= P2.pos.x-15 or ball_pos.x-19 <= P1.pos.x+15) and not (ball_pos.y+19 < P1.pos.y+86 and ball_pos.y-19 > P1.pos.y-86):
				passed = True
				ball_yspeed = -ball_yspeed
			else:
				passed = False
			if ball_xspeed > 0 and (started or menu == 1) and not passed:
				ball_xspeed = -ball_xspeed
				ball_xspeed -= 20 * dt
			elif ball_xspeed < 0 and (started or menu == 1) and not passed:
				ball_xspeed = -ball_xspeed
				ball_xspeed += 20 * dt


		OpponentMovement(P1,ball_pos,AI_Speed,dt)
		OpponentMovement(P2,ball_pos,AI_Speed,dt)

		if ball_pos.x > 1280 or ball_pos.x < 0:
			if ball_pos.x > 1280:
				P1_score += 1
			elif ball_pos.x < 0:
				P2_score += 1
			SCOREBOARD = get_font(40).render(str(P1_score)+" - "+str(P2_score),True,"#ffffff")
			# ball_xspeed = random.randint(-200,200) * dt
			# ball_yspeed = random.randint(-200,200) * dt
			P1.pos = pygame.Vector2(50, screen.get_height() / 2)
			P2.pos = pygame.Vector2(1230, screen.get_height() / 2)
			ball_pos = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
			started = False
			if menu == 0:
				ball_xspeed = 0
				ball_yspeed = 0
			elif menu == 1:
				direction_x = random.choice([1,-1])
				direction_y = random.choice([-1,1])
				ball_xspeed = random.randint(100,200) * dt * direction_x
				ball_yspeed = random.randint(100,200) * dt * direction_y
			START_TEXT.set_alpha(255)

		
		if P1.pos.y+86+P1_speed*dt < 720 and P1.pos.y-86+P1_speed*dt > 0:
			P1.pos.y += P1_speed * dt

		if P2.pos.y+86+P2_speed*dt < 720 and P2.pos.y-86+P2_speed*dt > 0:
			P2.pos.y += P2_speed * dt

		if menu == 1:
			for button in [START,SETTINGS,QUIT_BUTTON]:
				mousePos = pygame.mouse.get_pos()
				button.changeColor(mousePos)
				button.update(surf)
		elif menu == 0 and players == 0:
			for button in [ONEPLAYER,TWOPLAYERS]:
				mousePos = pygame.mouse.get_pos()
				button.changeColor(mousePos)
				button.update(startsurf)

		ball_pos.x += ball_xspeed
		ball_pos.y += ball_yspeed
		P1.PlayerUpdate(P1.pos.x,P1.pos.y)
		P2.PlayerUpdate(P2.pos.x,P2.pos.y)
		ball.BallUpdate(ball_pos.x,ball_pos.y)
		screen.fill("Black")
		screen.blit(mask_img,(ball_pos.x-20,ball_pos.y-20))
		layers.draw(screen)
		if menu == 0 and players != 0:
			screen.blit(START_TEXT,(300,360))
		elif menu == 0 and players == 0:
			screen.blit(startsurf,(0,0))
		elif menu == 0 and (players == 1 or players == 2):
			screen.blit(scoresurf)
			screen.blit(SCORE_TEXT,(575,100))
		screen.blit(SCOREBOARD,(575,20))
		if menu == 1:
			screen.blit(surf,(0,0))
		# fill the screen with background to wipe away anything from last frame
		pygame.display.flip()

Pong()