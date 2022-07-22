import cadquery as cq

from constants import INCH, NUT, SHAFT

driver = (
    cq.Workplane()
    .sketch()
    .circle(NUT / 2 * 1.6)
    .regularPolygon(r=NUT / 3**0.5, n=6, mode="s")
    .finalize()
    .extrude(SHAFT.length)
)

driver = (
    driver.faces(">Z")
    .workplane(offset=0.25 * INCH)
    .sketch()
    .regularPolygon(r=0.25 * INCH / 3**0.5, n=6)
    .finalize()
    .extrude(0.75 * INCH)
)

driver = driver.faces(">Z[1]").wires().first().toPending().extrude(2 * INCH, taper=25)

driver = (
    driver.faces("<Z[1]")
    .wires()
    .toPending()
    .extrude(0.75 * INCH, taper=25, combine="cut")
)

cq.exporters.export(driver, "nut_driver.stl")
