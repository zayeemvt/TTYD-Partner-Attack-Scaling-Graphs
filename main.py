from damage_calculator import *

def initialize_data() -> list[Partner]:
    partner_list = []

    partner_list.append(Partner(name="Goombella",base_dmg_list=[1,2,3], ability_list=[
        Ability("Headbonk", base_dmg=0, num_hits=2, piercing=False, rank=1),
        Ability("Multibonk (3 hits)", base_dmg=0, num_hits=3, piercing=False, rank=2),
        Ability("Multibonk (4 hits)", base_dmg=0, num_hits=4, piercing=False, rank=2),
        Ability("Multibonk (5 hits)", base_dmg=0, num_hits=5, piercing=False, rank=2)
        ]))

    partner_list.append(Partner(name="Koops", base_dmg_list=[2,3,5], ability_list=[
        Ability("Shell Toss/Power Shell", base_dmg=0, num_hits=1, piercing=False, rank=1),
        Ability("Shell Slam", base_dmg=1, num_hits=1, piercing=True, rank=3)
        ]))
    
    partner_list.append(Partner(name="Flurrie", base_dmg_list=[2,4,6], ability_list=[
        Ability("Body Slam", base_dmg=0, num_hits=1, piercing=False, rank=1),
        Ability("Lip Lock", base_dmg=0, num_hits=1, piercing=True, rank=2)
        ]))
    
    partner_list.append(Partner(name="Yoshi", base_dmg_list=[1,1,1], ability_list=[
        Ability("Ground Pound", base_dmg=0, num_hits=4, piercing=False, rank=1),
        Ability("Gulp", base_dmg=0, num_hits=1, piercing=True, rank=1),
        Ability("Mini-Egg", base_dmg=3, num_hits=3, piercing=False, rank=2)
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

    data = [[],[],[]] # [rank][move][modifier]

    for r in [1,2,3]:
        lowest_mod = -3 - (r-1)
        highest_mod = 4 + (r-1)
        for partner in partner_list:
            move_data = []
            for m in range(lowest_mod,highest_mod+1):
                results = partner.calculate_all_ability_damage(rank=r,atk_modifier=m)

                if len(move_data) == 0:
                    for i in range(len(results)):
                        move_data.append([results[i]])
                else:
                    for i in range(len(results)):
                        move_data[i].append(results[i])
            
            data[r-1].extend(move_data)

    # for i in range(8):
    #     print(f"+{i}: {calculate_damage(1, i, 6)} damage")

if __name__ == "__main__":
    main()