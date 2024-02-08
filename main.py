import windowlocator
import scraper
import speaker
from overlay import Overlay
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
import sys

# Get the size of the target application
left, top,right,  bottom = windowlocator.detect_notepad_changes()
width = right - left
height = bottom - top

# Get the text from the application using OCR
scrape_datas = scraper.scrape_text(left, top, right, bottom)

# Start the GUI overlay
app = QApplication(sys.argv)
overlay = Overlay(left, top, width, height)

# Function the will update the highlight while speaking
global previous_text
previous_text = ''
global loop_counter
loop_counter = 0
global num_scrape_data
num_scrape_data = len(scrape_datas)
def display(overlay):
    timer = QTimer()
    timer.setInterval(1)

    scrape_data_iterator = iter(scrape_datas)
    
    def process_next_scrape_data():
        global previous_text
        global loop_counter
        global num_scrape_data
        try:
            scrape_data = next(scrape_data_iterator)
            bounding_box, text, confidence = scrape_data
            x1, y1, x2, y2 = bounding_box
            x = min(x1[0], x2[0])
            y = min(y1[1], y2[1])
            width = abs(x1[0] - x2[0])
            height = abs(y1[1] - y2[1])
            print("text: ", text)
            print("x:", x)
            print("y:", y)
            print("width:", width)
            print("height:", height)
            print("\n")
            overlay.draw_rectangle(x, y, width, height)

            if(previous_text == ''):
                print("No previous text")
            else:
                speaker.speak(previous_text)
            
            previous_text = text
            # speaker.speak(text)
            if loop_counter == num_scrape_data - 1:
                speaker.speak(text)
            loop_counter += 1
            timer.start()
        except StopIteration:
            timer.stop()
            sys.exit()

    timer.timeout.connect(process_next_scrape_data)
    timer.start()
    

display(overlay)

sys.exit(app.exec_())

