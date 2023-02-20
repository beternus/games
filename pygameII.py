 //como criar um jogo com python
 //criar um objeto, criar movimento
 
 import pygame
 pygame.init()
 
 janela = pygame.display.set_mode((800, 600))//tamanho da janela em pixels
 pygame.display.set_caption("Criando um jogo com Python")
 
 janela_aberta = True
 while_janela_aberta : 
 
 for event in pygame.event.get()
    if event.type == pygame.QUIT:
      janela_aberta = False
        
 pygame.draw.circle(janela, (0,255,0),(400,300),50) //azul e vermelho, azul  n tem nada, vermelho no maximo
 pygame.quit() //fecha a janela
  //criou a janela e ela nao é fechada mais
  
    
