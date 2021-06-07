#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:14:56 2021

@author: emilejetzer
"""

import tkinter as tk
from tkinter import ttk


class MainFrame(tk.Tk):

    def __init__(self):
        ...

    def frame_switch(self, nouveau):
        ...

    def closing_procedure(self):
        ...

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.closing_procedure()


class ZurichFrame(tk.Frame):

    class Scope:
        ...

    class BoxCar:
        ...

    class Plotter:
        ...

    class GraphFrame:
        ...

    class ScopeOptionFrame:
        ...

    class BoxOptionFrame:
        ...

    class PlotterOptionFrame:
        ...

    def __init__(self, parent, mainf=None):
        ...
        self.__connectionframe()
        self.__inputframe()
        self.__outputframe()
        self.__demodulatorframe()
        self.__oscframe()
        self.__graphicframe()
        self.after(1000, self.measure_guide, 1000)

    def __connectionframe(self): ...

    def __inputframe(self): ...

    def __outputframe(self): ...

    def __demodulatorframe(self): ...

    def __oscframe(self): ...

    def __graphicframe(self): ...

    def __frame_switch(self, frames, nouveau): ...

    def measure_guide(self, t=1000):
        self.after(t, self.measure_guide, t)

    def create_bind(self, liste=None, type_=None): ...


class MonoFrame(tk.Frame):

    class Dialog:
        ...

    class Interface:
        ...

    class DaisyChain:
        ...

    class Identification:
        ...

    def __init__(self, parent, mainf=None):
        ...

    def __update_speed(scale, variable): ...

    def frame_switch(self, new, textbox): ...


class SpectroFrame(tk.Frame):

    def __init__(self, parent, mainf=None):
        ...

    def measure(self):
        ...


class UeyeFrame(tk.Frame):

    def __init__(self, parent, mainf=None):
        ...

    def live_update(self):
        ...

    def measure(self):
        ...


class Experiment(ttk.LabelFrame):

    def __init__(self, parent, mainf=None):
        ...

    def __frame_switch(liste, nouvelle):
        ...

    def __create_layout(self):
        ...


if __name__ == '__main__':
    with MainFrame() as app:
        app.mainloop()
