from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

marker_list = ["o", "v", "d", "*"]
color_dict = {"Goombella" : "tab:pink",
                "Koops" : "tab:olive",
                "Flurrie" : "tab:cyan",
                "Yoshi" : "tab:green",
                "Vivian" : "tab:purple",
                "Bobbery" : "tab:blue",
                "Ms. Mowz" : "tab:red"}

@dataclass
class DamageResult:
    partner: str
    ability: str
    total_damage: int

    def __repr__(self) -> str:
        return f'{self.partner}|{self.ability}:{self.total_damage} damage'




def draw_line(data: list[DamageResult]):
    pass

def generate_rank_plot(rank: int, data: list[list[DamageResult]], modifier_range: list[int]):
    fig = plt.figure(rank, figsize=[6.4*1.5,4.8*1.5])

    num_points = len(modifier_range)
    x = np.array(modifier_range)

    partner = ""
    move_index = 0
    offset_shift = -0.005

    for move_data in data:
        curr_partner = move_data[0].partner

        if partner != curr_partner:
            partner = curr_partner
            move_index = 0

        y = np.array([ability.total_damage for ability in move_data])

        move_label = f"{partner} ({move_data[0].ability})"

        # x_noise = np.random.normal(0,0.035, len(x))
        # y_noise = np.random.normal(0,0.015, len(x))
        x_noise = np.ones(len(x)) * offset_shift
        y_noise = np.zeros(len(x))

        offset_shift = offset_shift + 0.01 if offset_shift > 0.0 else offset_shift - 0.01
        offset_shift *= -1.0

        plt.plot(x + x_noise, y + y_noise, label=move_label, marker=marker_list[move_index], color=color_dict[partner],
                 alpha=0.9, linestyle='--', markersize=6.0)
        move_index += 1
        move_index %= len(marker_list)
    
    fig.legend(bbox_to_anchor=(0.4, 0.85), fontsize='small')
    fig.supxlabel("Net Attack Modifier")
    fig.supylabel("Total Damage")
    fig.suptitle(f'{"Ultra" if (rank == 3) else "Super" if (rank == 2) else "Normal"} Rank')
    
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(4))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(True, which='major')
    ax.grid(True, which='minor', linewidth=0.5, color='#DDDDDD')
    ax.axhline(0, color='tab:gray')
    ax.axvline(0, color='tab:gray')

    fig.show()