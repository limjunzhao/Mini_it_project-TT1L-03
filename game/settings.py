import pygame
pygame.init()


# game setup
WIDTH    = 1280	
HEIGHT   = 720
FPS      = 60
TILESIZE = 16

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128,128,128)
GREEN = (0, 255, 0)  # Green text for correct!
RED = (255, 0, 0)  # Red text for incorrect

FONT_SIZE = 35
clock = pygame.time.Clock()
speech_text = ""

#morse code minigame 
FONT_SIZE_GAME = 24
font_game = pygame.font.Font(None, FONT_SIZE_GAME)
font_large = pygame.font.Font(None, 50)  # Define the learning language font here
NOTES_WIDTH = 300
X_OFFSET_RIGHT = 160  # Adjust this value to control the right offset for letters T-Z

SEMI_TRANSPARENT_BLACK = (0, 0, 0, 128)

# Fonts dialogue
FONT = pygame.font.SysFont(None, 24)
FONT_NAME = pygame.font.SysFont(None, 30)
SPEECH_FONT = pygame.font.SysFont(None, 28)

# fonts jumblewords
font = pygame.font.Font(None, 36)
instruction_font = pygame.font.Font(None, 24)
score_font = pygame.font.Font(None, 24)

#fonts loveletter
cursive_font_path = 'images/loveletter/font/GreatVibes-Regular.ttf'  # Path to the cursive font file
love_letter_font = pygame.font.Font(cursive_font_path, 22)  # Load cursive font



#npc dino dialogue info
npc_data = {
    'Maria': {'who': "My name is Maria.",
                'where' : 'In the morning, I made breakfast for my husband, then proceeded to do house chores until afternoon. After lunch with my husband, I engaged in a pleasant chit-chat with out neighbor, Amber', 
                'what' : 'I eagerly awaited my husband’s return from work, and once he was back, we cooked dinner together and went to sleep afterwards.',
                "greeting":'',
                'img': 'sprites sheet for maps/sprites/characters/npc/maria/idle/0.png',
                "rawr": "raaawr rawr"
            }, 

    'Willie': {'who': "My name is Willie.",
                'where' : 'I started my day by having breakfast with my wife Maria, followed by me heading to work, I then head to lunch with my wife and returned to work.', 
                'what' : 'I came back home from work and got the ingredients ready and cooked dinner with my wife. After that, we went to bed before 10pm.',
                "greeting":'',
                'img': 'sprites sheet for maps/sprites/characters/npc/willie/idle/0.png',
                "rawr": "raaawr rawr"
            },
    
    'Amber': {'who': "My name is Amber.",
                'where' : 'In the day, I exercised in the park. And after that I had my coffee and breakfast. Meanwhile I watched TV for the time to pass. During lunch, I ate my leftover dinner from yesterday as my lunch. After lunch, me and Maria had our usual chit-chat but it was shorter than usual. And we were supposed to get groceries after that. So I went to buy the groceries myself and made dinner.', 
                'what' : 'As night falls, I took my dog for a night walk and went to bed.',
                "greeting":'',
                'img':'sprites sheet for maps/sprites/characters/npc/amber/idle/0.png',
                "rawr": "raaawr rawr"
            },
    
    
    'Officer': {'who': '',
                'where' : '', 
                'what' : '',
                "greeting": "Please help me find the killer before it's too late!",
                'img':'sprites sheet for maps/sprites/characters/npc/officer/idle/0.png',
                "rawr": "raaawr rawr"
            },
    'Alex': {'who': 'My name is Alex, just a normal maildino',
                'where' : 'I reached here 7.00 am morning and start my work instanly. Before that I am on the way from my office which is Dino City Centre', 
                'what' : 'I am here to send a mail to Mr Willie, here it is...',
                "greeting": 'Im here to give the letter to Mr Willie',
                'img' : 'sprites sheet for maps/sprites/characters/npc/alex/idle/0.png',
                "rawr": "raaawr rawr"
                
            },


    'Professor':{'who': '',
                'where' : '', 
                'what' : '',
                "greeting": 'Hello there dear treveller, would you likde to learn our language?',
                'img' : 'sprites sheet for maps/sprites/characters/npc/professor/idle/0.png'
                
            },
        
    
}

#npc dialogue question ask
npc_ques =  ' A. Where were you you yesterday? \n B. Who are you, whats your name? \n C. What did you do last night?'
prof_congrats = 'Congrats to you have graduate from Dino School'
detective_dialogue = 'I am here to investigate the incidents. Let me ask you a few question.'
rejected_dialogue = 'Fine, but I believe we will meet again soon..'

# Messages to display
messages = [
    {"text": "Dearest Willie,", "color": (0, 0, 0), "position": (380, 200)},
    {"text": "In your presence, my heart dances to a melody only you", "color": (0, 0, 0), "position": (380, 230)},
    {"text": "compose. Your laughter is the rhythm that sets my soul", "color": (0, 0, 0), "position": (380, 260)},
    {"text": "alight. With every glance, you paint the canvas of my world", "color": (0, 0, 0), "position": (380, 290)},
    {"text": "with hues of affection. I am but a poet entranced by your", "color": (0, 0, 0), "position": (380, 320)},
    {"text": "verses, lost in the depths of your gaze. In your arms, I find", "color": (0, 0, 0), "position": (380, 350)},
    {"text": "the solace of home, and in your love, I discover the true", "color": (0, 0, 0), "position": (380, 380)},
    {"text": "essence of belonging.", "color": (0, 0, 0), "position": (380, 410)},
    {"text": "Love sidechick,", "color": (0, 0, 0), "position": (380, 440)},
    {"text": "rawr", "color": (0, 0, 0), "position": (380, 470)},
]

# Words for the jumbled word game and their hints
word_hints = {
    "DETECTIVE": "Hint: Someone who solves crimes and investigates mysteries.",
    "LETTER": "Hint: A written thing commonly writing to someone.",
    "ARCADIA": "Hint: The name of the village where the murders took place.",
    "TRANQUILITY": "Hint: A peaceful and calm atmosphere.",
    "MURDER": "Hint: The person responsible for the grisly acts.",
    "GRISLY": "Hint: Something that is horrifying, gruesome.",
    "MYSTERY": "Hint: Something that is difficult or impossible to understand or explain.",
    "DAMPED": "Hint: Slightly wet, often unpleasantly so."

}

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
} 


ms_questions = [
          ("Translate 'HELLO' to Morse Code", ".... . .-.. .-.. ---"),
          ("Translate 'WORLD' to Morse Code", ".-- --- .-. .-.. -.."),
          ("Translate 'PYTHON' to Morse Code", ".--. -.-- - .... --- -."),
          ("Translate 'GAME' to Morse Code", "--. .- -- ."),
          ("Translate 'OPENAI' to Morse Code", "--- .--. . -. .- ..")
      ]

controls_font = pygame.font.Font(None, 40)

controls_info = [
    {"controls_text": "Press 'W' to walk up", "controls_color": (0, 0, 0), "controls_position": (420, 190)},
    {"controls_text": "Press 'S' to walk down", "controls_color": (0, 0, 0), "controls_position": (420, 270)},
    {"controls_text": "Press 'A' to walk left", "controls_color": (0, 0, 0), "controls_position": (420, 350)},
    {"controls_text": "Press 'D' to walk right", "controls_color": (0, 0, 0), "controls_position": (420, 430)},
    {"controls_text": "Press 'Left-Shift' to sprint", "controls_color": (0, 0, 0), "controls_position": (420, 500)},
    {"controls_text": "Player:", "controls_color": (0, 0, 0), "controls_position": (5, 135)},
]