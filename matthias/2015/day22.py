from typing import Optional, List, Dict
from dataclasses import dataclass, field
from copy import copy, deepcopy


@dataclass
class Player:
    health: int = 50
    mana: int = 500
    armor: int = 0
    mana_spent: int = 0
    actions: List[str] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"- Player has {self.health} hit points, {self.armor} armor, {self.mana} mana, {self.mana_spent} mana spent"


@dataclass
class Boss:
    health: int = 55
    damage: int = 8

    def __repr__(self) -> str:
        return f"- Boss has {self.health} hit points"


known_actions = [
    "Missile",
    "Drain",
    "Shield",
    "Poison",
    "Recharge"
]

def trigger_effects(player: Player, boss: Boss, effects: Dict[str, int]):
    for effect in list(effects.keys()): # needs to be copied into a list to be able to drop it
        effects[effect] -= 1
        if effect == "Poison":
            boss.health -= 3
        elif effect == "Recharge":
            player.mana += 101
        if effects[effect] <= 0:
            effects.pop(effect)
            if effect == "Shield":
                player.armor -= 7


def player_turn(player: Player, boss: Boss, action: str, effects: Dict[str, int], hard_mode: bool = False):
    if hard_mode:
        player.health -= 1
        if player.health <= 0:
            return
    trigger_effects(player, boss, effects)
    player.actions.append(action)
    if action == "Missile":
        player.mana -= 53
        player.mana_spent += 53
        boss.health -= 4
    elif action == "Drain":
        player.mana -= 73
        player.mana_spent += 73
        boss.health -= 2
        player.health += 2
    elif action == "Shield":
        player.mana -= 113
        player.mana_spent += 113
        player.armor += 7
        effects[action] = 6
    elif action == "Poison":
        player.mana -= 173
        player.mana_spent += 173
        effects[action] = 6
    elif action == "Recharge":
        player.mana -= 229
        player.mana_spent += 229
        effects[action] = 5


def boss_turn(player: Player, boss: Boss, effects: Dict[str, int]):
    trigger_effects(player, boss, effects)
    if boss.health <= 0:
        return
    attack = max(1, boss.damage - player.armor)
    player.health -= attack


def round(player: Player, boss: Boss, action: str, effects: Dict[str, int], hard_mode: bool = False):
    player_turn(player, boss, action, effects, hard_mode=hard_mode)
    if boss.health <= 0 or player.mana < 0 or player.health <= 0:
        return
    boss_turn(player, boss, effects)


def filter_actions(actions: List[str], effects: Dict[str, int]):
    for action in actions:
        if effects.get(action, 0) <= 1:
            yield action


def min_max(player: Player, boss: Boss, effects: Dict[str, int]={}, actions=known_actions, best_mana=10_000, hard_mode: bool=False) -> Optional[Player]:
    if player.mana_spent > best_mana:
        return None
    optimal_player = None
    optimal_mana = best_mana
    for action in filter_actions(actions, effects):
        p = deepcopy(player)
        e = copy(boss)
        effs = deepcopy(effects)
        round(p, e, action, effs, hard_mode=hard_mode)
        if p.health <= 0 or p.mana < 0:
            continue
        if e.health <= 0:
            if p.mana_spent < optimal_mana:
                optimal_mana = p.mana_spent
                optimal_player = p
            continue
        final_p = min_max(p, e, effects=effs, actions=actions, best_mana=optimal_mana, hard_mode=hard_mode)
        if final_p and final_p.mana_spent < optimal_mana:
            optimal_mana = final_p.mana_spent
            optimal_player = final_p

    return optimal_player


def simulate(player: Player, boss: Boss, actions: List[str], hard_mode: bool=False):
    effects = {}
    for i, action in enumerate(actions):
        print(f"Round {i}: \n{player}\n{boss}\nCasting {action}\n")
        round(player, boss, action, effects, hard_mode=hard_mode)
    print(f"Results: \n{player}\n{boss}")
    
    

player = min_max(Player(), Boss())
print("Rätsel 1: ", player.mana_spent)

player = min_max(Player(), Boss(), hard_mode=True)
print("Rätsel 1: ", player.mana_spent)
