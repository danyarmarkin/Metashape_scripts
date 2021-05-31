import math

try:
    import Metashape
except:
    print("Cant find Metashape")


def vectorLength(x, y, z):
    print(x)
    print(y)
    print(z)
    return math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))


def scale():
    print("start script")
    app = Metashape.app
    print("got app")
    doc = app.document
    print("got document")
    chunk = doc.chunk
    print("got chunk")
    markers = chunk.markers
    print("got markers")

    enable_markers = []
    for marker in markers:
        if marker.selected:
            enable_markers.append(marker)
    if len(enable_markers) != 2:
        print("error")
        app.messageBox("Ошибка: Выделите 2 маркера.")
        return
    v1 = enable_markers[0].reference.location
    v2 = enable_markers[1].reference.location
    v3 = v2 - v1
    l = vectorLength(v3.x, v3.y, v3.z)
    app.messageBox("Расстояние между маркерами {} м".format(l))

def init():
    label = "Scripts/Distance"
    try:
        Metashape.app.removeMenuItem(label)
    except:
        pass
    Metashape.app.addMenuItem(label, scale)
    print("To execute this script press {}".format(label))
