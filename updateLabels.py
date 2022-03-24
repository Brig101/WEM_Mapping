# Function updating QGIS labels. Copies old files, moves them into new folder with todays date, runs R Scripts that alter
# the downloaded files from iLandman.


import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, ElementClickInterceptedException
import os
#from selenium.webdriver import ActionChains

# =============================================================================
# Peters old environment paths:
# os.environ['PYTHONHOME'] = r'C:\Users\Accounting\Anaconda3'
# os.environ['PYTHONPATH'] = r'C:\Users\Accounting\Anaconda3\lib\site-packages'
# os.environ['R_HOME'] = 'C:/Program Files/R/R-4.0.2'
# os.environ['R_USER'] = r'C:\Users\Accounting\Anaconda3\envs\rstudio'
# =============================================================================

#Set paths so python knows where to look for R code
os.environ['PYTHONHOME'] = r'C:\Users\GISUser\anaconda3'
os.environ['PYTHONPATH'] = r'C:\Users\GISUser\anaconda3\Lib\site-packages'
os.environ['R_HOME'] = r'C:\Users\GISUser\anaconda3\Lib\R'
os.environ['R_USER'] = r'C:\Users\GISUser\anaconda3\envs\rstudio'
# This makes R work
#import rpy2.robjects as ro
import time
import glob
from datetime import datetime
from labels import labels
from labels import leaseLabel


# Function that finds the element and waits for it to load before continuing


def updateLabels(webscrape, workingInterestFile, ownershipFile):
    if webscrape == True:

        # Set up
        user_email = r'duckmuck@verizon.net'
        user_password = r'Crinoid@252Ma'
        path = r'\\WEM-MASTER\Working Projects\WEMU Leasing\Python Codes\Python Code\chromedriver.exe'
        driver = webdriver.Chrome(path)

        # Go to iLandman
        driver.get(r'https://www.p2central.com/ilandman/Project')

        def findElement(XPATH):
            # path = r'\\WEM-MASTER\Working Projects\WEMU Leasing\Python Codes\Python Code\chromedriver.exe'
            # driver = webdriver.Chrome(path)
            find = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH)))
            return find

        # Log in
        email = findElement(
            r'//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div[2]/span/div/div/div/div/div/div/div/div/div/div[1]/div/input')
        counter = 0
        while counter < 10:
            try:
                email.click()
                counter = 10
            except ElementNotInteractableException:
                counter += 0.1

        email.click()
        email.send_keys(user_email)
        password = findElement(
            r'//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div[2]/span/div/div/div/div/div/div/div/div/div/div[2]/div/div/input')
        password.click()
        password.send_keys(user_password)
        password.send_keys(Keys.RETURN)
        
        #clicks WEM Uintah project
        project = findElement(r'//*[@id="projectList"]/table/tbody/tr/td[1]/a')
        project.click()
        
        #clicks ilandman Dropdown reports carrot
        reportdrop = findElement(r'//*[@id="menu"]/ul/li[6]/span/a')
        reportdrop.click()
        #clicks 'tract reports' button from dropdown menu
        tractreport = findElement(r'//*[@id="menu"]/ul/li[6]/div[1]/div/a[1]')
        tractreport.click()
        ##this option is not interactable... I think we can just skip it
        #tractr = findElement(r'//*[@id="Tract_reports"]/a')
        #tractr.click()
        time.sleep(1)
        ##following two lines are old, and have been replaced
        #tractowner = findElement(r'//*[@id="ui-id-2"]/div[contains(.,"Tract Ownership List")]/a')
        #tractowner.click()
        #This selects the "tract ownership list" excel 
        tractowner = findElement(r'//*[@id="ui-id-1"]/div[25]/a')
        tractowner.click()
        # Get download ID
        #target = findElement(f'//*[@id="filters"]/table/tbody/tr[11]/td[2]/div/a')
        target = findElement(r'/html/body/div[137]/div[2]/div[1]/div[2]')
        target = str(target.get_attribute('id'))
        ids = target[len('data-picker-'):-len('-advanced')]
        #selowner = findElement(f'//*[@id="data-picker-{ids}-trigger"]')
        selowner = findElement(f'//*[@id="data-picker-{ids}-trigger"]')
        selowner.click()
        bar = findElement(f'//*[@id="data-picker-{ids}-simple"]/div/input[2]')
        bar.click()
        #fourx = findElement(r'//*[@id="4108947"]')
        #fourx.click()
        bar.send_keys('WEM')
        wem = findElement(r'//*[@id="4081860"]')
        wem.click()
        wem2 = findElement(r'//*[@id="4220353"]')
        wem2.click()
        wem3 = findElement(r'//*[@id="4275915"]')
        wem3.click()
# =============================================================================
#         bar.click()
#         bar.clear()
#         bar.send_keys('UT 1808')
#         ut = findElement(r'//*[@id="4059790"]')
#         ut.click()
# =============================================================================
        ok = findElement(r'/html/body/div[137]/div[3]/div/button[2]/span')
        ok.click()
        viewreport = findElement(r'//*[@id="save-form"]')
        viewreport.click()
        time.sleep(15)
        #cls = findElement(r'/html/body/div[contains(.,"Generating")]/div[3]/div/button')
        #cls.click()
        x = findElement(r'/html/body/div[1]/table/tbody/tr/td[2]/a')
        x.click()
        close = findElement(r'/html/body/div[147]/div[3]/div/button/span')
        close.click()

        # Rename last download to ownership
        todayDate = datetime.date(datetime.now())
        time.sleep(5)
        ownerDate = r'ownerLabels ' + str(todayDate) + '.xlsx'
        list_of_files = glob.glob(r'C:\Users\GISUser\Downloads\*')
        ownership = max(list_of_files, key=os.path.getctime)
        newownerName = r'C:\\Users\\GISUser\\Downloads\\' + str(ownerDate)
        os.rename(ownership, newownerName)

        # Contract Reports
        contreport = findElement(r'//*[@id="contract-reports-submenu-link"]')
        contreport.click()
        #contreportbut = findElement(r'//*[@id="Contract_reports"]')
        #contreportbut.click()
        time.sleep(4)
        #workinginterest = findElement(r'//*[@id="ui-id-2"]/div[contains(.,"Working")]/a')
        workinginterest = findElement(r'//*[@id="ui-id-1"]/div[40]/a')
        workinginterest.click()
        target2 = findElement('//*[@id="filters"]/table/tbody/tr[1]/td[2]/div/a')
        target2 = str(target2.get_attribute('id'))
        ids2 = target2[len('data-picker-'):-len('-trigger')]
        showacres = findElement(f'//*[@id="data-picker-{ids2}-trigger"]')
        showacres.click()
        search = findElement(f'//*[@id="data-picker-{ids2}-simple"]/div/input[2]')
        search.click()
        search.send_keys('WEM')
        time.sleep(1)
        wemii = findElement(r'//*[@id="115153"]')
        wemii.click()
        wemi = findElement(r'//*[@id="90095"]')
        wemi.click()
        wemiii = findElement(r'//*[@id="122549"]')
        wemiii.click()
        okay = findElement(r'/html/body/div[contains(.,"OK")]/div[3]/div/button[2]')
        okay.click()
        target3 = findElement('//*[@id="filters"]/table/tbody/tr[3]/td[2]/div/a')
        target3 = str(target3.get_attribute('id'))
        ids3 = target3[len('data-picker-'):-len('-trigger')]
        contowner = findElement(f'//*[@id="data-picker-{ids3}-trigger"]')
        contowner.click()
        search2 = findElement(f'//*[@id="data-picker-{ids3}-simple"]/div/input[2]')
        search2.click()
        search2.send_keys('WEM')
        time.sleep(2)        
        #wem1 = findElement(f'//*[@id="data-picker-{ids3}-multiple-results"]/ul/li[2]')
        wem1 = findElement(r'//*[@id="90095"]')
        wem1.click()
        wem2 = findElement(r'//*[@id="115153"]')
        #wem2 = findElement(f'//*[@id="data-picker-{ids3}-multiple-results"]/ul/li[1]')
        wem2.click()
        wem3 = findElement(r'//*[@id="122549"]')
        wem3.click()
        time.sleep(1)
        #okkk = findElement(r'/html/body/div[97]/div[3]/div/button[2]')
        okkk = findElement(r'/html/body/div[98]/div[3]/div/button[2]/span')
        okkk.click()
        target4 = findElement('//*[@id="filters"]/table/tbody/tr[7]/td[2]/div/a')
        target4 = str(target4.get_attribute('id'))
        ids4 = target4[len('data-picker-'):-len('-trigger')]
        owntype = findElement(f'//*[@id="data-picker-{ids4}-trigger"]')
        owntype.click()
        own = findElement(r'//*[@id="Ownership"]')
        own.click()
        okk = findElement(r'/html/body/div[102]/div[3]/div/button[2]/span')
        okk.click()
        viewrep = findElement(r'//*[@id="save-form"]')
        viewrep.click()
        time.sleep(15)
        print('please waite... this step is hard for the computer to do')
        # TODO: This line doesn't work very well, the old XPath was [@id="ui-id-46"] and now its //*[@id="ui-id-50"]/p/p/a
        #time.sleep(5)
        #downloadclick = findElement(r'//*[@id="ui-id-50"]/p/p/a')
        #downloadclick.click()
        time.sleep(100)

        # Rename last download to leasehold
        todayDate = datetime.date(datetime.now())
        time.sleep(2)
        leasingDate = r'leasingLabels ' + str(todayDate) + '.xlsx'
        list_of_files = glob.glob(r'C:\Users\GISUser\Downloads\*')
        leasehold = max(list_of_files, key=os.path.getctime)
        newleaseName = r'C:\\Users\\GISUser\\Downloads\\' + str(leasingDate)
        os.rename(leasehold, newleaseName)

        
# =============================================================================
#This is the old directory that files were being saved to (for "Python Coding Labels v2" in QGIS).
#         # MAKE A COPY OF THE PREVIOUS FILES AND STORE THEM IN A NEW FOLDER WITH THE DATE
#         dir = r"//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/"
#         todayDate = datetime.date(datetime.now())
#         dateFolder = dir + str(todayDate) + ' Backup'
#         # check if directory exists or not yet
#         if not os.path.exists(dateFolder):
#             os.makedirs(dateFolder)
#         # move files into created directory
#         file_pathLeasing = r"//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/" \
#                            r"QGIS - WEM LEASE Crop List.csv"
#         file_pathOwnership = r'//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/' \
#                              r'QGIS - WEM, UT, 4X Import List.csv'
#         shutil.copy(file_pathLeasing, dateFolder)
#         shutil.copy(file_pathOwnership, dateFolder)
#         # rename the files
#         shutil.move(dateFolder + '/QGIS - WEM LEASE Crop List.csv',
#                     dateFolder + '/QGIS - WEM LEASE Crop List (moved ' + str(todayDate) + ').csv')
#         shutil.move(dateFolder + '/QGIS - WEM, UT, 4X Import List.csv',
#                     dateFolder + '/QGIS - WEM, UT, 4X Import List (moved ' + str(todayDate) + ').csv')
#         driver.quit()
# 
# =============================================================================

        # MAKE A COPY OF THE PREVIOUS FILES AND STORE THEM IN A NEW FOLDER WITH THE DATE
        dir = r"//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/Python Coding Labels v3/"
        todayDate = datetime.date(datetime.now())
        dateFolder = dir + str(todayDate) + ' Backup'
        # check if directory exists or not yet
        if not os.path.exists(dateFolder):
            os.makedirs(dateFolder)
        # move files into created directory
        file_LeasingWEM1 = r"//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/" \
                           r"Python Coding Labels v3/WEM1Leasehold.csv"
        file_pathOwnerWEM1 = r'//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/' \
                             r'Python Coding Labels v3/WEM1Ownership.csv'
        shutil.copy(file_LeasingWEM1, dateFolder)
        shutil.copy(file_pathOwnerWEM1, dateFolder)
        
        file_LeasingWEM2 = r"//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/" \
                           r"Python Coding Labels v3/WEM2Leasehold.csv"
        file_pathOwnerWEM2 = r'//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/' \
                             r'Python Coding Labels v3/WEM2Ownership.csv'
        shutil.copy(file_LeasingWEM2, dateFolder)
        shutil.copy(file_pathOwnerWEM2, dateFolder)
        
        file_LeasingWEM3 = r"//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/" \
                           r"Python Coding Labels v3/WEM3Leasehold.csv"
        file_pathOwnerWEM3 = r'//WEM-MASTER/Sensitive Data/WEM Uintah/Maps/QGIS/IMPORTANT EXCEL DOCS/QGIS/' \
                             r'Python Coding Labels v3/WEM3Ownership.csv'
        shutil.copy(file_LeasingWEM3, dateFolder)
        shutil.copy(file_pathOwnerWEM3, dateFolder)
        
        # rename the files
        shutil.move(dateFolder + '/WEM1Leasehold.csv',
                    dateFolder + '//WEM1Leasehold (moved ' + str(todayDate) + ').csv')
        shutil.move(dateFolder + '/WEM1Ownership.csv',
                    dateFolder + '//WEM1Ownership (moved ' + str(todayDate) + ').csv')
        driver.quit()

        shutil.move(dateFolder + '/WEM2Leasehold.csv',
                    dateFolder + '//WEM2Leasehold (moved ' + str(todayDate) + ').csv')
        shutil.move(dateFolder + '/WEM2Ownership.csv',
                    dateFolder + '//WEM2Ownership (moved ' + str(todayDate) + ').csv')
        driver.quit()
        
        shutil.move(dateFolder + '/WEM3Leasehold.csv',
                    dateFolder + '//WEM3Leasehold (moved ' + str(todayDate) + ').csv')
        shutil.move(dateFolder + '/WEM3Ownership.csv',
                    dateFolder + '//WEM3Ownership (moved ' + str(todayDate) + ').csv')
        driver.quit()        


    if webscrape == False:
        newleaseName = workingInterestFile
        newownerName = ownershipFile
        
    labels(newownerName, r'X:\WEM Uintah\Maps\QGIS\IMPORTANT EXCEL DOCS\QGIS\Python Coding Labels v3')
    leaseLabel(newleaseName, r'X:\WEM Uintah\Maps\QGIS\IMPORTANT EXCEL DOCS\QGIS\Python Coding Labels v3')
    
    
        
# =============================================================================
# This is the old R code. this has been replaced by labels and leaseLabel         
#     # RUN THE R SCRIPTS FIXING THE DATA FROM ILANDMAN TO QGIS
#     test = r"\\WEM-MASTER\Sensitive Data\WEM Uintah\Maps\Code\leasingLabels.R"
#     ro.r.source(test)
#     ro.r["leasingLabels"](newleaseName)  # Have the input to the function be the file path
#     fpOwnership = r"\\WEM-MASTER\Sensitive Data\WEM Uintah\Maps\Code\ownershipLabels.R"
#     ro.r.source(fpOwnership)
#     ro.r["ownershipLabels"](newownerName)
# =============================================================================


    print("Done!")


updateLabels(True, '', '')