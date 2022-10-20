import pygame
import sys
import copy
import random
import time

pygame.init()

width = 500
height = 500
scale = 10
score = 0

comida_x = 10
comida_y = 10

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da Cobrinha")
clock = pygame.time.Clock()

tela = (23, 32, 42)
cor_cobra = (247, 220, 111)
cor_comida = (0, 255, 0)
cabeca_cobra = (0, 0, 255)


class Cobra:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def reset(self):
        self.x = width / 2 - scale
        self.y = height / 2 - scale
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    # corpo da cobra
    def show(self):
        for i in range(self.length):
            if not i == 0:
                pygame.draw.rect(display, cor_cobra, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                pygame.draw.rect(display, cabeca_cobra, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):
        if abs(self.history[0][0] - comida_x) < scale and abs(self.history[0][1] - comida_y) < scale:
            return True

    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(
                    self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

    def autoplay(self):

        if abs(comida_x - self.history[0][0]) < 10 and abs(comida_y - self.history[0][1]) < 10:
            print("")
        elif abs(comida_x - self.history[0][0]) < 10:

            if self.x_dir == 1 or self.x_dir == -1:
                if comida_y > self.history[0][1]:
                    self.y_dir = 1
                else:
                    self.y_dir = -1
                self.x_dir = 0
        elif abs(comida_y - self.history[0][1]) < 10:

            if self.y_dir == 1 or self.y_dir == -1:
                self.y_dir = 0
                if comida_x > self.history[0][0]:
                    self.x_dir = 1
                else:
                    self.x_dir = -1


        elif comida_x - self.history[0][0] >= 10 and comida_y - self.history[0][1] >= 10:

            if self.x_dir == -1:
                self.y_dir = 1
                self.x_dir = 0
            elif self.y_dir == -1:
                self.y_dir = 0
                self.x_dir = 1
        elif self.history[0][0] - comida_x >= 10 and comida_y - self.history[0][1] >= 10:

            if self.x_dir == 1:
                self.y_dir = 1
                self.x_dir = 0
            elif self.y_dir == 1:
                self.y_dir = 0
                self.x_dir = -1
        elif self.history[0][0] - comida_x >= 10 and self.history[0][1] - comida_y >= 10:

            if self.x_dir == 1:
                self.y_dir = -1
                self.x_dir = 0
            elif self.y_dir == 1:
                self.y_dir = 0
                self.x_dir = -1

        elif comida_x - self.history[0][0] >= 10 and self.history[0][1] - comida_y >= 10:

            if self.x_dir == -1:
                self.y_dir = -1
                self.x_dir = 0
            elif self.y_dir == 1:
                self.y_dir = 0
                self.x_dir = 1

        self.update()


# ----------- Comida --------------
class Comida:
    def new_location(self):
        global comida_x, comida_y
        comida_x = random.randrange(1, width / scale - 1) * scale
        comida_y = random.randrange(1, height / scale - 1) * scale

    def show(self):
        pygame.draw.rect(display, cor_comida, (comida_x, comida_y, scale, scale))


def show_score():
    font = pygame.font.SysFont("Copperplate Gothic Bold", 20)
    text = font.render("Score: " + str(score), True, cor_cobra)
    display.blit(text, (scale, scale))


# ----------- Jogo Principal -------------
def gameLoop():
    loop = True

    global score

    cobra = Cobra(width / 2, height / 2)  #começando do meio
    comida = Comida()
    comida.new_location()
    ap = False

    while loop:

        display.fill(tela)
        cobra.show()
        comida.show()
        show_score()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:  #início da reprodução automática
                    ap = True
                if event.key == pygame.K_TAB:  #fim da reprodução automática
                    ap = False
                else:
                    if cobra.y_dir == 0:
                        if event.key == pygame.K_UP:
                            cobra.x_dir = 0
                            cobra.y_dir = -1
                        if event.key == pygame.K_DOWN:
                            cobra.x_dir = 0
                            cobra.y_dir = 1

                    if cobra.x_dir == 0:
                        if event.key == pygame.K_LEFT:
                            cobra.x_dir = -1
                            cobra.y_dir = 0
                        if event.key == pygame.K_RIGHT:
                            cobra.x_dir = 1
                            cobra.y_dir = 0

        if ap:
            cobra.autoplay()
        else:
            cobra.update()

        if cobra.check_eaten():
            comida.new_location()
            score += 1
            cobra.grow()

        if cobra.death():
            score = 0
            font = pygame.font.SysFont("Copperplate Gothic Bold", 50)
            text = font.render("Game Over!", True, cor_cobra)
            display.blit(text, (width / 2 - 50, height / 2))
            pygame.display.update()
            time.sleep(3)
            cobra.reset()

        # atualizar os valores se a cobra sair do jogo
        if cobra.history[0][0] > width:
            cobra.history[0][0] = 0
        if cobra.history[0][0] < 0:
            cobra.history[0][0] = width

        if cobra.history[0][1] > height:
            cobra.history[0][1] = 0
        if cobra.history[0][1] < 0:
            cobra.history[0][1] = height

        pygame.display.update()
        clock.tick(10)  #utilizado para controlar a velocidade da cobra


gameLoop()
