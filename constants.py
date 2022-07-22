from types import SimpleNamespace as ns

INCH = 25.4
TOLERANCE = 0.35

SCREW = ns(head_diameter=11, length=20, clearance_diameter=4.25, grip_diameter=2.75)
M4 = ns(thread_diameter=3.9)

ORING = ns(id=15 / 16 * INCH, od=(1 + 3 / 16) * INCH, thickness=1 / 8 * INCH)
SHAFT = ns(diameter=1 / 4 * INCH, length=1 * INCH)
ORING.radius = (ORING.id + ORING.od) / 4
SHAFT.radius = SHAFT.diameter / 2

POTE = ns(
    external_diameter=1 * INCH,
    threaded_diameter=0.36 * INCH,
    flat_separation=0.32 * INCH,
    thread_depth=0.15 * INCH,
)
NUT = 0.5 * INCH + 0.5

WALL = 4
ROD = ns(width=INCH / 4, clearance=0.35)
