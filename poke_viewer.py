from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info
from tkinter import messagebox

# Create the window
root = Tk()
root.title("Pokemon info view")
root.resizable(False, False)
# TODO: Additional window configuration

# Add frames to top frame

frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, sticky=N, padx=10, pady=(10, 0))

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, sticky=N, padx=10, pady=(0, 10))

#Add widgets to top frame
lbl_name = ttk.Label(frm_top, text='Pokemon name:')
lbl_name.grid(row=0, column=0)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=10)


def handle_button_click():
    #Get the name of pokemon
    poke_name = ent_name.get().strip()
    if poke_name =='':
        return

    
    #Get the pokemon from the poke API
    poke_info = get_pokemon_info(poke_name)

    if poke_info is None:
        err_msg = f"unable to get information from the PokeAPI for {poke_name}"
        messagebox.showinfo(title='Error', message=err_msg, icon='error')
        return
    


    #populates the info values
    lbl_height_value['text'] = f"{poke_info['height']} dm"
    
    #populates stat values
    prg_hp['value'] = poke_info['Stats'][0]['base_stat']
    prg_attack['value'] = poke_info['Stats'][2]['base_stat']
    prg_deffense['value'] = poke_info['Stats'][2]['base_stat']
    return

    
    
    return

btn_get_info = ttk.Button(frm_top, text='Get info', command=handle_button_click)
btn_get_info.grid(row=0, column=2)

#add widgets to bottom left frame
lbl_height = ttk.Label(frm_top, text='Height:')
lbl_height.grid(row=1, column=0)

lbl_height_value = ttk.Label(frm_top, text='TBD:')
lbl_height_value.grid(row=2, column=0)

#add widgets to bottom frame
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=1, column=0, sticky=E)
prg_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_hp.grid(row=0, column=1, padx=(0,5))

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, sticky=E)
prg_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_attack.grid(row=1, column=1, pady=5, padx=(0,5))

lbl_deffense = ttk.Label(frm_btm_right, text='Deffence:')
lbl_deffense.grid(row=1, column=0, sticky=E, pady=(0,5))
prg_deffense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_deffense.grid(row=1, column=1, pady=(0,5), padx=(0,5))

#Add widgets to bottom right



# Loop until window is closed


root.mainloop()