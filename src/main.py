from pyray import *

width = get_screen_width()
height = get_screen_height()

init_window(width, height, "ホロウ")

while not window_should_close():
    begin_drawing()
    clear_background((26, 27, 38))

    width = get_screen_width()
    height = get_screen_height()
    
    rech = int(height) 
    w = int (width * 0.2) 

    draw_rectangle(-5, -2, w, rech+4, (22, 22, 30,255)) 

    draw_rectangle_lines(-5, -2, w, rech+4, (8,194, 148,255))  

    

    end_drawing()

close_window()
