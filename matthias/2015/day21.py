from dataclasses import dataclass


@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int


class Character:
    def get_attack(self) -> int:
        pass

    def get_armor(self) -> int:
        pass

@dataclass
class Player(Character):
    health: int
    weapon: Item
    armor: Item
    left_ring: Item
    right_ring: Item

    def get_attack(self) -> int:
        return sum(it.damage for it in [self.weapon, self.left_ring, self.right_ring])

    def get_armor(self) -> int:
        return sum(it.armor for it in [self.armor, self.left_ring, self.right_ring])
    
    def costs(self) -> int:
        return sum(it.cost for it in [self.weapon, self.armor, self.left_ring, self.right_ring])

@dataclass
class Enemy(Character):
    health: int
    damage: int
    armor: int

    def get_attack(self) -> int:
        return self.damage
    
    def get_armor(self) -> int:
        return self.armor

enemy = Enemy(health=103, damage=9, armor=2)

weapons = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
]

armors = [
    Item("EMPTY", 0, 0, 0),
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5),
]

rings = [
    Item("EMPTY", 0, 0, 0),
    Item("Damage+1", 25, 1, 0),
    Item("Damage+2", 50, 2, 0),
    Item("Damage+3", 100, 3, 0),
    Item("Defense+1", 20, 0, 1),
    Item("Defense+2", 40, 0, 2),
    Item("Defense+3", 80, 0, 3),
]

def simulate_fight(p1: Character, p2: Character):
    health1 = p1.health
    health2 = p2.health
    while health1 > 0 and health2 > 0:
        health2 -= max(1, p1.get_attack() - p2.get_armor())
        if health2 <= 0:
            break
        health1 -= max(1, p2.get_attack() - p1.get_armor())
    return health1 > 0


def find_cheapest_solution(enemy=enemy, weapons=weapons, armors=armors, rings=rings):
    cheapest = 0xFFFFFFFF
    for weapon in weapons:
        for armor in armors:
            for left_ring in rings:
                for right_ring in rings:
                    player = Player(100, weapon, armor, left_ring, right_ring)
                    if simulate_fight(player, enemy) and player.costs() < cheapest:
                        cheapest = player.costs()
    return cheapest


def find_expensive_loss(enemy=enemy, weapons=weapons, armors=armors, rings=rings):
    max_cost = 0
    for weapon in weapons:
        for armor in armors:
            for left_ring in rings:
                for right_ring in rings:
                    if right_ring == left_ring: # every ring only exists once
                        continue
                    player = Player(100, weapon, armor, left_ring, right_ring)
                    if not simulate_fight(player, enemy) and player.costs() > max_cost:
                        max_cost = player.costs()
    return max_cost


if __name__ == "__main__":
    print("Rätsel 1:", find_cheapest_solution())
    print("Rätsel 2:", find_expensive_loss())