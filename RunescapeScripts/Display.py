import datetime
import tkinter as tk

# Location constants as X and Y coordinates for position on screen where 0,0 is top left corner
top_left = "+0+120"


class ExampleApp(tk.Tk):

    # Constructor to initialize on screen number visual info
    def __init__(self, time):
        tk.Tk.__init__(self)
        self.label = tk.Label(text='Text on the screen', font=('Times New Roman', '35'), fg='green', bg='white')
        self.label.master.overrideredirect(True)
        self.label.master.geometry(top_left)
        self.label.master.lift()
        self.label.master.wm_attributes("-topmost", True)
        self.label.master.wm_attributes("-disabled", True)
        self.label.master.wm_attributes("-transparentcolor", "white")
        self.label.pack()
        self.remaining = 0
        self.countdown(time)
        self.mainloop()

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="Time's Up!")
        else:
            # Convert seconds to dtg to be displayed
            dtg = str(datetime.timedelta(seconds=self.remaining))

            # Update time remaining display text
            self.label.configure(text=dtg)
            self.remaining = self.remaining - 1

            # Wait/Sleep for a second
            self.after(1000, self.countdown)


# Only run if called from this script
if __name__ == "__main__":
    app = ExampleApp(90)
