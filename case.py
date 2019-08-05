import Part
import Draft
from FreeCAD import Base
import ProfileLib.RegularPolygon

doc = FreeCAD.newDocument()
myPart = doc.addObject("Part::Feature","myPartName")

#incut = 4	    # padding which will be used to add buttons etc.

batteryheight = 40

drivelength = 145
drivewidth = 102
driveheight = 26  # floppy drive height in mm
wallthickness = 3.0 # wall thickness in mm
textpercent = 30    # percentage of wall, which will be cut into for text

cube = Part.makeBox(drivelength+batteryheight,drivewidth,driveheight)
cube = cube.makeThickness([ cube.Faces[0] ],wallthickness,0.1)

#logo = Part.makeBox(drivelength,drivewidth,incut)
#logo.Placement.Base.z = driveheight

txt = Draft.makeShapeString(str("TurboDrive"),"/usr/share/fonts/liberation/LiberationSans-Regular.ttf",20.0) 
mvec = FreeCAD.Vector(30,5,driveheight+wallthickness-((wallthickness/100)*textpercent))
Draft.move(txt,mvec)

comp = Part.makeCompound([txt.Shape])
extrude = comp.extrude(Base.Vector(0,0,(wallthickness/100)*textpercent))

"""
pl = Part.makeBox(10,10,10)
#pl.Placement = App.Placement(App.Vector((drivelength + (batteryheight/2.0) + (18/2)),driveheight/2,0),App.Rotation(0,0,0))
pl.Placement = App.Placement(App.Vector(drivelength + (batteryheight/2.0) + (18/2),drivewidth-4,(driveheight / 2.0) - (10/2)),App.Rotation(0,0,0))
cube = cube.cut(pl)

"""

#Part.show(pl)

cube=cube.cut(extrude)

doc.recompute()
doc.removeObject(txt.Label)





myPart.Shape = cube

doc.addObject('PartDesign::Body','Body001')



SocketSketch = doc.Body001.newObject('Sketcher::SketchObject','SketchHole0') 
SocketSketch.Support = (myPart,["Face7"])
SocketSketch.MapMode = 'FlatFace'
doc.recompute()


# play and pause, back, forward, volume

for i in range(0,4):
    SocketSketch.addGeometry(Part.Circle(App.Vector(15,10+(i*20),0), App.Vector(0,0,1), 10/2),False)






pocket = doc.Body001.newObject("PartDesign::Pocket","Pocket0")
pocket.Profile = SocketSketch
pocket.Length = 5.0

Gui.activeDocument().hide("SketchHole0")

doc.recompute()

















a = 21
b = a + 60
c = a + 90
d = 5



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

HoleSketch.addGeometry(Part.Circle(App.Vector(a,d,0), App.Vector(0,0,1), 3),False)
HoleSketch.addGeometry(Part.Circle(App.Vector(b,d,0), App.Vector(0,0,1), 3),False)
HoleSketch.addGeometry(Part.Circle(App.Vector(c,d,0), App.Vector(0,0,1), 3),False)

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

HoleSketch2.addGeometry(Part.Circle(App.Vector(-a,d,0), App.Vector(0,0,1), 3),False)
HoleSketch2.addGeometry(Part.Circle(App.Vector(-b,d,0), App.Vector(0,0,1), 3),False)
HoleSketch2.addGeometry(Part.Circle(App.Vector(-c,d,0), App.Vector(0,0,1), 3),False)

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







HoleSketch3 = doc.Body001.newObject('Sketcher::SketchObject','SketchHole3') 
HoleSketch3.Support = (myPart,["Face13"])
HoleSketch3.MapMode = 'FlatFace'
#HoleSketch2.MapReversed = True

doc.recompute()

HoleSketch3.addGeometry(Part.Circle(App.Vector(-(drivelength + (batteryheight/4)),driveheight/2,0), App.Vector(0,0,1), 3),False)
HoleSketch3.addGeometry(Part.Circle(App.Vector(-(drivelength + (batteryheight/4) + 18),driveheight/2,0), App.Vector(0,0,1), 3),False)

#HoleSketch3.addGeometry(Part.Circle(App.Vector(-drivelength - batteryheight - 18,driveheight/2,0), App.Vector(0,0,1), 3),False)

#HoleSketch2.addGeometry(Part.Circle(App.Vector(-drivelength + A7 + A6,driveheight/2,0), App.Vector(0,0,1), 3),False)
#HoleSketch2.addGeometry(Part.Circle(App.Vector(-drivelength + A7 + A13,driveheight/2,0), App.Vector(0,0,1), 3),False)

Gui.activeDocument().hide("SketchHole3")

Hole3 = doc.Body001.newObject("PartDesign::Hole", "Hole3")
Hole3.Profile = HoleSketch3
Hole3.Depth = 10
Hole3.Threaded = 0
Hole3.ThreadType = 1
Hole3.ThreadSize = 3
Hole3.DrillPointAngle = 118.000000

Gui.activeDocument().hide("myPartName")
Gui.activeDocument().setEdit('Hole3', 0)

doc.recompute()


SocketSketch3 = doc.Body001.newObject('Sketcher::SketchObject','SketchHoleSocket3') 
SocketSketch3.Support = (myPart,["Face13"])
SocketSketch3.MapMode = 'FlatFace'
doc.recompute()

geoList = []

l = -(drivelength + (batteryheight/4) + 4)
l2 = -(drivelength + (batteryheight/4) + (18 - 4))
h = (driveheight / 2) - 4
h2 = (driveheight / 2) + 4

geoList.append(Part.LineSegment(App.Vector(l,h,0),App.Vector(l2,h,0)))
geoList.append(Part.LineSegment(App.Vector(l2,h,0),App.Vector(l2,h2,0)))
geoList.append(Part.LineSegment(App.Vector(l2,h2,0),App.Vector(l,h2,0)))
geoList.append(Part.LineSegment(App.Vector(l,h2,0),App.Vector(l,h,0)))

SocketSketch3.addGeometry(geoList,False)


"""
App.ActiveDocument.Sketch001.addGeometry(geoList,False)
conList = []
conList.append(Sketcher.Constraint('Coincident',0,2,1,1))
conList.append(Sketcher.Constraint('Coincident',1,2,2,1))
conList.append(Sketcher.Constraint('Coincident',2,2,3,1))
conList.append(Sketcher.Constraint('Coincident',3,2,0,1))
conList.append(Sketcher.Constraint('Horizontal',0))
conList.append(Sketcher.Constraint('Horizontal',2))
conList.append(Sketcher.Constraint('Vertical',1))
conList.append(Sketcher.Constraint('Vertical',3))
App.ActiveDocument.Sketch001.addConstraint(conList)
"""


#SocketSketch3.addGeometry(Part.Circle(App.Vector(drivelength + (batteryheight/2.0),driveheight/2,0), App.Vector(0,0,1), 7),False)
#ProfileLib.RegularPolygon.makeRegularPolygon('Sketch',4,App.Vector(84.002243,49.425522,0),App.Vector(92.170052,40.777252,0)))

pocket2 = doc.Body001.newObject("PartDesign::Pocket","Pocket2")
pocket2.Profile = SocketSketch3
pocket2.Length = 5.0

#Gui.activeDocument().hide("myPartName")
Gui.activeDocument().hide("myPartName")

Gui.activeDocument().setEdit('Pocket2', 0)


doc.recompute()

