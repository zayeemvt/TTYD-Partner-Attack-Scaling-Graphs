from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Dictionaries and lists used to make iteration simpler
marker_list = ["o", "v", "d", "*"]
color_dict = {"Goombella" : "tab:pink",
                "Koops" : "tab:olive",
                "Flurrie" : "tab:cyan",
                "Yoshi" : "tab:green",
                "Vivian" : "tab:purple",
                "Bobbery" : "tab:blue",
                "Ms. Mowz" : "tab:red"}
rank_name_dict = { 1 : "Normal",
                   2 : "Super", 
                   3 : "Ultra"}
rank_colors_dict = { 1 : "tab:blue",
                     2 : "tab:green",
                     3 : "tab:red"}

@dataclass
class DamageResult:
    partner: str
    ability: str
    total_damage: int

    def __repr__(self) -> str:
        return f'{self.partner}|{self.ability}:{self.total_damage} damage'


# Global variables
current_figure_num = 1



def generate_rank_plot(rank: int, data: list[list[DamageResult]], modifier_range: list[int]) -> None:
    global current_figure_num
    fig = plt.figure(current_figure_num, figsize=[6.4*1.5,4.8*1.5])

    num_points = len(modifier_range)
    x = np.array(modifier_range)

    partner = ""
    move_index = 0 # used for marker styles, ensures basic attacks all start with the same marker
    offset_shift = -0.005 # used to add small noise to data points

    for move_data in data:
        curr_partner = move_data[0].partner

        if partner != curr_partner: # reset marker style if new partner
            partner = curr_partner
            move_index = 0

        y = np.array([ability.total_damage for ability in move_data])

        ### Add offsets to each data point, to prevent them from
        ### overlapping and hiding other data beneath them.
        # x_noise = np.random.normal(0,0.035, num_points)
        # y_noise = np.random.normal(0,0.015, num_points)
        x_noise = np.ones(num_points) * offset_shift
        y_noise = np.zeros(num_points)

        offset_shift = offset_shift + 0.01 if offset_shift > 0.0 else offset_shift - 0.01
        offset_shift *= -1.0


        move_label = f"{partner} ({move_data[0].ability})"

        plt.plot(x + x_noise, y + y_noise, label=move_label, marker=marker_list[move_index], color=color_dict[partner],
                 alpha=0.9, linestyle='--', markersize=6.0)
        

        move_index += 1
        move_index %= len(marker_list)
    
    fig.legend(bbox_to_anchor=(0.4, 0.85), fontsize='small')
    fig.supxlabel("Net Attack Modifier")
    fig.supylabel("Total Damage")
    fig.suptitle(f'{rank_name_dict[rank]} Rank')
    
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(4))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(True, which='major')
    ax.grid(True, which='minor', linewidth=0.5, color='#DDDDDD')
    ax.axhline(0, color='tab:gray')
    ax.axvline(0, color='tab:gray')

    fig.show()
    current_figure_num += 1




def generate_partner_plot(partner: str, data: list[list[list[DamageResult]]], modifier_range_list: list[list[int]]) -> None:
    global current_figure_num
    fig = plt.figure(current_figure_num, figsize=[6.4*1.5,4.8*1.5])

    offset_shift = -0.005 # used to add small noise to data points

    rank = 1
    marker_color = "tab:yellow"

    for rank_data in data:
        marker_color = rank_colors_dict[rank]
        move_index = 0 # used for marker styles, ensures that the same attack uses the same marker
        
        num_points = len(modifier_range_list[rank-1])
        x = np.array(modifier_range_list[rank-1])

        # Filter data for only relevant partner
        rank_data = [move_data for move_data in rank_data if (move_data[0].partner == partner)]

        for move_data in rank_data:
            y = np.array([ability.total_damage for ability in move_data])

            ### Add offsets to each data point, to prevent them from
            ### overlapping and hiding other data beneath them.
            # x_noise = np.random.normal(0,0.035, num_points)
            # y_noise = np.random.normal(0,0.015, num_points)
            x_noise = np.ones(num_points) * offset_shift
            y_noise = np.zeros(num_points)

            offset_shift = offset_shift + 0.01 if offset_shift > 0.0 else offset_shift - 0.01
            offset_shift *= -1.0

            
            move_label = f"{move_data[0].ability} ({rank_name_dict[rank]} Rank)"

            plt.plot(x + x_noise, y + y_noise, label=move_label, marker=marker_list[move_index], color=marker_color,
                    alpha=0.9, linestyle='--', markersize=6.0)
            

            move_index += 1
            move_index %= len(marker_list)

        
        rank += 1
    
    fig.legend(bbox_to_anchor=(0.4, 0.85), fontsize='small')
    fig.supxlabel("Net Attack Modifier")
    fig.supylabel("Total Damage")
    fig.suptitle(f'{partner}')
    
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(4))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(True, which='major')
    ax.grid(True, which='minor', linewidth=0.5, color='#DDDDDD')
    ax.axhline(0, color='tab:gray')
    ax.axvline(0, color='tab:gray')

    fig.show()
    current_figure_num += 1