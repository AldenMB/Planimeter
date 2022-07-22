import cadquery as cq

from constants import ROD, SCREW, TOLERANCE

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
