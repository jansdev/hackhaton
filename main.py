from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from plot_functions import mapPlot, polutionHistogram
from data_models import TricityPM10PolutionModel

# -------------------------------  MATPLOTLIB  -------------------------------

fig, (ax1, ax2) = plt.subplots(1, 2)
ax2 = polutionHistogram(TricityPM10PolutionModel.pm_sop_bi_plowc)
ax1 = mapPlot()

# ------------------------------- MATPLOTLIB -------------------------------

# ------------------------------- Beginning of Matplotlib helper code -----------------------

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# ------------------------------- Beginning of GUI CODE -------------------------------

# define the window layout
layout = [[sg.Text('Jakość powietrze w trójmieście [PM10, NO2, CO]')],
          [sg.Canvas(key='-CANVAS-')],
          [sg.Button('Ok'), sg.Button('PM10'), sg.Button('NO2'), sg.Button('CO')],]

# create the form and show it without the plot
window = sg.Window('AirQ', layout, finalize=True, element_justification='center', font='Helvetica 18')

# add the plot to the window
fig_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)

event, values = window.read()

window.close()