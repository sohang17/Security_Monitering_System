import tkinter as tk
import math
import last

class Speedometer(tk.Canvas):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.width = 400
        self.height = 400
        self.values = ["Very Bad", "Bad", "Good", "Average", "Excellent"]
        self.selected_index = self.values.index("Very Bad")
        self.stop_value = last.x  # Change this value to stop at a different value

        self.create_speedometer()

    def create_speedometer(self):
        self.delete("all")

        center_x = self.width / 2
        center_y = self.height / 2
        radius = min(center_x, center_y) - 10

        # Draw the background
        self.create_rectangle(0, 0, self.width, self.height, fill="lightgray", width=0)

        # Draw the semicircle speedometer
        start_angle = -90
        end_angle = 90
        self.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius, start=start_angle, extent=(end_angle - start_angle), style=tk.ARC, width=2, outline="black")

        # Draw the value labels
        label_radius = radius * 0.7
        label_angle = (end_angle - start_angle) / (len(self.values) - 1)
        for i, value in enumerate(self.values):
            angle = start_angle + label_angle * i
            angle_rad = math.radians(angle)
            label_x = center_x + label_radius * math.cos(angle_rad)
            label_y = center_y + label_radius * math.sin(angle_rad)
            self.create_text(label_x, label_y, text=value, font=("Arial", 12), fill="black")

        # Draw the needle
        needle_length = radius * 0.8
        needle_angle = start_angle + (label_angle * self.selected_index)
        needle_angle_rad = math.radians(needle_angle)
        needle_x = center_x + needle_length * math.cos(needle_angle_rad)
        needle_y = center_y + needle_length * math.sin(needle_angle_rad)
        self.create_line(center_x, center_y, needle_x, needle_y, fill="red", width=3)

    def start_speedometer(self):
        while self.values[self.selected_index] != self.stop_value:
            self.selected_index = (self.selected_index + 1) % len(self.values)
            self.create_speedometer()
            self.update()
            self.after(3000)  # Update speedometer every 3 seconds

        self.after_cancel(self.after_id)  # Stop updating the speedometer

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x400")
    root.title("Speedometer")

    # Create the speedometer on the left side
    speedometer = Speedometer(root, width=400, height=400)
    speedometer.grid(row=0, column=0, padx=20, pady=20)

    # Get the suggestion from the 'last' module
    suggestion = last.b
    print(suggestion)
    # Create the text label on the right side with the suggestion
    suggestion_label = tk.Label(root, text="Suggestion: " + suggestion, font=("Arial", 14))
    suggestion_label.grid(row=0, column=1, padx=20, pady=20)

    speedometer.create_speedometer()  # Create the initial speedometer

    root.after(0, speedometer.start_speedometer)  # Start updating the speedometer after the 'last.x' value is assigned

    root.mainloop()
