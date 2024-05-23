from customtkinter import filedialog
import customtkinter
import pyqrcode
from PIL import Image

#Generate QRCode

def imageGen():
    global qr_image, qr, btn3
    #check if text alrady or buttons already exists on display
    if label2.cget("text") or ('btn3' in globals() and btn3.winfo_ismapped()):
        clear()
    data = data1.get()
    if data:
        #generate QRCode
        qr = pyqrcode.create(data)
        qr.png("qrcode.png", scale=10)
        #display QRCode
        img = Image.open("qrcode.png")
        qr_image = customtkinter.CTkImage(light_image=img, size=(250, 250))
        label2.configure(image=qr_image)
        data1.delete(0, 'end')
        #generate clear button
        btn3 = customtkinter.CTkButton(app, text = "Clear", font=("Arial",14), command= clear)
        btn3.pack(padx= 10, pady = 10)
        #generate save button
        btn1.configure(text="Save image", command=save_qrcode)
    elif data == "":
        label2.configure(image= '', text= "invalid request", font = ("Arial",14), text_color = "red")
        btn3 = customtkinter.CTkButton(app, text = "Clear", font=("Arial",14), command= clear)
        btn3.pack()

       

# Save QRCode
def save_qrcode():
    filepath = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG FILE", ".png"),("All Files","*.*")))
    if filepath:
        qr.png(filepath, scale=20)

#clear display
def clear():
    label2.configure(image= '', text="")
    btn1.configure(text="Generate", command= imageGen)
    
    if 'btn3' in globals() and btn3.winfo_ismapped():
        btn3.pack_forget()
    
    

#GUI
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x500")
app.title("QRCODE GENERATOR")

label = customtkinter.CTkLabel(app, text ="Enter URL/ data", font= ("Arial",20))
label.pack(padx = 10, pady = 10)

data1 = customtkinter.CTkEntry(app,placeholder_text= "input data", width= 350, height = 30, font=("Arial",16))
data1.pack(padx = 10, pady = 10)

frame1 = customtkinter.CTkFrame(app)
frame1.pack(padx = 10, pady = 10)
btn1 = customtkinter.CTkButton(frame1, text = "Generate", font=("Arial",14), state= "normal", command= imageGen)
btn1.pack(padx = 10, pady = 10)

label2 = customtkinter.CTkLabel(app, text='', corner_radius= 8)
label2.pack(padx = 10, pady = 20)


app.mainloop()