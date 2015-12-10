from Game import players, Winner

combat = 'combat'


def draw(player, num, cause=None):
    # procs for before draw
    for x in range(num):
        if not len(player.deck):
            raise Winner(player)
        else:
            player.draw()
    # procs for after draw


def attack(attacker, target):
    # procs for on attack declaration
    deal_damage(target, attacker.strength, combat, attacker)
    deal_damage(attacker, target.strength, combat, target)
    if target.strength <= 0:
        destroy(target, combat)
    if attacker.strength <= 0:
        destroy(attacker, combat)


def deal_damage(creature, damage, cause=None, cause_card=None):
    # procs for before damage
    creature.strength -= damage
    # procs for after damage
    if creature.strength <= 0:
        destroy(creature, cause, cause_card)


def destroy(card, cause=None, cause_card=None):
    # procs for before destruction
    for player in players:
        if card in player.board:
            player.remove_from_board(card)
            player.send_to_grave([card])
    # procs for after destruction


def mill(num, player):
    player.send_to_grave(player.get_top_deck(num))
    # procs for effects that happen after mill

