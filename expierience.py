import math
import random
from collections import OrderedDict
from dataclasses import dataclass

import matplotlib.pyplot as plt
import seaborn as sns


@dataclass
class Position:
    company: str
    type: str  # Enterprise/Startup/etc.
    tenure: float


class PieChart:
    positions: list[Position]

    def __init__(self, positions: list[Position]):
        self.positions = positions
        self.yoe_by_type = self._group_by_type(self.positions)

    def _create_colors(self):
        n_colors = len(self.positions) + len(self.yoe_by_type.keys())
        if n_colors < 11:
            return sns.color_palette("pastel", n_colors=len(self.positions) + len(self.yoe_by_type.keys()),
                                     as_cmap=True)
        else:
            vibrant_palette = sns.color_palette("tab10", n_colors)
            colors = [(0.5 * r + 0.4, 0.5 * g + 0.4, 0.6 * b + 0.4) for r, g, b in vibrant_palette]
            random.shuffle(colors)
            return colors

    def _group_by_type(self, positions: list[Position]):
        class DefaultOrderedDict(OrderedDict):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

            def __missing__(self, key):
                return 0

        yoe_by_type = DefaultOrderedDict()
        for position in positions:
            yoe_by_type[position.type] += position.tenure
        return yoe_by_type

    def make(self):
        fig, ax = plt.subplots()
        size = 0.55

        colors = self._create_colors()

        # company slices
        ax.pie([position.tenure for position in self.positions],
               labels=[position.company for position in self.positions],
               colors=colors[:len(self.positions)],
               radius=1.5,
               wedgeprops=dict(width=size, edgecolor='w'),
               labeldistance=1.05,
               textprops=dict(fontsize='12'))

        # experience type slices
        ax.pie(self.yoe_by_type.values(),
               labels=self.yoe_by_type.keys(),
               colors=colors[len(self.positions):],
               radius=1.5 - size,
               wedgeprops=dict(width=size, edgecolor='w'),
               labeldistance=0.7,
               textprops=dict(rotation_mode='anchor', va='center', ha='center', fontsize='13'))

        # YOE text in the center of the pie
        ax.text(0.5, 0.5, f'{math.ceil(sum([position.tenure for position in self.positions]))} YOE',
                transform=ax.transAxes,
                va='center',
                ha='center', backgroundcolor='white',
                size='xx-large')

        plt.show()
