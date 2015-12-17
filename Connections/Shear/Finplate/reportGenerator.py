'''
Created on Dec 10, 2015

@author: deepa
'''
<<<<<<< HEAD
'''
Created on Dec 10, 2015

@author: deepa
'''
import time

def save_html(): # (outObj, uiObj, dictBeamData, dictColData)
    fileName = '/home/deepa/finPlateReport.html'
=======
import time

def save_html(): # (outObj, uiObj, dictBeamData, dictColData)
    fileName = 'output/finplate/finPlateReport.html'
>>>>>>> origin/master
    # /home/deepa/EclipseWorkspace/OsdagLive/Connections/Shear/Finplate/output
    f = open(fileName,'w')
    f.write(t('html'))
    f.write(t('head'))
    f.write(t('''link rel="stylesheet" type="text/css" href="mystyle.css"'''))
    f.write(t('/head'))
    f.write(t('body')) 
    f.write(t('div id="logodiv"'))
    f.write(t('img src="osdag_logo.png" style="width:100px;height:100px;" '))
  

    f.write(t('img src="osdagname.png"  style="width:300px;height:50px;"'))
    f.write(t('/div'))    
    f.write(t('div id="dateDiv"'))
    f.write('Date:'+ time.strftime("%d/%m/%Y"))
    f.write(t('/div'))   

    #---------------------
   
    
    rstr = t('table')
    rstr += t('''col width=70%''')
    rstr += t('''col width=30%''')
    

    row = [0, 'Project Summary', ' ']
    rstr += t('tr')
    rstr += t('td colspan="2" class="header0"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')

    row = [1, "Project Title", "Finplate Connection"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header1"') + row[2] + t('/td')
    rstr += t('/tr')

    row = [1, "Company", "Osdag"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header1"') + row[2] + t('/td')
    rstr += t('/tr')

    row = [1, "Designer", "Hashmi Suhel"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header1"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Job Number", "test_1"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header1"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Design Code", "IS 800:2007"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header1"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Method", "Limit state design (LSD)"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header1"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Design Conclusion", "IS800:2007/Limit state design"]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header0"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
     
    row = [1, "Finplate", "Pass"]
    rstr += t('tr')
    rstr += t('td class="header1 "') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header1 safe"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Finplate", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header0"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Connection Properties", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1_1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Connection ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Connection Title", " Single Finplate"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Connection Type", "Shear Connection"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Connection Category ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Connectivity", "Column Web Beam Web"]
<<<<<<< HEAD
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Beam Connection", "Bolted"]
=======
>>>>>>> origin/master
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
<<<<<<< HEAD
=======
    row = [1, "Beam Connection", "Bolted"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
>>>>>>> origin/master
    row = [1, "Column Connection", "Welded"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Loading (Factored Load) ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Shear Force (kN)", "140"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    
    row = [0, "Components ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Column Section", "ISSC 200"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Material", "Fe250"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Beam Section", "ISMB 400"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Material", "Fe250"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Hole", "STD"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Plate Section ", "PLT 300X10X100 "]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Thickness (mm)", "10"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Width (mm)", "10"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Depth (mm)", "300"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Hole", "STD"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Weld ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Type", "Double Fillet"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Size (mm)", "6"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Bolts ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Type", "HSFG"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Grade", "8.8"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Diameter (mm)", "20"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Bolt Numbers", "3"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Columns (Vertical Lines)", "1 "]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Bolts Per Column", "3"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Gauge (mm)", "0"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Pitch (mm)", "100"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "End Distance (mm)", "50"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Edge Distance (mm)", "50"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Assembly ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Column-Beam Clearance (mm)", "20"]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    rstr += t('/table')
    
    rstr += t('table border="1"')
    row = [0, "Views", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class=" viewtbl header1_1"') + space(row[0]) + row[1] + t('/td')
    #rstr += t('td class=" viewtbl "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, '<img src="webconnWBg.png" width = "600">', '<img src="finTop.png" width = "600"> ']
    rstr += t('tr')
    rstr += t('td  align="center" class=" viewtbl"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td  align="center" class=" viewtbl"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, '<img src="finSide.png" width = "300"> ', '<img src="finfront.png" width = "600"> ']
    rstr += t('tr')
    rstr += t('td align="center" class=" viewtbl"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td align="center" class=" viewtbl "') + row[2] + t('/td')
    rstr += t('/tr')
    
    rstr += t('/table')
    
    rstr += t('table')
<<<<<<< HEAD
    row = [0, "Views", " "]
    rstr += t('tr')
    rstr += t('td class=" viewtbl"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class=" viewtbl "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "1", " 1st "]
    rstr += t('tr')
    rstr += t('td class=" viewtbl"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class=" viewtbl"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "2", "2nd "]
    rstr += t('tr')
    rstr += t('td class=" viewtbl"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class=" viewtbl "') + row[2] + t('/td')
=======
    row = [0, "Design Check", " "]
    rstr += t('tr')
    rstr += t('td colspan="4" class="header1_1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Check","Required","Provided","Remark"]
    rstr += t('td class="header2_hder"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2_hder"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2_hder"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2_hder"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt shear capacity (kN)"," ","<i>V</i><sub>dsb</sub> = ((800*0.6123*20*20)/(&#8730;3*1.25*1000) = 90.53 <br> [cl. 10.3.3]"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt bearing capacity (kN)",""," <i>V</i><sub>dsb</sub> = (2.5*0.5*20*8.9*410)  = 72.98<br> [cl. 10.3.4]"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt capacity (kN)","","Min (90.53,72.98) = 72.98","<p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"No. of bolts","140/72.98 = 1.9","3","<p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    
    rstr += t('tr')
    row =[0,"No.of column(s)","&#8804;2","1"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"No. of bolts per column"," ","3"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt pitch (mm)","&#8805;2.5*20 = 50, &#8804; Min(32*8.9, 300) = 300 <br> [cl. 10.2.2]","100"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt gauge (mm)","&#8805;2.5*20 = 50,&#8804; Min(32*8.9, 300) = 300 <br> [cl. 10.2.2]","0"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"End distance (mm)","&#8805;1.7* 22 = 37.4,&#8804;12*8.9 = 106.9 <br> [cl. 10.2.4]","50"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Edge distance (mm)","&#8805; 1.7* 22 = 37.4,&#8804;12*8.9 = 106.9<br> [cl. 10.2.4]","50"," <p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    
    rstr += t('tr')
    row =[0,"Plate thickness (mm)","(5*140*1000)/(300*250)= 9.33","10"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Plate height (mm)","","300"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Plate width (mm)","","100"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Plate moment capacity (kNm)","(2*90.5*100<sup>2</sup>)/100 = 18.1","<i>M</i><sub>d</sub> =1.2*250*<i>Z</i> = 40.9 <br>[cl. 8.2.1.2]","<p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Weld thickness (mm)","&#8804;5.27","6"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Weld strength (kN/mm)","&#8730;[(18100*6)/(2*288)<sup>2</sup>]<sup>2</sup> + [140/(2*288)]<sup>2</sup> <br>=0.699","<i>f</i><sub>v</sub>=(6*250)/(&#8730;3*1.25*1000)<br>= 0.96<br>[cl. 10.5.7]"," <p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
>>>>>>> origin/master
    rstr += t('/tr')
    
    rstr += t('/table')
    
<<<<<<< HEAD
    rstr += t('table')
    row = [0, "Design Check", " "]
    rstr += t('tr')
    rstr += t('td colspan="3" class="header1_1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Check","Required","Provided"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2_col1"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2_col1"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt shear capacity (kN)","<i>V</i><sub>dsb</sub> = ((800*0.6123*20*20)/(&#8730;3*1.25*1000) = 90.53 <br> [cl. 10.3.3]",""]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt bearing capacity (kN)","<i>V</i><sub>dsb</sub> = (2.5*0.5*20*8.9*410)  = 72.98<br> [cl. 10.3.4]",""]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt Capacity (kN)","Min (90.53,72.98) = 72.98","<p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"No. of bolts","140/72.98 = 1.9","3"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"No.of column(s)","&#8804;2","1"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"No. of bolts per column"," ","3"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt pitch (mm)","&#8805;2.5*20 = 50, &#8804; Min(32*8.9, 300) = 300 <br> [cl. 10.2.2]","100"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Bolt gauge (mm)","&#8805;2.5*20 = 50,&#8804; Min(32*8.9, 300) = 300 <br> [cl. 10.2.2]","0"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"End distance (mm)","&#8805;1.7* 22 = 37.4,&#8804;12*8.9 = 106.9 <br> [cl. 10.2.4]","50"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Edge distance (mm)","&#8805; 1.7* 22 = 37.4,&#8804;12*8.9 = 106.9<br> [cl. 10.2.4]","50"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    
    rstr += t('tr')
    row =[0,"Plate thickness (mm)","9.33","10"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Plate height (mm)","","300"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Plate width (mm)","","100"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Plate moment capacity (kNm)","18.1","<i>M</i><sub>d</sub> =1.2*250*Z = 40.9 <br>[cl. 8.2.1.2]<p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Weld thickness (mm)","6","6"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Weld strength (kN/mm)","0.699","<i>f</i><sub>v</sub>=(6*250)/(&#8730;3*1.25*1000)<br>= 0.96<br>[cl. 10.5.7] <p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    rstr += t('/table')
    
=======
>>>>>>> origin/master
    
    f.write(rstr)
    f.write(t('/body'))        
    f.write(t('/html'))    
    f.close()
    

def space(n):
    rstr = "&nbsp;" * 4 * n
    return rstr

def t(n):
    return '<' + n + '>'

def quote(m):
    return '"' + m + '"'

if __name__ == '__main__':
    save_html()
    print "hiiiiii"