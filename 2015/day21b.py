from functools import cache

@cache
def win_fight(damage, armor):
    hit_points = 100
    boss_hit_points = 104
    boss_damage = 8
    boss_armor = 1
    while 1:
        # our turn
        boss_hit_points -= max(1, damage - boss_armor)
        if boss_hit_points <= 0: return True # we win
        # boss's turn
        hit_points -= max(1, boss_damage - armor)
        if hit_points <= 0: return False # we lose

ring_info = ((0,0,0),(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3))

max_gold = 0
for weapon_cost, weapon_damage in ((8,4),(10,5),(25,6),(40,7),(74,8)):
    for armor_cost, armor_armor in ((0,0),(13,1),(31,2),(53,3),(75,5),(102,5)):
        for ring1_cost, ring1_damage, ring1_armor in ring_info:
            for ring2_cost, ring2_damage, ring2_armor in ring_info:
                if not win_fight(damage=weapon_damage+ring1_damage+ring2_damage, armor=armor_armor+ring1_armor+ring2_armor):
                    max_gold = max(max_gold, weapon_cost+armor_cost+ring1_cost+ring2_cost)
print(max_gold)