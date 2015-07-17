import sys,argparse
from astropy.io import ascii
from astropy.io import fits
import os
from os.path import dirname,abspath
import matplotlib.pyplot as plt
import matplotlib.pyplot as pl
import numpy as np
from numpy import pi,sqrt,exp,cos,sin
import itertools
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
from pylab import *
#from mpltools import layout
import matplotlib as mpl

def DataFilePath(fname):
    """Return full path to a data file"""
    return os.path.join(dirname(abspath(__file__)),"data",fname)

markers='dhs^vodhs1^'
linestyles=["solid", "dashed", "dotted", "dashdot"]

def SaveFigure(filename):
    pl.savefig(filename,bbox_inches="tight")

def UnBox(ax=None):
    if not ax: ax = pl.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

def SetRcDefaults():
    #mpl.rcParams['mathtext.default']='regular'
#    mpl.rcParams['font.family']='sans-serif'
    mpl.rcParams['font.serif']='Times Roman, Palatino, New Century Schoolbook, Bookman, Computer Modern Roman'
    mpl.rcParams['font.sans-serif']='Verdana, Helvetica, Avant Garde, Computer Modern Sans serif'
    mpl.rcParams['font.cursive']='Zapf Chancery'
    mpl.rcParams['font.monospace']='Courier, Computer Modern Typewriter'
#    mpl.rcParams['text.usetex']='true'
#    mpl.rcParams['mathtext.fontset'] = 'cm'
#    mpl.rcParams['font.family']='serif'
#    mpl.rcParams['font.serif']=["Times","Times New Roman"]
    mpl.rcParams['font.size']=13
#    mpl.rcParams['axes.labelsize']=15
    mpl.rcParams['lines.linewidth'] = 1.4
    mpl.rcParams['figure.figsize']=(4,3)

SetRcDefaults()

def FastText(): mpl.rcParams['text.usetex']='false'



def Monochrome(fig=None,MARKERSIZE = 3,
                   COLORMAP = {
        'b': {'marker': None, 'dash': (None,None)},
        'g': {'marker': None, 'dash': [5,5]},
        'r': {'marker': None, 'dash': [5,3,1,3]},
        'c': {'marker': None, 'dash': [1,3]},
        'm': {'marker': None, 'dash': [5,2,5,2,5,10]},
        'y': {'marker': None, 'dash': [5,3,1,2,1,10]},
        'k': {'marker': 'o', 'dash': (None,None)} #[1,2,1,10]}
        }
    ):
    """
    Take each line in a figure and convert the line style to be 
    suitable for black and white viewing.
    """
    if not fig: fig=plt.gcf()
    for ax in fig.get_axes():
        for line in ax.get_lines():
            origColor = line.get_color()
            line.set_color('black')
            line.set_dashes(COLORMAP[origColor]['dash'])
            line.set_marker(COLORMAP[origColor]['marker'])
            line.set_markersize(MARKERSIZE)

def LineStyleCycler(styles=linestyles):
    "Return an iterator over line styles"
    return itertools.cycle(styles)
def MarkerCycler(styles=markers):
    "Return an iterator over line styles"
    return itertools.cycle(markers)

# Allow specifying function call from command-line
def main(defaultFunction="default()"):
    parser=argparse.ArgumentParser()
    parser.add_argument('function', nargs='?',default=defaultFunction)
    parser.add_argument('--save', nargs="?",const="figure.pdf",default=None)
    args=parser.parse_args()
    eval(args.function)
    if args.save is None:
        plt.show()
    else:
        plt.savefig(args.save,transparent=True,bbox_inches="tight")

# Derive plot function name from script name
def DoPlot(plotFunction=None):
    if plotFunction is None:
        funcName=os.path.basename(os.path.splitext(sys.argv[0])[0])
        plotFunction=getattr('__main__', funcName)
    plotFunction()
    ShowOrSave()

def ShowOrSave():
    if len(sys.argv)==1:
        plt.show()
    else:
        plotFile=sys.argv[1]
        plt.savefig(plotFile,bbox_inches="tight")

def ArrowAxes(ax=None,al=7):
  "Put arrowed axes instead of box axes"
  if ax is None: ax=gca()
  arrowprops=dict(clip_on=False, # plotting outside axes on purpose
      frac=1., # make end arrowhead the whole size of arrow
      headwidth=al, # in points
      facecolor='k')
  kwargs = dict(  
                  xycoords='axes fraction',
                  textcoords='offset points',
                  arrowprops= arrowprops,
               )
  
  ax.annotate("",(1,0),xytext=(-al,0), **kwargs) # bottom spine arrow
  ax.annotate("",(0,1),xytext=(0,-al), **kwargs) # left spin arrow
  
  # hide the top and right spines
  [sp.set_visible(False) for sp in (ax.spines['top'],ax.spines['right'])]
  
  #hide the right and top tick marks
  ax.yaxis.tick_left()
  ax.xaxis.tick_bottom()

def ScalarLogAxes(ax=None,xscalar=True,yscalar=True):
    """Label log-log axes without using powers of 10"""
    if ax is None:
        ax=gca()
    if xscalar: ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
    if yscalar: ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())

