import tkinter as tk
from tkinter import ttk

def update_process_list(frame, data):
    # Clear existing widgets (for full refresh)
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a scrollable Treeview
    tree_frame = tk.Frame(frame)
    tree_frame.pack(fill=tk.BOTH, expand=True)

    tree_scroll = tk.Scrollbar(tree_frame)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    tree = ttk.Treeview(
        tree_frame,
        columns=("Process", "CPU"),
        show='headings',
        yscrollcommand=tree_scroll.set
    )

    tree.heading("Process", text="Process Name")
    tree.heading("CPU", text="CPU Usage (%)")

    tree.column("Process", anchor=tk.W, width=250)
    tree.column("CPU", anchor=tk.CENTER, width=120)

    # Attach scrollbar
    tree_scroll.config(command=tree.yview)

    # Sort data by CPU usage descending
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    for name, cpu in sorted_data:
        tree.insert('', 'end', values=(name, f"{cpu:.1f}"))

    tree.pack(fill=tk.BOTH, expand=True)