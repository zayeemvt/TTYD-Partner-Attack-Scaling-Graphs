from damage_calculator import *
from discrete_plotter import *

from matplotlib import interactive

common_only = True # Restricts data to just moves that would be sensibly used for single-target
common_moves = ["Headbonk", "Multibonk (3 hits)", "Multibonk (4 hits)", "Multibonk (5 hits)",
                "Shell Toss", "Body Slam", "Ground Pound", "Mini-Egg", "Shade Fist", "Bomb", "Love Slap"]



def initialize_data() -> list[Partner]:
    partner_list = []

    partner_list.append(Partner(name="Goombella",base_dmg_list=[1,2,3], ability_list=[
        Ability("Headbonk", base_dmg=0, num_hits=2, piercing=False, rank=1),
        Ability("Multibonk (3 hits)", base_dmg=0, num_hits=3, piercing=False, rank=2),
        Ability("Multibonk (4 hits)", base_dmg=0, num_hits=4, piercing=False, rank=2),
        Ability("Multibonk (5 hits)", base_dmg=0, num_hits=5, piercing=False, rank=2)
        ]))

    partner_list.append(Partner(name="Koops", base_dmg_list=[2,3,5], ability_list=[
        Ability("Shell Toss", base_dmg=0, num_hits=1, piercing=False, rank=1),
        Ability("Shell Slam", base_dmg=1, num_hits=1, piercing=True, rank=3)
        ]))
    
    partner_list.append(Partner(name="Flurrie", base_dmg_list=[2,4,6], ability_list=[
        Ability("Body Slam", base_dmg=0, num_hits=1, piercing=False, rank=1),
        Ability("Lip Lock", base_dmg=0, num_hits=1, piercing=True, rank=2)
        ]))
    
    partner_list.append(Partner(name="Yoshi", base_dmg_list=[1,1,1], ability_list=[
        Ability("Ground Pound", base_dmg=0, num_hits=4, piercing=False, rank=1),
        Ability("Gulp", base_dmg=0, num_hits=1, piercing=True, rank=1),
        Ability("Mini-Egg", base_dmg=0, num_hits=3, piercing=False, rank=2)
        ]))

    partner_list.append(Partner(name="Vivian", base_dmg_list=[3,4,5], ability_list=[
        Ability("Shade Fist", base_dmg=0, num_hits=1, piercing=False, rank=1),
        Ability("Fiery Jinx", base_dmg=1, num_hits=1, piercing=True, rank=2)
        ]))

    partner_list.append(Partner(name="Bobbery", base_dmg_list=[2,4,6], ability_list=[
        Ability("Bomb", base_dmg=0, num_hits=1, piercing=False, rank=1),
        Ability("Bob-ombast", base_dmg=2, num_hits=1, piercing=False, rank=3)
        ]))

    partner_list.append(Partner(name="Ms. Mowz", base_dmg_list=[2,3,4], ability_list=[
        Ability("Love Slap", base_dmg=0, num_hits=1, piercing=True, rank=1),
        ]))

    return partner_list




def main():
    partner_list = initialize_data()

    all_data = [[],[],[]] # [rank][move][modifier]

    # For the sake of conciseness, each rank has their own range of attack modifiers
    # ... since you're not likely to see huge modifiers at lower ranks
    modifier_range_list = [
        range(-3,5+1),
        range(-4,6+1),
        range(-6,8+1)
    ]

    for r in [1,2,3]: # for each rank...
        modifier_range = modifier_range_list[r-1]

        for partner in partner_list:
            move_data = []
            move_data_is_empty = True

            for m in modifier_range: # for each attack modifier...

                # Calculate total damage for all of a partner's abilities
                results = partner.calculate_all_ability_damage(rank=r,atk_modifier=m)

                move_index = 0

                # Rearrange results from [modifier][move] format to [move][modifier]
                for i in range(len(results)):

                    if (not common_only or (common_only and (results[i].ability in common_moves))):
                        if move_data_is_empty:
                            move_data.append([results[i]])
                        else:
                            move_data[move_index].append(results[i])
                            move_index += 1

                move_data_is_empty = False
            
            all_data[r-1].extend(move_data)

        generate_rank_plot(r, all_data[r-1], modifier_range)
    
    
    ### Uncomment this if you want to see graphs for ALL partners
    ### Realistically, only Goombella and Yoshi's graphs are interesting
    for partner in partner_list:
        generate_partner_plot(partner.name, all_data, modifier_range_list)

    ### Comment out this loop if you want to see graphs for ALL partners
    # for partner in ["Goombella", "Yoshi"]:
    #     generate_partner_plot(partner, all_data, modifier_range_list)
    
    input() # prevents graphs from instantly disappearing

if __name__ == "__main__":
    main()