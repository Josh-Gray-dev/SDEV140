import tkinter as tk
from tkinter import ttk, messagebox

# Global list to store game data
games_list = []

# Add Game Window Function
def open_add_game_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add New Game")
    add_window.geometry("400x500")

    # Labels and Entry widgets
    tk.Label(add_window, text="Game Title:").pack(pady=5)
    title_entry = tk.Entry(add_window, width=40)
    title_entry.pack(pady=5)

    tk.Label(add_window, text="Platform:").pack(pady=5)
    platform_var = tk.StringVar()
    platform_dropdown = ttk.Combobox(add_window, textvariable=platform_var, state="readonly")
    platform_dropdown['values'] = ("PC", "PS5", "Xbox", "Switch", "Other")
    platform_dropdown.pack(pady=5)

    tk.Label(add_window, text="Status:").pack(pady=5)
    status_var = tk.StringVar()
    status_dropdown = ttk.Combobox(add_window, textvariable=status_var, state="readonly")
    status_dropdown['values'] = ("Not Started", "In Progress", "Completed")
    status_dropdown.pack(pady=5)

    tk.Label(add_window, text="Rating (1-10):").pack(pady=5)
    rating_entry = tk.Entry(add_window, width=10)
    rating_entry.pack(pady=5)

    tk.Label(add_window, text="Notes / Review:").pack(pady=5)
    notes_entry = tk.Text(add_window, height=4, width=30)
    notes_entry.pack(pady=5)

    priority_var = tk.BooleanVar()
    priority_checkbox = tk.Checkbutton(add_window, text="Mark as Play Next", variable=priority_var)
    priority_checkbox.pack(pady=5)

    # Add Game Button Function
    def submit_game(clear_after=True):
        game_data = {
            "title": title_entry.get(),
            "platform": platform_var.get(),
            "status": status_var.get(),
            "rating": rating_entry.get(),
            "notes": notes_entry.get("1.0", tk.END).strip(),
            "priority": priority_var.get()
        }

        # Basic validation
        if not game_data["title"] or not game_data["platform"] or not game_data["status"]:
            messagebox.showerror("Missing Information", "Please fill in at least the title, platform, and status.")
            return

        games_list.append(game_data)
        messagebox.showinfo("Success", f"'{game_data['title']}' added to your backlog!")

        if clear_after:
            # Clear the fields for next input
            title_entry.delete(0, tk.END)
            platform_var.set("")
            status_var.set("")
            rating_entry.delete(0, tk.END)
            notes_entry.delete("1.0", tk.END)
            priority_var.set(False)
        else:
            add_window.destroy()

    # Buttons
    submit_btn = tk.Button(add_window, text="Submit Game", command=lambda: submit_game(clear_after=True), bg="#4CAF50", fg="white", width=20)
    submit_btn.pack(pady=10)

# View All Games Window Function
def open_view_games_window():
    view_window = tk.Toplevel(root)
    view_window.title("View All Games")
    view_window.geometry("700x400")

    # Create treeview (like a table)
    columns = ("Title", "Platform", "Status", "Rating", "Priority")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(fill="both", expand=True)

    # Insert data into the tree
    for game in games_list:
        tree.insert("", tk.END, values=(
            game["title"], 
            game["platform"], 
            game["status"], 
            game["rating"], 
            "Yes" if game["priority"] else "No"
        ))

    # Edit or Delete Selected Game
    def delete_game():
        selected_item = tree.selection()
        if selected_item:
            index = tree.index(selected_item)
            del games_list[index]
            tree.delete(selected_item)
            messagebox.showinfo("Deleted", "Game deleted from backlog.")
        else:
            messagebox.showerror("No selection", "Please select a game to delete.")

    tk.Button(view_window, text="Delete Selected Game", command=delete_game).pack(pady=10)

# Save / Load Functions Placeholder
def save_library():
    messagebox.showinfo("Coming Soon", "Save feature will be added later!")

def load_library():
    messagebox.showinfo("Coming Soon", "Load feature will be added later!")

# Main Window
root = tk.Tk()
root.title("Game Backlog Tracker")
root.geometry("400x300")

# Title Label
tk.Label(root, text="Game Backlog Tracker", font=("Helvetica", 16)).pack(pady=20)

# Buttons
tk.Button(root, text="Add Game", width=20, command=open_add_game_window).pack(pady=5)
tk.Button(root, text="View All Games", width=20, command=open_view_games_window).pack(pady=5)
tk.Button(root, text="Save Library", width=20, command=save_library).pack(pady=5)
tk.Button(root, text="Load Library", width=20, command=load_library).pack(pady=5)

root.mainloop()
