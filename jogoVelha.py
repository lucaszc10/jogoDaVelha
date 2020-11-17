import pygame


# Tabuleiro, dicionário que registra os movimentos/
# Board, dict that registrate the moves

theBoard = {'a1': '', 'a2': '', 'a3' : '', 'b1': '', 'b2': '', 'b3': '', 'c1': '', 'c2': '', 'c3' : ''}

# Variáveis do tabuleiro / board and position variables									
a1x = False; a1o = False; a2x = False; a2o = False; a3x = False; a3o = False
b1x = False; b1o = False; b2x = False; b2o = False; b3x = False; b3o = False
c1x = False; c1o = False; c2x = False; c2o = False; c3x = False; c3o = False

# Escolha do objeto
X_choose = False
O_choose = False


class Game():

	def __init__(self, player):
		global a1x, a1o, a2x, a2o, a3x, a3o, b1x, b1o, b2x, b2o, b3x, b3o, c1x, c2o, c2x, c2o, c3x, c3o

                # Variáveis inicias, de imagens e de telas / Init variables, images and screen variables.
		self.player = player
		pygame.init()
		self.game_img = pygame.image.load("icon.png")
		pygame.display.set_caption("Jogo da Velha")
		pygame.display.set_icon(self.game_img)
		self.size = (398, 278)
		self.height = 278
		self.width = 398
		self.screen = pygame.display.set_mode(self.size)
		self.board = pygame.image.load("board.png")
		self.X = pygame.image.load("x_resize.png")
		self.O = pygame.image.load("o_resize.png")
		self.white = 255, 255, 255
		self.font = pygame.font.SysFont("comicsans", 62)
		

	def run_menu(self):
                # Abrir menu inical / Run Main Menu method
		global input1, input2, X_choose, O_choose
		run = True
		self.input1 = ''
		self.choose = ''
		font2 = pygame.font.SysFont("comicsans", 32)
		while run:
			self.white = (255, 255, 255)
			self.screen.fill(self.white)
			self.p_text = font2.render(self.player, True, (0, 0, 0))
			self.text_input = font2.render('Digite seu nome: ', True, (18, 10 ,143))
			self.screen.blit(self.text_input, (20, 60))
			self.screen.blit(self.p_text, (self.width / 2 - 40, 10))
			self.obj_text = font2.render('Objeto:', True, (18, 10, 143))
			self.screen.blit(self.obj_text, (self.width / 2 - 40, 120))
			mousep = pygame.mouse.get_pos()
			self.print_input = font2.render(self.input1, True, (255, 35 ,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if 75 <= mousep[0] <= self.X.get_width() + 75 and 170 <= mousep[1] <= self.O.get_height() + 170: # Click on X
						X_choose = True
						self.choose = 'X'
						run = False
					if self.width - 75 - self.O.get_width() <= mousep[0] <= (self.width - 75 - self.O.get_width()) + self.O.get_width() and 170 <= mousep[1] <= self.O.get_height() + 170: # click on O
						O_choose = True
						self.choose = 'O'
						run = False
				if event.type == pygame.KEYDOWN:
					#  Digitação na tela / For typing on screen:
					if event.key == pygame.K_BACKSPACE:
						self.input1 = self.input1[:-1]
						
					elif event.key == pygame.K_RETURN:
						pass
					elif event.key == pygame.K_SPACE:
						pass
					else:
						if len(self.input1) <= 14:
							self.char = event.unicode
							self.input1 = self.input1 + str(self.char)
							
			self.screen.blit(self.print_input, (self.text_input.get_width() + 23, 60))
			if not X_choose:
				self.screen.blit(self.X, (75, 170))
			if not O_choose:
				self.screen.blit(self.O, (self.width - 75 - self.O.get_width(), 170))
			pygame.display.update()
		self.player = self.input1
		




	def run_main_app(self):
                # Método que inica a aplicação e é responsável por roda-la / Init game and Menu methods
		global run_game
		run = True
		run_game = False
		p1.run_menu()
		p2.run_menu()
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					run_game = False
			run_game = True
			
			p1.run_game()
			run_game = True
			p2.run_game()



	def run_game(self):
                # Método do jogo Run Game method
		global run_game
		
		while run_game:
			self.screen.blit(self.board, (0, 0))
			mouse = pygame.mouse.get_pos()
			self.board_draw()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					
					pygame.quit()
			
                                # Se o clique do mouse for nessa posição, chame o método para escrever o objeto no dicionário
                                # If click is in the right position, it calls the postion method to write the object in the dict.
				if event.type == pygame.MOUSEBUTTONDOWN:
					if 25 <= mouse[0] <= (self.width/3 + 10) and 15 <= mouse[1] <= (self.height/3):
						if theBoard['a1'] == '':
							self.writePosition('a1')
					if 147 <= mouse[0] <= ((self.width/3) * 2 + 10) and 15 <= mouse[1] <= (self.height/3):
						if theBoard['a2'] == '':
							self.writePosition('a2')	
					if 280 <= mouse[0] <= (self.width - 10) and 15 <= mouse[1] <= (self.height/3):
						if a3x == False and a3o == False:
							self.writePosition('a3')
					
					if 25 <= mouse[0] <= (self.width/3 + 10) and (self.height/3 + 20) <= mouse[1] <= ((self.height/3) * 2 - 20):
						if b1x == False and b1o == False:
							self.writePosition('b1')
					if 147 <= mouse[0] <= ((self.width/3) * 2 -10) and (self.height/3+ 20) <= mouse[1] <= ((self.height/3) * 2 -20):
						if b2x == False and b2o == False:
							self.writePosition('b2')
					if 280 <= mouse[0] <= (self.width - 10) and (self.height/ 3 + 20) <= mouse[1] <= ((self.height/3) * 2 - 20):
						if b3x == False and b3o == False: 
							self.writePosition('b3')
					
					if 25 <=  mouse[0] <= (self.width/3 + 10) and (self.height/3 * 2) <=  mouse[1] <= (self.height - 10):
						if c1x == False and c1o == False: 
							self.writePosition('c1')
					if 147 <= mouse[0] <= ((self.width/3) * 2 - 10) and ((self.height/3)  * 2) <= mouse[1] <= (self.height -10):
						if c2x == False and c2o == False:
							self.writePosition('c2')
					if 280 <= mouse[0] <= (self.width -10) and ((self.height/3) * 2 ) <= mouse[1] <= (self.height - 10):
						if c3x == False and c3o == False:
							self.writePosition('c3')




                        # Preview da jogada, desenha ao passar o mouse em cima da posição
                        # Previes of the move, draws when holding the mouse in the position
			if 25 <= mouse[0] <= (self.width/3 + 10) and 15 <= mouse[1] <= (self.height/3 - 10 ):
				if a1x == False and a1o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (70, 10))
							
					else:
						self.screen.blit(self.O, (70, 10)) 

			if 147 <= mouse[0] <= ((self.width/3) * 2 - 10) and 15 <= mouse[1] <= (self.height/3):
				if a2x == False and a2o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (175, 10))
					else:
						self.screen.blit(self.O, (175, 10))

			if 280 <= mouse[0] <= (self.width - 10) and 15 <= mouse[1] <= (self.height/3):
				if a3x == False and a3o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (285, 10))
					else:
						self.screen.blit(self.O, (285, 10))

			if 25 <= mouse[0] <= (self.width/3 + 10) and (self.height/3 + 20) <= mouse[1] <= ((self.height/3) * 2 - 20):
				if b1x == False and b1o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (70, 100))
					else:
						self.screen.blit(self.O, (70, 100))

			if 147 <= mouse[0] <= ((self.width/3) * 2 -10) and (self.height/3+ 20) <= mouse[1] <= ((self.height/3) * 2 -20):
				if b2x == False and b2o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (175, 100))
					else:
						self.screen.blit(self.O, (175, 100))

			if 280 <= mouse[0] <= (self.width - 10) and (self.height/ 3 + 20) <= mouse[1] <= ((self.height/3) * 2 - 20):
				if b3x == False and b3o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (285, 100))
					else:
						self.screen.blit(self.O, (285, 100))

			if 25 <=  mouse[0] <= (self.width/3 + 10) and (self.height/3 * 2) <=  mouse[1] <= (self.height - 10):
				if c1x == False and c1o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (70, 190))
					else:
						self.screen.blit(self.O, (70, 190))
			
			if 147 <= mouse[0] <= ((self.width/3) * 2 - 10) and ((self.height/3)  * 2) <= mouse[1] <= (self.height -10):
				if c2x == False and c2o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (175, 190))
					else:
						self.screen.blit(self.O, (175, 190))

			if 280 <= mouse[0] <= (self.width -10) and ((self.height/3) * 2 ) <= mouse[1] <= (self.height - 10):
				if c3x == False and c3o == False:
					if self.choose == 'X':
						self.screen.blit(self.X, (285, 190))
					else:
						self.screen.blit(self.O, (285, 190))



			self.winner()
			
			
			
			pygame.display.update()




				
	def board_draw(self):
		# Desenha a imagem na tela, chamado sempre no inicio do método run_game, imagem contínua.
		# Draws the image on screen, called in the beggining of the run_game method, continuous images.
		global a1x, a1o, a2x, a2o 
		if a1x == True:
			self.screen.blit(self.X, (70, 10))
		if a1o == True:
			self.screen.blit(self.O, (70, 10))
		if a2x == True:
			self.screen.blit(self.X, (175, 10))
		if a2o == True: 
			self.screen.blit(self.O, (175, 10))
		if a3x == True:
			self.screen.blit(self.X, (285, 10))
		if a3o == True:
			self.screen.blit(self.O, (285, 10))
		if b1x == True:
			self.screen.blit(self.X, (70, 100))
		if b1o == True:
			self.screen.blit(self.O, (70, 100))
		if b2x == True:
			self.screen.blit(self.X, (175, 100))
		if b2o == True:
			self.screen.blit(self.O, (175, 100))
		if b3x == True:
			self.screen.blit(self.X, (285, 100))
		if b3o == True:
			self.screen.blit(self.O, (285, 100))
		if c1x == True:
			self.screen.blit(self.X, (70, 190))
		if c1o == True:
			self.screen.blit(self.O, (70, 190))
		if c2x == True:
			self.screen.blit(self.X, (175, 190))
		if c2o == True:
			self.screen.blit(self.O, (175, 190))
		if c3x == True:
			self.screen.blit(self.X, (285, 190))
		if c3o == True:
			self.screen.blit(self.O, (285, 190))	
				


	def writePosition(self, position):
                # Escreve o objeto e a posição no dicionário, recebe a posição na própria função chamada.
                # Writes the object in the position of the dict, receives the position in the function.
		global a1o, a1x, a2x, a2o, a3x, a3o, b1x, b1o, b2x, b2o, b3x, b3o, c1x, c1o, c2x, c2o, c3x, c3o, run_game
		if position == 'a1':
			if self.choose == 'X':
				a1x = True
				theBoard[position] = 'X'
				print('Object drawed')
				run_game = False
			
			else:
				a1o = True
				theBoard[position] = 'O'
				print('Object drawed')
				print(theBoard)
				run_game = False
				
		if position == 'a2':
			if self.choose == 'X':
				a2x = True
				theBoard[position] = 'X'
				print('Object drawed')
				run_game = False
					
			else:
				a2o = True
				theBoard[position] = 'O'
				print('Object drawed')
				run_game = False
		
		if position == 'a3':
			if self.choose == 'X':
				a3x = True
				theBoard[position] = 'X'
				run_game = False
			else:
				a3o = True
				theBoard[position] = 'O'
				run_game = False
		
		if position == 'b1':
			if self.choose == 'X':
				b1x = True
				theBoard[position] = 'X'
				run_game = False
			else:
				b1o = True
				theBoard[position] = 'O'
				run_game = False

		if position == 'b2':
			if self.choose == 'X':
				b2x = True
				theBoard[position] = 'X'
				run_game = False
			else:
				b2o = True
				theBoard[position] = 'O'
				run_game = False

		if position == 'b3':
			if self.choose == 'X':
				b3x = True
				theBoard[position] = 'X'
				run_game = False
			else:
				b3o = True
				theBoard[position] = 'O'
				run_game = False	

		if position == 'c1':
			if self.choose == 'X':
				c1x = True
				theBoard[position] = 'X'
				run_game = False
			else:
				c1o = True
				theBoard[position] = 'O'
				run_game = False	

		if position == 'c2':
			if self.choose == 'X':
				c2x = True
				theBoard[position] = 'X'
				run_game = False
			else:
				c2o = True
				theBoard[position] = 'O'
				run_game = False

		if position == 'c3':
			if self.choose == 'X':
				c3x = True
				theBoard[position] = 'X'
				run_game = False
			else:
				c3o = True
				theBoard[position] = 'O'
				run_game = False		


	



	def winner(self):
                # Checa se há algum vencedor ou empate, analisa o dicionário e cria uma imagem na tela.
                # Check if there is an winner or a tie, analises the dict and draws an image on the screen.
		values = 0 # Variável para o empate validar / tie variable to validate the tie. 
		if theBoard['a1'] == 'X' and theBoard['a2'] == 'X' and theBoard['a3'] == 'X':
			if self.p1.choose == 'X':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
		
		elif theBoard['a1'] == 'O' and theBoard['a2'] == 'O' and theBoard['a3'] == 'O':
			if p1.choose == 'O':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a1'] == 'X' and theBoard['b1'] == 'X' and theBoard['c1'] == 'X':
			if p1.choose == 'X':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a1'] == 'O' and theBoard['b1'] == 'O' and theBoard['c1'] == 'O':
			if p1.choose == 'O':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a2'] == 'X' and theBoard['b2'] == 'X' and theBoard['c2'] == 'X':
			if p1.choose == 'X':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a2'] == 'O' and theBoard['b2'] == 'O' and theBoard['c2'] == 'O':
			if p1.choose == 'O':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a3'] == 'X' and theBoard['b3'] == 'X' and theBoard['c3'] == 'X':
			if p1.choose == 'X':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a3'] == 'O' and theBoard['b3'] == 'O' and theBoard['c3'] == 'O':
			if p1.choose == 'O':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['b1'] == 'X' and theBoard['b2'] == 'X' and theBoard['b3'] == 'X':
			if p1.choose == 'X':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['b1'] == 'O' and theBoard['b2'] == 'O' and theBoard['b3'] == 'O':
			if p1.choose == 'O':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['c1'] == 'X' and theBoard['c2'] == 'X' and theBoard['c3'] == 'X':
			if p1.choose == 'X':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['c1'] == 'O' and theBoard['c2'] == 'O' and theBoard['c3'] == 'O':
			if p1.choose == 'O':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a1'] == 'X' and theBoard['b2'] == 'X' and theBoard['c3'] == 'X':
			if p1.choose == 'X':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a1'] == 'O' and theBoard['b2'] == 'O' and theBoard['c3'] == 'O':
			if p1.choose == 'O':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a3'] == 'X' and theBoard['b2'] == 'X' and theBoard['c1'] == 'X':
			if p1.choose == 'X':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		elif theBoard['a3'] == 'O' and theBoard['b2'] == 'O' and theBoard['c3'] == 'O':
			if p1.choose == 'O':
				print('{} ganhou!'.format(p1.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()
			else:
				print('{} ganhou!'.format(p2.player))
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('{} ganhou!'.format(self.player), True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

		for k, v in theBoard.items():
			if v != '':
				values += 1
			if values == 9:
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								pygame.quit()
					self.screen.fill((255, 255, 255))
					text = self.font.render('Deu velha!', True, (18, 10 ,143 ))
					self.screen.blit(text, (199 - text.get_width() // 2, 139 - text.get_height() // 2))
					pygame.display.update()

			

p1 = Game('Player 1')
p2 = Game('Player 2')
p1.run_main_app()
