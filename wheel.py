import cadquery as cq

from constants import ORING, SHAFT, TOLERANCE

wheel = cq.Workplane().cylinder(height=ORING.thickness + 6, radius=ORING.radius)

wheel = (
    wheel.faces(">Z")
    .circle(SHAFT.radius + 6)
    .circle(SHAFT.radius)
    .extrude(SHAFT.length / 2 - 2)
)

wheel = wheel.edges(">>Z[2]").edges(cq.selectors.RadiusNthSelector(1)).fillet(4)
wheel = wheel.edges("<<Z").chamfer(1)
wheel = wheel.edges(">>Z").chamfer(1)

ring = (
    cq.Workplane("YZ")
    .move(ORING.radius + TOLERANCE)
    .circle(ORING.thickness / 2)
    .revolve()
)
wheel = wheel.cut(ring)

cq.exporters.export(wheel, "wheel.stl")
