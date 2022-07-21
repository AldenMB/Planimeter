import cadquery as cq
from types import SimpleNamespace as ns

INCH = 25.4
ORING = ns(id=15 / 16 * INCH, od=(1 + 3 / 16) * INCH, thickness=1 / 8 * INCH)
SHAFT = ns(length=0.5 * INCH, diameter=1 / 4 * INCH)
TOLERANCE = 0.35
ORING.radius = (ORING.id + ORING.od) / 4
SHAFT.radius = SHAFT.diameter / 2

wheel = cq.Workplane().cylinder(height=ORING.thickness + 2, radius=ORING.radius)

wheel = (
    wheel.faces(">Z")
    .circle(SHAFT.radius + 4)
    .circle(SHAFT.radius + TOLERANCE)
    .extrude(SHAFT.length - 2)
)

wheel = wheel.edges(">>Z[2]").edges(cq.selectors.RadiusNthSelector(1)).fillet(4)

ring = (
    cq.Workplane("YZ")
    .move(ORING.radius)
    .circle(ORING.thickness / 2 + TOLERANCE)
    .revolve()
)
wheel = wheel.cut(ring)

cq.exporters.export(wheel, "wheel.stl")
