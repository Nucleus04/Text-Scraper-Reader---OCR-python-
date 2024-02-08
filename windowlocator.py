import pywinauto

def detect_notepad_changes():
# title_re='Calculator'
#  class_name="Notepad"

    notepad_app = pywinauto.Application().connect(title_re='Calculator')
    notepad_window = notepad_app.top_window()
    rect = notepad_window.rectangle()
    print(rect)
    # Unpack the values from the RECT object
    left = rect.left
    top = rect.top
    right = rect.right
    bottom = rect.bottom

    # Return the values if needed
    return left, top, right, bottom