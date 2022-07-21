import cadquery as cq
from types import SimpleNamespace as ns

INCH = 25.4
ROD = ns(width=INCH / 4, clearance=INCH / 16)
SCREW = ns(head_diameter=11, length=20, clearance_diameter=4.25, grip_diameter=2.75)
M4 = ns(thread_diameter=3.3)
WALL = 4
TOLERANCE = 0.35

hinge = cq.Workplane().box(
    SCREW.head_diameter, SCREW.head_diameter, SCREW.head_diameter
)

hinge = (
    hinge.faces(">X")
    .workplane()
    .rect(ROD.width + TOLERANCE, ROD.width + TOLERANCE)
    .cutBlind(-SCREW.head_diameter * 3 / 4)
)

hinge = (
    hinge.faces("<Z")
    .vertices("<XY")
    .workplane(centerOption="CenterOfBoundBox")
    .hLine(-SCREW.head_diameter / 2)
    .tangentArcPoint([0, -SCREW.head_diameter])
    .hLineTo(0)
    .close()
    .extrude(-4)
)

hinge = (
    hinge.faces("<Z")
    .workplane()
    .move(-SCREW.head_diameter / 2, -SCREW.head_diameter / 2)
    .hole(SCREW.clearance_diameter)
)

hinge = hinge.edges().fillet(1)

cq.exporters.export(hinge, "hinge.stl")
