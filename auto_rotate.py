import math

try:
    import Metashape
except:
    print("Cant find Metashape")

def rotate():
    print("start script")
    app = Metashape.app
    print("got app")
    doc = app.document
    print("got document")
    chunk = doc.chunk
    print("got chunk")
    markers = chunk.markers
    print("got markers")
    m = Metashape.Matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
    t1 = chunk.transform.translation
    chunk.transform.rotation = m
    t2 = chunk.transform.translation
    t3 = t1 - t2
    chunk.transform.translation += t3
    for marker in markers:
        marker.reference.location *= m

def init():
    label = "Scripts/Auto Rotate"
    try:
        Metashape.app.removeMenuItem(label)
    except:
        pass
    Metashape.app.addMenuItem(label, rotate)
    print("To execute this script press {}".format(label))