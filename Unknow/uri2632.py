def magic_and_sword(width_w: int, height_h:int, coordinate_x0: int, coordinate_y0: int, spell: str, spell_level: int, coordinate_cx: int, coordinate_cy: int) -> int:
    from math import sqrt
    
    spells: dict = {    
        'fire':  {'dmg': 200, 'l1': 20, 'l2': 30, 'l3': 50},
        'water': {'dmg': 300, 'l1': 10, 'l2': 25, 'l3': 40},
        'earth': {'dmg': 400, 'l1': 25, 'l2': 55, 'l3': 70},
        'air':   {'dmg': 100, 'l1': 18, 'l2': 38, 'l3': 60}
    }
    
    range: bool = True
    if coordinate_x0 <= coordinate_cx <= coordinate_x0 + width_w and coordinate_y0 <= coordinate_cy <= coordinate_y0 + height_h:
        range = False
    
    if range:
        c1: int = (coordinate_x0 - coordinate_cx) ** 2
        c2: int = (coordinate_y0 + height_h - coordinate_cy) ** 2
        for i in range(coordinate_x0, coordinate_x0 + width_w + 1):  # type: ignore
            d1 = sqrt((i - coordinate_cx) ** 2 + c1)
            d2 = sqrt((i - coordinate_cx) ** 2 + c2)
    
    return 0
