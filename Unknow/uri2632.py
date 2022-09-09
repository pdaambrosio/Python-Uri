def magic_and_sword(width_w: int, height_h:int, coordinate_x0: int, coordinate_y0: int, spell: str, spell_level: int, coordinate_cx: int, coordinate_cy: int) -> int:
    spells: dict = {    
        'fire':  {'dmg': 200, 'l1': 20, 'l2': 30, 'l3': 50},
        'water': {'dmg': 300, 'l1': 10, 'l2': 25, 'l3': 40},
        'earth': {'dmg': 400, 'l1': 25, 'l2': 55, 'l3': 70},
        'air':   {'dmg': 100, 'l1': 18, 'l2': 38, 'l3': 60}
    }
    
    range: bool = True
    if spell_level == 1:
        if abs(coordinate_x0 - coordinate_cx) + abs(coordinate_y0 - coordinate_cy) > spells[spell]['l1']:
            range = False
    elif spell_level == 2:
        if abs(coordinate_x0 - coordinate_cx) + abs(coordinate_y0 - coordinate_cy) > spells[spell]['l2']:
            range = False
    elif spell_level == 3:
        if abs(coordinate_x0 - coordinate_cx) + abs(coordinate_y0 - coordinate_cy) > spells[spell]['l3']:
            range = False
    
    return 0
