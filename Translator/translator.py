from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from googletrans import LANGUAGES
from deep_translator import GoogleTranslator
from langdetect import detect

root = Tk()
root.title("Language Translator")
root.geometry("1000x800")
root.configure(bg='#5582f9')

def show():
    v1 = comb1.get()
    v2 = comb2.get()
    lab1.config(text=v1)
    lab2.config(text=v2)
    root.after(1000, show)

def translate():
    try:
        src_lang = comb1.get().lower()
        dest_lang = comb2.get().lower()
        trans = GoogleTranslator(source=src_lang, target=dest_lang)
        trans_lang = trans.translate(input_text.get(1.0, END))
        
        output_text.delete(1.0, END)
        output_text.insert(END, trans_lang)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def clear():
    output_text.delete(1.0, END)
    input_text.delete(1.0, END)

def exit():
    root.destroy()


image_path = 'C:/Users/canoz/Downloads/solid-concrete-wall-textured-backdrop.jpg'
img = Image.open(image_path)
img = img.resize((1000, 800), Image.LANCZOS) 
bg_image = ImageTk.PhotoImage(img)


bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


lab1 = Label(root, text='English', font=('Engravers', '30', 'bold'), bg="black", fg='white')
lab1.place(x=170, y=20)


lab2 = Label(root, text='Turkish', font=('Engravers', '30', 'bold'), bg="black", fg='white')
lab2.place(x=580, y=20)
language = list(LANGUAGES.values())

# Birinci dil seçimi 
comb1 = ttk.Combobox(root, values=language, width=65)
comb1.place(x=30, y=80)
comb1.set("English")

# İkinci dil seçimi 
comb2 = ttk.Combobox(root, values=language, width=65)
comb2.place(x=450, y=80)
comb2.set("Turkish")

# Metin giriş alanları
input_text = Text(root, height=15, width=45, borderwidth=5, bg='#E0E0E0', fg='black', relief=RIDGE, wrap=WORD, font=('Arial', 12))
input_text.place(x=30, y=120)
output_text = Text(root, height=15, width=45, borderwidth=5, bg='#E0E0E0', fg='black', relief=RIDGE, wrap=WORD, font=('Arial', 12))
output_text.place(x=450, y=120)

# Translate butonu
convert = Button(root, text='Translate', command=translate, font=('Arial', 16), bd=0, bg='white', cursor='hand2')
convert.place(x=100, y=500, width=200)

#Clear butonu
clear_btn = Button(root, text='clear', command=clear, font=('Arial', 16), bd=0, bg='white', cursor='hand2')
clear_btn.place(x=500, y=500, width=100)

# Çıkış butonu
ext = Button(root, text='Exit', command=exit, font=('Arial', 16), bd=0, bg='#5582f9', fg='white', cursor='hand2')
ext.place(x=800, y=500, width=70)

show()
mainloop()