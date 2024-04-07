# pacemaker
For controlling time per iteration loop in Python.

A carefully regulated loop comes in handy for managing rate-limited APIs,
frame refreshes in animations, and cycles in real-time simulations.
This package provides an accurate metronome for your code to keep time with,
good up to 1 MHz (one microsecond per iteration).

The pacemaker package is intentionally minimalistic and has no external dependencies.
It's a glorified snippet. The whole package's code is shorter than this README.
Works on Linux, Windows, and MacOS.

## Installation

```bash
pip install pacemaker-lite
```

## Usage

```python
from pacemaker.pacemaker import Pacemaker

iterations_per_second = 2.5
pm = Pacemaker(iterations_per_second)

for i in range(100):
    _ = pm.beat()
    print(i)
```

The repetitive import line can be better understood as
```python
from pacemaker_package.pacemaker_module import PacemakerClass
```

## What it does

The Pacemaker class keeps a loop operating at a steady rhythm,
according to a wall clock. It's useful for coordinating the activities
of several asynchronous and real-time processes.

Initialize Pacemaker(clock_frequency) with the desired number of iterations per second.
Call Pacemaker.beat() in a loop to keep it cycling
at the clock frequency.

If the pacemaker experiences a delay, it will allow faster iterations to try
to catch up. Heads up: because of this, any individual iteration might end up being much
shorter than suggested by the pacemaker's target rate.

beat() returns the amount of time that it was off from the ideal pace, counting
back from the first beat.
```python
off_by = pm.beat()
```
A return value of 0 means it
was exactly correct. If it's higher than that, it means that the
cycle came in late.
It will usually be off by a little. You can create a
set of checks on the return value if it's important to keep the cycle
time tightly controlled.
```python
a_little_late = .1  # seconds
a_lot_late = .5  # seconds
off_by = pm.beat()
if off_by > a_lot_late:
    raise RuntimeError(f"Last beat was running behind by {elapsed} seconds.")
if off_by > a_little_late:
    print(f"Last beat was running behind by {elapsed} seconds.")  # or log this
```

For a deep dive on what the pacemaker does and why, check out
[Chapter 2 of How to Train Your Robot: Keeping Time with Python](https://brandonrohrer.com/httyr2pdf).
