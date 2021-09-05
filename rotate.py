try:
    import Metashape
except:
    print("Cant find Metashape")

consts_markers = {
    "NW": "target 45",
    "N": "target 43",
    "NE": "target 48",
    "W": "target 37",
    "C": "target 40",
    "E": "target 38",
    "SW": "target 46",
    "S": "target 44",
    "SE": "target 47",
}

def rotate():
    global consts_markers
    print("start script")
    app = Metashape.app
    print("got app")
    doc = app.document
    print("got document")
    chunk = doc.chunk
    print("got chunk")
    markers = chunk.markers
    print("got markers")

    main_cross = {}
    for key, val in consts_markers:
        if val in markers:
            main_cross[key] = val

    sn = main_cross["N"].reference.location - main_cross["S"].reference.location
    print(sn)

def init():
    label = "Scripts/Auto Rotate"
    try:
        Metashape.app.removeMenuItem(label)
    except:
        pass
    Metashape.app.addMenuItem(label, rotate)
    print("To execute this script press {}".format(label))