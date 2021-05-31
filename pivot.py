import math

try:
    import Metashape
except:
    print("Cant find Metashape")

def vectorLength(x, y, z):
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)

def setPivot():
    print("start script")
    app = Metashape.app
    doc = app.document
    chunk = doc.chunk
    point_cloud = chunk.point_cloud
    print("got point cloud")
    points = point_cloud.points
    print("got points")
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for i in range(0, len(points), 10):
        x_sum += points[i].coord.x
        y_sum += points[i].coord.y
        z_sum += points[i].coord.z
    c = len(points) // 10
    vc = points[0].coord.copy()
    x = x_sum / c
    y = y_sum / c
    z = z_sum / c
    print(x, y, z)
    chunk.transform.translation(Metashape.Vector((x, y, z)))
    print("finish script")

label = "Scripts/Pivot"
try:
    Metashape.app.removeMenuItem(label)
except:
    pass
Metashape.app.addMenuItem(label, setPivot)
print("To execute this script press {}".format(label))