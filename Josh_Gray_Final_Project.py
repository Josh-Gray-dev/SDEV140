import tkinter as tk
from tkinter import ttk, messagebox

# Global list to store game data
games_list = []

# Add Game Window Function
def open_add_game_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add New Game")
    add_window.geometry("400x400")

    tk.Label(add_window, text="Game Title:").pack(pady=5)
    title_entry = tk.Entry(add_window, width=40)
    title_entry.pack(pady=5)

    tk.Label(add_window, text="Platform:").pack(pady=5)
    platform_var = tk.StringVar()
    platform_dropdown = tk.OptionMenu(add_window, platform_var, "PC", "PS5", "Xbox", "Switch", "Other")
    platform_dropdown.pack(pady=5)

    tk.Label(add_window, text="Status:").pack(pady=5)
    status_var = tk.StringVar()
    status_dropdown = tk.OptionMenu(add_window, status_var, "Not Started", "In Progress", "Completed")
    status_dropdown.pack(pady=5)

    tk.Label(add_window, text="Rating (1-10):").pack(pady=5)
    rating_entry = tk.Entry(add_window, width=10)
    rating_entry.pack(pady=5)

    priority_var = tk.BooleanVar()
    tk.Checkbutton(add_window, text="Mark as Play Next", variable=priority_var).pack(pady=5)

# Submit Game to Library
    def submit_game():
        rating_value = rating_entry.get() or "No Rating"
        game_data = {"title": title_entry.get(), "platform": platform_var.get(), "status": status_var.get(), "rating": rating_value, "priority": priority_var.get()}

        if not game_data["title"] or not game_data["platform"] or not game_data["status"]:
            messagebox.showerror("Missing Information", "Please fill in at least the title, platform, and status.")
            return

        games_list.append(game_data)
        messagebox.showinfo("Success", "Game added!")
        add_window.destroy()  # Automatically close the window

    tk.Button(add_window, text="Submit Game", command=submit_game).pack(pady=10)
    

# View and Edit Games Window
def open_view_games_window():
    view_window = tk.Toplevel(root)
    view_window.title("View/Edit Games")
    view_window.geometry("800x400")

    tk.Label(view_window, text="Your Game Backlog", font=("Helvetica", 14)).pack(pady=5)

    columns_frame = tk.Frame(view_window)
    columns_frame.pack()
    tk.Label(columns_frame, text="Title", width=8, font=("Helvetica", 12, "bold")).grid(row=0, column=0)
    tk.Label(columns_frame, text="Platform", width=8, font=("Helvetica", 12, "bold")).grid(row=0, column=1)
    tk.Label(columns_frame, text="Status", width=8, font=("Helvetica", 12, "bold")).grid(row=0, column=2)
    tk.Label(columns_frame, text="Rating", width=8, font=("Helvetica", 12, "bold")).grid(row=0, column=3)
    tk.Label(columns_frame, text="Priority", width=8, font=("Helvetica", 12, "bold")).grid(row=0, column=4)
    
    game_listbox = tk.Listbox(view_window, width=100, height=15)
    game_listbox.pack(pady=5)

    # Update Game Library
    def update_game_list():
        game_listbox.delete(0, tk.END)
        for game in games_list:
            game_listbox.insert(tk.END, f'{game["title"]} | {game["platform"]} | {game["status"]} | {game["rating"]} | {"Play Next" if game["priority"] else ""}')

    # Edit Selected Entry
    def edit_game():
        selected_index = game_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a game to edit.")
            return

        game = games_list[selected_index[0]]

        edit_window = tk.Toplevel(view_window)
        edit_window.title("Edit Game")

        tk.Label(edit_window, text="Game Title:").pack()
        title_entry = tk.Entry(edit_window, width=40)
        title_entry.insert(0, game["title"])
        title_entry.pack()

        tk.Label(edit_window, text="Platform:").pack()
        platform_var = tk.StringVar(value=game["platform"])
        platform_dropdown = tk.OptionMenu(edit_window, platform_var, "PC", "PS5", "Xbox", "Switch", "Other")
        platform_dropdown.pack()

        tk.Label(edit_window, text="Status:").pack()
        status_var = tk.StringVar(value=game["status"])
        status_dropdown = tk.OptionMenu(edit_window, status_var, "Not Started", "In Progress", "Completed")
        status_dropdown.pack()

        tk.Label(edit_window, text="Rating (1-10):").pack()
        rating_entry = tk.Entry(edit_window, width=10)
        rating_entry.insert(0, game["rating"])
        rating_entry.pack()

        priority_var = tk.BooleanVar(value=game["priority"])
        tk.Checkbutton(edit_window, text="Mark as Play Next", variable=priority_var).pack()

        # Save Entry
        def save_edits():
            game["title"] = title_entry.get()
            game["platform"] = platform_var.get()
            game["status"] = status_var.get()
            game["rating"] = rating_entry.get()
            game["priority"] = priority_var.get()
            update_game_list()
            edit_window.destroy()

        tk.Button(edit_window, text="Save Changes", command=save_edits).pack(pady=5)

    # Delete Game from Library
    def delete_game():
        selected_index = game_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select a game to delete.")
            return
        del games_list[selected_index[0]]
        update_game_list()

    update_game_list()

    tk.Button(view_window, text="Edit Game", command=edit_game).pack()
    tk.Button(view_window, text="Delete Game", command=delete_game).pack()
    tk.Button(view_window, text="Exit", command=view_window.destroy).pack()

# Main Window
def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Game Backlog Tracker")
root.geometry("300x200")

# Main Buttons
tk.Button(root, text="Add Game", width=20, command=open_add_game_window).pack(pady=5)
tk.Button(root, text="View/Edit Game Library", width=20, command=open_view_games_window).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=exit_app).pack(pady=5)

root.mainloop()
