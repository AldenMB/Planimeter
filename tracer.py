import cadquery as cq

from constants import INCH, ROD, TOLERANCE, WALL

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
    .workplane(offset=0.5 * INCH, centerOption="CenterOfBoundBox")
    .circle(1.5)
    .loft()
)

tracer = tracer.edges().fillet(1)

cq.exporters.export(tracer, "tracer.stl")
