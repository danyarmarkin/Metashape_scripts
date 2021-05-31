import math
try:
    import Metashape
except:
    print("Cant find Metashape")

def vectorLength(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

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
        if marker.enabled:
            enable_markers.append(marker)
    if len(enable_markers) != 2:
        print("error")
        app.messageBox("Ошибка: Выделите 2 маркера.")
        return
    v1 = enable_markers[0].reference.location
    v2 = enable_markers[1].reference.location
    v3 = v1 - v2
    l = vectorLength(v3.x, v3.y, v3.z)
    new_l = app.getFloat("Реальное расстояние между маркерами", l)
    now_scale = chunk.transform.scale
    new_scale = now_scale * new_l / l
    chunk.transform.scale = new_scale
    app.messageBox("Размер фигуры успешно увеличен в {} раз(а)".format(new_scale / now_scale))


label = "Scripts/Scaling"
Metashape.app.addMenuItem(label, scale)
print("To execute this script press {}".format(label))