import time


class Pacemaker:
    """
    The Pacemaker class keeps a loop operating at a steady rhythm,
    according to a wall clock. It's useful for coordinating the activities
    of several asynchronous and real-time processes.

    Initialize Pacemaker(clock_freq) with the desired clock frequency in Hz.
    Call Pacemaker.beat() in a loop to keep it cycling
    at the clock frequency.

    beat() returns the amount of time elapsed for that cycle that was
    in excess of the desired clock period. A return value of 0 means it
    was exactly correct. If it's higher than that, it means that the
    cycle took a little longer to run than desired.
    It will usually be off by a little. You can create a
    set of checks on the return value if it's important to keep the cycle
    time tightly controlled.

    For consistency, all the time units are in seconds.

    See brandonrohrer.com/httyr2 for a detailed development of the method.
    """

    def __init__(self, clock_freq_Hz):
        self.clock_period = 1 / float(clock_freq_Hz)
        self.last_run_completed = time.monotonic()
        self.start_time = time.monotonic()
        self.i_iter = -1

    def beat(self):
        self.i_iter += 1
        end = self.start_time + (self.i_iter + 1) * self.clock_period

        sleep_time = end - time.monotonic()
        if sleep_time > 0:
            time.sleep(sleep_time)

        this_run_completed = time.monotonic()
        dt = this_run_completed - self.last_run_completed
        overtime = dt - self.clock_period
        self.last_run_completed = this_run_completed
        return overtime
