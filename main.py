# encoding:utf-8
import os
import pyhfss.HfssGeneral as pg
import pyhfss.Hfss3DModeler as pd
def op():

    testscript = pg.HfssGeneral()
    testscript.HfssNewProject()
    testscript.HfssInsertDesign()
    testmodel = pd.Hfss3DModeler(testscript.fid)
    testmodel.HfssDrawBox('box2',['0','1','1'],['1','2','3'],'pec','False')
    testscript.HfssClosefid()

    os.system(r"D:\Software\AnsysEM\AnsysEM19.3\Win64\ansysedt.exe /RunScript D:\code\hfss\tmp.py")


if __name__ == '__main__':
    op()