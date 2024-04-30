import pygame
pygame.init()


music_sfx = pygame.mixer.Sound("music_background.mp3")

vol = 0.01

music_sfx.play()
music_sfx.set_volume(vol)

def story_info(): 

    font =  pygame.font.Font('freesansbold.ttf', 24)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()
    messages = ['write game backstory and context here'
                '(click enter to see next page)',
                'this is another page',
                'blaaa bla bla heeee heeeeeee']
    snip = font.render('' , True, 'white')
    counter = 0 
    speed = 1
    active_message = 0
    message = messages[active_message]
    done = False

    run = True 
    while run:
        screen.fill('grey')
        timer.tick(60)
        # this is a box for the text, first two numbers are x y coordinate for the text, last two numbers are for the box sizes 
        pygame.draw.rect(screen, 'black', [0, 300, 800, 200])
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed*len(message):
            done = True 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message < len(messages) -1:
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0

            
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (10, 310))
        pygame.display.flip()

def main_menu():
    SCREEN_HEIGHT = 1280
    SCREEN_WIDTH = 720



    font =  pygame.font.Font('freesansbold.ttf', 50)
    screen = pygame.display.set_mode([800, 500])
    timer = pygame.time.Clock()
    message = 'game title !!!'
    snip = font.render('' , True, 'white')
    counter = 0 
    speed = 3
    done = False

    # Load images
    image = startstatic_img = pygame.image.load('start_static.png')
    image = starthover_img = pygame.image.load('start_hover.png')
    image = quitstatic_img = pygame.image.load('quit_static.png')
    image = quithover_img = pygame.image.load('quit_hover.png')
    optionhover_img = pygame.image.load('opt_hover.png')
    optionstatic_img = pygame.image.load('opt_static.png')
    # background_image = pygame.image.load('background43.jpg')
    # background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))


    image_rect = image.get_rect()
    image_x = (SCREEN_HEIGHT - image_rect.width) // 2

    # x = SCREEN_HEIGHT
    # y = SCREEN_WIDTH

    # Main screen
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption('platform game')

    # load music
    button_sfx = pygame.mixer.Sound("button_sfx.mp3")
    

   
    
    # Class for button
    class Button():
        def __init__(self, x, y, static_image, hover_image, scale):
            self.static_image = pygame.transform.scale(static_image, scale)
            self.hover_image = pygame.transform.scale(hover_image, scale)
            self.image = self.static_image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                self.image = self.hover_image
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            else:
                self.image = self.static_image
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action
    
            

    start_button = Button(image_x, 400, startstatic_img, starthover_img, (200, 100))
    quit_button = Button(image_x, 500, quitstatic_img, quithover_img, (200, 100))
    option_button = Button(10, 10, optionstatic_img, optionhover_img, (75, 75))


    run = True
    while run:
        screen.fill('grey')
        # screen.blit(background_image, (0,0))



        
        timer.tick(60)
        pygame.draw.rect(screen, 'black', [500, 50, 350, 150 ])
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (510, 100))
        

        if start_button.draw():
            button_sfx.play()
            story_info()
          

        if quit_button.draw():
            button_sfx.play()
            run = False

        if option_button.draw():
            button_sfx.play()
            option()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

def option():
    SCREEN_HEIGHT = 1280
    SCREEN_WIDTH = 720



    # Load images
    image = volup_static = pygame.image.load('vol_up.png')
    image = volup_hover = pygame.image.load('vol_up-hover.png')
    image = voldown_static = pygame.image.load('vol_down-static.png')
    image = voldown_hover = pygame.image.load('vol_down-hover.png')
    image = volmute_static = pygame.image.load('vol_mute-static.png')
    image = volmute_hover = pygame.image.load('vol_mute-hover.png')
    # background_image = pygame.image.load('background43.jpg')
    # background_image = pygame.transform.scale(background_image, (SCREEN_HEIGHT, SCREEN_WIDTH))


    image_rect = image.get_rect()
    image_x = (SCREEN_HEIGHT - image_rect.width) // 2


    # Main screen
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption('platform game')

    # load music
    button_sfx = pygame.mixer.Sound("button_sfx.mp3")
    

   
    
    # Class for button
    class Button():
        def __init__(self, x, y, static_image, hover_image, scale):
            self.static_image = pygame.transform.scale(static_image, scale)
            self.hover_image = pygame.transform.scale(hover_image, scale)
            self.image = self.static_image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self):
            action = False
            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                self.image = self.hover_image
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            else:
                self.image = self.static_image
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            screen.blit(self.image, (self.rect.x, self.rect.y))

            return action
    
            

    vol_up_button = Button(image_x, 400, volup_static, volup_hover, (200, 100))
    vol_down_button = Button(image_x, 500, voldown_hover, voldown_static, (200, 100))
    vol_mute_button = Button(10, 10, volmute_static, volmute_hover, (75, 75))


    run = True
    while run:
        screen.fill('grey')
        # screen.blit(background_image, (0,0))


        if vol_up_button.draw():
            button_sfx.play()
            vol = vol + 0.1
  

        # if vol_down_button.draw():


        # if vol_mute_button.draw():


        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False

        pygame.display.update()





main_menu()
