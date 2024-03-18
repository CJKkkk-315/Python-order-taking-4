from __future__ import annotations
from a2_support import *
# Implement your classes here


class Card:
    def __init__(self):
        pass

    def get_damage_amount(self) -> int:
        """
        This function returns the damage caused by the card.

        Parameters:
            None.

        Returns:
            int: The damage value caused by the card.
        """
        return 0

    def get_block(self) -> int:
        """
        This function returns the block value of the card.

        Parameters:
            None.

        Returns:
            int: The block value of the card.
            """

        return 0

    def get_energy_cost(self) -> int:
        """
        This function returns the energy cost of the card.

        Parameters:
            None.

        Returns:
            int: The energy cost of the card.
        """

        return 1

    def get_status_modifiers(self) -> dict[str, int]:
        """
        This function returns the status dictionary of the card.

        Parameters:
            None.

        Returns:
            dict[str, int]: The status dictionary of the card.
        """

        return {}

    def get_name(self) -> str:
        """
        This function returns the name of the card.

        Parameters:
            None.

        Returns:
            str: The name of the card.
        """
        return 'Card'

    def get_description(self) -> str:
        """
        This function returns the description of the card.

        Parameters:
            None.

        Returns:
            str: The description of the card.
        """

        return 'A card.'

    def requires_target(self) -> bool:
        """
        This function determines whether the card requires a target.

        Parameters:
            None.

        Returns:
            bool: True if the card requires a target, False if it does not.
        """

        return True

    def __str__(self):
        return f'{self.get_name()}: {self.get_description()}'

    def __repr__(self):
        return 'Card()'


class Strike(Card):

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return 'Strike'

    def get_damage_amount(self) -> int:
        return 6

    def requires_target(self) -> bool:
        return True

    def get_description(self) -> str:
        return 'Deal 6 damage.'

    def __repr__(self):
        return 'Strike()'


class Defend(Card):

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return 'Defend'

    def get_block(self) -> int:
        return 5

    def get_description(self) -> str:
        return 'Gain 5 block.'

    def requires_target(self) -> bool:
        return False

    def __repr__(self):
        return 'Defend()'


class Bash(Card):

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return 'Bash'

    def get_damage_amount(self) -> int:
        return 7

    def get_block(self) -> int:
        return 5

    def get_energy_cost(self) -> int:
        return 2

    def requires_target(self) -> bool:
        return True

    def get_description(self) -> str:
        return 'Deal 7 damage. Gain 5 block.'

    def __repr__(self):
        return 'Bash()'


class Neutralize(Card):

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return 'Neutralize'

    def get_damage_amount(self) -> int:
        return 3

    def get_energy_cost(self) -> int:
        return 0

    def get_status_modifiers(self) -> dict[str, int]:
        return {'weak': 1, 'vulnerable': 2}

    def requires_target(self) -> bool:
        return True

    def get_description(self) -> str:
        return 'Deal 3 damage. Apply 1 weak. Apply 2 vulnerable.'

    def __repr__(self):
        return 'Neutralize()'


class Survivor(Card):

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return 'Survivor'

    def get_block(self) -> int:
        return 8

    def requires_target(self) -> bool:
        return False

    def get_status_modifiers(self) -> dict[str, int]:
        return {'strength': 1}

    def get_description(self) -> str:
        return 'Gain 8 block and 1 strength.'

    def __repr__(self):
        return 'Survivor()'


class Eruption(Card):

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return 'Eruption'

    def get_damage_amount(self) -> int:
        return 9

    def get_energy_cost(self) -> int:
        return 2

    def requires_target(self) -> bool:
        return True

    def get_description(self) -> str:
        return 'Deal 9 damage.'

    def __repr__(self):
        return 'Eruption()'


class Vigilance(Card):

    def __init__(self):
        super().__init__()

    def get_name(self) -> str:
        return 'Vigilance'

    def get_block(self) -> int:
        return 8

    def requires_target(self) -> bool:
        return False

    def get_energy_cost(self) -> int:
        return 2

    def get_status_modifiers(self) -> dict[str, int]:
        return {'strength': 1}

    def get_description(self) -> str:
        return 'Gain 8 block and 1 strength.'

    def __repr__(self):
        return 'Vigilance()'


class Entity:

    def __init__(self, max_hp: int) -> None:
        """
        This function initializes the instance with a maximum HP value.

        Parameters:
            max_hp (int): The maximum HP value to assign to the instance.

        Returns:
            None.
        """

        self.max_hp = max_hp
        self.hp = max_hp
        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0

    def get_hp(self) -> int:
        """
        This function returns the current HP value of the entity.

        Parameters:
            None.

        Returns:
            int: The current HP value of the entity.
        """

        return self.hp

    def get_max_hp(self) -> int:
        """
        This function returns the maximum HP value of the entity.

        Parameters:
            None.

        Returns:
            int: The maximum HP value of the entity.
        """

        return self.max_hp

    def get_block(self) -> int:
        """
        This function returns the block value of the entity.

        Parameters:
            None.

        Returns:
            int: The block value of the entity.
        """

        return self.block

    def get_strength(self) -> int:
        """
        This function returns the strength value of the entity.

        Parameters:
            None.

        Returns:
            int: The strength value of the entity.
        """

        return self.strength

    def get_weak(self) -> int:
        """
        This function returns the weak value of the entity.

        Parameters:
            None.

        Returns:
            int: The weak value of the entity.
        """
        return self.weak

    def get_vulnerable(self) -> int:
        """
        This function returns the vulnerable value of the entity.

        Parameters:
            None.

        Returns:
            int: The vulnerable value of the entity.
        """
        return self.vulnerable

    def get_name(self) -> str:
        """
        This function returns the name of the entity.

        Parameters:
            None.

        Returns:
            str: The name of the entity.
        """

        return 'Entity'

    def reduce_hp(self, amount: int) -> None:
        """
        This function inflicts a certain amount of damage to the entity.

        Parameters:
            amount (int): The amount of damage to inflict.

        Returns:
            None.
        """

        # Determine whether to break through the block
        if amount <= self.block:
            self.block -= amount
        else:
            amount -= self.block
            self.block = 0
            # The minimum hp can only be 0
            self.hp = max(0, self.hp - amount)

    def is_defeated(self) -> bool:
        """
        This function determines whether the entity has been defeated.

        Parameters:
            None.

        Returns:
            bool: True if the entity has been defeated, False otherwise.
        """
        return not self.hp

    def add_block(self, amount: int) -> None:
        """
        This function increases the block value of the entity by a certain amount.

        Parameters:
            amount (int): The amount to increase the block value by.

        Returns:
            None.
        """

        self.block += amount

    def add_strength(self, amount: int) -> None:
        """
        This function increases the strength value of the entity by a certain amount.

        Parameters:
            amount (int): The amount to increase the strength value by.

        Returns:
            None.
        """

        self.strength += amount

    def add_weak(self, amount: int) -> None:
        """
        This function increases the weak value of the entity by a certain amount.

        Parameters:
            amount (int): The amount to increase the weak value by.

        Returns:
            None.
        """

        self.weak += amount

    def add_vulnerable(self, amount: int) -> None:
        """
        This function increases the vulnerable value of the entity by a certain amount.

        Parameters:
            amount (int): The amount to increase the vulnerable value by.

        Returns:
            None.
        """

        self.vulnerable += amount

    def new_turn(self) -> None:
        """
        This function starts a new turn for the entity, decreasing the duration of any active
        status effects by 1 and resetting the block value to 0.

        Parameters:
            None.

        Returns:
            None.
        """

        self.block = 0
        if self.weak:
            self.weak -= 1
        if self.vulnerable:
            self.vulnerable -= 1

    def __str__(self):
        return f'{self.get_name()}: {self.hp}/{self.max_hp} HP'

    def __repr__(self):
        return f'Entity({self.max_hp})'


class Player(Entity):

    def __init__(self, max_hp: int, cards: list[Card] | None = None) -> None:
        """
        This function initializes a player instance with a maximum HP value, an initial energy
        value of 3, and empty decks for their draw pile, hand, and discard pile. The player's
        deck can be optionally initialized with a list of cards.

        Parameters:
            max_hp (int): The maximum HP value of the player.
            cards (list[Card]|None): The list of cards to initialize the player's draw pile with,
                                     or None if the player should start with an empty draw pile.

        Returns:
            None.
        """

        super().__init__(max_hp)
        self.start_cards = cards
        self.energy = 3
        if cards:
            self.desk = cards
        else:
            self.desk = []
        self.hand = []
        self.discard = []

    def get_name(self):
        return 'Player'

    def get_energy(self) -> int:
        """
        This function returns the current energy value of the player.

        Parameters:
            None.

        Returns:
            int: The current energy value of the player.
        """

        return self.energy

    def get_hand(self) -> list[Card]:
        """
        This function returns the current hand of cards held by the player.

        Parameters:
            None.

        Returns:
            list[Card]: The current hand of cards held by the player.
        """

        return self.hand

    def get_deck(self) -> list[Card]:
        """
        This function returns the current desk of cards by the player.

        Parameters:
            None.

        Returns:
            list[Card]: The current desk of cards by the player.
        """

        return self.desk

    def get_discarded(self) -> list[Card]:
        """
        This function returns the current discarded of cards by the player.

        Parameters:
            None.

        Returns:
            list[Card]: The current discarded of cards by the player.
        """
        return self.discard

    def start_new_encounter(self) -> None:
        """
        This function starts a new encounter for the player by shuffling their discard pile
        into their draw pile.

        Parameters:
            None.

        Returns:
            None.
        """
        if not self.hand:
            # Append discard to the end of the desk list and clear discard at the same time
            self.desk.extend(self.discard)
            self.discard = []

    def end_turn(self) -> None:
        """
        This function ends the current turn for the player by discarding their hand and adding
        it to their discard pile.

        Parameters:
            None.

        Returns:
            None.
        """

        self.discard.extend(self.hand)
        self.hand = []

    def new_turn(self) -> None:
        super().new_turn()
        draw_cards(self.desk, self.hand, self.discard)
        self.energy = 3

    def play_card(self, card_name: str) -> Card | None:
        """
        This function checks whether the player can play the specified card. If they have
        enough energy to play the card, the card is discarded from their hand and added to
        their discard pile, and the player's energy is reduced by the card's energy cost.

        Parameters:
            card_name (str): The name of the card to play.

        Returns:
            None.
        """

        for card in self.hand:
            # Find the corresponding card
            if card.get_name() == card_name:
                # Determine if the energy is sufficient
                if card.get_energy_cost() <= self.energy:
                    # Deduct energy, discard the card, and return
                    self.energy -= card.get_energy_cost()
                    this_card = card
                    self.hand.remove(this_card)
                    self.discard.append(this_card)

                    return this_card
        # If the above conditions are not met, return none
        return None

    def __repr__(self):
        return f'Player({self.max_hp}, {self.start_cards})'


class IronClad(Player):

    def __init__(self) -> None:
        super().__init__(80, [Strike(), Strike(), Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Defend(), Bash()])

    def get_name(self):
        return 'IronClad'

    def __repr__(self):
        return 'IronClad()'


class Silent(Player):

    def __init__(self) -> None:
        super().__init__(70, [Strike(), Strike(), Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Defend(), Defend(), Neutralize(), Survivor()])

    def get_name(self):
        return 'Silent'

    def __repr__(self):
        return 'Silent()'


class Watcher(Player):

    def __init__(self) -> None:
        super().__init__(72, [Strike(), Strike(), Strike(), Strike(), Defend(), Defend(), Defend(), Defend(), Eruption(), Vigilance()])

    def get_name(self):
        return 'Watcher'

    def __repr__(self):
        return 'Watcher()'


class Monster(Entity):
    # Set Monster_ ID is a static member
    monster_id = 0

    def __init__(self, max_hp: int) -> None:
        """
        This function initializes a monster instance with a maximum HP value and automatically
        assigns it an ID.

        Parameters:
            max_hp (int): The maximum HP value of the monster.

        Returns:
            None.
        """
        super().__init__(max_hp)
        self.id = Monster.monster_id
        # monster_ ID self increasing 1
        Monster.monster_id += 1

    def get_id(self) -> int:
        """
        This function returns the ID of the monster.

        Parameters:
            None.

        Returns:
            int: The ID of the monster.
        """

        return self.id

    def action(self) -> dict[str, int]:
        """
        This function triggers a specific action for the monster and generates a status
        dictionary to describe the result of the action.

        Parameters:
            None.

        Returns:
            dict[str, int]: The status dictionary describing the result of the monster's action.
        """

        raise NotImplementedError

    def get_name(self):
        return 'Monster'

    def __repr__(self):
        return f'Monster({self.max_hp})'


class Louse(Monster):

    def __init__(self, max_hp: int) -> None:
        super().__init__(max_hp)
        self.amount = random_louse_amount()

    def action(self) -> dict[str, int]:
        return {'damage': self.amount}

    def get_name(self):
        return 'Louse'

    def __repr__(self):
        return super().__repr__().replace('Monster', 'Louse')


class Cultist(Monster):

    def __init__(self, max_hp: int) -> None:
        super().__init__(max_hp)
        self.damage_amount = 0
        self.weak_amount = 0

    def action(self) -> dict[str, int]:
        res = {'damage': self.damage_amount, 'weak': self.weak_amount}
        if not self.damage_amount:
            self.damage_amount = 6
        self.damage_amount += 1
        self.weak_amount = (self.weak_amount + 1) % 2
        return res

    def get_name(self):
        return 'Cultist'

    def __repr__(self):
        return super().__repr__().replace('Monster', 'Cultist')


class JawWorm(Monster):

    def __init__(self, max_hp: int) -> None:
        super().__init__(max_hp)

    def action(self) -> dict[str, int]:
        now_damage = (self.max_hp - self.hp) / 2
        if now_damage - int(now_damage) >= 0.5:
            self.block += int(now_damage) + 1
        else:
            self.block += int(now_damage)

        return {'damage': int(now_damage)}

    def get_name(self):
        return 'JawWorm'

    def __repr__(self):
        return super().__repr__().replace('Monster', 'JawWorm')


class Encounter:

    def __init__(self, player: Player, monsters: list[tuple[str, int]]) -> None:
        """
        This function initializes an encounter by instantiating a list of monsters and starting
        a new turn for the player.

        Parameters:
            player (Player): The player instance for the encounter.
            monsters (list[tuple[str, int]]): The list of monsters for the encounter.

        Returns:
            None.
        """

        self.player_turn = False
        self.player = player
        # Instantiate each monster using the eval method
        self.monsters = [eval(f'{monster[0]}({monster[1]})') for monster in monsters]
        player.start_new_encounter()
        self.start_new_turn()

    def start_new_turn(self) -> None:
        """
        This function starts a new turn for the encounter, with the player going first and
        entering their turn.

        Parameters:
            None.

        Returns:
            None.
        """

        self.player_turn = True
        self.player.new_turn()

    def end_player_turn(self) -> None:
        """
        This function ends the player's turn and automatically processes the turn for each
        monster.

        Parameters:
            None.

        Returns:
            None.
        """

        self.player_turn = False
        # Traverse the monster list and enter a new turn for each monster
        for monster in self.monsters:
            monster.new_turn()
        self.player.discard.extend(self.player.hand)
        self.player.hand = []

    def get_player(self) -> Player:
        """
        This function returns the player instance for the current encounter.

        Parameters:
            None.

        Returns:
            Player: The player instance for the current encounter.
        """

        return self.player

    def get_monsters(self) -> list[Monster]:
        """
        This function returns the list of monster instances for the current encounter.

        Parameters:
            None.

        Returns:
            list[Monster]: The list of monster instances for the current encounter.
        """

        return self.monsters

    def is_active(self) -> bool:
        """
        This function checks whether there are any monsters remaining in the current encounter.

        Parameters:
            None.

        Returns:
            bool: True if there are monsters remaining, False otherwise.
        """
        return len(self.get_monsters()) != 0

    def player_apply_card(self, card_name: str, target_id: int | None = None) -> bool:
        """
        This function checks whether the player can successfully use the specified card,
        optionally targeting a specific monster by ID. If the card can be played, the card's
        effect is applied to the target, and the function returns True. If the card cannot be
        played, the function returns False.

        Parameters:
            card_name (str): The name of the card to play.
            target_id (int | None): The ID of the target monster, or None if the card does
                                     not require a target.

        Returns:
            bool: True if the card was played successfully, False otherwise.
        """
        # Determine if the card exists
        if card_name not in ['Eruption','Vigilance','Strike','Defend','Bash','Survivor','Neutralize']:
            return False
        # Create a temporary instance of the card
        need_card = eval(f'{card_name}()')
        # Determine if it is a player turn
        if self.player_turn is False:
            return False
        # If the card requires a target but the player does not provide a target, return false
        if need_card.requires_target() and target_id is None:

            return False
        # If the card requires a target but the target provided by the player is not in the monster list, return false
        if target_id is None:
            pass
        else:

            if target_id not in [monster.get_id() for monster in self.monsters]:
                return False
        # Call method play_card to use this card and record the result
        target_card = self.player.play_card(card_name)
        if target_card is None:

            return False
        # Find the target monster in the monster list
        target_monster_idx = 0
        for monster in self.monsters:
            if monster.get_id() == target_id:
                target_monster_idx = self.monsters.index(monster)
                break
        # Obtain the status dictionary applied by the card and assign it to the target monster
        status = target_card.get_status_modifiers()
        self.player.block += target_card.get_block()
        if 'strength' in status:
            self.player.strength += status['strength']
        if 'weak' in status:
            self.monsters[target_monster_idx].weak += status['weak']

        if 'vulnerable' in status:
            self.monsters[target_monster_idx].vulnerable += status['vulnerable']
        # If the card has damage, Calculate the damage caused by this card.
        if target_card.get_damage_amount():
            damage = target_card.get_damage_amount() + self.player.strength
            if self.monsters[target_monster_idx].vulnerable:
                damage = int(damage*1.5)
            if self.player.weak:
                damage = int(damage*0.75)
            # Target monster deducts corresponding hp
            self.monsters[target_monster_idx].reduce_hp(damage)
            # Determine whether the monster has been defeated, and if defeated, remove it from the monster list
            if self.monsters[target_monster_idx].is_defeated():
                del self.monsters[target_monster_idx]
        return True

    def enemy_turn(self) -> None:
        """
        This function processes the turn for each monster in the encounter by executing its
        assigned action.

        Parameters:
            None.

        Returns:
            None.
        """

        if self.player_turn:
            return
        for monster in self.monsters:
            # Obtain the monster's action dictionary
            status = monster.action()
            # Apply strength to oneself, weight and vulnerable to players
            if 'weak' in status:
                self.player.weak += status['weak']
            if 'vulnerable' in status:
                self.player.vulnerable += status['vulnerable']
            if 'strength' in status:
                monster.strength += status['strength']
            # Calculate the damage caused by the monster's action
            damage = status['damage'] + monster.strength
            if self.player.vulnerable:
                damage = int(damage*1.5)
            if monster.weak:
                damage = int(damage*0.75)
            # Players deduct corresponding hp
            self.player.reduce_hp(damage)
        # The end of the monster's turn corresponds to the end of the entire turn, starting a new turn
        self.start_new_turn()



def main():
    # Prompt for player type and game file to play
    player_type = input('Enter a player type: ')
    player = {'ironclad':IronClad(),'silent':Silent(),'watcher':Watcher()}[player_type]
    file_path = input('Enter a game file: ')
    # Read game based on file path
    encounters = read_game_file(file_path)
    # Cycle through each encounter battle
    for encounter in encounters:
        print('New encounter!\n')
        now_game = Encounter(player, encounter)
        display_encounter(now_game)
        while True:
            # Determine whether the encounter battle has ended
            if not now_game.is_active():
                print(ENCOUNTER_WIN_MESSAGE)
                now_game.end_player_turn()
                break
            # Prompt players to enter the action they want to take
            move = input('Enter a move: ')
            # The player chooses to end the turn and proceed to the monster's turn.
            if move == 'end turn':
                now_game.end_player_turn()
                now_game.enemy_turn()
                # After the monster ends its action, determine whether the player has been defeated
                if player.is_defeated():
                    print(GAME_LOSE_MESSAGE)
                    return
                else:
                    display_encounter(now_game)
            # Players select inspect and display the cards in their inspect position
            if move.split()[0] == 'inspect':
                if move.split()[1] == 'deck':
                    print()
                    print(player.desk)
                    print()
                else:
                    print()
                    print(player.discard)
                    print()
            # Players choose describe and call the corresponding method of the player describe object
            if move.split()[0] == 'describe':
                print()
                card_useless = eval(f'{move.split()[1]}()')
                print(card_useless.get_description())
                print()
            # Players choose to play cards
            if move.split()[0] == 'play':
                # Determine whether the card has a target based on the length separated by spaces
                if len(move.split()) == 2:
                    result_statu = now_game.player_apply_card(move.split()[1])
                else:
                    result_statu = now_game.player_apply_card(move.split()[1], int(move.split()[2]))
                # If the use fails, print the corresponding information
                if result_statu is False:
                    print(CARD_FAILURE_MESSAGE)
                else:
                    display_encounter(now_game)
    # All encounters have ended, printing game victory information
    print(GAME_WIN_MESSAGE)


if __name__ == '__main__':
    main()