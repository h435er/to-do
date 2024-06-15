import customtkinter as ctk

def main(app):
    def switch_color():
        if switch_var.get():
            ctk.set_appearance_mode("Dark")
            app.configure(bg_color="black")
            for widget in app.winfo_children():
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
        else:
            ctk.set_appearance_mode("Light")
            app.configure(bg_color="white")
            for widget in app.winfo_children():
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

    tasks = []

    def update_task_positions():
        for i, (_, _, frame) in enumerate(tasks):
            frame.pack_forget()
            frame.pack(padx=20, pady=(10 if i == 0 else 5))

    def move_task_up(task_frame):
        index = next((i for i, task in enumerate(tasks) if task[2] == task_frame), None)
        if index is not None and index > 0:
            tasks[index], tasks[index - 1] = tasks[index - 1], tasks[index]
            update_task_positions()

    def move_task_down(task_frame):
        index = next((i for i, task in enumerate(tasks) if task[2] == task_frame), None)
        if index is not None and index < len(tasks) - 1:
            tasks[index], tasks[index + 1] = tasks[index + 1], tasks[index]
            update_task_positions()

    def add_task():
        task_text = textbox.get(1.0, "end-1c")
        task_frame = ctk.CTkFrame(app, corner_radius=10, width=300, height=50, fg_color="black")
        task_frame.pack(padx=20, pady=10)
        checkbox = ctk.CTkCheckBox(task_frame, text=task_text, hover=True, hover_color="darkgreen", width=100, height=50)
        checkbox.pack(side="left", padx=10)
        up_button = ctk.CTkButton(task_frame, text="↑", command=lambda frame=task_frame: move_task_up(frame), width=20, height=20)
        up_button.pack(side="left", padx=5)
        down_button = ctk.CTkButton(task_frame, text="↓", command=lambda frame=task_frame: move_task_down(frame), width=20, height=20)
        down_button.pack(side="left", padx=5)
        clear_button = ctk.CTkButton(task_frame, text="Delete task", command=lambda frame=task_frame, checkbox=checkbox: clear_box(frame, checkbox), hover=True, fg_color="red", width=80, height=20)
        clear_button.pack(side="right", padx=10)
        tasks.append((checkbox, clear_button, task_frame))
        update_task_positions()

    def clear_box(task_frame, checkbox):
        task_frame.destroy()
        checkbox.destroy()
        tasks[:] = [task for task in tasks if task[0] != checkbox]
        update_task_positions()

    task_button = ctk.CTkButton(app, text="Add task", command=add_task, fg_color="green", width=200, height=70)
    task_button.pack(pady=20)
    return app

app = ctk.CTk()
app.geometry("1920x1080")
app = main(app)
app.mainloop()
