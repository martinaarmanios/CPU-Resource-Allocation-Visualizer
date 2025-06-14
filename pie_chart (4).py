import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_pie_chart(data, parent_frame, title="CPU Usage Distribution", explode_max=True):
    """
    Draw a CPU-usage pie chart and embed it in a Tkinter frame.
    """
    labels = list(data.keys())
    sizes = list(data.values())

    fig, ax = plt.subplots(figsize=(6, 6), dpi=100)

    if explode_max:
        m = max(sizes)
        explode = [0.08 if s == m else 0 for s in sizes]
    else:
        explode = None

    ax.pie(sizes, labels=labels, explode=explode,
           autopct='%1.1f%%', startangle=90)
    ax.set_title(title)
    ax.axis('equal')

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
