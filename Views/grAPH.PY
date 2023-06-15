import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib Graph in Tkinter")

# Create a figure and axes for the graph
fig, ax = plt.subplots()

# Generate sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot the data
ax.plot(x, y)

# Create a canvas to display the graph
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# Add the canvas to the Tkinter window
canvas.get_tk_widget().pack()

# Start the Tkinter event loop
root.mainloop()

