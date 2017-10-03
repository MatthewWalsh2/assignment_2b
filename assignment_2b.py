# created by: Matthew Walsh
# created for: ICS3U
# created on oct 2017
# this program calculates distance an object has fallen
import ui

def calculation_button(sender):
    # constants
    g = 9.81
    cliff_height = 100
    
    #input
    time = float(view['time_textfield'].text)
    
    #process
    #insuring program follows BEDMAS
    time_squared = time * time
    distance_fallen = 0.5 * g * time_squared
    height = cliff_height - distance_fallen
    if height < 0: height = 0
    view['answer_label'].text = 'The object will be ' + str(height) + ' metres high'
view = ui.load_view()
view.present('full_screen')
