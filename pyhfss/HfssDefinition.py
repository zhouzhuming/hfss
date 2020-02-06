class HfssDefinition:
    def __init__(self,f):
        self.fid = f
        self.fid.write('\noDefinitionManager = oProject.GetDefinitionManager()')

    def HfssAddmaterial(self,name,dk,df,freq):
        self.fid.write('\noDefinitionManager.AddMaterial(\n\
	[\n\
		"NAME:'+name+'",\n\
		"CoordinateSystemType:=", "Cartesian",\n\
		"BulkOrSurfaceType:="	, 1,\n\
		[\n\
			"NAME:PhysicsTypes",\n\
			"set:="			, ["Electromagnetic"]\n\
		],\n\
		"permittivity:="	, "'+dk+'",\n\
		"dielectric_loss_tangent:=", "'+df+'",\n\
		"delta_H_freq:="	, "'+freq+'"\n\
	])')