
import tkinter as tk
from cpu_data import get_cpu_usage_data          
from bar_chart import draw_bar_chart              
from pie_chart import draw_pie_chart            
from refresh import schedule_refresh              
from process_list import update_process_list     
from style import apply_style                   
# psutil for real-time system and process information
import psutil

current_chart = "bar"

def update_gui():
    data = get_cpu_usage_data() 
    update_process_list(process_frame, data)  

    #overall CPU usage percentage (measured over 0.5 seconds)
    cpu_value = psutil.cpu_percent(interval=0.5)
    cpu_label.config(text=f"CPU Usage: {cpu_value:.2f}%") 

    # Clear any existing chart in the chart frame
    for widget in chart_frame.winfo_children():
        widget.destroy()

   
    if current_chart == "bar":
        draw_bar_chart(data, chart_frame)  
    elif current_chart == "pie":
        draw_pie_chart(data, chart_frame)  

    # Exit if the main window no longer exists 
    if not root.winfo_exists():
        return    


def set_bar_chart():
    global current_chart
    current_chart = "bar"
    update_gui()


def set_pie_chart():
    global current_chart
    current_chart = "pie"
    update_gui()


root = tk.Tk()

apply_style(root)

root.title("CPU Resource Allocation Visualizer")
root.geometry("900x600")


title = tk.Label(root, text="CPU Resource Allocation Visualizer", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10) 

cpu_label = tk.Label(root, text="CPU Usage: 0%", font=("Arial", 14), bg="#f0f0f0", fg="blue")
cpu_label.pack(pady=5)

# frame to hold the chart toggle buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)


bar_button = tk.Button(button_frame, text="Bar Chart", command=set_bar_chart)
bar_button.pack(side=tk.LEFT, padx=10)  


pie_button = tk.Button(button_frame, text="Pie Chart", command=set_pie_chart)
pie_button.pack(side=tk.LEFT, padx=10)


process_frame = tk.Frame(root)
process_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10) 


chart_frame = tk.Frame(root)
chart_frame.pack(fill=tk.BOTH, expand=True) 

# Start the scheduled auto-refresh using the root window and function
schedule_refresh(root, update_gui)

# Trigger the first GUI update right away
update_gui()

# Start the Tkinter main event loop 
root.mainloop()
