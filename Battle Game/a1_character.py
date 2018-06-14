mage_attack_image = ['mage_attack_0','mage_attack_1','mage_attack_2','mage_attack_3',
                     'mage_attack_4','mage_attack_5','mage_attack_6','mage_attack_7',
                     'mage_attack_8','mage_attack_9']

mage_idle_image = ['mage_idle_0','mage_idle_1','mage_idle_2','mage_idle_3',
                   'mage_idle_4','mage_idle_5','mage_idle_6','mage_idle_7',
                   'mage_idle_8','mage_idle_9']

mage_special_image = ['mage_special_0','mage_special_1','mage_special_2','mage_special_3',
                      'mage_special_4','mage_special_5','mage_special_6','mage_special_7',
                      'mage_special_8','mage_special_9']

rogue_attack_image = ['rogue_attack_0','rogue_attack_1','rogue_attack_2','rogue_attack_3',
                      'rogue_attack_4','rogue_attack_5','rogue_attack_6','rogue_attack_7',
                      'rogue_attack_8','rogue_attack_9']

rogue_idle_image = ['rogue_idle_0','rogue_idle_1','rogue_idle_2','rogue_idle_3',
                    'rogue_idle_4','rogue_idle_5','rogue_idle_6','rogue_idle_7',
                    'rogue_idle_8','rogue_idle_9']

rogue_special_image = ['rogue_special_0','rogue_special_1','rogue_special_2','rogue_special_3',
                       'rogue_special_4','rogue_special_5','rogue_special_6','rogue_special_7',
                       'rogue_special_8','rogue_special_9']

class Character:

    """
    The character class
    """
    def __init__(self):
        """
        The character has 100 HP and 100 SP
        """
        self._HP = 100
        self._SP = 100
        self.counter = -1

    @property
    def SP(self):
        if self._SP < 0:
            return 0
        return self._SP

    @SP.setter
    def SP(self, sp_value):
        self._SP = sp_value

    @property
    def HP(self):
        if self._HP < 0:
            return 0
        return self._HP

    @HP.setter
    def HP(self, hp_value):
        self._HP = hp_value

    def attack(self):
        """
        Attack
        """
        raise NotImplementedError

    def special_attack(self):
        """
        Special attack
        """
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def get_hp(self):
        """
        Get Hp of the character
        """
        return self.HP

    def get_sp(self):
        """
        Get Sp of the character
        """
        return self.SP

    def get_available_actions(self):
        """
        Get character's available actions
        """
        raise NotImplementedError

    def get_name(self):
        """
        Get the name of character
        """
        raise NotImplementedError

    def get_next_sprite(self):
        """
        Get the next image for ui
        """
        raise NotImplementedError

    def is_valid_action(self, action):
        """
        return a bool to decide whether it is a valid action
        """
        raise NotImplementedError


class Rogue(Character):
    """
    A type of character
    """
    def __init__(self, name, battle_queue, playstyle):
        """
        Initialize this Character
        """
        super().__init__()
        self.defense = 10
        self.name = name
        self.battle_queue = battle_queue
        self.enemy = None
        self.playstyle = playstyle
        self.chosen_list = rogue_idle_image

    def attack(self):
        """
        attack the enemy, taking the SP, put himself into the end
        of the battlequene
        """
        self.enemy.HP += self.enemy.defense - 15
        self.SP += -3
        self.battle_queue.add(self.enemy.enemy)
        self.counter = -1
        self.chosen_list = rogue_attack_image


    def special_attack(self):
        """
        use special_attack to attack enemy, taking the SP,
        adds the Rogue to the BattleQueue twice.
        """
        self.enemy.HP += (self.enemy.defense - 20)
        self.SP += -10
        self.battle_queue.add(self.enemy.enemy)
        self.battle_queue.add(self.enemy.enemy)
        self.counter = -1
        self.chosen_list = rogue_special_image

    def __repr__(self):
        """
        To make print a str look like Name (Character): HP/SP
        """
        return str(self.name) + ' (Rogue): ' + str(self.HP) \
        + '/' + str(self.SP)

    def get_name(self):
        """
        Get the name of character
        """
        return self.name

    def is_valid_action(self, action):
        """
        return a bool to decide whether it is a valid action
        """
        if action == "A":
            if self.SP > 3:
                return True
            return False
        if action == "S":
            if self.SP > 10:
                return True
            return False

    def get_available_actions(self):
        """
        Get character's available actions
        """
        if self.SP < 3:
            return []
        if 10 > self.SP >= 3:
            return ["A"]
        if self.SP >= 10:
            return ["A", "S"]

    def get_next_sprite(self):
        """
        Get the next image for ui
        """
        if self.counter == 9:
            self.counter = -1
            self.chosen_list = rogue_idle_image
        self.counter += 1
        return self.chosen_list[self.counter % 10]


class Mage(Character):
    """
    A type of Character
    """
    def __init__(self, name, battle_queue, playstyle):
        """
        Initialize this Character
        """
        super().__init__()
        self.defense = 8
        self.name = name
        self.battle_queue = battle_queue
        self.enemy = None
        self.playstyle = playstyle
        self.chosen_list = mage_idle_image

    def attack(self):
        """
        attack the enemy, taking the SP, put himself into the end
        of the battlequene
        """
        self.enemy.HP += (self.enemy.defense - 20)
        self.SP += -5
        self.battle_queue.characters.append(self.enemy.enemy)
        self.chosen_list = mage_attack_image
        self.counter = -1

    def special_attack(self):
        """
        use special_attack to attack enemy, taking the SP,
        adds its enemy to the BattleQueue once before adding
        the Mage itself into the BattleQueue.
        """
        self.enemy.HP += (self.enemy.defense - 40)
        self.SP += -30
        self.battle_queue.add(self.enemy)
        self.battle_queue.add(self.enemy.enemy)
        self.chosen_list = mage_special_image
        self.counter = -1

    def get_name(self):
        """
        Get the name of character
        """
        return self.name

    def is_valid_action(self, action):
        """
        return a bool to decide whether it is a valid action
        """
        if action == "A":
            if self.SP > 5:
                return True
            return False
        if action == "S":
            if self.SP > 30:
                return True
            return False

    def get_available_actions(self):
        """
        Get character's available actions
        """
        if self.SP < 5:
            return []
        elif 30 >= self.SP > 5:
            return ['A']
        elif self.SP >= 30:
            return ['A', 'S']

    def get_next_sprite(self):
        """
        Get the next image for ui
        """
        if self.counter == 9:
            self.counter = -1
            self.chosen_list = mage_idle_image
        self.counter += 1
        return self.chosen_list[self.counter % 10]

    def __repr__(self):
        """
        To make print a str look like Name (Character): HP/SP
        """
        return str(self.name) + ' (Mage): ' + str(self.HP) \
        + '/' + str(self.SP)