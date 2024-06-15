import customtkinter as ctk

def main(app):
    ctk.set_appearance_mode("Dark")
    global tasks 
    tasks = []  
    
    def switch_color():
        if switch_var.get():
            ctk.set_appearance_mode("Dark")
            app.configure(bg_color="black")
            for widget in app.winfo_children():
                apply_dark_theme(widget)
        else:
            ctk.set_appearance_mode("Light")
            app.configure(bg_color="white")
            for widget in app.winfo_children():
                apply_light_theme(widget)

    def apply_dark_theme(widget):
        if isinstance(widget, ctk.CTkFrame):
            widget.configure(fg_color="black")
        elif isinstance(widget, ctk.CTkLabel):
            widget.configure(fg_color="black", text_color="white")
        elif isinstance(widget, ctk.CTkButton):
            widget.configure(fg_color="black", text_color="white", hover_color="darkgray")
        elif isinstance(widget, ctk.CTkTextbox):
            widget.configure(fg_color="black", text_color="white")
        elif isinstance(widget, ctk.CTkOptionMenu):
            widget.configure(fg_color="black", button_color="gray", text_color="white")

    def apply_light_theme(widget):
        if isinstance(widget, ctk.CTkFrame):
            widget.configure(fg_color="white")
        elif isinstance(widget, ctk.CTkLabel):
            widget.configure(fg_color="white", text_color="black")
        elif isinstance(widget, ctk.CTkButton):
            widget.configure(fg_color="white", text_color="black", hover_color="grey")
        elif isinstance(widget, ctk.CTkTextbox):
            widget.configure(fg_color="white", text_color="grey")
        elif isinstance(widget, ctk.CTkOptionMenu):
            widget.configure(fg_color="white", button_color="gray", text_color="black")

    switch_var = ctk.BooleanVar(value=False)
    color_switch = ctk.CTkSwitch(app, width=100, height=50, text="", command=switch_color, variable=switch_var, onvalue=True, offvalue=False, progress_color="green")
    color_switch.pack(side="bottom", pady=10, anchor="e")

    textbox = ctk.CTkTextbox(app, width=700, height=50)
    textbox.pack(padx=20, pady=20)

    

    def add_task():
        task_text = textbox.get('1.0', 'end-1c').strip() 
        if task_text: 
            with open("task.txt", "a") as file: 
                file.write(task_text + "\n") 
            
            task_frame = ctk.CTkFrame(app, corner_radius=10, width=300, height=50, fg_color="black")
            task_frame.pack(padx=20, pady=10)
            checkbox = ctk.CTkCheckBox(task_frame, text=task_text, hover=True, hover_color="darkgreen", width=100, height=50)
            checkbox.pack(side="left", padx=10)
            clear_button = ctk.CTkButton(task_frame, text="Delete task", command=lambda: clear_box(task_text, task_frame, checkbox), hover=True, fg_color="red", width=80, height=20)
            clear_button.pack(side="right", padx=10)
            
            tasks.append((task_text, clear_button, task_frame)) 
            update_task_positions()

    def clear_box(task_text, task_frame, checkbox):
        with open("task.txt", "r") as file:
            lines = file.readlines()
        with open("task.txt", "w") as file:
            for line in lines:
                if line.strip() != task_text:
                    file.write(line)
        
        task_frame.destroy()
        checkbox.destroy()
        tasks[:] = [task for task in tasks if task[0] != task_text] 

        update_task_positions()

    def update_task_positions():
        for idx, (_, _, frame) in enumerate(tasks):
            frame.pack_forget() 
            frame.pack(padx=20, pady=10) 

    task_button = ctk.CTkButton(app, text="Add task", command=add_task, fg_color="green", width=200, height=70)
    task_button.pack(pady=20)

    try:
        with open("task.txt", "r") as file:
            for line in file:
                task_text = line.strip()
                if task_text:
                    task_frame = ctk.CTkFrame(app, corner_radius=10, width=300, height=50, fg_color="black")
                    task_frame.pack(padx=20, pady=10)
                    checkbox = ctk.CTkCheckBox(task_frame, text=task_text, hover=True, hover_color="darkgreen", width=100, height=50)
                    checkbox.pack(side="left", padx=10)
                    clear_button = ctk.CTkButton(task_frame, text="Delete task", command=lambda t=task_text, f=task_frame, c=checkbox: clear_box(t, f, c), hover=True, fg_color="red", width=80, height=20)
                    clear_button.pack(side="right", padx=10)
                    
                    tasks.append((task_text, clear_button, task_frame))
    except FileNotFoundError:
        pass

    return app

app = ctk.CTk()
app.geometry("1920x1080")
app = main(app)
app.mainloop()

