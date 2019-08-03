import Part
import Draft
from FreeCAD import Base

doc = FreeCAD.newDocument()
myPart = doc.addObject("Part::Feature","myPartName")

incut = 4	    # padding which will be used to add buttons etc.

batteryheight = 40

drivelength = 150
drivewidth = 102
driveheight = 25    # floppy drive height in mm
wallthickness = 3.0 # wall thickness in mm
textpercent = 30    # percentage of wall, which will be cut into for text

A7 = 41.28
A6 = 44.45 
A13 = 76.20   

cube = Part.makeBox(drivelength+batteryheight,drivewidth,driveheight+incut)
cube = cube.makeThickness([ cube.Faces[0] ],wallthickness,0.1)

logo = Part.makeBox(drivelength,drivewidth,incut)
logo.Placement.Base.z = driveheight

txt = Draft.makeShapeString(str("TurboDrive"),"/usr/share/fonts/liberation/LiberationSans-Regular.ttf",9.0) 
mvec = FreeCAD.Vector(5,5,driveheight+incut+wallthickness-((wallthickness/100)*textpercent))
Draft.move(txt,mvec)

comp = Part.makeCompound([txt.Shape])
extrude = comp.extrude(Base.Vector(0,0,(wallthickness/100)*textpercent))
cube = cube.cut(extrude)

doc.removeObject(txt.Label)
myPart.Shape = cube

doc.addObject('PartDesign::Body','Body001')

SocketSketch = doc.Body001.newObject('Sketcher::SketchObject','SketchHoleSocket') 
SocketSketch.Support = (myPart,["Face9"])
SocketSketch.MapMode = 'FlatFace'
doc.recompute()

SocketSketch.addGeometry(Part.Circle(App.Vector(drivelength + (batteryheight/2.0),driveheight/2,0), App.Vector(0,0,1), 7),False)

pocket = doc.Body001.newObject("PartDesign::Pocket","Pocket")
pocket.Profile = App.activeDocument().SketchHoleSocket
pocket.Length = 5.0

Gui.activeDocument().hide("SketchHoleSocket")

doc.recompute()

HoleSketch = doc.Body001.newObject('Sketcher::SketchObject','SketchHole') 
HoleSketch.Support = (myPart,["Face9"])
HoleSketch.MapMode = 'FlatFace'

doc.recompute()

HoleSketch.addGeometry(Part.Circle(App.Vector(drivelength - A7,driveheight/2,0), App.Vector(0,0,1), 3),False)
HoleSketch.addGeometry(Part.Circle(App.Vector(drivelength - A7 - A6,driveheight/2,0), App.Vector(0,0,1), 3),False)
HoleSketch.addGeometry(Part.Circle(App.Vector(drivelength - A7 - A13,driveheight/2,0), App.Vector(0,0,1), 3),False)

Gui.activeDocument().hide("SketchHole")

Hole = doc.Body001.newObject("PartDesign::Hole", "Hole")
Hole.Profile = HoleSketch
Hole.Depth = 10
Hole.Threaded = 0
Hole.ThreadType = 1
Hole.ThreadSize = 3
Hole.DrillPointAngle = 118.000000

Gui.activeDocument().hide("myPartName")
Gui.activeDocument().setEdit('Hole', 0)

doc.recompute()
HoleSketch2 = doc.Body001.newObject('Sketcher::SketchObject','SketchHole2') 
HoleSketch2.Support = (myPart,["Face13"])
HoleSketch2.MapMode = 'FlatFace'
#HoleSketch2.MapReversed = True

doc.recompute()

HoleSketch2.addGeometry(Part.Circle(App.Vector(-drivelength + A7,driveheight/2,0), App.Vector(0,0,1), 3),False)
HoleSketch2.addGeometry(Part.Circle(App.Vector(-drivelength + A7 + A6,driveheight/2,0), App.Vector(0,0,1), 3),False)
HoleSketch2.addGeometry(Part.Circle(App.Vector(-drivelength + A7 + A13,driveheight/2,0), App.Vector(0,0,1), 3),False)

Gui.activeDocument().hide("SketchHole2")

Hole2 = doc.Body001.newObject("PartDesign::Hole", "Hole2")
Hole2.Profile = HoleSketch2
Hole2.Depth = 10
Hole2.Threaded = 0
Hole2.ThreadType = 1
Hole2.ThreadSize = 3
Hole2.DrillPointAngle = 118.000000

Gui.activeDocument().hide("myPartName")
Gui.activeDocument().setEdit('Hole2', 0)

doc.recompute()
