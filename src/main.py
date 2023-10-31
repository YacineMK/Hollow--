from pyray import *
import os

os.system("clear")

file_path = str(input("Path to the file: "))


def read(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print("File not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

def wrap_text(text, width):
    lines = []
    words = text.split()
    current_line = ""
    for word in words:
        if measure_text(current_line + " " + word, font_size) < width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return "\n".join(lines)

width = 800
height = 500

init_window(width, height, "ホロウ")

font_size = 20
font = load_font("../config/assets/Poppins.ttf", font_size)

while not window_should_close():
    begin_drawing()
    clear_background((26, 27, 38))
    
    file_contents = read(file_path)
    text = wrap_text(file_contents, width - 10)  # Subtracting some padding
    text_width = measure_text(text, font_size)

    width = 800
    height = 500    

    text_x = 14
    text_y = 15

    draw_text(text, text_x, text_y, font_size, (240, 240, 240, 200))

    end_drawing()

close_window()
