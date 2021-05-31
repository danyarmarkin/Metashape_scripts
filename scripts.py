import scaling
import pivot
try:
    import Metashape
except:
    print("Cant find Metashape")



label_scaling = "Scripts/Scaling"
label_pivot = "Scripts/Pivot"
try:
    Metashape.app.removeMenuItem(label_scaling)
    Metashape.app.removeMenuItem(label_pivot)
except:
    pass
Metashape.app.addMenuItem(label_pivot, pivot.setPivot)
Metashape.app.addMenuItem(label_scaling, scaling.scale)
