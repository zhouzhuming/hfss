class Hfss3DModeler:
    """default unit :mm"""
    def __init__(self,f):
        self.fid = f
        self.fid.write('')
        self.fid.write('\noEditor = oDesign.SetActiveEditor("3D Modeler")')

    def HfssDrawCone(self,name,corr,axis,h,br,tr,material,solveinside,unit=None):
        if unit:
            ut = unit
        else:
            ut = 'mm'
        self.fid.write('\noEditor.CreateCone(\n\
    [\n\
        "NAME:ConeParameters",\n\
        "XCenter:="		, "'+corr[0]+ut+'",\n\
        "YCenter:="		, "'+corr[1]+ut+'",\n\
        "ZCenter:="		, "'+corr[2]+ut+'",\n\
        "WhichAxis:="		, "'+axis+'",\n\
        "Height:="		, "'+h+ut+'",\n\
        "BottomRadius:="	, "'+br+ut+'",\n\
        "TopRadius:="		, "'+tr+ut+'"\n\
    ], \n\
    [\n\
        "NAME:Attributes",\n\
        "Name:="		, "'+name+'",\n\
        "Flags:="		, "",\n\
        "Color:="		, "(143 175 143)",\n\
        "Transparency:="	, 0,\n\
        "PartCoordinateSystem:=", "Global",\n\
        "UDMId:="		, "",\n\
        "MaterialValue:="	, "\\"'+material+'\\"",\n\
        "SurfaceMaterialValue:=", "\\"\\"",\n\
        "SolveInside:="		, '+solveinside+',\n\
        "IsMaterialEditable:="	, True,\n\
        "UseMaterialAppearance:=", False,\n\
        "IsLightweight:="	, False\n\
    ])')

    def HfssDrawCylinder(self,name,corr,axis,r,h,material,solveinside,unit=None):
        if unit:
            ut = unit
        else:
            ut = 'mm'
        self.fid.write('\noEditor.CreateCylinder(\n\
    [\n\
        "NAME:CylinderParameters",\n\
        "XCenter:="		, "'+corr[0]+ut+'",\n\
        "YCenter:="		, "'+corr[1]+ut+'",\n\
        "ZCenter:="		, "'+corr[2]+ut+'",\n\
        "Radius:="		, "'+r+ut+'",\n\
        "Height:="		, "'+h+ut+'",\n\
        "WhichAxis:="		, "'+axis+'",\n\
        "NumSides:="		, "0"\n\
    ], \n\
    [\n\
        "NAME:Attributes",\n\
        "Name:="		, "'+name+'",\n\
        "Flags:="		, "",\n\
        "Color:="		, "(143 175 143)",\n\
        "Transparency:="	, 0,\n\
        "PartCoordinateSystem:=", "Global",\n\
        "UDMId:="		, "",\n\
        "MaterialValue:="	, "\\"'+material+'\\"",\n\
        "SurfaceMaterialValue:=", "\\"\\"",\n\
        "SolveInside:="		, '+solveinside+',\n\
        "IsMaterialEditable:="	, True,\n\
        "UseMaterialAppearance:=", False,\n\
        "IsLightweight:="	, False\n\
    ])')

    def HfssDrawBox(self,name,corr,size,material,solveinside,unit=None):
        if unit:
            ut = unit
        else:
            ut = 'mm'
        self.fid.write('\noEditor.CreateBox(\n\
	[\n\
		"NAME:BoxParameters",\n\
		"XPosition:="		, "'+corr[0]+ut+'",\n\
		"YPosition:="		, "'+corr[1]+ut+'",\n\
		"ZPosition:="		, "'+corr[2]+ut+'",\n\
		"XSize:="		, "'+size[0]+ut+'",\n\
		"YSize:="		, "'+size[1]+ut+'",\n\
		"ZSize:="		, "'+size[2]+ut+'"\n\
	], \n\
	[\n\
		"NAME:Attributes",\n\
		"Name:="		, "'+name+'",\n\
		"Flags:="		, "",\n\
		"Color:="		, "(143 175 143)",\n\
		"Transparency:="	, 0,\n\
		"PartCoordinateSystem:=", "Global",\n\
		"UDMId:="		, "",\n\
		"MaterialValue:="	, "\\"'+material+'\\"",\n\
		"SurfaceMaterialValue:=", "\\"\\"",\n\
		"SolveInside:="		, '+solveinside+',\n\
		"IsMaterialEditable:="	, True,\n\
		"UseMaterialAppearance:=", False,\n\
		"IsLightweight:="	, False\n\
	])')

    def HfssUnite(self,name,keep='False'):
            self.fid.write('\noEditor.Unite(\n\
	[\n\
		"NAME:Selections",\n\
		"Selections:="		, "'+name+'"\n\
	], \n\
	[\n\
		"NAME:UniteParameters",\n\
		"KeepOriginals:="	, '+keep+'\n\
	])\n\
')

    def HfssSubtract(self,blank,tool,keep='False'):
        self.fid.write('\noEditor.Subtract(\n\
	[\n\
		"NAME:Selections",\n\
		"Blank Parts:="		, "'+blank+'",\n\
		"Tool Parts:="		, "'+tool+'"\n\
	], \n\
	[\n\
		"NAME:SubtractParameters",\n\
		"KeepOriginals:="	, '+keep+'\n\
	])\n\
')