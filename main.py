import customtkinter
from tkinter import filedialog
import importlib
from customtkinter import CTkButton, CTkImage
from tkinter import PhotoImage
from PIL import Image, ImageDraw, ImageTk
from tkinter import Tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue") 

app = customtkinter.CTk()
app.geometry("600x500")
app.title(" ")

def run():
    global entry_result, completion_label 

    dir = str(entry_1.get())
    module_name = "test"
    function_name = "runtest"
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)

    result = function(dir)

    completion_label = customtkinter.CTkLabel(master=app, text="Completion: 100%")
    completion_label.pack(pady=(40, 5), padx=5)

    if not hasattr(run, 'completion_counter'):
        run.completion_counter = 0

    run.completion_counter += 1

    completion_label.configure(text=f"{run.completion_counter}. operation completed")

    entry_result = customtkinter.CTkEntry(master=app, fg_color="white", text_color="black", justify="center")
    entry_result.pack(padx=5, pady=(5, 0), ipadx=70)
    entry_result.insert("0", result)

def my_fun():
    global entry_result, completion_label

    entry_1.delete(0, "end")
    my_dir1 = filedialog.askopenfilename()
    entry_1.insert("0", my_dir1)

    if 'entry_result' in globals() and entry_result is not None:
        entry_result.destroy()

    if 'completion_label' in globals() and completion_label is not None:
        completion_label.destroy()


logo_image = customtkinter.CTkImage(Image.open("ai.png"), size=(64, 64))

label_1 = customtkinter.CTkLabel(master=app, justify=customtkinter.LEFT, image=logo_image,text="    Deepfake Audio Detection",
                                 compound="left",
                                 font=customtkinter.CTkFont(size=20, weight="bold"))
label_1.pack(pady=20, padx=10)

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20)

label_2 = customtkinter.CTkLabel(master=frame, justify=customtkinter.LEFT, text="  Upload the Audio File:  ")
label_2.pack(pady=5, padx=10, anchor='w')  

entry_1 = customtkinter.CTkEntry(master=frame, placeholder_text=".wav")
entry_1.pack(side=customtkinter.LEFT, padx=5, ipadx=100)

folder_button = customtkinter.CTkButton(master=frame, text="Browse", border_width=2, fg_color="black", command=my_fun)
folder_button.pack(side=customtkinter.LEFT, padx=5)

checkbox_1 = customtkinter.CTkCheckBox(master=app,text="Model accuracy rate")
checkbox_1.pack(pady=30, padx=10)

def create_gradient_image(width, height, color1, color2):
    image = Image.new("RGB", (width, height), color1)
    draw = ImageDraw.Draw(image)
    draw.rectangle([0, height // 2, width, height], fill=color2)
    return CTkImage(image)

button_width = 100
button_height = 30

gradient_image = create_gradient_image(button_width, button_height, "cyan", "blue")

button_1 = CTkButton(master=app, command=run)
button_1.configure(image=gradient_image, compound="center", text="Run")
button_1.pack(pady=0, padx=10)

app.mainloop()

#onurkaya
