import typing

import numpy as np

import ipywidgets as widgets
from IPython.display import display


class Slider:
    def __init__(self):
        self.q_list: typing.List[np.ndarray] = []
        self.slider = widgets.IntSlider(value=0, min=0, max=0)

    def display(self):
        display(self.slider)

    def reset(self):
        self.q_list = []

    def append_q(self, q: np.ndarray):
        self.q_list.append(q)

    def update(self):
        self.slider.value = 0
        self.slider.max = max(len(self.q_list) - 1, 0)

    def set_interaction(self, cb: typing.Callable[[np.ndarray], None]):
        widgets.interactive_output(
            lambda slider: cb(self.q_list[slider]), {"slider": self.slider}
        )
