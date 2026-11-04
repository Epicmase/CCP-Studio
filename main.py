import tkinter as tk

# =====================
# SETTINGS
# =====================

ROWS = 5
COLS = 5
DOT_RADIUS = 20
BG_COLOR = "#222222"

# Pinned colors
COLORS = [
    "#FF0000",  # Red
    "#00FF00",  # Green
    "#0000FF",  # Blue
    "#FFFF00",  # Yellow
    "#000000",  # Black
    "#FFFFFF"   # White
]

current_color = COLORS[0]

# Grid data
grid_data = []

# =====================
# FUNCTIONS
# =====================

def set_color(color):
    global current_color
    current_color = color

def redraw_grid():
    canvas.delete("all")

    spacing = max(50, DOT_RADIUS *3)

    start_x = 50
    start_y = 50

    for row in range(len(grid_data)):
        for col in range(len(grid_data[row])):

            x = start_x + col * spacing
            y = start_y + row * spacing

            color = grid_data[row][col]

            canvas.create_oval(
                x - DOT_RADIUS,
                y - DOT_RADIUS,
                x + DOT_RADIUS,
                y + DOT_RADIUS,
                fill=color,
                outline=""
            )

def canvas_click(event):

    spacing = max(50, DOT_RADIUS *3)

    start_x = 50
    start_y = 50

    for row in range(len(grid_data)):
        for col in range(len(grid_data[row])):

            x = start_x + col * spacing
            y = start_y + row * spacing

            distance = ((event.x - x)**2 +
                        (event.y - y)**2) ** 0.5

            if distance <= DOT_RADIUS:
                grid_data[row][col] = current_color
                redraw_grid()
                return

def rebuild_grid():

    global grid_data
    global DOT_RADIUS
    global BG_COLOR

    rows = int(rows_entry.get())
    cols = int(cols_entry.get())

    DOT_RADIUS = int(radius_entry.get())
    try:
        BG_COLOR = bg_entry.get()
        canvas.config(bg=BG_COLOR)

    except:
        print("Invalid color:", bg_entry.get())
        bg_entry.delete(0, tk.END)

    grid_data = [
        ["gray" for _ in range(cols)]
        for _ in range(rows)
    ]

    redraw_grid()

# =====================
# WINDOW
# =====================

root = tk.Tk()
root.title("CCP Studio")
root.geometry("1000x700")

# =====================
# LEFT PANEL
# =====================

left_panel = tk.Frame(root, width=250)
left_panel.pack(side="left", fill="y")

tk.Label(left_panel, text="Rows").pack()

rows_entry = tk.Entry(left_panel)
rows_entry.insert(0, "5")
rows_entry.pack()

tk.Label(left_panel, text="Columns").pack()

cols_entry = tk.Entry(left_panel)
cols_entry.insert(0, "5")
cols_entry.pack()

tk.Button(
    left_panel,
    text="Create Grid",
    command=rebuild_grid
).pack(pady=10)

tk.Label(
    left_panel,
    text="Palette"
).pack(pady=5)

for color in COLORS:

    tk.Button(
        left_panel,
        bg=color,
        width=10,
        command=lambda c=color: set_color(c)
    ).pack()

tk.Label(left_panel, text="Dot Size").pack()

radius_entry = tk.Entry(left_panel)
radius_entry.insert(0, "20")
radius_entry.pack()

tk.Label(
    left_panel,
    text="Background Color\n"
         "(basic colors like red, blue, silver,\n"
         "cyan, and gray work)\n"
         "Hex codes are also supported\n"
         "(remember the #)"
).pack()

bg_entry = tk.Entry(left_panel)
bg_entry.insert(0, "#222222")
bg_entry.pack()

tk.Button(
    left_panel,
    text="Apply Background",
    command=rebuild_grid
)

# =====================
# CANVAS
# =====================

canvas = tk.Canvas(
    root,
    bg=BG_COLOR
)

canvas.pack(
    side="right",
    fill="both",
    expand=True
)

canvas.bind("<Button-1>", canvas_click)

# =====================
# STARTUP
# =====================

rebuild_grid()

root.mainloop()