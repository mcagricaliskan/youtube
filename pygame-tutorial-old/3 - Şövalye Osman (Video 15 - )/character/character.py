import pygame
import json


class Character:
    def __init__(self):
        self.x = 200
        self.y = 700
        self.hp = 100
        self.gold = 0
        self.speed = 5
        self.status = "idle"
        self.sprite_path = "character/data/sprites/"
        self.direction = False
        self.action_mode = False
        self.animation_mode = False
        self.key = None
        self.mouse = None
        self.scale = (200, 148)
        self.save_dict = {}
        self.time = pygame.time.get_ticks()
        self.load()

        # idle
        self.idle_1 = pygame.image.load(self.sprite_path + "adventurer-idle-00.png").convert_alpha()
        self.idle_2 = pygame.image.load(self.sprite_path + "adventurer-idle-01.png").convert_alpha()
        self.idle_3 = pygame.image.load(self.sprite_path + "adventurer-idle-02.png").convert_alpha()
        self.idle_animation_counter = 0
        self.idle_1 = pygame.transform.scale(self.idle_1, self.scale)
        self.idle_2 = pygame.transform.scale(self.idle_2, self.scale)
        self.idle_3 = pygame.transform.scale(self.idle_3, self.scale)
        self.idle_delay = 250

        self.idle_list = [
            self.idle_1,
            self.idle_2,
            self.idle_3
        ]

        # idle with sword
        self.idle_sword_1 = pygame.image.load(self.sprite_path + "adventurer-idle-2-00.png").convert_alpha()
        self.idle_sword_2 = pygame.image.load(self.sprite_path + "adventurer-idle-2-01.png").convert_alpha()
        self.idle_sword_3 = pygame.image.load(self.sprite_path + "adventurer-idle-2-02.png").convert_alpha()
        self.idle_sword_4 = pygame.image.load(self.sprite_path + "adventurer-idle-2-03.png").convert_alpha()
        self.idle_sword_animation_counter = 0
        self.idle_sword_1 = pygame.transform.scale(self.idle_sword_1, self.scale)
        self.idle_sword_2 = pygame.transform.scale(self.idle_sword_2, self.scale)
        self.idle_sword_3 = pygame.transform.scale(self.idle_sword_3, self.scale)
        self.idle_sword_4 = pygame.transform.scale(self.idle_sword_4, self.scale)
        self.idle_sword_delay = 250

        self.idle_sword_list = [
            self.idle_sword_1,
            self.idle_sword_2,
            self.idle_sword_3,
            self.idle_sword_4
        ]

        # run
        self.run_1 = pygame.image.load(self.sprite_path + "adventurer-run-00.png")
        self.run_2 = pygame.image.load(self.sprite_path + "adventurer-run-01.png")
        self.run_3 = pygame.image.load(self.sprite_path + "adventurer-run-02.png")
        self.run_4 = pygame.image.load(self.sprite_path + "adventurer-run-03.png")
        self.run_5 = pygame.image.load(self.sprite_path + "adventurer-run-04.png")
        self.run_6 = pygame.image.load(self.sprite_path + "adventurer-run-05.png")
        self.run_animation_counter = 0
        self.run_1 = pygame.transform.scale(self.run_1, self.scale)
        self.run_2 = pygame.transform.scale(self.run_2, self.scale)
        self.run_3 = pygame.transform.scale(self.run_3, self.scale)
        self.run_4 = pygame.transform.scale(self.run_4, self.scale)
        self.run_5 = pygame.transform.scale(self.run_5, self.scale)
        self.run_6 = pygame.transform.scale(self.run_6, self.scale)
        self.run_delay = 250

        self.run_list = [
            self.run_1,
            self.run_2,
            self.run_3,
            self.run_4,
            self.run_5,
            self.run_6
        ]

        self.draw_sword_1 = pygame.image.load(self.sprite_path + "adventurer-swrd-drw-00.png").convert_alpha()
        self.draw_sword_2 = pygame.image.load(self.sprite_path + "adventurer-swrd-drw-01.png").convert_alpha()
        self.draw_sword_3 = pygame.image.load(self.sprite_path + "adventurer-swrd-drw-02.png").convert_alpha()
        self.draw_sword_4 = pygame.image.load(self.sprite_path + "adventurer-swrd-drw-03.png").convert_alpha()
        self.draw_sword_animation_counter = 0
        self.draw_sword_1 = pygame.transform.scale(self.draw_sword_1, self.scale)
        self.draw_sword_2 = pygame.transform.scale(self.draw_sword_2, self.scale)
        self.draw_sword_3 = pygame.transform.scale(self.draw_sword_3, self.scale)
        self.draw_sword_4 = pygame.transform.scale(self.draw_sword_4, self.scale)
        self.draw_sword_delay = 50

        self.draw_sword_list = [
            self.draw_sword_1,
            self.draw_sword_2,
            self.draw_sword_3,
            self.draw_sword_4,
        ]

        self.draw_sword_back_List = [
            self.draw_sword_4,
            self.draw_sword_3,
            self.draw_sword_2,
            self.draw_sword_1,
        ]

        self.attack_one_1 = pygame.image.load(self.sprite_path + "adventurer-attack1-00.png").convert_alpha()
        self.attack_one_2 = pygame.image.load(self.sprite_path + "adventurer-attack1-01.png").convert_alpha()
        self.attack_one_3 = pygame.image.load(self.sprite_path + "adventurer-attack1-02.png").convert_alpha()
        self.attack_one_4 = pygame.image.load(self.sprite_path + "adventurer-attack1-03.png").convert_alpha()
        self.attack_one_5 = pygame.image.load(self.sprite_path + "adventurer-attack1-04.png").convert_alpha()
        self.attack_one_animation_counter = 0
        self.attack_one_1 = pygame.transform.scale(self.attack_one_1, self.scale)
        self.attack_one_2 = pygame.transform.scale(self.attack_one_2, self.scale)
        self.attack_one_3 = pygame.transform.scale(self.attack_one_3, self.scale)
        self.attack_one_4 = pygame.transform.scale(self.attack_one_4, self.scale)
        self.attack_one_5 = pygame.transform.scale(self.attack_one_5, self.scale)
        self.attack_one_delay = 50

        self.attack_one_list = [
            self.attack_one_1,
            self.attack_one_2,
            self.attack_one_3,
            self.attack_one_4,
            self.attack_one_5
        ]

    def save(self):
        self.save_dict = {
            "Gold" : self.gold
        }

        json.dump(self.save_dict, open("character/player_data.txt", "w"))

    def load(self):

        self.save_dict = json.load(open("character/player_data.txt"))

        self.gold = self.save_dict["Gold"]

    def draw(self, window):

        if self.status == "idle":
            window.blit(pygame.transform.flip(self.idle_list[self.idle_animation_counter], self.direction, False),
                        (self.x, self.y))
        elif self.status == "idle_sword":
            window.blit(pygame.transform.flip(self.idle_sword_list[self.idle_sword_animation_counter], self.direction, False),
                        (self.x, self.y))
        elif self.status == "Run":
            window.blit(pygame.transform.flip(self.run_list[self.run_animation_counter], self.direction, False),
                        (self.x, self.y))
        elif self.status == "draw_sword":
            window.blit(pygame.transform.flip(self.draw_sword_list[self.draw_sword_animation_counter],
                                              self.direction, False), (self.x, self.y))
        elif self.status == "draw_sword_back":
            window.blit(pygame.transform.flip(self.draw_sword_back_List[self.draw_sword_animation_counter],
                                              self.direction, False), (self.x, self.y))
        elif self.status == "attack_one":
            window.blit(pygame.transform.flip(self.attack_one_list[self.attack_one_animation_counter],
                                              self.direction, False), (self.x, self.y))

        # pygame.draw.rect(window, (255, 0, 0), (self.x + 65, self.y + 25, 67, 120), 3)

    def animation(self, delay, animation_number, limit_of_the_animation, condition=False,
                  action_mode_end=False, status_mode_end="idle"):
        if pygame.time.get_ticks() - self.time > delay:
            animation_number += 1
            if animation_number == limit_of_the_animation:
                animation_number = 0

                if condition:
                    self.action_mode = action_mode_end
                    self.status = status_mode_end
                    self.animation_mode = False

            self.time = pygame.time.get_ticks()
        return animation_number

    def game_loop(self, key, mouse):

        self.key = key
        self.mouse = mouse

        if self.key[pygame.K_d]:
            self.status = "Run"
            self.direction = False
            self.x += self.speed
        elif self.key[pygame.K_a]:
            self.status = "Run"
            self.direction = True
            self.x -= self.speed

        elif self.key[pygame.K_j]:
            self.Character_Save_Files()

        elif self.key[pygame.K_r]:
            if not self.action_mode:
                self.status = "draw_sword"
                self.animation_mode = True
            elif self.action_mode:
                self.status = "draw_sword_back"
                self.animation_mode = True

        elif self.mouse[0] == 1:
            self.status = "attack_one"
            self.animation_mode = True

        else:
            if not self.animation_mode:
                if self.action_mode:
                    self.status = "idle_sword"
                else:
                    self.status = "idle"

        # Animation #########
        if not self.action_mode:
            if self.status == "idle":
                self.idle_animation_counter = self.animation(self.idle_delay,
                                                             self.idle_animation_counter, 3)

            elif self.status == "Run":
                self.run_animation_counter = self.animation(self.run_delay,
                                                            self.run_animation_counter, 6)

            elif self.status == "draw_sword":
                self.draw_sword_animation_counter = self.animation(self.draw_sword_delay,
                                                                   self.draw_sword_animation_counter,
                                                                   4, self.animation_mode, True, "idle_sword")

            elif self.status == "attack_one":
                self.attack_one_animation_counter = self.animation(self.attack_one_delay,
                                                                   self.attack_one_animation_counter,
                                                                   5, self.animation_mode, True, "idle_sword")

        elif self.action_mode:
            if self.status == "idle_sword":
                self.idle_sword_animation_counter = self.animation(self.idle_sword_delay,
                                                                   self.idle_sword_animation_counter,
                                                                   4)
            elif self.status == "Run":
                self.run_animation_counter = self.animation(self.run_delay,
                                                            self.run_animation_counter, 6)

            elif self.status == "draw_sword_back":
                self.draw_sword_animation_counter = self.animation(self.draw_sword_delay,
                                                                   self.draw_sword_animation_counter,
                                                                   4, self.animation_mode, False, "idle")

            elif self.status == "attack_one":
                self.attack_one_animation_counter = self.animation(self.attack_one_delay,
                                                                   self.attack_one_animation_counter,
                                                                   5, self.animation_mode, True, "idle_sword")

    def get_rect(self):
        return pygame.Rect(self.x + 65, self.y + 25, 67, 120)