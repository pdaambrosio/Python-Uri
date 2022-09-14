def magic_and_sword(width_w: int, height_h:int, coordinate_x0: int, coordinate_y0: int, spell: str, spell_level: int, coordinate_cx: int, coordinate_cy: int) -> int:
    from math import sqrt
    
    spells: dict = {    
        'fire':  {'dmg': 200, 'l1': 20, 'l2': 30, 'l3': 50},
        'water': {'dmg': 300, 'l1': 10, 'l2': 25, 'l3': 40},
        'earth': {'dmg': 400, 'l1': 25, 'l2': 55, 'l3': 70},
        'air':   {'dmg': 100, 'l1': 18, 'l2': 38, 'l3': 60}
    }
    
    spell_type: dict = spells[spell]
    spell_damage: int = spell_type['dmg']
    spell_n: int = spell_type[f'l{spell_level}']
    zone: bool = True
    
    if coordinate_x0 <= coordinate_cx <= coordinate_x0 + width_w and coordinate_y0 <= coordinate_cy <= coordinate_y0 + height_h:
        zone = False
    
    if zone:
        c1: int = (coordinate_x0 - coordinate_cx) ** 2
        c2: int = (coordinate_y0 + height_h - coordinate_cy) ** 2
        for i in range(coordinate_x0, coordinate_x0 + width_w + 1):  # type: ignore
            d1 = sqrt((i - coordinate_cx) ** 2 + c1)
            d2 = sqrt((i - coordinate_cx) ** 2 + c2)
            if spell_n >= d1 or spell_n >= d2:
                zone = False
                break
            
    if zone:
        c1: int = (coordinate_y0 - coordinate_cy) ** 2
        c2: int = (coordinate_x0 + width_w - coordinate_cx) ** 2
        for i in range(coordinate_y0, coordinate_y0 + height_h + 1):  # type: ignore
            d1: float = sqrt(c1 + (i - coordinate_cy) ** 2)
            d2: float = sqrt(c2 + (i - coordinate_cy) ** 2)
            if spell_n >= d1 or spell_n >= d2:
                zone = False
                break
    
    return spell_damage if not range else 0


def main() -> None:
    
    loop: int = int(input())
    w: int
    h: int
    x0: int
    y0: int
    spell: str
    n: int
    cx: int
    cy: int
    
    for _ in range(loop):
        [w, h, x0, y0] = map(int, input().split())
        e: list = input().split()
        spell: str = e[0]
        [n, cx, cy] = map(int, e[1:])
        print(magic_and_sword(w, h, x0, y0, spell, n, cx, cy))
        

if __name__ == '__main__':
    main()
