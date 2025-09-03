from customtkinter import *
from settings.Functions import *

win = CTk()
win.title('Weather Gate')
win.geometry("800x600+250+50")
win.resizable(False,False)

font_text = CTkFont(family='Arial',size=24,weight='normal')

Frame_app = CTkFrame(win,750,580,15,fg_color="#FF0000")

Fram_textbox = CTkFrame(Frame_app,530,560,fg_color="#E6FAF9")

Frame_entry_and_button =CTkFrame(Frame_app,200,550,fg_color="#FFFFFF",border_width=2,
                                 border_color="#FFFFFF",corner_radius=15)

text_box = CTkTextbox(Fram_textbox,520,550,border_width=1,border_color="#FF5100")
text_box.configure(state="disabled")

entry_city_name = CTkEntry(Frame_entry_and_button,190,50,border_width=1,corner_radius=10,
                           border_color="#FF0000",placeholder_text='name city'
                           ,placeholder_text_color="#FF5100",font=('Arial',20))

btn_search = CTkButton(Frame_entry_and_button,150,50,text='Search',corner_radius=15,fg_color="#FF5100",
                       text_color="#FFFFFF",font=font_text,command=search_btn(entry_city_name))

btn_delete = CTkButton(Frame_entry_and_button,150,50,text='Delete',corner_radius=15,fg_color="#FF5100",
                       text_color="#FFFFFF",font=font_text, command=delete_btn(text_box,load_data))


Frame_app.pack_configure(padx=10,pady=10)
Fram_textbox.pack_configure(padx=10,pady=10,side='right')
Frame_entry_and_button.pack_configure(padx=10,pady=10,side='left')


text_box.pack_configure(padx=10,pady=10)
entry_city_name.pack(padx=10,pady=10)
btn_search.pack(padx=10,pady=10)
btn_delete.pack(padx=10,pady=10)


win.mainloop()