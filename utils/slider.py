import typing

import numpy as np

import ipywidgets as widgets
from IPython.display import display


class Slider:
    def __init__(self, cb: typing.Callable[[np.ndarray], None]):
        self.q_list: typing.List[np.ndarray] = []
        self.slider = widgets.IntSlider(value=0, min=0, max=0)
        self.slider.observe(lambda change: cb(self.q_list[change.new]), names="value")

    def display(self):
        self.slider.max = max(len(self.q_list) - 1, 0)
        display(self.slider)

    def append_q(self, q: np.ndarray):
        self.q_list.append(q)
