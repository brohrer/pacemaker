# pacemaker
For controlling time per iteration loop in Python.

A carefully regulated loop comes in handy for managing rate-limited APIs,
frame refreshes in animations, and cycles in real-time simulations.

The pacemaker package is intentionally minimalistic and has no external dependencies.
It's a glorified snippet, shorter than this README.
Works on Linux, Windows, and MacOS

## Installation

```bash
python3 -m pip install pacemaker-lite
```

## Usage

```python
from pacemaker.pacemaker import Pacemaker

iterations_per_second = 2.5
pm = Pacemaker(iterations_per_second)

for i in range(100):
    pm.beat()
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


beat() returns the amount of time elapsed for that cycle that was
in excess of the desired clock period.
```python
elapsed = pm.beat()
```
A return value of 0 means it
was exactly correct. If it's higher than that, it means that the
cycle took a little longer to run than desired.
It will usually be off by a little. You can create a
set of checks on the return value if it's important to keep the cycle
time tightly controlled.
```python
short_delay = .1  # seconds
long_delay = .5  # seconds
elapsed = pm.beat()
if elapsed > long_delay:
    raise RuntimeError(f"Loop duration exceeded by {elapsed} seconds.")
if elapsed > short_delay:
    print(f"Loop duration exceeded by {elapsed} seconds.")  # or log this
```

For a deep dive on what the pacemaker does and why, check out
[Chapter 2 of How to Train Your Robot](https://brandonrohrer.com/httyr2).
