import math

try:
    import Metashape
except:
    print("Cant find Metashape")


def vectorLength(x, y, z):
    print(x)
    print(y)
    print(z)
    print("")
    print(x ** 2)
    print(y ** 2)
    print(z ** 2)
    print(pow(round(x, 5), 2) + pow(round(y, 5), 2) + pow(round(z, 5), 2))
    return math.sqrt(pow(round(x, 5), 2) + pow(round(y, 5), 2) + pow(round(z, 5), 2))


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
    print(v1)
    print(v2)
    # v3 = v1 - v2
    # print(v3)
    l = vectorLength(v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
    print(l)
    new_l = app.getFloat("Реальное расстояние между маркерами, m", l)
    now_scale = chunk.transform.scale
    new_scale = now_scale * new_l / l
    chunk.transform.scale = new_scale
    app.messageBox("Размер фигуры успешно увеличен в {} раз(а)".format(new_scale / now_scale))


label = "Scripts/Scaling"
try:
    Metashape.app.removeMenuItem(label)
except:
    pass
Metashape.app.addMenuItem(label, scale)
print("To execute this script press {}".format(label))
