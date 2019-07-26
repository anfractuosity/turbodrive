import Part
import Draft
from FreeCAD import Base

doc = FreeCAD.newDocument()
myPart = doc.addObject("Part::Feature","myPartName")

incut = 4	    # padding which will be used to add buttons etc.
driveheight = 25    # floppy drive height in mm
wallthickness = 1.5 # wall thickness in mm
textpercent = 80    # percentage of wall, which will be cut into for text

cube = Part.makeBox(150,102,driveheight+incut)
cube = cube.makeThickness([ cube.Faces[0] ],wallthickness,0.1)

logo = Part.makeBox(150,102,incut)
logo.Placement.Base.z = driveheight
mvec = FreeCAD.Vector(driveheight-incut,0,0)
Draft.move(logo,mvec)

txt = Draft.makeShapeString(str("TurboDrive"),"/usr/share/fonts/liberation/LiberationSans-Regular.ttf",9.0) 
mvec = FreeCAD.Vector(5,5,driveheight+incut+wallthickness-((wallthickness/100)*textpercent))
#Draft.rotate(txt,90)
Draft.move(txt,mvec)

comp = Part.makeCompound([txt.Shape])
extrude = comp.extrude(Base.Vector(0,0,(wallthickness/100)*textpercent))
cube = cube.cut(extrude)

doc.removeObject(txt.Label)

myPart.Shape = Part.Compound([cube,logo])
doc.recompute()
