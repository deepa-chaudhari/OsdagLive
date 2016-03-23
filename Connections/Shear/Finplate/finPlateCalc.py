'''
Created on 17-Mar-2016

@author: Subhrajit
'''
# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from model import *
from PyQt4.Qt import QString
import math

# Function for net area of ordinary bolts
# Source: Subramanian's book, page: 348
def netArea_calc(dia):
    netArea = {12:84.5, 16:157, 20:245, 22:303, 24:353, 27:459, 30:561, 36:817};
    return netArea[dia]

# BOLT: determination of shear capacity 
def bolt_shear(dia, n, fu):
    A = netArea_calc(dia)
    root3 = math.sqrt(3);
    Vs = fu * n * A / (root3 * 1.25 * 1000);
    Vs = round(Vs.real,3);
    return Vs
    
# BOLT: determination of bearing capacity 
def bolt_bearing(dia, t, kb, fu):
    Vb = 2.5 * kb * dia * t * fu / (1.25 * 1000);
    Vb = round(Vb.real,3);
    return Vb;
 

# PLATE HEIGHT: minimum height of fin plate
# [Source: INSDAG detailing manual, page: 5-7] 
def fin_min_h(beam_d):
    min_plate_ht = 0.6*beam_d;
    return min_plate_ht;

# PLATE THICKNESS: minimum thickness of fin plate
# Source: Subramanian's book, page: 373
def fin_min_thk(shear_load,bolt_fy,web_plate_l):
    min_plate_thk = (5*shear_load*1000)/(bolt_fy*web_plate_l);
    return min_plate_thk;

# PLATE THICKNESS: maximum thickness of fin plate
# [Source: INSDAG detailing manual, page: 5-7]
def fin_max_thk(beam_d):
    max_plate_thk = 0.5 * beam_d;
    return max_plate_thk;

def blockshear(numrow,numcol,dia_hole,fy,fu,edge_dist,end_dist,pitch,gauge,platethk):
    if numcol == 1:
        Avg = platethk * ((numrow-1)*pitch + end_dist)
        Avn = platethk * ((numrow-1)*pitch + end_dist - (numrow-1+0.5)*dia_hole)
        Atg = platethk * edge_dist
        Atn = platethk * (edge_dist - 0.5 * dia_hole)
        
        Tdb1 = (Avg * fy / (math.sqrt(3)*1.1) + 0.9 * Atn * fu / 1.25)
        Tdb2 = (0.9 * Avn * fu / (math.sqrt(3)*1.25) + Atg * fy / 1.1)
        Tdb = min (Tdb1,Tdb2)
        Tdb = round(Tdb/1000,3)
        
    elif numcol == 2:
        Avg = platethk * ((numrow-1)*pitch + end_dist)
        Avn = platethk * ((numrow-1)*pitch + end_dist - (numrow-1+0.5)*dia_hole)
        Atg = platethk * (edge_dist + gauge)
        Atn = platethk * (edge_dist + gauge - 0.5 * dia_hole)
        
        Tdb1 = (Avg * fy / (math.sqrt(3)*1.1) + 0.9 * Atn * fu / 1.25)
        Tdb2 = (0.9 * Avn * fu / (math.sqrt(3)*1.25) + Atg * fy / 1.1)
        Tdb = min (Tdb1,Tdb2)
        Tdb = round(Tdb/1000,3)
        
    return Tdb
        

##################################################################################
# Start of main program
def finConn(uiObj):
    global logger
    beam_sec = uiObj['Member']['BeamSection']
    column_sec = uiObj['Member']['ColumSection']
    connectivity = uiObj['Member']['Connectivity']
    beam_fu = uiObj['Member']['fu (MPa)']
    beam_fy = uiObj['Member']['fy (MPa)']
                  
    shear_load = uiObj['Load']['ShearForce (kN)']
                      
    bolt_dia = uiObj['Bolt']['Diameter (mm)']
    bolt_type  = uiObj["Bolt"]["Type"]
    bolt_grade = uiObj['Bolt']['Grade']
                  
    web_plate_t = uiObj['Plate']['Thickness (mm)']
    web_plate_w = uiObj['Plate']['Width (mm)']
    web_plate_l = uiObj['Plate']['Height (mm)']
    web_plate_fu = uiObj['Member']['fu (MPa)']
    web_plate_fy = uiObj['Member']['fy (MPa)']
                  
    weld_t = uiObj["Weld"]['Size (mm)']
     
#####################################################################################

# Hard-code input data required to check overall calculation as independent file  
#     beam_sec = 'ISMB300'
#     column_sec = 'ISSC180'
#     connectivity = 'Beam-Column'
#     beam_fu = 410
#     beam_fy = 250
#     beam_w_t = 8.9   
#     beam_d = 400
#     beam_f_t = 16  
#     beam_R1 = 18   
#                  
#     shear_load = 180
#                      
#     bolt_dia = 16
#     bolt_type  = 'HSFG'
#     bolt_grade = 4.8
#        
#                  
#     web_plate_t = 10
#     web_plate_w = 150
#     web_plate_l = 300
#     web_plate_fu = 410
#     web_plate_fy = 250
#                  
#     weld_t = 8
#     weld_fu = 410
#     bolt_planes = 1 
##################################################################################
    
    dictbeamdata  = get_beamdata(beam_sec)
    beam_w_t = float(dictbeamdata[QString("tw")])
    beam_f_t = float(dictbeamdata[QString("T")])
    beam_d = float(dictbeamdata[QString("D")])
    beam_R1 = float(dictbeamdata[QString("R1")])

    ########################################################################
    # INPUT FOR PLATE DIMENSIONS (FOR OPTIONAL INPUTS) AND VALIDATION
    
    # Plate thickness check
    if web_plate_t < beam_w_t:
        web_plate_t = beam_w_t
        logger.error(": Chosen web plate thickness is not sufficient" )
        logger.warning(" : Minimum required thickness %2.2f mm" % (beam_w_t))
    
    # Plate height check
    # Maximum/minimum plate height
    max_plate_height = beam_d - 2 * beam_f_t - 2* beam_R1 - 2*5; 
    min_plate_height = fin_min_h(beam_d);
#     min_plate_height = int(min_plate_height) /10 * 10 +10;
    min_plate_height = round(min_plate_height,3)
    
    # Plate height input and check for maximum and minimum values
             
    if web_plate_l != 0:
        if web_plate_l > max_plate_height :
            logger.error(": Height of plate is more than the clear depth of the beam")
            logger.warning(": Maximum plate height allowed is %2.2f mm " % (max_plate_height))
            web_plate_l = max_plate_height ; 
              
        elif min_plate_height > max_plate_height:
            logger.error(": Minimum required plate height is more than the clear depth of the beam")
            logger.warning(": Plate height required should be more than  %2.2f mm " % (min_plate_height))
            logger.warning(": Maximum plate height allowed is %2.2f mm " % (max_plate_height))
            logger.info(": Increase the plate thickness")
            web_plate_l = max_plate_height;
            
        elif min_plate_height >= web_plate_l:
            
            logger.error(": Plate height provided is less than the minimum required ")
            logger.warning(": Plate height required should be more than  %2.2f mm " % (min_plate_height))
            
            web_plate_l = min_plate_height 
    else:
        if min_plate_height < max_plate_height:
            web_plate_l = min_plate_height +10
        elif min_plate_height >= max_plate_height:
            web_plate_l = (max_plate_height-10)//10*10 ;
        
    
    ########################################################################
    # Bolt design function
    def boltDesign():
        # I: Check for number of bolts -------------------
        bolt_fu = int(bolt_grade) * 100
        bolt_fy = (bolt_grade - int(bolt_grade))*bolt_fu;
         
        # Spacing of bolts for web plate -------------------
        if bolt_dia == 12 or bolt_dia == 14:
            dia_hole = bolt_dia + 1
        elif bolt_dia == 16 or bolt_dia == 18 or bolt_dia == 20 or bolt_dia == 22 or bolt_dia == 24:
            dia_hole = bolt_dia + 2
        else:
            dia_hole = bolt_dia + 3    
     
        # Minimum spacing
        min_pitch = int(2.5 * bolt_dia);
        min_gauge = int(2.5 * bolt_dia);
        min_end_dist = int(1.7 * (dia_hole));
         
        # Calculation of kb
        kbChk1 = min_end_dist/float(3*dia_hole);
        kbChk2 = min_pitch/float(3*dia_hole)-0.25;
        kbChk3 = bolt_fu/float(beam_fu);
        kbChk4 = 1;
        kb = min(kbChk1,kbChk2,kbChk3,kbChk4);
        kb = round(kb,3)
         
        # Bolt capacity calculation
        t_thinner = min(beam_w_t.real,web_plate_t.real);
        bolt_planes = 1
        bolt_shear_capacity = bolt_shear(bolt_dia,bolt_planes,bolt_fu).real;
        bolt_bearing_capacity = bolt_bearing(bolt_dia,t_thinner,beam_fu,kb).real;
         
        bolt_capacity = min(bolt_shear_capacity, bolt_bearing_capacity);
         
        bolts_required = int(shear_load/bolt_capacity) + 1; 
        if bolts_required <= 2:
            bolts_required = 3;
         
        # Bolt group capacity
        bolt_group_capacity = bolts_required * bolt_capacity;
         
        if min_pitch%10 != 0 or min_gauge%10 != 0:
            min_pitch = (min_pitch/10)*10 + 10;
            min_gauge = (min_gauge/10)*10 + 10;
        else:
            min_pitch = min_pitch;
            min_gauge = min_gauge;
        #clause 10.2.2 is800
        max_spacing = int(min(100 + 4 * t_thinner, 200));   #clause 10.2.3.3 is800
             
        if min_end_dist%10 != 0:
            min_end_dist = (min_end_dist/10)*10 + 10;
        else:
            min_end_dist = min_end_dist;
             
        min_plate_thk = (5*shear_load*1000)/(bolt_fy*web_plate_l);
        max_edge_dist = int((12 * min_plate_thk * math.sqrt(250/beam_fy)).real)-1;
     
        # Determine single or double line of bolts
        length_avail = (web_plate_l-2*min_end_dist);
        pitch = round(length_avail/(bolts_required-1),3);
         
         
        ## Calculation of moment demand
        M1 = bolt_shear_capacity * (20 + min_end_dist/2);
        
        # Moment demand for single line of bolts
        if pitch >= min_pitch:
            bolt_line =1;
            gauge = 0;
            bolts_one_line = bolts_required;
            K = bolts_one_line / 2;
            M2=0;
            if bolts_required % 2 ==0 or bolts_required % 2 !=0:
                for k in range (0,K):
                    M2 = M2 + 2*(bolt_shear_capacity * ((length_avail/2 - k * pitch)**2/(length_avail/2 - k * pitch)));
                moment_demand = max(M1,M2);
                moment_demand =  round(moment_demand * 0.001,3)
         
        # moment demand for multi-line of bolts
        if pitch < min_pitch:
            bolt_line = 2;
            if bolts_required % 2 == 0:
                bolts_one_line = bolts_required/2;
            else:
                bolts_one_line = (bolts_required/2) + 1;
             
            pitch = round(length_avail/(bolts_one_line-1),3); 
            gauge = min_gauge;        
            M1 = bolt_shear_capacity * (20 + min_end_dist + gauge/2);
             
            if pitch >= min_pitch:
                K = bolts_one_line / 2;
                M2=0;
                if bolts_required % 2 ==0 or bolts_required % 2 !=0:
                    for k in range (0,K):
                        V = length_avail/2 - k * pitch
                        H = gauge/2;
                        d = math.sqrt(V**2 + H**2);
                        M2 = M2 + 2*(bolt_shear_capacity * (d**2/d));
                    M2=M2*2;
                    moment_demand = max(M1,M2);
                    moment_demand =  round(moment_demand * 0.001,3)
         
            # Design is not safe: iterations required
            else:
                logger.error(": Bolt strength is insufficient to carry the shear force")
                logger.warning (": Increase bolt diameter and/or bolt grade")
                moment_demand=0.0
    
        # Fetch bolt design output parameters dictionary
        boltParam = {}
        boltParam['shearcapacity'] = bolt_shear_capacity
        boltParam['bearingcapacity'] = bolt_bearing_capacity
        boltParam['boltcapacity'] = bolt_capacity
        boltParam['numofbolts'] = bolts_required
        boltParam['boltgrpcapacity'] = bolt_group_capacity
        boltParam['numofrow'] = bolts_one_line
        boltParam['numofcol'] = bolt_line
        boltParam['pitch'] = pitch
        boltParam['minpitch'] = min_pitch
#         boltParam['edge']= float(edge_dist)
        boltParam['enddist'] = float(min_end_dist)
        boltParam['gauge'] = float(gauge)
        boltParam['moment'] = moment_demand
        
        # Return bolt design parameters (used for design report)
        boltParam['bolt_fu'] = bolt_fu
        boltParam['bolt_fy'] = bolt_fy
        boltParam['dia_hole'] = dia_hole
        boltParam['kb'] = kb
        return boltParam
    
    # Call function for bolt design output
    boltParameters = boltDesign(); 
    
    # Check for long joint connections
    length_joint =(boltParameters['numofrow']-1) * boltParameters['pitch']
    if length_joint > 15*bolt_dia:
        beta_lj = 1.075 - length_joint/(200*bolt_dia);
        bolt_shear_capacity = beta_lj *  boltParameters['shearcapacity']
#         new_bolt_param = boltDesign(bolt_shear_capacity_new)
        new_bolt_param = boltDesign()
    else:
        new_bolt_param = boltParameters
      
    ####################################################################################
    
    # Design of fin plate
    # Calculation for maximum/minimum plate thickness
    max_plate_thk = fin_max_thk(beam_d);
    max_plate_thk = round(max_plate_thk,3);
    min_plate_thk = fin_min_thk(shear_load,boltParameters['bolt_fy'],web_plate_l);
    min_plate_thk = round(min_plate_thk,3);
    
    # Plate width input (optional) and validation
    # Note: For calculation of edge distance on bean edge side, 20 mm is added for clearance b/w beam edge and column web/flange 
    if web_plate_w != 0:
        if boltParameters['numofcol'] == 1:
            edge_dist = boltParameters['enddist']
            plate_edge = web_plate_w - edge_dist       
            web_plate_w_req = 2 * boltParameters['enddist'] + 20
        if boltParameters['numofcol'] == 2:
            edge_dist = boltParameters['enddist']
            plate_edge = web_plate_w - boltParameters['enddist']    
            web_plate_w_req = boltParameters['gauge'] + 2 * boltParameters['enddist'] + 20
            
            
    if web_plate_w == 0:   
        if boltParameters['numofcol'] == 1:
            edge_dist = boltParameters['enddist']
            plate_edge = edge_dist + 20      
            web_plate_w_req = plate_edge + boltParameters['enddist'];
            web_plate_w = web_plate_w_req
        if boltParameters['numofcol'] == 2:
            edge_dist = boltParameters['enddist'] 
            plate_edge = edge_dist + 20 
            web_plate_w_req = boltParameters['gauge'] + plate_edge + boltParameters['enddist'];
            web_plate_w = web_plate_w_req;      

    
    # Moment capacity of the fin plate (also known as web-side plate)
    moment_capacity = 1.2 * (web_plate_fy/1.1) * (web_plate_t * web_plate_l * web_plate_l)/6 * 0.001;
    moment_capacity = round(moment_capacity * 0.001,3);
    
    if moment_capacity > boltParameters['moment']:
        pass
    else:
        logger.error(": Plate moment capacity is less than the moment demand [cl. 8.2.1.2]")
        logger.warning(": Re-design with increased plate dimensions")
        
        
    ## Calculation of plate height and thickness and checks for extreme values 
    # Check for maximum and minimum plate thickness
    if web_plate_t < min_plate_thk:
        logger.error(": Plate thickness provided is less than the minimum required [Ref. Owens and Cheal, 1989]")
        logger.warning(": Minimum plate thickness required is %2.2f mm " % (min_plate_thk))
    elif web_plate_t < min_plate_thk:
        logger.error(": Plate thickness provided is less than the minimum required [Ref. Owens and Cheal, 1989]")
        logger.warning(": Minimum plate thickness required is %2.2f mm " % (min_plate_thk))  
    
    # Calculation of plate height (for optional input) and checking its extreme values
    web_plate_l_req1 = math.sqrt((boltParameters['moment']*1000*6*1.1)/(1.2*beam_fy*web_plate_t));
    # Single line of bolts
    if boltParameters['numofcol'] == 1:
        web_plate_l_req2 = (boltParameters['numofbolts']-1) * boltParameters['minpitch'] + 2 * boltParameters['enddist'];
        if web_plate_l == 0 or web_plate_l == min_plate_height or web_plate_l == max_plate_height:
            web_plate_l_req = max(web_plate_l_req1, web_plate_l_req2, web_plate_l);
        else:
            web_plate_l_req = max(web_plate_l_req1, web_plate_l_req2,min_plate_height);

    # Multi line of bolts
    if boltParameters['numofcol'] == 2:
        web_plate_l_req2 = (boltParameters['numofrow']-1) * boltParameters['minpitch'] + 2 * boltParameters['enddist'];
    
        if web_plate_l == 0 or web_plate_l == min_plate_height or web_plate_l == max_plate_height:
            web_plate_l_req = max(web_plate_l_req1, web_plate_l_req2, web_plate_l);
        elif web_plate_l > min_plate_height or web_plate_l < max_plate_height:
            web_plate_l_req = max(web_plate_l_req1, web_plate_l_req2, min_plate_height);
    
    if web_plate_l != min_plate_height +10 or web_plate_l != (max_plate_height-10)//10*10 :
        pass
    else:
        if web_plate_l < web_plate_l_req:
            logger.error(": Plate height provided is less than the minimum required [cl. 10.2.2/10.2.4]")
            logger.warning(": Minimum plate width required is %2.2f mm " %(web_plate_w_req))
            
    if web_plate_w < web_plate_w_req: 
           
        logger.error(": Plate width provided is less than the minimum required [cl. 10.2.2/10.2.4]")
        logger.warning(": Minimum plate width required is %2.2f mm " %(web_plate_w_req))
    
    # Block shear capacity of plate
    
    Tdb = blockshear(boltParameters['numofrow'],boltParameters['numofcol'],boltParameters['dia_hole'],\
                     beam_fy,beam_fu,boltParameters['enddist'],\
                     boltParameters['enddist'],boltParameters['pitch'],\
                     boltParameters['gauge'],web_plate_t) 
    if Tdb < shear_load:
        logger.error(": The block shear capacity of the plate is lass than the applied shear force [cl. 6.4.1]")
        logger.warning(": Minimum block shear capacity required is " %(shear_load))
        logger.info(": Increase the plate thickness")
        
    ##################################################################################
    
    ## Weld design
    # Ultimate and yield strength of welding material is assumed as Fe410 (E41 electrode) [source: Subramanian's book]
    weld_fu = 410;
    weld_fy = 250;
    
    # Effective length of the weld required
    weld_l = web_plate_l - weld_t * 2;
    
    ## Weld shear strength 
    # Direct shear
    Vy1 = shear_load *1000 /float(2*weld_l);        
    
    # Shear due to moment
    xCritical = 0;                    #single line weld
    yCritical = weld_l * 0.5;        #single line weld
    
    Ip = weld_l * weld_l * weld_l / 12;
    
    Vx = boltParameters['moment'] * yCritical *1000000 / (2 * Ip);
    Vy2 = boltParameters['moment'] * xCritical * 1000000 / (2 * Ip);
    
    # Resultant shear
    Vr = math.sqrt(Vx ** 2 + (Vy1 + Vy2) ** 2);
    Vr = round(Vr,3);
    
    weld_strength = 0.7 * weld_t * weld_fu / (math.sqrt(3) * 1.25);
    weld_strength = round(weld_strength,3);
    
    weld_t_req_chk1 = (Vr * (math.sqrt(3) * 1.25))/(0.7 * weld_fu);
    weld_t_req_chk2 = 0.8 * web_plate_t;
    weld_t_req = max(weld_t_req_chk1,weld_t_req_chk2);
    
    if weld_t_req != int(weld_t_req):
        weld_t_req = int(weld_t_req) + 1;
    else:
        weld_t_req = weld_t_req;
    
    if weld_t < weld_t_req:
        logger.error(": Weld thickness is not sufficient [cl. 10.5.7]")
        logger.warning(": Minimum weld thickness is required is %2.2f mm " % (weld_t_req))
        pass
    
    # End of calculation
    outputObj = {}
    outputObj['Bolt'] ={}
    outputObj['Bolt']['status'] = True
    outputObj['Bolt']['shearcapacity'] = new_bolt_param['shearcapacity']
    outputObj['Bolt']['bearingcapacity'] = new_bolt_param['bearingcapacity']
    outputObj['Bolt']['boltcapacity'] = new_bolt_param['boltcapacity']
    outputObj['Bolt']['numofbolts'] = new_bolt_param['numofbolts']
    outputObj['Bolt']['boltgrpcapacity'] = new_bolt_param['boltgrpcapacity']
    outputObj['Bolt']['numofrow'] = new_bolt_param['numofrow']
    outputObj['Bolt']['numofcol'] = new_bolt_param['numofcol']
    outputObj['Bolt']['pitch'] = new_bolt_param['pitch']
    outputObj['Bolt']['edge'] = float(edge_dist)
    outputObj['Bolt']['enddist'] = new_bolt_param['enddist']
    outputObj['Bolt']['gauge'] = new_bolt_param['gauge']
     
    outputObj['Weld'] = {}
    outputObj['Weld']['thickness'] = weld_t_req
    outputObj['Weld']['thicknessprovided'] = weld_t
    outputObj['Weld']['resultantshear'] = Vr
    outputObj['Weld']['weldstrength'] = weld_strength
     
    outputObj['Plate'] = {}
    outputObj['Plate']['minHeight'] = web_plate_l_req
    outputObj['Plate']['minWidth'] = web_plate_w_req
    outputObj['Plate']['plateedge'] = plate_edge
    outputObj['Plate']['externalmoment'] = new_bolt_param['moment']
    outputObj['Plate']['momentcapacity'] = moment_capacity
    outputObj['Plate']['height'] = float(web_plate_l)
    outputObj['Plate']['width'] = float(web_plate_w)
    outputObj['Plate']['blockshear'] = float(Tdb)
    
    # Parameters dictionary for design report

    outputObj['Bolt']['bolt_fu'] = boltParameters['bolt_fu']
    outputObj['Bolt']['bolt_dia'] = bolt_dia
    outputObj['Bolt']['k_b'] = boltParameters['kb']
    outputObj['Bolt']['beam_w_t'] = beam_w_t
    outputObj['Bolt']['web_plate_t'] = web_plate_t
    outputObj['Bolt']['beam_fu'] = beam_fu
    outputObj['Bolt']['shearforce'] = shear_load
    outputObj['Bolt']['dia_hole'] = boltParameters['dia_hole']
    
    outputObj['Plate']['web_plate_fy'] = web_plate_fy
    
    outputObj['Weld']['weld_fu'] = weld_fu
    outputObj['Weld']['effectiveWeldlength'] = weld_l
    
#   Print the output design parameters in console  
#     print outputObj
    #return outputObj
   
    
    if web_plate_l == (min_plate_height+10) or web_plate_l == ((max_plate_height-10)//10*10):
        if boltParameters['numofcol']==1:
            if web_plate_l == min_plate_height or web_plate_l == max_plate_height or web_plate_l < web_plate_l_req or web_plate_w < web_plate_w_req or weld_t_req > weld_t or weld_strength < Vr:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
            elif moment_capacity < boltParameters['moment']:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
            elif Tdb < shear_load:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
            elif web_plate_t < min_plate_thk or web_plate_t > max_plate_thk:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
        
        if boltParameters['numofcol']==2:
            if boltParameters['pitch'] < boltParameters['minpitch']:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
            elif web_plate_l == min_plate_height or web_plate_l == max_plate_height or web_plate_l < web_plate_l_req or web_plate_w < web_plate_w_req or weld_t_req > weld_t or weld_strength < Vr:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
            elif moment_capacity < boltParameters['moment']:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
            elif Tdb < shear_load:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
            elif web_plate_t < min_plate_thk or web_plate_t > max_plate_thk:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
        else:
            pass
        
    else:
        if web_plate_l == min_plate_height or web_plate_l == max_plate_height or web_plate_l < web_plate_l_req or web_plate_w < web_plate_w_req or weld_t_req > weld_t or weld_strength < Vr:
            for k in outputObj.keys():
                for key in outputObj[k].keys():
                    outputObj[k][key] = ""
        elif moment_capacity < boltParameters['moment']:
            for k in outputObj.keys():
                for key in outputObj[k].keys():
                    outputObj[k][key] = ""
        elif boltParameters['numofcol']==2:
            if boltParameters['pitch'] < boltParameters['minpitch']:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
        elif Tdb < shear_load:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
        elif web_plate_t < min_plate_thk or web_plate_t > max_plate_thk:
                for k in outputObj.keys():
                    for key in outputObj[k].keys():
                        outputObj[k][key] = ""
    
# Log message for safe /usafe design                         
    if  outputObj['Bolt']['status'] == True:
        logger.info(": Overall finplate connection design is safe \n")
        logger.debug(" :=========End Of design===========")
            
    else:
        logger.error(": Design is not safe \n ")
        logger.debug(" :=========End Of design===========")
        
    return outputObj
# Print the output values for hard-code inputs required to check independent calculation file   
#     print outputObj
 
# if __name__ == '__main__':
#      
#     finConn()