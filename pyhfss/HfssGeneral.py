class HfssGeneral:
    def __init__(self,f=None):
        if f:
            self.fid = f
        else:
            self.fid = open('tmp.py','w')
        self.fid.write('import ScriptEnv\n\
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")\n\
oDesktop.RestoreWindow()\n'
                        )

    def HfssNewProject(self):
        self.fid.write('\noProject = oDesktop.NewProject()')

    def HfssInsertDesign(self,name=None,model=None):
        if name:
            if model:
                self.fid.write('\noProject.InsertDesign("HFSS", "'+name+'", "'+model+'", "")')
            else:
                self.fid.write('\noProject.InsertDesign("HFSS", "' + name + '", "DrivenModal", "")')
            self.fid.write('\noDesign = oProject.SetActiveDesign("'+name+'")')
        else:
            if model:
                self.fid.write('\noProject.InsertDesign("HFSS", "HFSSDesign1", "' + model + '", "")')
            else:
                self.fid.write('\noProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")')
            self.fid.write('\noDesign = oProject.SetActiveDesign("HFSSDesign1")')

    def HfssSaveAs(self,name=None):
        if name:
            self.fid.write('\noProject.SaveAs("'+name+'", True)')
        else:
            self.fid.write('\noProject.SaveAs("tmp.aedt", True)')

    def HfssSave(self):
        self.fid.write('\noProject.Save()')

    def HfssClosefid(self):
        self.fid.close()

    def HfssAddParameter(self,name,value,unit):
        self.fid.write(\
            '\noDesign.ChangeProperty(\n\
	    [\n\
		"NAME:AllTabs",\n\
		[\n\
			"NAME:LocalVariableTab",\n\
			[\n\
				"NAME:PropServers",\n\
				"LocalVariables"\n\
			],\n\
			[\n\
				"NAME:NewProps",\n\
				[\n\
					"NAME:'+name+'",\n\
					"PropType:="		, "VariableProp",\n\
					"UserDef:="		, True,\n\
					"Value:="		, "'+value+unit+'"\n\
				]\n\
			]\n\
		]\n\
	])')