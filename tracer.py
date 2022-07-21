import cadquery as cq
from types import SimpleNamespace as ns

INCH = 25.4
ROD = ns(width=INCH / 4, clearance=INCH / 16)
SCREW = ns(head_diameter=11, length=20, clearance_diameter=4.25, grip_diameter=2.75)
M4 = ns(thread_diameter=3.3)
WALL = 4
TOLERANCE = 0.35


w = ROD.width + 2 * WALL
tracer = cq.Workplane().box(w, w, w)
tracer = (
    tracer.faces(">Z")
    .workplane()
    .rect(ROD.width + TOLERANCE, ROD.width + TOLERANCE)
    .cutBlind(-(ROD.width + WALL))
)

tracer = (
    tracer.faces(">X")
    .wires()
    .toPending()
    .workplane(offset=1 * INCH, centerOption="CenterOfBoundBox")
    .circle(1.5)
    .loft()
)

tracer = tracer.edges().fillet(1)

cq.exporters.export(tracer, "tracer.stl")
