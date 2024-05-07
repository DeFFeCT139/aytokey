import keyboard

def on_ctrl_alt_x_press():
        print('Программа завершена')

def on_ctrl_alt_z_press():
        print('Программа завершена 1')

keyboard.add_hotkey('ctrl+alt+x', on_ctrl_alt_x_press)

keyboard.add_hotkey('ctrl+alt+z', on_ctrl_alt_z_press)


keyboard.wait()