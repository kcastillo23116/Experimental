import datetime
import timeit
import tkinter as tk
from threading import Thread

import Common
import Display

# Location constants as X and Y coordinates for position on screen where 0,0 is top left corner
top_left = "+0+120"

# static variables
timer_started = False


# Starts a timer on a new thread so it can be run beside other scripts
def start_timer_thread(iterations, seconds_per_iteration):
    # If timer hasn't started use runtime to estimate
    if not Display.timer_started:
        # Calculate runtime
        total_runtime_seconds = Common.print_runtime(iterations, seconds_per_iteration, 0)

        # Create new threads for timer and alching so both can run at same time since timer has it's
        # mainloop that'll block other function calls/loops
        timer_thread = Thread(target=CountdownTimer, args=(total_runtime_seconds,))

        # Start timer thread
        timer_thread.start()

        Display.timer_started = True


# Start timer countdown thread with total number of seconds
def start_timer_thread_total_time(total_seconds):
    start_timer_thread(1, total_seconds)


def convert_seconds_to_dtg(runtime_in_seconds):
    dtg = str(datetime.timedelta(seconds=runtime_in_seconds))
    return dtg


# Helper function that returns timer start time
def start_timer():
    return timeit.default_timer()


# Helper function that gets stop time and displays timer to be used with start_timer function above
def stop_timer(start_time, loops_till_done):
    # Get stop time now to calculate how much time to make a single iteration
    stop = timeit.default_timer()
    seconds_per_iteration = round(stop - start_time)

    # Subtract iteration already ran
    Display.start_timer_thread(loops_till_done - 1, seconds_per_iteration)


class CountdownTimer(tk.Tk):

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

    # Counts down timer by seconds and updates numbers displayed in graphic
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
    app = CountdownTimer(90)
