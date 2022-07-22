import cadquery as cq

from constants import INCH, M4, POTE, ROD, SCREW, TOLERANCE

block = cq.Workplane().box(2 * INCH, 0.5 * INCH, SCREW.length)


block = (
    block.faces(">X")
    .workplane()
    .rect(ROD.width + ROD.clearance, ROD.width + ROD.clearance * 3)
    .cutThruAll()
)


block = (
    block.faces(">Z").workplane(centerOption="CenterOfBoundBox")
    # .rarray(xSpacing=1.5 * INCH, ySpacing=1, xCount=2, yCount=1)
    .hole(M4.thread_diameter, depth=SCREW.length / 2)
)


# potentiometer mount
block = (
    block.faces("<Y")
    .edges(">X")
    .workplane(centerOption="CenterOfBoundBox")
    .rect(-POTE.thread_depth, SCREW.length, centered=(False, True))
    .extrude(1.25 * INCH)
)
block = (
    block.faces(">X")
    .edges("<Y")
    .workplane(centerOption="CenterOfBoundBox")
    .move(0.5 * INCH)
    .sketch()
    .circle(POTE.threaded_diameter / 2 + TOLERANCE)
    .rect(POTE.flat_separation + TOLERANCE, 0.5 * INCH, mode="i")
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

block = block.edges().fillet(0.4)

cq.exporters.export(block, "elbow.stl")
