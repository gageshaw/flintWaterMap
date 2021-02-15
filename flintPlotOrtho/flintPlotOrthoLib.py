import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('/Users/Gage/Flint/Library')
import flintPlot1117lib as flintLib
import importlib
importlib.reload(flintLib)


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
    
dataType = 'Orthophosphate'
unit = '(mg/L PO4)'
    
def plot(dataFile, locationFile,date, saveName):
    
    Xscat,Yscat,Zscat,Xcont,Ycont,Zcont,T,F = flintLib.readExcel(dataFile, locationFile)

    m, legendHandles = flintLib.basePlot(Xscat,Yscat,Zscat)
    
    contourPlot(m, Xcont, Ycont, Zcont)

    legend(legendHandles, date, T, F)
    
    flintLib.plotSave(saveName)
    

    
def legend(legendHandles, date, T, F):
    #Generate WTP label
    tempLabel = ''
    flowLabel = ''
    openBracket = ''
    closedBracket = ''
    comma = ''
    if(T!=False):
        T = str(T)
        tempLabel = 'Temp:'+T+chr(176)+'C'
        openBracket = '['
        closedBracket = ']'
    if(F!=False):
        F = str(F)
        flowLabel = 'Flow:'+F+' MG'
        openBracket = '['
        closedBracket = ']'
        if(T!=False):
            comma = ' ,'
    wtpLabel = 'Water Treatment Plant '+openBracket+tempLabel+comma+flowLabel+closedBracket
    #Create necessary markers and their labels
    blueLine = mlines.Line2D([], [], color='blue', label='ChlorineHigh', linewidth = 4)
    blueLineLabel = dataType + ' '+unit
    #Add new markers to legendHandles
    legendHandles += [blueLine]
    #Plot legend
    plt.legend(handles = legendHandles, labels = [ 'Lead Service Lateral','Measurement Site','Reservoir', wtpLabel,'Chlorine Injection', blueLineLabel],loc = 'lower left', ncol=2, edgecolor = '.5')
    #Create date box
    plt.annotate( dataType+' - '+date, (200,1500), fontsize=23, fontweight='bold', bbox=dict(facecolor = 'white', alpha = .8,boxstyle='round', edgecolor = '.5'), zorder=11)
    
    
def contourPlot(m, Xcont, Ycont, Zcont):
    # Contour plot
    Xcont, Ycont = m(Xcont, Ycont)
    Xcont, Ycont = np.meshgrid(Xcont, Ycont)
    contourArray = np.arange(.0000001, 5.0000001 , .2) 
    colorList = ['blue'] * 50
    contours = m.contour(Xcont, Ycont, Zcont ,  contourArray, linewidths = flintLib.lineWidths , colors = colorList)
    #Set bold lines
    contours.collections[0].set_linewidth(4)
    contours.collections[5].set_linewidth(4)
    contours.collections[10].set_linewidth(4)
    contours.collections[15].set_linewidth(4)
    contours.collections[20].set_linewidth(4)
   
 
 
    plt.clabel(contours, levels = contourArray,inline=1, fontsize= flintLib.contFontSize, fmt = '%1.1f')
    







