from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage, filedialog
import threading

from assets.script import screen 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")
path = None
thread = None


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def center_cursor(event,widget):
    initial_text = "\n"+" " * (widget.winfo_width() // 25)
    widget.delete(1.0, "end")
    widget.insert("1.0", initial_text)

def get_path():
    global path
    
    folder_path = filedialog.askdirectory()
    if folder_path:  
        path = folder_path
        path_components = path.split("/")
        canvas.itemconfig(text_path, text="PATH:\n.../"+f"{path_components[len(path_components)-2]}/{path_components[len(path_components)-1]}")
        canvas.coords(text_path, 592.0, 247.0) 
        canvas.coords(text_path, 592.0-100, 247.0)   
        
def start_thread():
    global thread
    thread = threading.Thread(
        target=screen.run,
        args=(
            int(text_widget.get("1.0", "end-1c").strip()),
            path
        )
    ).start()
    print(thread)
    

def on_closing():
    global window
    window.destroy()
    screen.terminate_thread = True

window = Tk()

window.geometry("800x600")
window.configure(bg = "#1A1B26")
window.title("screen time")
window.iconbitmap("assets/img/screen icon.ico")
window.resizable(False,False)
window.protocol("WM_DELETE_WINDOW", on_closing)


canvas = Canvas(
    window,
    bg = "#1A1B26",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    100.0,
    fill="#16161E",
    outline="")

canvas.create_text(
    270.0,
    36.0,
    anchor="nw",
    text="Automated Screenshot",
    fill="#A77FD6",
    font=("Inter", 26 * -1)
)

text_area = PhotoImage(
    file=relative_to_assets("entry_1.png")
)

entry_bg_1 = canvas.create_image(
    174.5,
    335.5,
    image=text_area
)

text_widget = Text(
    bd=0,
    bg="#182531",
    fg="#c0caf5",
    highlightthickness=0
)

text_widget.bind(
    "<FocusIn>"
    , lambda event, widget=text_widget: center_cursor(event, widget)
)

text_widget.place(
    x=52.0,
    y=300.0,
    width=245.0,
    height=69.0
)

canvas.create_text(
    113.0,
    247.0,
    anchor="nw",
    text="SECONDS:",
    fill="#7AA2F7",
    font=("Inter", 24 * -1)
)

image_start = PhotoImage(
    file=relative_to_assets("button_1.png")
)

button_run = Button(
    image=image_start,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_thread(),
    relief="flat"
)
button_run.place(
    x=270.0,
    y=423.0,
    width=261.0,
    height=66.0
)

image_explorer = PhotoImage(
    file=relative_to_assets("button_2.png")
)

button_explorer= Button(
    image=image_explorer,
    borderwidth=0,
    highlightthickness=0,
    command=get_path,
    relief="flat"
)

button_explorer.place(
    x=491.0,
    y=300.0,
    width=268.0,
    height=71.0
)

text_path = canvas.create_text(
    592.0,
    247.0,
    anchor="nw",
    text="PATH:",
    fill="#7AA2F7",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    0.0,
    542.0,
    800.0,
    600.0,
    fill="#16161E",
    outline=""
)

canvas.create_text(
    70.0,
    563.0,
    anchor="nw",
    text="made by: t.me/d3enny04",
    fill="#A77FD6",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    526.0,
    563.0,
    anchor="nw",
    text="theme ispired by: Tokyo Night Theme",
    fill="#A77FD6",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    65.0,
    130.0,
    anchor="nw",
    text="this script allows you to choose how often your PC will take a\nscreenshot, it will do it automatically and save it in the folder you\nchose",
    fill="#57A0BF",
    font=("Inter", 24 * -1),
    justify="center"
)
window.resizable(False, False)
window.mainloop()
