init python:
    import random
    from abc import ABC, abstractmethod
    """
    Available magic elements:
        FIRE
        WATER
        EARTH
        AIR
        LIGHTNING
        ICE
        LIGHT
        DARK
        PHYSICAL
    """

    class BattleException(Exception):
        pass

    class MagicAbility:
        def __init__(self, name: str, description: str, damage: int, cost: int, element: str, cast_time: float, effect: str | None = None, effect_chance: float = 0, *, _transform=None, _image: str = None, _sound=None, multi:bool = False):
            self.name = name
            self.description = description
            self.damage = damage
            self.cost = cost
            self.element = element
            self.cast_time = cast_time # this will be used as a delay before showing the results
            self.effect = effect
            self.effect_chance = effect_chance
            self._transform = _transform
            self._image = _image
            self._sound = _sound
            self.multi = multi
    
    class HealingAbility:
        def __init__(self, name: str, description: str, heal: int, cost: int, cast_time: float, negative_effects: list[str] | None = None, negative_effect_chance: float = 0, positive_effect: str | None = None, positive_effect_chance: float = 0, *, _transform=None, _image: str = None, _sound=None, multi:bool = False):
            self.name = name
            self.description = description
            self.heal = heal
            self.cost = cost
            self.element = "HEALING"
            self.cast_time = cast_time # this will be used as a delay before showing the results
            self.negative_effects = negative_effects
            self.negative_effect_chance = negative_effect_chance
            self.positive_effect = positive_effect
            self.positive_effect_chance = positive_effect_chance
            self._transform = _transform
            self._image = _image
            self._sound = _sound
            self.multi = multi
    
    class Item(ABC): # inherit off of this for healing items and attack items
        def __init__(self, name: str, description: str, cast_time: float):
            self.name = name
            self.description = description
            self.cast_time = cast_time
        
        @abstractmethod
        def use_item(self, target):
            global party_inventory
            if self in party_inventory:
                party_inventory.remove(self)
            else:
                raise BattleException("Item not in inventory")
        
        @abstractmethod
        def single(self, target):
            pass
        
        @abstractmethod
        def multiple(self, targets):
            pass
    
    class AttackItem(Item):
        def __init__(self, name: str, description: str, damage: int, element: str, cast_time: float, effect: str | None = None, effect_chance: float = 0, *, _transform=None, _image: str = None, _sound=None, multi:bool = False):
            self.name = name
            self.description = description
            self.damage = damage
            self.element = element
            self.cast_time = cast_time # this will be used as a delay before showing the results
            self.effect = effect
            self.effect_chance = effect_chance
            self._transform = _transform
            self._image = _image
            self._sound = _sound
            self.multi = multi
        
        def use_item(self, target):
            super().use_item(target)

            if self.multi:
                return self.multiple(target)
            return self.single(target)

        def single(self, target) -> str:
            damage = random.randint(self.damage // 2, self.damage)
            hit = random.randint(1, self.accuracy - (100 if "BLIND" in self.current_effects else 0)) > random.randint(1, target.evasion) or self.name == "Follow Up" or self.name == "Band Together" or target.is_guarding
            affected = ""
            critical = False
            if not self.multi: # since this is used in the multi-target function, I want to prevent the cost from being subtracted twice
                self.magic -= self.cost
            if hit:
                if target.is_guarding:
                    damage //= 2
                else:
                    if self.element in target.weaknesses:
                        damage *= 2
                    elif self.element == "PHYSICAL":
                        critical = random.randint(1, self.strength) > random.randint(1, target.defense)
                        if critical:
                            damage *= 2
                damage -= target.defense
                if self.effect is not None and random.random() <= (self.effect_chance / 100.0):
                    target.apply_effect(self.effect)
                    f"APPLIED {self.effect}\n"
                if damage < 0:
                    damage = 0
                target.health -= damage
                if target.health <= 0:
                    affected += f"KILLED\n"
                if target.is_guarding:
                    return f"HIT\nGUARDED\n{damage}\n{affected}"
                if self.element in target.weaknesses:
                    return f"HIT\nWEAKNESS\n{damage}\n{affected}"
                if critical:
                    return f"HIT\nCRITICAL\n{damage}\n{affected}"
                return f"HIT\n{damage}\n{affected}"
            return f"MISS"
        
        def single(self, target) -> str:
            heal = random.randint(ability.heal // 2, ability.heal)
            affected = ""
            if not ability.multi: # since this is used in the multi-target function, I want to prevent the cost from being subtracted twice
                self.magic -= ability.cost
            if ability.negative_effects is not None and random.random()*100.0 <= ability.negative_effect_chance:
                for effect in ability.negative_effects:
                    del target.current_effects[effect]
                    affected += f"CURED {effect}\n"
            if ability.positive_effect is not None and random.random()*100.0 <= ability.positive_effect_chance:
                target.apply_effect(ability.positive_effect)
                affected += f"APPLIED {ability.positive_effect}\n"
            target.health += heal
            if target.health > target.max_health:
                target.health = target.max_health
                return f"FULL\nHEAL\n{heal}\n{affected}"
            return f"HEAL\n{heal}\n{affected}"
        
        def multiple(self, targets) -> list[str]:
            if not self.multi:
                raise BattleException("This item is not multi-target (why did you call this when it was clearly for multi-target?)")
            attacks = [self.single(target) for target in targets]
            return attacks
        
    class HealingItem(Item):
        def __init__(self, name: str, description: str, damage: int, element: str, cast_time: float, effect: str | None = None, effect_chance: float = 0, *, _transform=None, _image: str = None, _sound=None, multi:bool = False):
            self.name = name
            self.description = description
            self.damage = damage
            self.element = element
            self.cast_time = cast_time # this will be used as a delay before showing the results
            self.effect = effect
            self.effect_chance = effect_chance
            self._transform = _transform
            self._image = _image
            self._sound = _sound
            self.multi = multi
        
        def use_item(self, target):
            super().use_item(target)

            if self.multi:
                return self.multiple(target)
            return self.single(target)
        
        def multiple(self, targets) -> list[str]:
            if not self.multi:
                raise BattleException("This item is not multi-target (why did you call this when it was clearly for multi-target?)")
            attacks = [self.single(target) for target in targets]
            return attacks

    class BattleMember(object, ABC): # Parent class for party members and enemies
        def __init__(self, name: str, kanji: str, max_health: int, strength: int, defense: int, max_magic: int, speed: int, accuracy: int, evasion: int, weaknesses: list[str], magic_abilities:list[MagicAbility | HealingAbility], follow_up:MagicAbility, band_together_attack:MagicAbility):
            self.name = name
            self.kanji = kanji
            self.max_health = max_health
            self.health = max_health
            self.strength = strength
            self.defense = defense
            self.max_magic = max_magic
            self.magic = max_magic
            self.speed = speed
            self.accuracy = accuracy
            self.evasion = evasion
            self.weaknesses = weaknesses
            self.magic_abilities = magic_abilities
            self.is_guarding = False
            self.current_effects = {}
            self.effect_tick = 0
            self.follow_up = follow_up
            self.confuse_action = [None, None]
            self.band_together_attack = band_together_attack

        def decide_turn(self) -> int:
            return random.randint(1, self.speed)
        
        def effect_tick_down(self) -> str:
            cured = ""
            for effect in self.current_effects:
                self.current_effects[effect] -= 1
                if self.current_effects[effect] <= 0:
                    del self.current_effects[effect]
                    cured += f"WORE OFF {effect}\n"
            return cured

        def apply_effect(self, effect: str) -> None:
            if effect in self.current_effects:
                self.current_effects[effect] += 3
            else:
                self.current_effects[effect] = 3
        
        def normal_attack(self, target) -> str:
            damage = random.randint(self.strength // 2, self.strength)
            hit = random.randint(1, self.accuracy - (100 if "BLIND" in self.current_effects else 0)) > random.randint(1, target.evasion) or target.is_guarding
            affected = ""
            critical = False
            if hit:
                if target.is_guarding:
                    damage //= 2
                else:
                    if "PHYSICAL" in target.weaknesses:
                        damage *= 2
                    else:
                        critical = random.randint(1, self.strength) > random.randint(1, target.defense)
                        if critical:
                            damage *= 2
                damage -= target.defense
                if damage < 0:
                    damage = 0
                target.health -= damage
                if target.health <= 0:
                    affected += f"KILLED\n"
                if target.is_guarding:
                    return f"HIT\nGUARDED\n{damage}\n{affected}"
                if "PHYSICAL" in target.weaknesses:
                    return f"HIT\nWEAKNESS\n{damage}\n{affected}"
                if critical:
                    return f"HIT\nCRITICAL\n{damage}\n{affected}"
                return f"HIT\n{damage}\n{affected}"
            return f"MISS"

        def magic_attack_single(self, ability: MagicAbility, target) -> str:
            damage = random.randint(ability.damage // 2, ability.damage)
            hit = random.randint(1, self.accuracy - (100 if "BLIND" in self.current_effects else 0)) > random.randint(1, target.evasion) or ability.name == "Follow Up" or ability.name == "Band Together" or target.is_guarding
            affected = ""
            critical = False
            if not ability.multi: # since this is used in the multi-target function, I want to prevent the cost from being subtracted twice
                self.magic -= ability.cost
            if hit:
                if target.is_guarding:
                    damage //= 2
                else:
                    if ability.element in target.weaknesses:
                        damage *= 2
                    elif ability.element == "PHYSICAL":
                        critical = random.randint(1, self.strength) > random.randint(1, target.defense)
                        if critical:
                            damage *= 2
                damage -= target.defense
                if ability.effect is not None and random.random() <= (ability.effect_chance / 100.0):
                    target.apply_effect(ability.effect)
                    f"APPLIED {ability.effect}\n"
                if damage < 0:
                    damage = 0
                target.health -= damage
                if target.health <= 0:
                    affected += f"KILLED\n"
                if target.is_guarding:
                    return f"HIT\nGUARDED\n{damage}\n{affected}"
                if ability.element in target.weaknesses:
                    return f"HIT\nWEAKNESS\n{damage}\n{affected}"
                if critical:
                    return f"HIT\nCRITICAL\n{damage}\n{affected}"
                return f"HIT\n{damage}\n{affected}"
            return f"MISS"

        def magic_attack_multi(self, ability: MagicAbility, targets: list) -> list[str]:
            if not ability.multi:
                raise BattleException("This ability is not multi-target (why did you call this when it was clearly for multi-target?)")
            attacks = [self.magic_attack_single(ability, target) for target in targets]
            return attacks

        def heal_single(self, ability: HealingAbility, target) -> str:
            heal = random.randint(ability.heal // 2, ability.heal)
            affected = ""
            if not ability.multi: # since this is used in the multi-target function, I want to prevent the cost from being subtracted twice
                self.magic -= ability.cost
            if ability.negative_effects is not None and random.random()*100.0 <= ability.negative_effect_chance:
                for effect in ability.negative_effects:
                    del target.current_effects[effect]
                    affected += f"CURED {effect}\n"
            if ability.positive_effect is not None and random.random()*100.0 <= ability.positive_effect_chance:
                target.apply_effect(ability.positive_effect)
                affected += f"APPLIED {ability.positive_effect}\n"
            target.health += heal
            if target.health > target.max_health:
                target.health = target.max_health
                return f"FULL\nHEAL\n{heal}\n{affected}"
            return f"HEAL\n{heal}\n{affected}"
        
        def heal_multi(self, ability: HealingAbility, targets: list) -> list[str]:
            if not ability.multi:
                raise BattleException("This ability is not multi-target (why did you call this when it was clearly for multi-target?)")
            self.magic -= ability.cost
            heals = [self.heal_single(ability, target) for target in targets]
            return heals

        def guard(self) -> str:
            self.is_guarding = True
            return "GAURD"
        
        def stop_guarding(self) -> None:
            self.is_guarding = False

        def perform_follow_up(self, target = None, multi_target: list | None = None) -> str | list[str]:
            global can_follow_up
            global followed_up
            if self in can_follow_up:
                can_follow_up.remove(self)
                followed_up.append(self)
            else:
                raise BattleException("This member isn't in the follow up list.")
            if self.follow_up.multi:
                return self.magic_attack_multi(self.follow_up, multi_target)
            return self.magic_attack_single(self.follow_up, target)
        
        def band_together_ability(self, targets: list) -> list[str]:
            if not self.band_together_attack.multi:
                raise BattleException("Band Together Ability must be a multi-target ability")
            return self.magic_attack_multi(self.band_together_attack, targets)
        
        def confuse_choose_action(self, party: list, enemies: list):
            all_abilities = ["Normal Attack", *self.magic_abilities]
            for ability in all_abilities[1:]:
                if ability.multi or ability.cost > self.magic:
                    all_abilities.remove(ability)
            self.confuse_action[0] = random.choice(all_abilities)
            all_members = [*party, *enemies]
            self.confuse_action[1] = random.choice([member for member in all_members if member.health > 0])
    
    class PartyMember(BattleMember):
        def __init__(self, *args, starting_exp:int=0, level_up:int=100, new_abilities:dict[int:list[MagicAbility | HealingAbility]]={}, max_level: int = 99, **kwargs):
            super().__init__(*args, **kwargs)
            self.exp = 0
            self.total_exp = starting_exp
            self.level = 1
            self.exp_to_next_level = level_up
            self.new_abilities = new_abilities
            self.max_level = max_level
            self.charm_action = [None, None]
            self.gain_exp(self.total_exp)

        def level_up(self) -> str:
            if self.level < self.max_level:
                self.level += 1
                self.exp_to_next_level *= 2
                self.max_health += 10
                self.health = self.max_health
                self.strength += 5
                self.defense += 5
                self.max_magic += 5
                self.magic = self.max_magic
                self.speed += 5
                self.accuracy += 5
                if self.new_abilities.get(self.level) is not None:
                    self.magic_abilities += self.new_abilities[self.level]
                return "LEVEL UP"
            return ""
        
        def gain_exp(self, exp: int) -> None:
            self.exp += exp
            self.total_exp += exp
            while self.exp >= self.exp_to_next_level:
                self.exp -= self.exp_to_next_level
                self.level_up()
        
        def get_needed_exp(self) -> int:
            return self.exp_to_next_level - self.exp
        
        def charm_choose_action(self, party: list, enemies: list):
            all_abilities = ["Normal Attack", *self.magic_abilities]
            for ability in all_abilities[1:]:
                if ability.cost > self.magic:
                    all_abilities.remove(ability)
            self.charm_action[0] = random.choice(all_abilities)
            if self.charm_action[0] == "Normal Attack" or isinstance(self.charm_action[0], MagicAbility):
                if self.charm_action[0] == "Normal Attack" or not self.charm_action[0].multi:
                    self.charm_action[1] = random.choice([member for member in party if member.health > 0])
                else:
                    self.charm_action[1] = party
            elif isinstance(self.charm_action[0], HealingAbility):
                if self.charm_action[0].multi:
                    self.charm_action[1] = enemies
                else:
                    self.charm_action[1] = random.choice([member for member in enemies if member.health > 0])
        
        
    class Enemy(BattleMember):
        def __init__(self, *args, _image: str, exp: int, **kwargs):
            super().__init__(*args, **kwargs)
            self.all_abilities = ("Normal Attack", *self.magic_abilities)
            self.exp = exp # This is the experience that will be obtained upon killing this enemy
            self._image = _image
            self.next_action = [None, None] # [ability, target], this is here because I believe we can have a certain character reveal the enemy's next action before it happens
        
        def attack(self, target: BattleMember) -> str:
            if self.next_action[0] == "Normal Attack":
                return self.normal_attack(self.next_action[1])
            elif isinstance(self.next_action[0], MagicAbility):
                return self.magic_attack(self.next_action[0], self.next_action[1])
            elif isinstance(self.next_action[0], HealingAbility):
                return self.heal(self.next_action[0], self.next_action[1])
            return "NOT AN ABILITY"
        
        def choose_action(self, party: list[PartyMember], enemies: list) -> None:
            self.next_action[0] = random.choice(self.all_abilities)
            if self.next_action[0] == "Normal Attack" or isinstance(self.next_action[0], MagicAbility):
                if self.next_action[0] == "Normal Attack" or not self.next_action[0].multi:
                    self.next_action[1] = random.choice([member for member in party if member.health > 0])
                else:
                    self.next_action[1] = party
            elif isinstance(self.next_action[0], HealingAbility):
                if self.next_action[0].multi:
                    self.next_action[1] = enemies
                else:
                    self.next_action[1] = random.choice([member for enemies in party if member.health > 0])

    class Boss(Enemy): # these will have special abilities and will be harder to defeat, also their turn number is not randomized
        def __init__(self, *args, phases: tuple, turn_number:int=-1, **kwargs):
            super().__init__(*args, **kwargs)
            self.turn_number = turn_number
            self.phases = phases
            self.current_phase = 0
            try:
                self.abilities_available = self.all_abilities[phases[0].abilites_available[0]:phases[0].abilites_available[1]]
            except:
                raise BattleException("Boss must have at least one phase, make sure they were properly created before passing them to the Boss class")
        
        def decide_turn(self) -> int:
            if self.turn_number == -1:
                return random.randint(1, self.speed)
            return self.turn_number
        
        def choose_action(self, party: list[PartyMember], enemies: list) -> None:
            self.next_action[0] = random.choice(self.abilities_available)
            if self.next_action[0] == "Normal Attack" or isinstance(self.next_action[0], MagicAbility):
                if self.next_action[0] == "Normal Attack" or not self.next_action[0].multi:
                    self.next_action[1] = random.choice([member for member in party if member.health > 0])
                else:
                    self.next_action[1] = party
            elif isinstance(self.next_action[0], HealingAbility):
                if self.next_action[0].multi:
                    self.next_action[1] = enemies
                else:
                    self.next_action[1] = random.choice([member for enemies in party if member.health > 0])

        def force_choose_action(self, ability: MagicAbility | HealingAbility, targets: list[BattleMember]) -> None:
            self.next_action[0] = ability
            self.next_action[1] = targets
    
    class BossPhase:
        def __init__(self, health_needed: int, abilites_available: tuple[int]):
            self.health_needed = health_needed
            self.abilites_available = abilites_available

    def decide_turn_order(party: list[PartyMember], enemies: list[Enemy | Boss]) -> None:
        global turn_order
        turn_numbers = {}
        for member in [*party, *enemies]:
            turn_numbers[member] = member.decide_turn()
        turn_order.clear()
        turn_order = sorted(turn_numbers, key=turn_numbers.get, reverse=True)
        global current_turn
        current_turn = 0
    
    def fill_follow_up(party: list[PartyMember], enemies: list[Enemy | Boss]) -> None:
        global can_follow_up
        can_follow_up.clear()
        global turn_order
        global current_turn
        who_started = turn_order[current_turn]
        if isinstance(who_started, PartyMember) != ("CHARM" in who_started.current_effects):
            for member in party:
                can_follow_up.append(member)
        else:
            for member in enemies:
                can_follow_up.append(member)
        if who_started in can_follow_up:
            can_follow_up.remove(who_started)
        for member in can_follow_up:
            if member.health <= 0 or any(effect for effect in member.current_effects if effect in available_negative_effects):
                can_follow_up.remove(member)
    
    def band_together_attack(party: list[PartyMember], enemies: list[Enemy | Boss]) -> list[str]:
        global turn_order
        global current_turn
        who_started = turn_order[current_turn]
        attacks = [member.band_together_ability(enemies if isinstance(who_started, PartyMember) else party) for member in (party if isinstance(who_started, PartyMember) else enemies)]
        return attacks
    
    def next_turn() -> None:
        global current_turn
        global turn_order
        global followed_up
        current_turn += 1
        current_turn %= len(turn_order)
        followed_up.clear()
    
    available_negative_effects = ("BURN", "POISON", "SLEEP", "PARALYZE", "FREEZE", "SEAL", "CONFUSE", "CHARM", "FEAR", "ENRAGE", "BLIND", "STAT DEBUFF")
    available_positive_effects = ("SHIELD", "REFLECT", "REGENERATE", "STAT BUFF")
    def effect_update(target: BattleMember) -> str:
        """
        Available negative effects:
            BURN: Reduces the target's health each turn for 3 turns, double damage if weak to fire
            POISON: Reduces the target's health each turn for 3 turns, double damage if weak to poison
            SLEEP: Puts the target to sleep, preventing them from attacking for 3 turns, but they heal each turn
            PARALYZE: Paralyzes the target, preventing them from attacking for 3 turns
            FREEZE: Freezes the target, preventing them from attacking for 3 turns, also gaurentees critical from normal attacks (this will break the freeze effect)
            SEAL: Prevents the target from using magic for 3 turns
            CONFUSE: Randomly chooses the target's action for 3 turns, these include attacking pary members and healing enemies
            CHARM: Puts the target on the user's side, if party, the player will control what the target doing for the next 3 turns, if enemy, the target will act as an enemy for the next 3 turns
            FEAR: On turn, 60% chance to force skip turn, 20% chance to run away, 20% chance to actually do commanded action
            ENRAGE: Force target to only use normal attacks for 3 turns, however strength is buffed
            BLIND: Severe, and I mean severe, disadvantage on accuracy for 3 turns
            STAT DEBUFF: Reduces the target's stats for 3 turns

        Available positive effects:
            SHIELD: Negates damage on the target for 3 turns
            REFLECT: Reflects damage back to the attacker for 3 turns
            REGENERATE: Heals the target each turn for 3 turns
            STAT BUFF: Increases the target's stats for 3 turns
        """
        r: str = ""
        for effect in target.current_effects:
            match effect:
                case "BURN":
                    damage = target.max_health // 10
                    target.health -= damage
                    r += f"BURN\n{damage}\n"
                case "POISON":
                    damage = target.max_health // 10
                    target.health -= damage
                    r += f"POISON\n{damage}\n"
                case "REGENERATE":
                    heal = target.max_health // 10
                    target.health += heal
                    if target.health > target.max_health:
                        target.health = target.max_health
                    r += f"REGENERATE\n{heal}\n"
                case "SLEEP":
                    heal = target.max_health // 10
                    target.health += heal
                    if target.health > target.max_health:
                        target.health = target.max_health
                    magic_recovery = target.max_magic // 10
                    target.magic += magic_recovery
                    if target.magic > target.max_magic:
                        target.magic = target.max_magic
                    r += f"SLEEP\n{heal}\n{magic_recovery}\n"
        return r
    
    def decide_enemy_actions(enemies: list[Enemy | Boss], party: list[PartyMember]) -> None:
        for enemy in enemies:
            enemy.choose_action(party, enemies)
    
    def get_article(word) -> str: # Curse English grammar for making me write a function like this!!!  (No acronym handling, but I don't think we'll need that)
        import re
        word = word.lower().strip()
        if not word:
            return ""

        if re.match(r'^(one|uni(v|t|f|l)|u(se|ti|p)|eu(l|p|r))', word):
            return "a"

        if re.match(r'^h(our|on|ei)', word):
            return "an"

        if word[0] in 'aeiou':
            return "an"

        return "a"
    
    def kill_yourself(targets: list[BattleMember]) -> list[str]:
        for target in targets:
            target.health = 0
        return [f"KILLED\n" for _ in targets]
    
    def get_target_center(target) -> tuple[int, int]:
        x: int = 0
        y: int = 0
        global active_party
        global active_enemies
        if target in active_party:
            center: int = 1280 // (len(active_party)*2)
            left: int = 1280 // len(active_party) * active_party.index(target)
            x = left + center
            y = 75
        elif target in active_enemies:
            center: int = 1280 // (len(active_enemies)*2)
            left: int = 1280 // len(active_enemies) * active_enemies.index(target)
            x = left + center
            y = 435
        else:
            BattleException("Target isn't actively in this battle")
        return (x, y)
    
    def party_restoration(party: list[PartyMember]) -> None:
        for member in party:
            member.health = member.max_health
            member.magic = member.max_magic
            member.current_effects.clear()
    
    def enemies_restoration(enemies: list[Enemy | Boss]) -> None:
        for enemy in enemies:
            enemy.health = enemy.max_health
            enemy.magic = enemy.max_magic
            enemy.current_effects.clear()

transform scroll_left(t):
    subpixel True
    xtile 2
    xpos 0.0
    blur 1.0 / t
    linear t xpos -1.0
    repeat

transform scroll_right(t):
    subpixel True
    xtile 2
    xpos -1.0
    blur 1.0 / t
    linear t xpos 0.0
    repeat


default name_of_battle = ""
default can_follow_up = [] # fill this with available party members who can follow up when conditions are fulfilled
default followed_up = [] # this will be filled with party members who have already followed up, this will be cleared at the start of each turn, if this matches the party during any turn, then the band together attack will happen
default turn_order = []
default active_party = []
default active_enemies = [] # remember to remove each enemy that is defeated from this list
default current_turn = 0
default selected_ability = None
default selected_target = None
default current_actor = None
default follow_up_actor = None
default ability_results = None
default checkpoint_to_jump = "battle_loop"
default start_of_battle = "battle_loop" # set this to the starting label of each battle
default last_checkpoint = None # set this to the checkpoint label of each battle phase (None if it is the very start of the battle)
default party_inventory = [] # fill this with any items that are obtained along the way, they will be used in battles mostly

# It is highly recommended to call a label that calls this one for this to work, because if you call this from the current main story label, the only real option to jump to is the start of that loop if the battle is failed, and it will cause the player to completely restart that story instead of just the battle
# I'm using they/them pronouns to address every member since there's no real way to identify gender here
# If battle is called twice in the same sequence (i.e. something you'd do for boss phase transitions or something), DO NOT CHANGE THE NAME FOR THE BATTLE
label battle(name, party, enemies, transition_background, battle_background, _music = audio.default_battle_music, *, override_victory = "battle_victory", override_defeat = "battle_defeat", victory_args = tuple(), defeat_args = tuple(), victory_kwargs = {}, defeat_kwargs = {}, restore_party = True, restore_enemies = True):
    if last_checkpoint is None:
        $ active_party = party
        $ active_enemies = enemies
        $ decide_turn_order(party, enemies)
    
    if _music is not None:
        $ renpy.music.play(_music)
    $ name_of_battle = name
    $ quick_menu = False
    $ current_turn = 0
    $ can_follow_up = []
    $ followed_up = []
    $ selected_ability = None
    if restore_party:
        $ party_restoration(party)
    if restore_enemies:
        $ enemies_restoration(enemies)
    scene expression transition_background at scroll_right(0.175)
    show battle_start at truecenter
    with Fade(0.1, 0.0, 0.1, color="#fff")
    pause 4.3
    hide battle_start with None
    scene expression battle_background
    show screen enemies_display
    show screen party_stats(party)
    with Fade(1.0, 0.0, 0.5, color="#fff")
    show screen turn_order_display
    pause 2.25
    $ decide_enemy_actions(enemies, party) # placed so the enemies have a decided move at the start of the battle

    label battle_loop:
        $ current_actor = turn_order[current_turn]
        $ current_actor.stop_guarding()
        $ followed_up.clear()

        if all(e.health <= 0 for e in enemies):
            $ quick_menu = True
            hide screen party_stats
            hide screen turn_order_display
            call expression override_victory pass (*victory_args, **victory_kwargs)
            hide screen enemies_display
            return
        if all(p.health <= 0 for p in party):
            $ quick_menu = True
            hide screen party_stats
            hide screen turn_order_display
            hide screen enemies_display
            call expression override_defeat pass (*defeat_args, **defeat_kwargs)
            jump expression checkpoint_to_jump

        $ selected_ability = None
        $ selected_target = None
        $ ability_results = None
        $ follow_up_actor = None
        if current_actor.health > 0 and "PARALYZE" not in current_actor.current_effects and "SLEEP" not in current_actor.current_effects:
            "[current_actor.name] takes their turn!"
            if isinstance(current_actor, PartyMember) != ("CHARM" in current_actor.current_effects):
                if isinstance(current_actor, Enemy):
                    "[current_actor.name] is charmed!  You're in control!"
                if "CONFUSE" in current_actor.current_effects:
                    "[current_actor.name] is confused!"
                    $ current_actor.confuse_choose_action(party, enemies)
                    $ selected_ability = current_actor.confuse_action[0]
                    $ selected_target = current_actor.confuse_action[1]
                else:
                    call screen battle_choice
            else:
                if isinstance(current_actor, PartyMember):
                    "[current_actor.name] is charmed!  They're in control!"
                    $ current_actor.charm_choose_action(party, enemies)
                    $ selected_ability = current_actor.charm_action[0]
                    $ selected_target = current_actor.charm_action[1]
                else:
                    $ selected_ability = current_actor.next_action[0]
                    $ selected_target = current_actor.next_action[1]
                    $ current_actor.choose_action(party, enemies)

            if selected_ability == "Guard":
                $ selected_target = current_actor
                $ ability_results = current_actor.guard()
                show screen attack_results_display(0.0)
                "[current_actor.name] raises their guard!"
            elif isinstance(selected_ability, Item):
                $ ability_results = selected_ability.use_item(selected_target)
                show screen attack_results_display(selected_ability.cast_time)
                "[current_actor.name] uses [get_article(selected_ability.name)] [selected_ability.name]!"
            elif isinstance(selected_ability, (MagicAbility, HealingAbility)):
                if isinstance(selected_ability, HealingAbility):
                    if selected_ability.multi:
                        $ ability_results = current_actor.heal_single(selected_ability, selected_target)
                    else:
                        $ ability_results = current_actor.heal_multi(selected_ability, selected_target)
                else:
                    if selected_ability.multi:
                        $ ability_results = current_actor.magic_attack_multi(selected_ability, selected_target)
                    else:
                        $ ability_results = current_actor.magic_attack_single(selected_ability, selected_target)
                play sound selected_ability._sound
                show expression selected_ability._image at selected_ability._transform
                show screen attack_results_display(selected_ability.cast_time)
                "[current_actor.name] casts [selected_ability.name]!"
            elif selected_ability == "Normal Attack":
                $ ability_results = current_actor.normal_attack(selected_target)
                show screen attack_results_display(0.25)
                "[current_actor.name] attacks!"
            else:
                $ selected_target = party
                $ ability_results = kill_yourself(selected_target)
                show screen attack_results_display(0.0)
                "The party comits suicide!"
        elif current_actor.health > 0:
            if "PARALYZE" in current_actor.current_effects:
                "[current_actor.name] is paralyzed!"
            elif "SLEEP" in current_actor.current_effects:
                "[current_actor.name] is asleep!"
            else:
                "[current_actor.name] can't act for unknown reasons!"
        else:
            "[current_actor.name] is dead!"

        # follow ups
        if "CONFUSE" not in current_actor.current_effects and ("WEAKNESS" in ability_results or "CRITICAL" in ability_results):
            $ fill_follow_up(party, enemies)
            call follow_up_loop
        
        $ ability_results = effect_update(current_actor)
        $ selected_target = current_actor
        $ current_actor.effect_tick_down()
        if current_actor.current_effects != {}:
            show screen attack_results_display(0.0)
            "[current_actor.name] gets affected by their current effects!"
        $ next_turn()

        jump battle_loop

screen attack_results_display(delay, center = None):
    if isinstance(ability_results, list):
        for result in range(len(ability_results)):
            text ability_results[result] text_align 0.5 at results_transform(delay, get_target_center(selected_target[result]) if center is None else center)
    elif ability_results is not None:
        text ability_results text_align 0.5 at results_transform(delay, get_target_center(selected_target) if center is None else center)
    timer delay+2.0 action Hide("attack_results_display")

transform results_transform(d, c):
    xcenter c[0]
    ycenter c[1]
    on show:
        xoffset -1280
        alpha 0.0
        d
        linear 0.1 xoffset -10 alpha 1.0
        linear 1.0 xoffset 10 
        linear 0.1 xoffset 1280 alpha 0.0

default ability_description = ""
screen ability_selection(member):
    frame:
        xysize (300, 700)
        frame: # frame for the viewport
            viewport: # viewport for the ability buttons
                has vbox
                for ability in member.magic_abilities:
                    button: # button for the ability
                        hovered SetVariable("ability_description", ability.description)
                        unhovered SetVariable("ability_description", "")
                        action If(member.magic >= ability.cost, [SetVariable("selected_ability", ability), Hide("ability_selection")])
                        hbox:
                            xalign 0.5
                            add "[ability.element].png" # will change this if the image happens to be in a different folder
                            frame:
                                xysize (250, 20)
                                text ability.name
                            frame:
                                xysize (20, 20)
                                text "[ability.cost:>2:0]" text_align 1.0
        frame: # frame for the ability description
            text ability_description

default item_description = ""
screen item_selection:
    frame:
        xysize (300, 700)
        frame: # frame for the viewport
            viewport: # viewport for the item buttons
                has vbox
                for item in party_inventory:
                    button: # button for the item
                        hovered SetVariable("item_description", item.description)
                        unhovered SetVariable("item_description", "")
                        action [SetVariable("selected_ability", item), Hide("item_selection")]
                        hbox:
                            xalign 0.5
                            add "[item.element].png" # will change this if the image happens to be in a different folder
                            frame:
                                xysize (250, 20)
                                text item.name
        frame: # frame for the item description
            text item_description

screen party_stats(party):
    for member in party:
        button at from_top(3.5, 0.5 * party.index(member)):
            xysize (1280 // len(party), 150)
            xpos (1280 // len(party)) * party.index(member)
            if member == turn_order[current_turn]:
                background "#3338" # turn highlight
            elif isinstance(selected_ability, HealingAbility) and selected_ability.multi:
                background "#5558"
            else:
                background "#0008" # unhighlight
            hover_background "#5558"
            vbox:
                #add "[member.icon].png" # Who knows if we will have icons for our party members
                text member.kanji size 25 font battle_font
                text member.name size 15 font battle_font
                text "HEALTH: [member.health]/[member.max_health]" font battle_font
                text "MAGIC: [member.magic]/[member.max_magic]" font battle_font
            action If(selected_target is None and isinstance(selected_ability, HealingAbility), [If(isinstance(selected_ability, HealingAbility) and selected_ability.multi, SetVariable("selected_target", active_party), SetVariable("selected_target", member)), Return()])

default scanned_action = ""
screen enemies_display:
    text scanned_action xalign 0.5 yalign 1.0 text_align 0.5
    for enemy in active_enemies:
        button at from_bottom(3.5, 0.5 * active_enemies.index(enemy)):
            xysize (1280 // len(active_enemies), 400)
            xpos (1280 // len(active_enemies)) * active_enemies.index(enemy)
            yalign 0.75
            if enemy == turn_order[current_turn]:
                background "#3338" # turn highlight
            elif isinstance(selected_ability, MagicAbility) and selected_ability.multi:
                background "#5558"
            else:
                background "#0000" # unhighlight
            hover_background "#5558"
            add enemy._image xalign 0.5 yalign 0.5
            text enemy.name xalign 0.5 size 13 font battle_font text_align 0.5
            action If(selected_target is None and (isinstance(selected_ability, (MagicAbility, str)) or isinstance(follow_up_actor, PartyMember)), [If(isinstance(selected_ability, MagicAbility) and selected_ability.multi, SetVariable("selected_target", active_enemies), SetVariable("selected_target", enemy)), Return()], If(current_actor == test_monika or current_actor == monika, NullAction()))
            hovered If(current_actor == test_monika or current_actor == monika, SetVariable("scanned_action", "NEXT ACTION: [enemy.next_action[0] if isinstance(enemy.next_action[0], str) else enemy.next_action[0].name]\nTARGET: [enemy.next_action[1].name]"))
            unhovered SetVariable("scanned_action", "")          

screen battle_choice:
    frame at from_top(1.0):
        ysize 50
        ypos 160
        xalign 0.5
        hbox:
            xalign 0.5
            if selected_ability is None:
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("ATTACK") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action [SetVariable("selected_ability", "Normal Attack"), Hide("ability_selection"), Hide("item_selection")]
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("MAGIC") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action Show("ability_selection", None, current_actor)
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("ITEM") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action Show("item_selection")
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("GUARD") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action [SetVariable("selected_ability", "Guard"), Hide("ability_selection"), Hide("item_selection")]
            elif selected_ability == "Guard":
                frame:
                    xsize 600
                    background "#0000"
                    text _("Confirm Guard?") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("CONFIRM") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action Return()
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("BACK") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action SetVariable("selected_ability", None)
            elif selected_ability == "Kill Yourself": # This is mainly gonna be used to reset the battle
                frame:
                    xsize 600
                    background "#0000"
                    text _("Confirm to commit suicide?") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("CONFIRM") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action Return()
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("BACK") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action SetVariable("selected_ability", None)
            else:
                frame:
                    xsize 900
                    background "#0000"
                    text "[selected_ability if isinstance(selected_ability, str) else selected_ability.name]" size 25 font battle_font align (0.5, 0.5) text_align 0.5
                button:
                    xsize 300
                    background "#0000"
                    hover_background "#3338"
                    text _("BACK") size 25 font battle_font align (0.5, 0.5) text_align 0.5
                    action SetVariable("selected_ability", None)
    key "K_k" action If(selected_ability is None, SetVariable("selected_ability", "Kill Yourself"))

screen turn_order_display:
    frame at [turn_order_transform, xzoom_open(0.5, 0.5)]:
        background "#0000"
        ysize 23*len(turn_order)
        hbox:
            frame:
                xsize 2
                background "#000"
            vbox:
                yalign 0.5
                for member in turn_order:
                    frame:
                        xysize (150, 21)
                        if member == turn_order[current_turn]:
                            background "#3338" # TODO: replace this with the turn highlight
                        else:
                            background "#1118" # TODO: replace this with the unhighlight
                        text member.name size 13 yalign 0.5 font battle_font

transform turn_order_transform:
    on show:
        xalign 0.5
        yalign 0.5
        yoffset -720
        zoom 2.0
        easein_quart 0.5 yoffset 0
        1.25
        easein_quart 0.5 xalign 0.9 zoom 1.0
        easein_elastic 0.2 xalign 0.0 xpos 0
    on hide:
        easeout_quart 1.0 xoffset -300

transform xzoom_open(t=0.5, d=0.0):
    on show:
        xzoom 0.0
        d
        easein_quart t xzoom 1.0
    on hide:
        easeout_quart t xzoom 0.0

transform from_top(t=0.5, d=0.0):
    on show:
        yoffset -720
        d
        easein_quart t yoffset 0
    on hide:
        easeout_quart t*0.5 yoffset -720

transform from_bottom(t=0.5, d=0.0):
    on show:
        yoffset 720
        d
        easein_quart t yoffset 0
    on hide:
        easeout_quart t*0.5 yoffset 720

transform fade_top(t=0.5, d=0.0):
    on show:
        yoffset -10 alpha 0.0
        d
        easein_quart t yoffset 0 alpha 1.0
    on hide:
        easeout_quart t yoffset -10 alpha 0.0

label follow_up_loop:
    $ follow_up_actor = None
    if can_follow_up == []:
        "No one is available to follow up!"
        return

    if isinstance(current_actor, PartyMember) != ("CHARM" in current_actor.current_effects):
        if len(followed_up) == len(active_party)-1:
            $ band_together_attack(party, enemies)
            show expression follow_up_actor.band_together_attack._image at follow_up_actor.band_together_attack._transform
            "The whole party bands together!"
            return
        else:
            call screen follow_up_choice
    else:
        if len(followed_up) == len(active_enemies)-1:
            $ band_together_attack(party, enemies)
            show expression follow_up_actor.band_together_attack._image at follow_up_actor.band_together_attack._transform
            "All the enemies band together!"
            return
        $ follow_up_actor = random.choice(can_follow_up)
        $ selected_target = random.choice([member for member in party if member.health > 0])
    
    $ followed_up.append(follow_up_actor)
    $ ability_results = follow_up_actor.perform_follow_up(selected_target)
    show expression follow_up_actor.follow_up._image at follow_up_actor.follow_up._transform
    "[follow_up_actor.name] follows up!"

    if "WEAKNESS" in ability_results or "CRITICAL" in ability_results:
        jump follow_up_loop

    return

label battle_victory:
    call screen victory_screen
    return

label battle_defeat:
    stop music
    call screen game_over
    return

screen game_over:
    add Solid("#000")
    add "noise" alpha 0.05
    text _("Death has fallen upon you") size 100 font medieval_font align (0.5, 0.5) text_align 0.5 at fade_top(5.0, 1.0)
    textbutton _("LAST CHECKPOINT") text_size 25 text_font medieval_font text_color "#fff" text_hover_color "#aaa" text_align 0.5 xalign 0.5 yalign 0.8 yoffset 0 text_insensitive_color "#fff8" action If(last_checkpoint is not None, [SetVariable("checkpoint_to_jump", last_checkpoint), Return()]) at fade_top(1.0, 1.5)
    textbutton _("RESTART BATTLE") text_size 25 text_font medieval_font text_color "#fff" text_hover_color "#aaa" text_align 0.5 xalign 0.5 yalign 0.8 yoffset 30 action [SetVariable("checkpoint_to_jump", start_of_battle), Return()] at fade_top(1.0, 2.0)
    textbutton _("TITLE SCREEN") text_size 25 text_font medieval_font text_color "#fff" text_hover_color "#aaa" text_align 0.5 xalign 0.5 yalign 0.8 yoffset 60 action MainMenu(True, False) at fade_top(1.0, 2.5)
    textbutton _("QUIT GAME") text_size 25 text_font medieval_font text_color "#fff" text_hover_color "#aaa" text_align 0.5 xalign 0.5 yalign 0.8 yoffset 90 action Quit() at fade_top(1.0, 3.0)

define audio.default_battle_music = "<loop 34.259 to 119.484>mod_assets/music/PLACEHOLDER BATTLE (Delete later).mp3"
define medieval_font = "mod_assets/fonts/PowerdarkBold-O9RP.ttf"
define battle_font = "mod_assets/fonts/NotoSerifJP-Regular.otf"

# battle_member_template = BattleMember(_("Name"), "Kanji", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""))
# TODO: fully define these
default test_monika = PartyMember(_("Monika"), "モニカ", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, "", 1.0), MagicAbility("Band Together", "", 100, 0, "", 1.0), starting_exp = 99999) 
default test_sayori = PartyMember(_("Sayori"), "さより", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, "", 1.0), MagicAbility("Band Together", "", 100, 0, "", 1.0), starting_exp = 99999)
default test_yuri = PartyMember(_("Yuri"), "百合", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, "", 1.0), MagicAbility("Band Together", "", 100, 0, "", 1.0), starting_exp = 99999)
default test_natsuki = PartyMember(_("Natsuki"), "無月", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, "", 1.0), MagicAbility("Band Together", "", 100, 0, "", 1.0), starting_exp = 99999)
default monika = PartyMember(_("Monika"), "モニカ", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, "", 1.0), MagicAbility("Band Together", "", 100, 0, "", 1.0), starting_exp = 99999) 

default test_enemy_1 = Enemy(_("Enemy 1"), "敵1", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, "", 1.0), MagicAbility("Band Together", "", 100, 0, "", 1.0), _image=None, exp=10)
default test_enemy_2 = Enemy(_("Enemy 2"), "敵2", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, "", 1.0), MagicAbility("Band Together", "", 100, 0, "", 1.0), _image=None, exp=10)
#default test_boss = Boss(_("Boss"), "ボス", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""))

image battle_start:
    "mod_assets/visuals/battle_start.png"
    on show:
        zoom 3.0
        linear 1.0 zoom 1.0
    on hide:
        linear 1.0 zoom 3.0
        alpha 0.0

label test_battle:
    "BEGINNING TEST"
    $ start_of_battle = "test_battle"
    $ last_checkpoint = None
    call battle("TEST BATTLE", [test_monika, test_sayori, test_yuri, test_natsuki], [test_enemy_1, test_enemy_2], "bg bedroom", "bg closet")
    "TEST COMPLETE"
    return