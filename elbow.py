import cadquery as cq
from types import SimpleNamespace as ns

INCH = 25.4
POTE = ns(
    external_diameter=1 * INCH,
    threaded_diameter=0.36 * INCH,
    flat_separation=0.32 * INCH,
    thread_depth=0.15 * INCH,
)
ROD = ns(width=INCH / 4, clearance=INCH / 16)
M4 = ns(thread_diameter=3.3)
SCREW = ns(head_diameter=11, length=20, clearance_diameter=4.25, grip_diameter=2.75)


block = cq.Workplane().box(2 * INCH, 0.5 * INCH, SCREW.length)


block = (
    block.faces(">X")
    .workplane()
    .rect(ROD.width + ROD.clearance, ROD.width + ROD.clearance)
    .cutThruAll()
)


block = (
    block.faces(">Z")
    .workplane(centerOption="CenterOfBoundBox")
    .rarray(xSpacing=1.5 * INCH, ySpacing=1, xCount=2, yCount=1)
    .hole(M4.thread_diameter, depth=0.25 * INCH)
)


# potentiometer mount
block = (
    block.faces("<Y")
    .edges(">X")
    .workplane(centerOption="CenterOfBoundBox")
    .rect(-POTE.thread_depth, SCREW.length, centered=(False, True))
    .extrude(1.25 * INCH)
)
block = block.edges("<Y and |X").fillet(0.3 * INCH)
block = (
    block.faces(">X")
    .edges("<Y")
    .workplane(centerOption="CenterOfBoundBox")
    .move(0.25 * INCH)
    .sketch()
    .circle(POTE.threaded_diameter / 2)
    .rect(POTE.flat_separation, 0.5 * INCH, mode="i")
    .finalize()
    .cutThruAll()
)

block = (
    block.faces(">Z")
    .vertices(">Y and <X")
    .workplane(centerOption="CenterOfBoundBox")
    .vLine(SCREW.head_diameter)
    .tangentArcPoint([SCREW.head_diameter, 0])
    .vLineTo(0)
    .close()
    .extrude(-SCREW.length)
)

block = (
    block.faces(">Z")
    .vertices(">Y and <X")
    .workplane(centerOption="CenterOfBoundBox")
    .move(SCREW.head_diameter / 2)
    .hole(SCREW.grip_diameter)
)

block = (
    block.faces("<X")
    .edges(">Y")
    .workplane(centerOption="CenterOfBoundBox")
    .rect(SCREW.head_diameter * 2, 6)
    .cutThruAll()
)

block = block.edges().fillet(1)

cq.exporters.export(block, "elbow.stl")
