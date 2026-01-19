# So this is gonna be a whole thing, here's my idea for this battle system:
# The battle starts by calling the screen and loading in the party and enemies as lists, then the turn order is randomized and the battle begins
# Party members are gonna have to be created using the character class, and enemies are gonna be created using the enemy class
# On a party member's turn, the player can choose to do a normal attack (these are physical element), use an item, use magic (magic is limited, so be careful), or guard to reduce damage by 50%
# If a party member gets a critical hit (which is a 20% chance) or hit the enemies weakness, they will deal double damage and the player gets to choose a different party member to follow up
#   Follow ups are predetermined attacks and they are gaurenteed to hit, meaning you won't choose what that party member does, but you can choose who does it, they can only do one attack on follow ups
#      You can not choose the same party member to follow up as the one who got the critical hit
#   If a follow up hits a critical or weakness like before, another follow up is triggered, otherwise, the turn is ended
#       You can not choose any party member that has already attacked this turn
#   If all party members manage to hit weaknesses on all follow ups, they will all band together and attack at the same time, dealing massive damage.  This will end the turn.
# On an enemy's turn, they will choose a random party member to attack and deal damage to them
# Enemies can do everything that party members can do, but they can also use special abilities once certain conditions are fulfilled
# Enemies will never guard or use items
#
# Yes, the follow up system takes inspiration from P5X, I did not think of too much originality here.  But that's okay.

init python:
    import random
    import asyncio
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
    
    Available negative effects:
        BURN: Reduces the target's health each turn for 3 turns, double damage if weak to fire
        POISON: Reduces the target's health each turn for 3 turns, double damage if weak to poison
        STUN: Stuns the target, preventing them from attacking for 1 turn
        SLEEP: Puts the target to sleep, preventing them from attacking for 3 turns, but they heal each turn
        PARALYZE: Paralyzes the target, preventing them from attacking for 3 turns
        MAGIC BLOCK: Prevents the target from using magic for 2 turns # this needs a different name
        CONFUSE: Randomly chooses the target's action for 3 turns, these include attacking pary members and healing enemies
        CHARM: Puts the target on the user's side, if party, the player will control what the target doing for the next 3 turns, if enemy, the target will act as an enemy for the next 3 turns
        FEAR: On turn, 60% chance to force skip turn, 20% chance to run away, 20% chance to actually do commanded action
        ENRAGE: Force target to only use normal attacks for 3 turns, however strength is boosted
        TARGET LOCK: Forces the target to only attack the user for 3 turns

    Available positive effects:
        SHIELD: Increases the target's defense for 3 turns
        REFLECT: Reflects damage back to the attacker for 3 turns
        REGENERATE: Heals the target each turn for 3 turns
        STAT BOOST: Increases the target's stats for 3 turns
    """

    class BattleException(Exception):
        pass

    class MagicAbility:
        def __init__(self, name: str, description: str, damage: int, cost: int, element: str, effect: str | None = None, effect_chance: int = 0, *, _transform=None, _image=None, _sound=None, multi:bool = False):
            self.name = name
            self.description = description
            self.damage = damage
            self.cost = cost
            self.element = element
            self.effect = effect
            self.effect_chance = effect_chance
            self._transform = _transform
            self._image = _image
            self._sound = _sound
            self.multi = multi
    
    class HealingAbility:
        def __init__(self, name: str, description: str, heal: int, cost: int, negative_effects: list[str] | None = None, negative_effect_chance: int = 0, positive_effect: str | None = None, positive_effect_chance: int = 0, *, _transform=None, _image=None, _sound=None, multi:bool = False):
            self.name = name
            self.description = description
            self.heal = heal
            self.cost = cost
            self.element = "HEALING"
            self.negative_effects = negative_effects
            self.negative_effect_chance = negative_effect_chance
            self.positive_effect = positive_effect
            self.positive_effect_chance = positive_effect_chance
            self._transform = _transform
            self._image = _image
            self._sound = _sound
            self.multi = multi

    class BattleMember(Object): # Parent class for party members and enemies
        def __init__(self, name: str, max_health: int, strength: int, defense: int, max_magic: int, speed: int, accuracy: int, evasion: int, weaknesses: list[str], magic_abilities:list[MagicAbility | HealingAbility], follow_up:MagicAbility, band_together_attack:MagicAbility):
            self.name = name
            self.max_health = max_health
            self.health = max_health
            self.strength = strength
            self.defense = defense
            self.max_magic = max_magic
            self.magic = max_magic
            self.speed = speed
            self.accuracy = accuracy
            self.evasion = evasion
            self.weakness = weakness
            self.magic_abilities = magic_abilities
            self.is_guarding = False
            self.current_effects = []
            self.follow_up = follow_up
            self.band_together_attack = band_together_attack

        def decide_turn(self):
            return random.randint(1, self.speed)
        
        def normal_attack(self, target: BattleMember):
            damage = random.randint(self.strength // 2, self.strength)
            hit = random.randint(1, self.accuracy) > random.randint(1, target.evasion) or target.is_guarding
            if hit:
                if target.is_guarding:
                    damage // 2
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
                if "PHYSICAL" in target.weaknesses:
                    return f"HIT\nWEAKNESS\n{damage}"
                elif critical:
                    return f"HIT\nCRITICAL\n{damage}"
                elif target.is_guarding:
                    return f"HIT\nGUARDED\n{damage}"
                return f"HIT\n{damage}"
            return f"MISS"

        async def magic_attack_single(self, ability: MagicAbility, target: BattleMember):
            damage = random.randint(ability.damage // 2, ability.damage)
            hit = random.randint(1, self.accuracy) > random.randint(1, target.evasion) or ability.name == "Follow Up" or target.is_guarding
            if not ability.multi: # since this is used in the multi-target function, I want to prevent the cost from being subtracted twice as well as the animation playing twice
                self.magic -= ability.cost
                renpy.show(ability._image, [ability._transform]) # play animation
                renpy.play(ability._sound, "sound") # play sound
            if hit:
                if ability.element in target.weaknesses:
                    damage *= 2
                damage -= target.defense
                if ability.effect is not None and random.randint(1, 100) <= ability.effect_chance:
                    target.current_effects.append(ability.effect)
                if damage < 0:
                    damage = 0
                target.health -= damage
                if ability.element in target.weaknesses:
                    return f"HIT\nWEAKNESS\n{damage}"
                return f"HIT\n{damage}"
            return f"MISS"

        async def magic_attack_multi(self, ability: MagicAbility, targets: list[BattleMember]):
            if not ability.multi:
                raise BattleException("This ability is not multi-target (why did you call this when it was clearly for multi-target?)")
            renpy.show(ability._image, [ability._transform]) # play animation
            renpy.play(ability._sound, "sound") # play sound
            attacks = [self.magic_attack_single(ability, target) for target in targets]
            return await asyncio.gather(*attacks)

        async def heal_single(self, ability: HealingAbility, target: BattleMember):
            heal = random.randint(ability.heal // 2, ability.heal)
            if not ability.multi: # since this is used in the multi-target function, I want to prevent the cost from being subtracted twice as well as the animation playing twice
                self.magic -= ability.cost
                renpy.show(ability._image, [ability._transform]) # play animation
                renpy.play(ability._sound, "sound") # play sound
            if ability.negative_effects is not None and random.randint(1, 100) <= ability.negative_effect_chance:
                for effect in ability.negative_effects:
                    target.current_effects.remove(effect)
            if ability.positive_effect is not None and random.randint(1, 100) <= ability.positive_effect_chance:
                target.current_effects.append(ability.positive_effect)
            target.health += heal
            if target.health > target.max_health:
                target.health = target.max_health
                return f"FULL\nHEAL\n{heal}"
            return f"HEAL\n{heal}"
        
        async def heal_multi(self, ability: HealingAbility, targets: list[BattleMember]):
            if not ability.multi:
                raise BattleException("This ability is not multi-target (why did you call this when it was clearly for multi-target?)")
            self.magic -= ability.cost
            renpy.show(ability._image, [ability._transform]) # play animation
            renpy.play(ability._sound, "sound") # play sound
            heals = [self.heal_single(ability, target) for target in targets]
            return await asyncio.gather(*heals)

        def guard(self):
            self.is_guarding = True
        
        def stop_guarding(self):
            self.is_guarding = False

        async def follow_up(self, target: BattleMember | None = None, multi_target: list[BattleMember] | None = None):
            if self.follow_up.multi:
                return await self.magic_attack_multi(self.follow_up, multi_target)
            return await self.magic_attack_single(self.follow_up, target)
        
        async def band_together_ability(self, targets: list[BattleMember]):
            if not self.band_together.multi:
                raise BattleException("Band Together Ability must be a multi-target ability")
            return self.magic_attack_multi(self.band_together, targets)
    
    class PartyMember(BattleMember):
        def __init__(self, *args, starting_exp:int=0, level_up:int=100, **kwargs):
            super().__init__(*args, **kwargs)
            self.exp = 0
            self.total_exp = starting_exp
            self.level = 1
            self.exp_to_next_level = level_up
            self.gain_exp(self.total_exp)

        def level_up(self):
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
        
        def gain_exp(self, exp: int):
            self.exp += exp
            self.total_exp += exp
            while self.exp >= self.exp_to_next_level:
                self.exp -= self.exp_to_next_level
                self.level_up()
        
        def get_needed_exp(self):
            return self.exp_to_next_level - self.exp
        
    class Enemy(BattleMember):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.all_abilities = ("NORMAL", *self.magic_abilities)
            self.next_action = [None, None] # [ability, target], this is here because I believe we can have a certain character reveal the enemy's next action before it happens
        
        def attack(self, target: BattleMember):
            if self.next_action[0] == "NORMAL":
                return self.normal_attack(self.next_action[1])
            elif self.next_action[0] is MagicAbility:
                return self.magic_attack(self.next_action[0], self.next_action[1])
            elif self.next_action[0] is HealingAbility:
                return self.heal(self.next_action[0], self.next_action[1])
        
        def choose_action(self, party: list[PartyMember], enemies: list[Enemy]):
            self.next_action[0] = random.choice(self.all_abilities)
            if self.next_action[0] == "NORMAL" or self.next_action[0] is MagicAbility:
                self.next_action[1] = random.choice(party)
            elif self.next_action[0] is HealingAbility:
                self.next_action[1] = random.choice(enemies)

    class Boss(Enemy): # these will have special abilities and will be harder to defeat, also their turn number is not randomized
        def __init__(self, name: str, max_health: int, strength: int, defense: int, max_magic: int, speed: int, accuracy: int, evasion: int, weakness: str, magic_abilities:list[MagicAbility], *, phases: list[BossPhase], turn_number:int=0):
            super().__init__(name, max_health, strength, defense, max_magic, speed, accuracy, evasion, weakness, magic_abilities)
            self.turn_number = turn_number
            self.phases = phases
        
        def decide_turn(self):
            return self.turn_number
    
    class BossPhase(Boss):
        def __init__(self, health_needed: int, abilites_available: tuple[int]):
            self.health_needed = health_needed
            self.abilities_available = super().all_abilities[abilites_available[0]:abilites_available[1]]

    def decide_turn_order(party: list[PartyMember], enemies: list[Enemy | Boss]):
        global turn_order
        turn_numbers = {}
        for member in [*party, *enemies]:
            turn_numbers[member] = member.decide_turn()
        turn_order.clear()
        turn_order = sorted(turn_numbers, key=turn_numbers.get, reverse=True)
        global current_turn
        current_turn = 0
    
    def fill_follow_up(party: list[PartyMember], enemies: list[Enemy | Boss]):
        global can_follow_up
        can_follow_up.clear()
        global turn_order
        global current_turn
        who_started = turn_order[current_turn]
        if who_started is PartyMember:
            for member in party:
                can_follow_up.append(member)
        else:
            for member in enemies:
                can_follow_up.append(member)
        can_follow_up.remove(who_started)
    
    async def band_together_attack(party: list[PartyMember], enemies: list[Enemy | Boss]):
        global turn_order
        global current_turn
        who_started = turn_order[current_turn]
        attacks = [member.band_together_ability(enemies if who_started is PartyMember else party) for member in (party if isinstance(who_started, PartyMember) else enemies)]
        return await asyncio.gather(*attacks)
    
    def next_turn():
        global current_turn
        global turn_order
        global followed_up
        current_turn += 1
        current_turn %= len(turn_order)
        followed_up.clear()

define can_follow_up = [] # fill this with available party members who can follow up when conditions are fulfilled
define followed_up = [] # this will be filled with party members who have already followed up, this will be cleared at the start of each turn, if this matches the party during any turn, then the band together attack will happen
define turn_order = []
define current_turn = 0
define selected_ability = None

screen battle(party:list[PartyMember], enemies:list[Enemy | Boss]):
    on "show" action Function(decide_turn_order, party, enemies)

define ability_description = ""
screen ability_selection(member:PartyMember):
    frame:
        xysize (100, 700)
        frame: # frame for the viewport
            viewport: # viewport for the ability buttons
                has vbox
                for ability in member.magic_abilities:
                    button: # button for the ability
                        hovered SetVariable("ability_description", ability.description)
                        unhovered SetVariable("ability_description", "")
                        action [SetVariable("selected_ability", ability), Hide("ability_selection")]
                        hbox:
                            add "[ability.element].png" # will change this if the image happens to be in a different folder
                            frame:
                                xysize (50, 10)
                                text ability.name
                            frame:
                                xysize (10, 10)
                                text ability.cost
        frame: # frame for the ability description
            text ability_description

screen party_member_stats(member:PartyMember, taking_turn:bool):
    pass # TODO: display this in a concise fashion where it will only show the information needed to be shown in battle, this information is, name, icon (maybe if we decide to have these), health, max health, magic, and max magic (could have bars for these), also highlight the screen if the turn is being taken