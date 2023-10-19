try:
    from pynput import keyboard
    from winsound import Beep
except:
    import os;os.system("pip install pynput")
    from winsound import Beep



# Keyboard Listener 
def ks(): # Key sound
    Beep(1222,25)

def ks1(): # Key sound 
    Beep(2222,25)

def press(key):

    try:
        k = key.char
        print("Char Name:",k)
        ks()

    except:
        k = key.name
        print("Key Name:",k)
        ks1()


listener = keyboard.Listener(on_press=press)
listener.start()
listener.join()

