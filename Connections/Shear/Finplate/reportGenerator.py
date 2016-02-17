'''
Created on Dec 10, 2015

@author: deepa
'''
from __builtin__ import str

'''
Created on Dec 10, 2015

@author: deepa
'''
import time
import math
from PyQt4.QtCore import QString


def save_html(outObj, uiObj, dictBeamData, dictColData):
    fileName = 'output/finplate/finPlateReport.html'
    f = open(fileName,'w')
    f.write(t('html'))
    f.write(t('head'))
    f.write(t('''link rel="stylesheet" type="text/css" P.breakhere {page-break-before: always} href="mystyle.css"'''))
    f.write(t('/head'))
    f.write(t('body')) 
    f.write(t('div id="logodiv"'))
    #f.write(t('img src="osdag_logo.png" style="width:100px;height:100px;" '))
    #f.write(t('img src="osdagname.png"  style="width:300px;height:50px;"'))
    f.write(t('img src="Osdag_header.png"  style="width:300px;height:80px;"'))
    f.write(t('/div'))    
    f.write(t('div id="dateDiv"'))
    f.write('Date:'+ time.strftime("%d/%m/%Y"))
    f.write(t('/div'))
    print "printing outObj"   
    print outObj

    #---------------------
    # Data params
    connectivity = str(uiObj['Member']['Connectivity'])
    shear_load = str(uiObj['Load']['ShearForce (kN)'])
    column_sec = str(uiObj['Member']['ColumSection'])
    beam_sec = str(uiObj['Member']['BeamSection'])
    plateThick = str(uiObj['Plate']['Thickness (mm)'])
    boltType = str(uiObj['Bolt']['Type'])
    boltGrade = str(uiObj['Bolt']['Grade'])
    boltDia = str(uiObj['Bolt']['Diameter (mm)'])
    #'Size (mm)'
    weld_Thick = str(uiObj['Weld']['Size (mm)'])
    
    
    plateWidth = str(int(round(outObj['Plate']['width'],1)))
    plateLength = str(int(round(outObj['Plate']['height'],1)))
    weldSize = str(int(round(outObj['Weld']['thickness'],1)))
    
    plateDimension = plateLength +'X'+ plateWidth + 'X'+ plateThick
    noOfBolts = str(outObj['Bolt']['numofbolts'])
    noOfRows = str(outObj['Bolt']['numofrow'])
    noOfCol = str(outObj['Bolt']['numofcol'])
    edge = str(int(round(outObj['Bolt']['edge'],1)))
    gauge = str(int(round(outObj['Bolt']['gauge'],1)))
    pitch = str(int(round(outObj['Bolt']['pitch'],1)))
    end = str(int(round(outObj['Bolt']['enddist'],1)))
    weld_strength = str(round(float(outObj['Weld']['weldstrength']/1000),3))
    moment_demand = str(outObj['Plate']['externalmoment'])
    gap = '20'
    beam_tw = str(float(dictBeamData[QString("tw")]))
    
    
    bolt_fu = str(outObj['Bolt']['bolt_fu'])
    bolt_dia = str(outObj['Bolt']['bolt_dia'] )
    kb = str(outObj['Bolt']['k_b'])
    beam_w_t = str(outObj['Bolt']['beam_w_t'] )
    web_plate_t = str(outObj['Bolt']['web_plate_t'])
    beam_fu = str(outObj['Bolt']['beam_fu'])
    dia_hole = str(outObj['Bolt']['dia_hole'])
    web_plate_fy = str(outObj['Plate']['web_plate_fy'])
    weld_fu = str(outObj['Weld']['weld_fu'] )
    weld_l = str(outObj['Weld']['effectiveWeldlength'])
    shearCapacity = str(round(outObj['Bolt']['shearcapacity'],3))
    bearingcapacity = str(round(outObj['Bolt']['bearingcapacity'],4))
    momentDemand = str(outObj['Plate']['externalmoment'])
    
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

    row = [1, "Designer", "Subhrajit Dutta"]
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
    
    #row = [1, "Connectivity", "Column Web Beam Web"]
    row = [1, "Connectivity", connectivity]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Beam Connection", "Bolted"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    

    row = [1, "Beam Connection", "Bolted"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    

    row = [1, "Column Connection", "Welded"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Loading (Factored Load) ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    #row = [1, "Shear Force (kN)", "140"]
    row = [1,"Shear Force (kN)", shear_load]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    
    row = [0, "Components ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    #row = [1, "Column Section", "ISSC 200"]
    row = [1,"Column Section", column_sec]
    
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Material", "Fe 410"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [1, "Beam Section", "ISMB 400"]
    row = [1,"Beam Section",beam_sec]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Material", "Fe 410"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [2, "Hole", "STD"]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [1, "Plate Section ", "PLT 300X10X100 "]
    row = [1, "Plate Section",plateDimension]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Thickness (mm)", "10"]
    row = [2, "Thickness (mm)", plateThick]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Width (mm)", "10"]
    row = [2, "Width (mm)", plateWidth]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Depth (mm)", "300"]
    row = [2, "Depth (mm)", plateLength]
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
    
    #row = [2, "Size (mm)", "6"]
    row = [2, "Size (mm)", weldSize]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [1, "Bolts ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Type", "HSFG"]
    row = [2, "Type", boltType]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Grade", "8.8"]
    row = [2, "Grade", boltGrade]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Diameter (mm)", "20"]
    row = [2, "Diameter (mm)", boltDia]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Bolt Numbers", "3"]
    row = [2, "Bolt Numbers", noOfBolts]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Columns (Vertical Lines)", "1 "]
    row = [2, "Columns (Vertical Lines)", noOfCol]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Bolts Per Column", "3"]
    row = [2, "Bolts Per Column", noOfRows]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Gauge (mm)", "0"]
    row = [2, "Gauge (mm)", gauge]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Pitch (mm)", "100"]
    row = [2, "Pitch (mm)", pitch]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "End Distance (mm)", "50"]
    row = [2, "End Distance (mm)", end]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + row[2] + t('/td')
    rstr += t('/tr')
    
    #row = [2, "Edge Distance (mm)", "50"]
    row = [2, "Edge Distance (mm)", edge]
    rstr += t('tr')
    rstr += t('td class="header2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, "Assembly ", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    #row = [1, "Column-Beam Clearance (mm)", "20"]
    row = [1, "Column-Beam Clearance (mm)", gap]
    rstr += t('tr')
    rstr += t('td class="header1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2 "') + row[2] + t('/td')
    rstr += t('/tr')
    
    rstr += t('/table')
    
#     rstr += t('p style="page-break-after:always;"')
#     rstr += t('/p')
    rstr +=t('footer')
#     rstr += t('p>Posted by: Deepa</p')
#     rstr += t('p>Posted by: Deepa</p')
#     rstr += t('p>Posted by: Deepa</p')
#     rstr += t('p>Posted by: Deepa</p')
#     rstr += t('p>Posted by: Deepa</p')
#     rstr += t('p>Posted by: Deepa</p')
    rstr += t('/footer')
    rstr += t('P CLASS="breakhere"')
    
    rstr += t('table border="1"')
    row = [0, "Views", " "]
    rstr += t('tr')
    rstr += t('td colspan="2" class=" viewtbl header1_1"') + space(row[0]) + row[1] + t('/td')
    #rstr += t('td class=" viewtbl "') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, '<object type="image/PNG" data="3D_Model.png"width ="500"></object>', '<object type="image/svg+xml" data="finTop.svg"width ="500"></object>']
    rstr += t('tr')
    rstr += t('td  align="center" class=" viewtbl"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td  align="center" class=" viewtbl"') + row[2] + t('/td')
    rstr += t('/tr')
    
    row = [0, '<object type="image/svg+xml" data="finSide.svg"width ="320"></object>', '<object type="image/svg+xml" data="finFront.svg"width ="650"></object>']
    rstr += t('tr')
    rstr += t('td align="center" class=" viewtbl"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td align="center" class=" viewtbl "') + row[2] + t('/td')
    rstr += t('/tr')
    
    rstr += t('/table')
#     rstr += t('p style="page-break-after:always;"')
#     rstr += t('/p')
    rstr += t('table')
    rstr += t('P CLASS="breakhere"')

    row = [0, "Design Check", " "]
    
    rstr += t('tr')
    rstr += t('td colspan="4" class="header1_1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Check","Required","Provided","Remark"]
    rstr += t('td class="header1_2"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header1_2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header1_2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header1_2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    const = str(round(math.pi/4 *0.78,4))
    #row =[0,"Bolt shear capacity (kN)"," ","<i>V</i><sub>dsb</sub> = ((800*0.6123*20*20)/(&#8730;3*1.25*1000) = 90.53 <br> [cl. 10.3.3]"]
    row =[0,"Bolt shear capacity (kN)"," ", "<i>V</i><sub>dsb</sub> = ((" + bolt_fu + "*" + const + "*" + bolt_dia + "*" + bolt_dia +")/(&#8730;3*1.25*1000) = " + shearCapacity + "<br> [cl. 10.3.3]"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Bolt bearing capacity (kN)",""," <i>V</i><sub>dsb</sub> = (2.5*0.5*20*8.9*410)  = 72.98<br> [cl. 10.3.4]"]
    row =[0,"Bolt bearing capacity (kN)",""," <i>V</i><sub>dsb</sub> = (2.5*"+ kb +"*" + bolt_dia + "*" + beam_tw +"*"+beam_fu +")/(1.25*1000)  =" + bearingcapacity + "<br> [cl. 10.3.4]"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Bolt capacity (kN)","","Min (90.53,72.98) = 72.98","<p align=right style=color:green><b>Pass</b></p>"]
    boltCapacity = bearingcapacity if bearingcapacity < shearCapacity else shearCapacity
    row =[0,"Bolt capacity (kN)","","Min (" + shearCapacity + "," + bearingcapacity + ") =" + boltCapacity  , "<p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"No. of bolts","140/72.98 = 1.9","3","<p align=right style=color:green><b>Pass</b></p>"]
    bolts = str(round(float(shear_load)/float(boltCapacity),1))
    row =[0,"No. of bolts", shear_load + "/" + boltCapacity + "=" + bolts, noOfBolts, " <p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"No.of column(s)","&#8804;2","1"]
    row =[0,"No.of column(s)","&#8804;2",noOfCol]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"No. of bolts per column"," ","3"]
    row =[0,"No. of bolts per column"," ",noOfRows]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Bolt pitch (mm)","&#8805;2.5*20 = 50, &#8804; Min(32*8.9, 300) = 300 <br> [cl. 10.2.2]","100"]
    minPitch =str(int(2.5 * float(bolt_dia)))
    maxPitch = str(300) if 32 * float(beam_tw)> 300 else str(int(math.ceil(32*float(beam_tw))))
    row =[0,"Bolt pitch (mm)","&#8805;2.5* "+ bolt_dia + "=" + minPitch +", &#8804; Min(32*"+ beam_tw +", 300) = "+ maxPitch +"<br> [cl. 10.2.2]",pitch]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Bolt gauge (mm)","&#8805;2.5*20 = 50,&#8804; Min(32*8.9, 300) = 300 <br> [cl. 10.2.2]","0"]
    minGauge =str(int(2.5 * float(bolt_dia)))
    maxGauge = str(300) if 32 * float(beam_tw)> 300 else str(int(math.ceil(32*float(beam_tw))))
    row =[0,"Bolt gauge (mm)","&#8805;2.5*"+ bolt_dia+ "=" +minGauge+", &#8804; Min(32*" + beam_tw + ", 300) = "+ maxGauge + " <br> [cl. 10.2.2]",gauge]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"End distance (mm)","&#8805;1.7* 22 = 37.4,&#8804;12*8.9 = 106.9 <br> [cl. 10.2.4]","50"]
    minEnd = str(1.7 * float(dia_hole))
    maxEnd = str(12*float(beam_tw))
    row =[0,"End distance (mm)","&#8805;1.7*" + dia_hole+"=" +minEnd+", &#8804;12*"+beam_tw+" = "+maxEnd+" <br> [cl. 10.2.4]",end]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Edge distance (mm)","&#8805; 1.7* 22 = 37.4,&#8804;12*8.9 = 106.9<br> [cl. 10.2.4]","50"," <p align=right style=color:green><b>Pass</b></p>"]
    minEdge = str(1.7 * float(dia_hole))
    maxEdge = str(12*float(beam_tw))
    row =[0,"Edge distance (mm)","&#8805;1.7*"+ dia_hole+ " = "+minEdge+",&#8804;12*"+beam_tw+" = "+maxEdge+"<br> [cl. 10.2.4]",edge," <p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Plate thickness (mm)","(5*140*1000)/(300*250)= 9.33","10"]
    minPlateThick = str(round(5 * float(shear_load) * 1000/(float(plateLength)*float(web_plate_fy)),2))
    row =[0,"Plate thickness (mm)","(5*" + shear_load + "*1000)/(" + plateLength + "*" + plateWidth + ")="+ minPlateThick,plateThick]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Plate height (mm)","","300"]
    #row =[0,"Plate height (mm)","",plateLength]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    row =[0,"Plate width (mm)","","100"]
    #row =[0,"Plate width (mm)","",plateWidth]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Plate moment capacity (kNm)","(2*90.5*100<sup>2</sup>)/100 = 18.1","<i>M</i><sub>d</sub> =1.2*250*<i>Z</i> = 40.9 <br>[cl. 8.2.1.2]","<p align=right style=color:green><b>Pass</b></p>"]
    z = math.pow(float(plateLength),2)* (float(plateThick)/(6 *1.1* 1000000))
    momentCapacity = str(round(1.2 * float(web_plate_fy)* z,2))
    row =[0,"Plate moment capacity (kNm)","(2*"+shearCapacity+"*"+pitch+"<sup>2</sup>)/("+pitch+"*1000) ="+ moment_demand,"<i>M</i><sub>d</sub> =(1.2*" +web_plate_fy+"*<i>Z</i>)/(1000*1.1) = "+ momentCapacity +"<br>[cl. 8.2.1.2]","<p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Effective weld length (mm)","","300 - 2*6 = 288"]
    effWeldLen = str(int(float(plateLength)-(2*float(weld_Thick))))
    row =[0,"Effective weld length (mm)","",  plateLength + "-2*" + weld_Thick +"=" + effWeldLen]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Weld strength (kN/mm)","&#8730;[(18100*6)/(2*288)<sup>2</sup>]<sup>2</sup> + [140/(2*288)]<sup>2</sup> <br>=0.699","<i>f</i><sub>v</sub>=(0.7*6*410)/(&#8730;3*1.25)<br>= 0.795<br>[cl. 10.5.7]"," <p align=right style=color:green><b>Pass</b></p>"]
    a = float(2*float(effWeldLen))
    b = 2*math.pow((float(effWeldLen)),2)
    x = (float(momentDemand) * 1000 * 6)
    resultant_shear = str(round(math.sqrt(math.pow((x/b),2) + math.pow((float(shear_load)/a),2)),3))
    momentDemand_knmm = str(int(float(momentDemand) * 1000))
    row =[0,"Weld strength (kN/mm)","&#8730;[("+momentDemand_knmm+"*6)/(2*"+effWeldLen+"<sup>2</sup>)]<sup>2</sup> + ["+shear_load+"/(2*"+effWeldLen+")]<sup>2</sup> <br>="+ resultant_shear ,"<i>f</i><sub>v</sub>=(0.7*"+weldSize+"*"+weld_fu+")/(&#8730;3*1.25)<br>="+ weld_strength+"<br>[cl. 10.5.7]"," <p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')
    rstr += t('/tr')
    
    rstr += t('tr')
    #row =[0,"Weld thickness (mm)","(0.699*&#8730;3*1.25)/(0.7*410)=5.27<br>[cl. 10.5.7]","6","<p align=right style=color:green><b>Pass</b></p>"]
    weld_thickness = str(round((float(resultant_shear) * 1000*(math.sqrt(3) * 1.25))/(0.7 * float(weld_fu)),2))
    row =[0,"Weld thickness (mm)","("+resultant_shear+"*&#8730;3*1.25)/(0.7*"+weld_fu+")="+weld_thickness+"<br>[cl. 10.5.7]",weldSize,"<p align=right style=color:green><b>Pass</b></p>"]
    rstr += t('td class="header2_col1"') + space(row[0]) + row[1] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[2] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[3] + t('/td')
    rstr += t('td class="header2"') + space(row[0]) + row[4] + t('/td')

    rstr += t('/tr')
    rstr += t('/table')
    
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


