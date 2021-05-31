import math
try:
    import Metashape
except:
    print("Cant find Metashape")

def vectorLength(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

def scale():
    app = Metashape.app
    doc = app.document
    chunk = doc.chunk
    markers = chunk.markers

    enable_mrakers = 0
    for marker in markers:
        if marker.enabled:
            enable_mrakers += 1
    if enable_mrakers != 2:
        print("error")
        app.MessageBox("Ошибка: Выделите 2 маркера.")
        return
    v1 = enable_mrakers[0].reference.location
    v2 = enable_mrakers[1].reference.location
    v3 = v1 - v2
    l = vectorLength(v3.x, v3.y, v3.z)
    new_l = app.nextFloat("Реальное расстояние между маркерами", l)
    now_scale = chunk.transform.scale
    new_scale = now_scale * new_l / l
    app.MessageBox("размер фигуры успешно увеличен в {} раз(а)".format(new_scale / now_scale))


label = "Scripts/Scaling"
Metashape.app.addMenuItem(label, scale)
print("To execute this script press {}".format(label))