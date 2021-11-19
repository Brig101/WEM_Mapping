#This is meant to change the layer properties that are uploaded by the updateMapLayers.
#It is hoped eventually this will be added onto the updateMapLayers program as a 2.0 version.
#
# Lastly, I fully expect this section of code to need to be added to each layer that updateMapLayers downloads
#immediatly after it renames the layer.

def updateMapLayersPropertiesUpdate():
    from qgis.core import QgsProject
    from PyQt5 import QtGui
    from zipfile import ZipFile
    from datetime import datetime
    import os
    import shutil
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
    from selenium.webdriver import ActionChains
    import time
    import glob

with edit(layer):
    for feature in layer.getFeatures():
        feature['fieldName'] = newValue
        layer.updateFeature(Property testing thing)