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
    
dataType = 'Chlorine Residual'
    
def plot(dataFile, locationFile, unit, date, saveName):
    
    Xscat,Yscat,Zscat,Xcont,Ycont,Zcont,T,F = flintLib.readExcel(dataFile, locationFile)

    m, legendHandles = flintLib.basePlot(Xscat,Yscat,Zscat)
    
    contourPlot(m, Xcont, Ycont, Zcont)

    legend(legendHandles, unit, date, T, F)
    
    flintLib.plotSave(saveName)
    

    
def legend(legendHandles, unit,  date, T, F):
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
    blueLineLabel = dataType +' >.2'+ unit
    redLine = mlines.Line2D([], [], color='red', label='ChlorineLow', linewidth = 4)
    redLineLabel = dataType+' ' +chr(8804)+'.2'+ unit
    #Add new markers to legendHandles
    legendHandles += [blueLine, redLine]
    #Plot legend
    plt.legend(handles = legendHandles, labels = [ 'Lead Service Lateral','Measurement Site','Reservoir', wtpLabel,'Chlorine Injection', blueLineLabel,redLineLabel ],loc = 'lower left', ncol=2, edgecolor = '.5')
    #Create date box
    plt.annotate( dataType+' - '+date, (200,1600), fontsize=23, fontweight='bold', bbox=dict(facecolor = 'white', alpha = .8,boxstyle='round', edgecolor = '.5'), zorder=10)
    
    
def contourPlot(m, Xcont, Ycont, Zcont):
    # Contour plot
    Xcont, Ycont = m(Xcont, Ycont)
    Xcont, Ycont = np.meshgrid(Xcont, Ycont)
    contourArray = np.arange(0.00001, 3.00001 , .05) 
    colorList = ['red']*5 + ['blue'] * 56
    contours = m.contour(Xcont, Ycont, Zcont ,  contourArray, linewidths = flintLib.lineWidths , colors = colorList)
    #Set bold lines
    contours.collections[0].set_linewidth(4)
    contours.collections[4].set_linewidth(4)
    contours.collections[8].set_linewidth(4)
    contours.collections[12].set_linewidth(4)
    contours.collections[16].set_linewidth(4)
    contours.collections[20].set_linewidth(4)
    contours.collections[24].set_linewidth(4)
    contours.collections[28].set_linewidth(4)
    contours.collections[32].set_linewidth(4)
    contours.collections[36].set_linewidth(4)
    contours.collections[40].set_linewidth(4)
    contours.collections[44].set_linewidth(4)
    contours.collections[48].set_linewidth(4)
    contours.collections[52].set_linewidth(4)
    contours.collections[56].set_linewidth(4)
    plt.clabel(contours, levels = contourArray,inline=1, fontsize= flintLib.contFontSize, fmt = '%1.2f')
    







