#music_lyrics_printing
import time
import sys
def print_lyrics():
    lyrics=[
        "Bandeya rey bandeya \nRaah pe chal bandeya",
        "Ruk jaa re bandeya.. \nYeh raat zara si hai..",
        "Baat samajh bandeya.. \nKuch der hi baaqi hai..",
        "Rakh yaqeen, aankhon se baadal.. \nAaj hat jayega",
        "Chand teri aankhon mein bandeya.. \nChal ke aayega",
        "Tanak tanu ta naanu.. \nTandanunum ta naanu…"
    ]
    delays=[1.0,0.1,1.12,0.9,0.8,1.0]
    print("Bandeya rey bandeya :\n")
    time.sleep(2.0) #pause for 2.0 second
    for i,line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char) # does add new line
            sys.stdout.flush() # give instant output 
            time.sleep(0.1) # create typing effect
        print()
        time.sleep(delays[i])  # pause after each line

print_lyrics()
    
