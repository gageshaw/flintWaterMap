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
    
dataType = 'Hardness'
unit = '(mg/L CaCO3)'
    
def plot(dataFile, locationFile,date, saveName):
    
    Xscat,Yscat,Zscat,Xcont,Ycont,Zcont,T,F = flintLib.readExcel(dataFile, locationFile)

    m, legendHandles = flintLib.basePlot(Xscat,Yscat,Zscat)
    
    #Asterisk 
    Xcs2, Ycs2 = m(-83.67091725,43.056074)
    #m.scatter(Xcs2,Ycs2,s=300,marker="$\u204E$",color='red',zorder = 10)
    
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
    #Asterisk note
    #plt.annotate("*Control Station 2 Omitted", (200,2000),color = 'red',bbox=dict(facecolor = 'white', alpha = .8,boxstyle='round', edgecolor = '.5'), zorder=11)
    
def contourPlot(m, Xcont, Ycont, Zcont):
    # Contour plot
    Xcont, Ycont = m(Xcont, Ycont)
    Xcont, Ycont = np.meshgrid(Xcont, Ycont)
    contourArray = np.arange(90.00001, 125.00001 , .2) 
    #contourArray = np.arange(80.00001, 145.00001 , .4) 
    colorList = ['blue'] * 50
    contours = m.contour(Xcont, Ycont, Zcont ,  contourArray, linewidths = flintLib.lineWidths , colors = colorList)
    #Set bold lines
    contours.collections[0].set_linewidth(4)
    contours.collections[5].set_linewidth(4)
    contours.collections[10].set_linewidth(4)
    contours.collections[15].set_linewidth(4)
    contours.collections[20].set_linewidth(4)
    contours.collections[25].set_linewidth(4)
    contours.collections[30].set_linewidth(4)
    contours.collections[35].set_linewidth(4)
    contours.collections[40].set_linewidth(4)
    contours.collections[45].set_linewidth(4)
    contours.collections[50].set_linewidth(4)
    contours.collections[55].set_linewidth(4)
    contours.collections[60].set_linewidth(4)
    contours.collections[65].set_linewidth(4)
    contours.collections[70].set_linewidth(4)
    contours.collections[75].set_linewidth(4)
    contours.collections[80].set_linewidth(4)
    contours.collections[85].set_linewidth(4)
    contours.collections[90].set_linewidth(4)
    contours.collections[95].set_linewidth(4)
    contours.collections[100].set_linewidth(4)
    contours.collections[105].set_linewidth(4)
    contours.collections[110].set_linewidth(4)
    contours.collections[115].set_linewidth(4)
    contours.collections[120].set_linewidth(4)
    contours.collections[125].set_linewidth(4)
    contours.collections[130].set_linewidth(4)
    contours.collections[135].set_linewidth(4)
    contours.collections[140].set_linewidth(4)
    contours.collections[145].set_linewidth(4)
    
    plt.clabel(contours, levels = contourArray,inline=1, fontsize= flintLib.contFontSize, fmt = '%1.1f')
    







