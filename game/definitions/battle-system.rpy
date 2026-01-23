# So this is gonna be a whole thing, here's my idea for this battle system:
# The battle starts by calling the screen and loading in the party and enemies as lists, then the turn order is randomized and the battle begins
# Party members are gonna have to be created using the character class, and enemies are gonna be created using the enemy class
# On a party member's turn, the player can choose to do a normal attack (these are physical element), use an item, use magic (magic is limited, so be careful), or guard to reduce damage by 50%
# If a party member gets a critical hit or hit the enemies weakness, they will deal double damage and the player gets to choose a different party member to follow up
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
    """

    class BattleException(Exception):
        pass

    class MagicAbility:
        def __init__(self, name: str, description: str, damage: int, cost: int, element: str, effect: str | None = None, effect_chance: float = 0, *, _transform=None, _image=None, _sound=None, multi:bool = False):
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
        def __init__(self, name: str, description: str, heal: int, cost: int, negative_effects: list[str] | None = None, negative_effect_chance: float = 0, positive_effect: str | None = None, positive_effect_chance: float = 0, *, _transform=None, _image=None, _sound=None, multi:bool = False):
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

    class BattleMember(object): # Parent class for party members and enemies
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
            hit = random.randint(1, self.accuracy) > random.randint(1, target.evasion) or target.is_guarding
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
                if "PHYSICAL" in target.weaknesses:
                    return f"HIT\nWEAKNESS\n{damage}"
                elif critical:
                    return f"HIT\nCRITICAL\n{damage}"
                elif target.is_guarding:
                    return f"HIT\nGUARDED\n{damage}"
                return f"HIT\n{damage}"
            return f"MISS"

        async def magic_attack_single(self, ability: MagicAbility, target) -> str:
            damage = random.randint(ability.damage // 2, ability.damage)
            hit = random.randint(1, self.accuracy) > random.randint(1, target.evasion) or ability.name == "Follow Up" or target.is_guarding
            affected = ""
            if not ability.multi: # since this is used in the multi-target function, I want to prevent the cost from being subtracted twice as well as the animation playing twice
                self.magic -= ability.cost
                renpy.show(ability._image, [ability._transform]) # play animation
                renpy.play(ability._sound, "sound") # play sound
            if hit:
                if ability.element in target.weaknesses:
                    damage *= 2
                damage -= target.defense
                if ability.effect is not None and random.uniform(1.0, 100.0) <= ability.effect_chance:
                    target.apply_effect(ability.effect)
                    f"APPLIED {ability.effect}\n"
                if damage < 0:
                    damage = 0
                target.health -= damage
                if ability.element in target.weaknesses:
                    return f"HIT\nWEAKNESS\n{damage}\n{affected}"
                return f"HIT\n{damage}\n{affected}"
            return f"MISS"

        async def magic_attack_multi(self, ability: MagicAbility, targets: list) -> list[str]:
            if not ability.multi:
                raise BattleException("This ability is not multi-target (why did you call this when it was clearly for multi-target?)")
            renpy.show(ability._image, [ability._transform]) # play animation
            renpy.play(ability._sound, "sound") # play sound
            attacks = [self.magic_attack_single(ability, target) for target in targets]
            return await asyncio.gather(*attacks)

        async def heal_single(self, ability: HealingAbility, target) -> str:
            heal = random.randint(ability.heal // 2, ability.heal)
            affected = ""
            if not ability.multi: # since this is used in the multi-target function, I want to prevent the cost from being subtracted twice as well as the animation playing twice
                self.magic -= ability.cost
                renpy.show(ability._image, [ability._transform]) # play animation
                renpy.play(ability._sound, "sound") # play sound
            if ability.negative_effects is not None and random.uniform(1.0, 100.0) <= ability.negative_effect_chance:
                for effect in ability.negative_effects:
                    del target.current_effects[effect]
                    affected += f"CURED {effect}\n"
            if ability.positive_effect is not None and random.uniform(1.0, 100.0) <= ability.positive_effect_chance:
                target.apply_effect(ability.positive_effect)
                affected += f"APPLIED {ability.positive_effect}\n"
            target.health += heal
            if target.health > target.max_health:
                target.health = target.max_health
                return f"FULL\nHEAL\n{heal}"
            return f"HEAL\n{heal}"
        
        async def heal_multi(self, ability: HealingAbility, targets: list)-> list[str]:
            if not ability.multi:
                raise BattleException("This ability is not multi-target (why did you call this when it was clearly for multi-target?)")
            self.magic -= ability.cost
            renpy.show(ability._image, [ability._transform]) # play animation
            renpy.play(ability._sound, "sound") # play sound
            heals = [self.heal_single(ability, target) for target in targets]
            return await asyncio.gather(*heals)

        def guard(self) -> str:
            self.is_guarding = True
            return "GAURD"
        
        def stop_guarding(self) -> None:
            self.is_guarding = False

        async def perform_follow_up(self, target = None, multi_target: list | None = None) -> str | list[str]:
            if self.follow_up.multi:
                return await self.magic_attack_multi(self.follow_up, multi_target)
            return await self.magic_attack_single(self.follow_up, target)
        
        async def band_together_ability(self, targets: list) -> list[str]:
            if not self.band_together_attack.multi:
                raise BattleException("Band Together Ability must be a multi-target ability")
            return self.magic_attack_multi(self.band_together_attack, targets)
    
    class PartyMember(BattleMember):
        def __init__(self, *args, starting_exp:int=0, level_up:int=100, new_abilities:dict[int:list[MagicAbility | HealingAbility]]={}, max_level: int = 99, **kwargs):
            super().__init__(*args, **kwargs)
            self.exp = 0
            self.total_exp = starting_exp
            self.level = 1
            self.exp_to_next_level = level_up
            self.new_abilities = new_abilities
            self.max_level = max_level
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
        
    class Enemy(BattleMember):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.all_abilities = ("NORMAL", *self.magic_abilities)
            self.next_action = [None, None] # [ability, target], this is here because I believe we can have a certain character reveal the enemy's next action before it happens
        
        def attack(self, target: BattleMember) -> str:
            if self.next_action[0] == "NORMAL":
                return self.normal_attack(self.next_action[1])
            elif isinstance(self.next_action[0], MagicAbility):
                return self.magic_attack(self.next_action[0], self.next_action[1])
            elif isinstance(self.next_action[0], HealingAbility):
                return self.heal(self.next_action[0], self.next_action[1])
            return "NOT AN ATTACK"
        
        def choose_action(self, party: list[PartyMember], enemies: list) -> None:
            self.next_action[0] = random.choice(self.all_abilities)
            if self.next_action[0] == "NORMAL" or isinstance(self.next_action[0], MagicAbility):
                self.next_action[1] = random.choice(party)
            elif isinstance(self.next_action[0], HealingAbility):
                self.next_action[1] = random.choice(enemies)

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
            if self.next_action[0] == "NORMAL" or isinstance(self.next_action[0], MagicAbility):
                self.next_action[1] = random.choice(party)
            elif isinstance(self.next_action[0], HealingAbility):
                self.next_action[1] = random.choice(enemies)

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
        if isinstance(who_started, PartyMember):
            for member in party:
                can_follow_up.append(member)
        else:
            for member in enemies:
                can_follow_up.append(member)
        if who_started in can_follow_up:
            can_follow_up.remove(who_started)
    
    async def band_together_attack(party: list[PartyMember], enemies: list[Enemy | Boss]) -> list[str]:
        global turn_order
        global current_turn
        who_started = turn_order[current_turn]
        attacks = [member.band_together_ability(enemies if isinstance(who_started, PartyMember) else party) for member in (party if isinstance(who_started, PartyMember) else enemies)]
        return await asyncio.gather(*attacks)
    
    def next_turn() -> None:
        global current_turn
        global turn_order
        global followed_up
        current_turn += 1
        current_turn %= len(turn_order)
        followed_up.clear()
    
    def effect_update(target: BattleMember) -> str:
        """
        Available negative effects:
            BURN: Reduces the target's health each turn for 3 turns, double damage if weak to fire
            POISON: Reduces the target's health each turn for 3 turns, double damage if weak to poison
            SLEEP: Puts the target to sleep, preventing them from attacking for 3 turns, but they heal each turn
            PARALYZE: Paralyzes the target, preventing them from attacking for 3 turns
            MAGIC BLOCK: Prevents the target from using magic for 2 turns # this needs a different name
            CONFUSE: Randomly chooses the target's action for 3 turns, these include attacking pary members and healing enemies
            CHARM: Puts the target on the user's side, if party, the player will control what the target doing for the next 3 turns, if enemy, the target will act as an enemy for the next 3 turns
            FEAR: On turn, 60% chance to force skip turn, 20% chance to run away, 20% chance to actually do commanded action
            ENRAGE: Force target to only use normal attacks for 3 turns, however strength is boosted

        Available positive effects:
            SHIELD: Increases the target's defense for 3 turns
            REFLECT: Reflects damage back to the attacker for 3 turns
            REGENERATE: Heals the target each turn for 3 turns
            STAT BOOST: Increases the target's stats for 3 turns
        """
        r: str = ""
        for effect in target.effects:
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
    
    def define_scrolling_segments(img_name, num_segments=8, scroll_speed=10.0):
        total_width = 1280
        segment_width = total_width / num_segments
        
        for i in range(num_segments):
            crop_rect = (i * segment_width, 0, segment_width, 1080)
            
            seg_name = f"seg_{i}"
            renpy.image(seg_name, At(Crop(crop_rect, img_name)))

transform scroll_left(delay):
    subpixel True
    xtile 2
    xpos 0.0
    linear delay xpos -1.0
    repeat

transform scroll_right(delay):
    subpixel True
    xtile 2
    xpos -1.0
    linear delay xpos 0.0
    repeat

default can_follow_up = [] # fill this with available party members who can follow up when conditions are fulfilled
default followed_up = [] # this will be filled with party members who have already followed up, this will be cleared at the start of each turn, if this matches the party during any turn, then the band together attack will happen
default turn_order = []
default current_turn = 0
default selected_ability = None
default checkpoint_to_jump = "battle_loop"
default start_of_battle = "battle_loop"
default last_checkpoint = None

label battle(party, enemies, _music = audio.default_battle_music, *, override_victory = "battle_victory", override_defeat = "battle_defeat", victory_args = tuple(), defeat_args = tuple(), victory_kwargs = {}, defeat_kwargs = {}):
    if last_checkpoint is None:
        $ decide_turn_order(party, enemies)
    
    $ renpy.music.play(_music)
    $ current_turn = 0
    $ can_follow_up = []
    $ followed_up = []
    $ selected_ability = None
    # TODO: show scrolling image
    call split_scroll
    show battle_start at truecenter
    pause 4.5
    hide battle_start with None
    show screen party_stats(party)
    with Fade(1.0, 0.0, 0.5, color="#fff")

    call battle_loop(party, enemies, override_victory, override_defeat, victory_args, defeat_args, victory_kwargs, defeat_kwargs)
label battle_loop(party, enemies, override_victory, override_defeat, victory_args, defeat_args, victory_kwargs, defeat_kwargs):
    $ current_actor = turn_order[current_turn]
    $ current_actor.stop_guarding()
    
    if all(e.health <= 0 for e in enemies):
        call expression override_victory pass (*victory_args, **victory_kwargs)
        return
    if all(p.health <= 0 for p in party):
        call expression override_defeat pass (*defeat_args, **defeat_kwargs)
        jump expression checkpoint_to_jump


    if current_actor.health > 0 and "PARALYZE" not in current_actor.current_effects and "SLEEP" not in current_actor.current_effects:
        if isinstance(current_actor, PartyMember) != "CHARM" in current_actor.current_effects:
            call player_turn_menu(current_actor)
        else:
            call enemy_turn_logic(current_actor)
    $ effect_update(current_actor)
    $ current_actor.effect_tick_down()
    $ next_turn()
    
    jump battle_loop

default ability_description = ""
screen ability_selection(member):
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

# TODO: display this in a concise fashion where it will only show the information needed to be shown in battle, this information is, name, icon (maybe if we decide to have these), health, max health, magic, and max magic (could have bars for these), also highlight the screen if the turn is being taken
screen party_stats(party):
    fixed:
        xysize (1280, 100)
        hbox:
            xalign 0.5
            for member in party:
                frame:
                    xysize (100, 100)
                    if member == turn_order[current_turn]:
                        background "#000" # TODO: replace this with the turn highlight
                    else:
                        background "#333" # TODO: replace this with the unhighlight
                    vbox:
                        #add "[member.icon].png" # Who knows if we will have icons for our party members
                        frame:
                            xysize (50, 10)
                            vbox:
                                text member.kanji size 25
                                text member.name size 15
                        frame:
                            xysize (10, 10)
                            text "HEALTH: [member.health]/[member.max_health]"
                        frame:
                            xysize (10, 10)
                            text "MAGIC: [member.magic]/[member.max_magic]"



define audio.default_battle_music = "<loop 34.259 to 119.484>mod_assets/music/PLACEHOLDER BATTLE (Delete later).mp3"

# battle_member_template = BattleMember("Name", "Kanji", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""))
# TODO: fully define these
default test_monika = PartyMember("Monika", "モニカ", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""), starting_exp = 99999) 
default test_sayori = PartyMember("Sayori", "さより", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""), starting_exp = 99999)
default test_yuri = PartyMember("Yuri", "百合", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""), starting_exp = 99999)
default test_natsuki = PartyMember("Natsuki", "無月", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""), starting_exp = 99999)

default test_enemy_1 = Enemy("Enemy 1", "敵1", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""))
default test_enemy_2 = Enemy("Enemy 2", "敵2", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""))
#default test_boss = Boss("Boss", "ボス", 300, 30, 20, 100, 250, 35, 30, [], [], MagicAbility("Follow Up", "", 100, 0, ""), MagicAbility("Band Together", "", 100, 0, ""))

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
    call battle([test_monika, test_sayori, test_yuri, test_natsuki], [test_enemy_1, test_enemy_2])