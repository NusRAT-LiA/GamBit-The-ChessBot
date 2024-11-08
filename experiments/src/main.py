import pygame
import sys

from const import *
from game import Game



class Main():

    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption("mini_chess_prottush")
        self.game = Game()


    def show_methods(self, screen):
        self.game.show_bg(screen)
        self.game.show_moves(screen)
        self.game.show_pieces(screen)   

    def mainloop(self):
        
        
        game = self.game
        screen = self.screen
        dragger = self.game.dragger
        board = self.game.board

        while True:
            self.show_methods(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    

                    clicked_row = dragger.mouseY//SQSIZE
                    clicked_col = dragger.mouseX//SQSIZE

                    #print(event.pos)
                    #print(clicked_row, clicked_col)
                    #print("***********************")

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece, clicked_row, clicked_col)

                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        self.show_methods(screen)

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        
                        dragger.update_mouse(event.pos)
                        self.show_methods(screen)
                        dragger.update_blit(screen)


                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    

        
            


main = Main()

main.mainloop()

