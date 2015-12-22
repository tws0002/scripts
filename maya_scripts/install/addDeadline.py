import os
import maya.mel as mel
import maya.cmds as cmds
deadline_path = r"C:\\Program Files\\Autodesk\\Maya2016\\scripts\\startup\\DeadlineMayaClient.mel"
if os.path.exists(deadline_path):
    mel.eval('source "DeadlineMayaClient.mel";')

