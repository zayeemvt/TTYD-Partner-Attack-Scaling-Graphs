from dataclasses import dataclass

from discrete_plotter import DamageResult

@dataclass
class Ability:
    name: str
    base_dmg: int
    num_hits: int
    piercing: bool
    rank: int


class Partner:
    def __init__(self, name: str, base_dmg_list: list[int], ability_list: list[Ability]) -> None:
        self.name = name
        self.base_dmg_list = base_dmg_list
        self.ability_list = ability_list
    
    def calculate_all_ability_damage(self, rank: int, atk_modifier: int) -> list[DamageResult]:
        results = []

        for ability in self.ability_list:
            if rank < ability.rank: # if ability isn't unlocked at this rank...
                continue
            
            # Copy parameters into local variables for ease of editing
            base_attack = self.base_dmg_list[rank-1] + ability.base_dmg
            modifier = atk_modifier
            num_hits = ability.num_hits
            falloff = True # does damage decrease with each attack? Only relevant for Mini-Egg...

            if ability.piercing and atk_modifier < 0:
                modifier = 0
            
            if self.name == "Yoshi": # This guy has so many exceptions...
                if ability.name == "Ground Pound":
                    num_hits += rank - 1
                elif ability.name == "Mini-Egg":
                    num_hits += 1 if (rank == 3) else 0
                    falloff = False
                elif ability.name == "Gulp":
                    base_attack += 3 + (rank - 1)

            
            damage = calculate_damage(base_attack, modifier, num_hits, falloff)
            
            results.append(DamageResult(partner=self.name, ability=ability.name, total_damage=damage))
        
        return results



def calculate_damage(base_attack: int, atk_modifier: int, num_hits: int, falloff: bool=True) -> int:

    if (num_hits < 3 or not falloff):
        total_damage = (base_attack + atk_modifier) * num_hits
        total_damage = 0 if (total_damage < 0) else total_damage

        return total_damage
    
    else:
        total_damage = 0

        for i in range(num_hits):
            initial_hit = base_attack + atk_modifier

            # If the initial hit does at least 1 damage, then every
            # subsequent hit will also deal at least 1 damage.
            # Otherwise, no damage is dealt at all.
            if (initial_hit <= 0):
                break
            else:
                damage_dealt = initial_hit - i

                if damage_dealt <= 0:
                    damage_dealt = 1

                total_damage += damage_dealt
        
        return total_damage

# Unit tests for debugging... this can be ignored
if __name__ == "__main__":
    for r in [1,2,3]:
        for m in range(-3, 5+1):
            print(f"Rank #{r} Bomb: {calculate_damage(2*r,m,1,False)} damage [Modifier: {m}]")
            # print(f"Rank #{r} Headbonk: {calculate_damage(r,m,2,False)} damage [Modifier: {m}]")
            # for h in [3,4,5]:
            #     print(f"Rank #{r} Multibonk ({h} hits): {calculate_damage(r,m,h)} damage [Modifier: {m}]")