# pip install keyboard

import keyboard
import time

i = 0

NUM_ROW_SPECIAL_CHAR = "!@#$%^&*()_+"


def map_by_keyboard(i: str) -> str:
    if i.isupper() or i in NUM_ROW_SPECIAL_CHAR:
        return f"shift+{i.lower()}"
    return i


def map_keys(value: str) -> list[str]:
    return [map_by_keyboard(i) for i in list(value)]


key_combination_n_values = {
    "alt+comma": map_keys("foo"), # Text you want to type when 'alt+comma' is hit
    "alt+.": map_keys("Bar01!"), # Text you want to type when 'alt+.' is hit
    "alt+/": 0, # 'alt+/' to exit the program
}

keyboard.press_and_release("alt+tab")
key_combinations = list(key_combination_n_values.keys())
while True:
    for key, value in key_combination_n_values.items():
        if keyboard.is_pressed(key):
            time.sleep(0.5)
            if value == 0:
                exit()
                break
            for character in value:
                keyboard.press_and_release(character)

