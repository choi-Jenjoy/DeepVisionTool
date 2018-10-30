import tkinter as tk
import re
import subprocess

root = tk.Tk()
root.title(" DeepVision GUI ")
root.geometry("500x245")


# Logo for GUI 
logo = tk.PhotoImage(file="assets/DEEPVISION.png")
logo_head = tk.Label(root, image=logo).pack(fill=tk.X)

# Label Text
w2 = tk.Label(root, text="Enter Your Queries Below").pack(fill=tk.X)

# For Entering Query
user_input = tk.Entry(root)
user_input.pack(fill=tk.X)

# Add list common phrases to be matched by this UI. Regex Approach for future
nlp_chtbt_module_phrases = ['nlp','chatbot','deus','bot','talk','chat','0','zero']
obj_module_phrases = ['vqa','visual','objective','1','one']
cntxt_module_phrases = ['context','activity','classification','2','two']
help_phrases = ['help','hlp','pardon']

# convert to set for comparison

cht_set = set(nlp_chtbt_module_phrases)
obj_set = set(obj_module_phrases)
cxt_set = set(cntxt_module_phrases)
hlp_set = set(help_phrases)

# Method for starting modules
def query_func():
    """Query method will open respective modules with phrases matching"""
    
    user_text = user_input.get()
    text_list = re.split(r'\W+',user_text)
    text_list = [x.lower() for x in text_list]
    txt_set = set(text_list)
    # two of the lists have one element in common for initiating the module
    if (cht_set & txt_set):
        ui_txt = 'Chatbot Module Started. Check Your Terminal!!'
        output.config(text=ui_txt)
        subprocess.call(['python3', 'test_scripts/script_zero.py'])
    elif (obj_set & txt_set):    
        ui_txt = 'VQA Module Started. Check Your Terminal!!'
        output.config(text=ui_txt)
        subprocess.call(['python3', 'test_scripts/script_one.py'])
    elif (cxt_set & txt_set):    
        ui_txt = 'Activity Classification Module Started. Check Your Terminal!!'
        output.config(text=ui_txt)
        subprocess.call(['python3', 'test_scripts/script_two.py'])
    elif (hlp_set & txt_set):
        ui_txt = 'Help File Open. Check you text editor!!'
        output.config(text=ui_txt)
        subprocess.call(['gedit', 'assets/HELP.md'])
    else:
        ui_txt = 'Didn\'t get you mate, Type Help!!'
        output.config(text=ui_txt)

# Button for Query
button = tk.Button(root, text="Query Now, Get Started!!", command=query_func)
button.pack()

output = tk.Label(root, text="[How may I Help you!!! ]")
output.pack()

root.mainloop()
