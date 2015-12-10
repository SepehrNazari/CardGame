from Game import players, Winner
import Card
import Player

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


def deal_damage(target, damage, cause=None, cause_card=None):
    if isinstance(target, Card.Creature):
        # procs for before damage
        target.strength -= damage
        # procs for after damage
        if target.strength <= 0:
            destroy(target, cause, cause_card)
    elif isinstance(target, Player.Player):
        mill(1, target)


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

