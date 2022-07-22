import cadquery as cq

from constants import M4, ROD, SCREW, WALL

shoulder = (
    cq.Workplane()
    .rect(ROD.width + SCREW.head_diameter + 2 * WALL, ROD.width + 2 * WALL)
    .extrude(SCREW.length / 2)
)

shoulder = (
    shoulder.faces(">Z")
    .edges(">X")
    .workplane(centerOption="CenterOfBoundBox")
    .move(-SCREW.head_diameter / 2)
    .hole(SCREW.grip_diameter)
)

shoulder = (
    shoulder.faces(">Z")
    .edges("<X")
    .workplane(centerOption="CenterOfBoundBox")
    .rect(ROD.width + 2 * WALL, ROD.width + 2 * WALL, centered=(False, True))
    .extrude(ROD.width + 2 * WALL)
)

shoulder = (
    shoulder.faces("<X")
    .edges(">Z")
    .workplane(centerOption="CenterOfBoundBox")
    .move(0, -ROD.width / 2 - WALL)
    .rect(ROD.width + ROD.clearance, ROD.width + ROD.clearance)
    .cutThruAll()
)

shoulder = (
    shoulder.faces(">Z")
    .workplane(centerOption="CenterOfBoundBox")
    .hole(M4.thread_diameter, depth=2 * WALL)
)

shoulder = shoulder.faces(">Z").wires().toPending().extrude(4)

shoulder = shoulder.edges("%line").fillet(1)

# cq.exporters.export(shoulder, "shoulder.stl")
