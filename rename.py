import maya.cmds as cmds

sel = cmds.ls(v=True, dag=True, shapes=True)
for shape in sel:
    cmds.rename(shape, "{0}Shape".format(cmds.listRelatives(shape, parent=True)[0]))
