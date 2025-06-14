import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_bar_chart(data, parent_frame):
    """
    Draws a horizontal bar chart and embeds it in a Tkinter frame.
    """
    if not data:
        print("No data to display.")
        return

    sorted_data = sorted(data.items(), key=lambda item: item[1], reverse=True)[:10]
    processes = [item[0] for item in sorted_data]
    cpu_usage = [item[1] for item in sorted_data]

    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
    bars = ax.barh(processes, cpu_usage, color='skyblue')
    ax.set_xlabel("CPU Usage (%)")
    ax.set_title("Top CPU-Consuming Processes")
    ax.invert_yaxis()
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    for bar in bars:
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height() / 2,
                f'{width:.1f}%', va='center', fontsize=9)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
