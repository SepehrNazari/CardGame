from Game import players, Winner
import Card
import Player
import random

combat = 'combat'


def draw(player, num, cause=None):
    # triggers for before draw
    for x in range(num):
        if not len(player.deck):
            raise Winner(player)
        else:
            player.draw()
    # triggers for after draw


def attack(attacker, target):
    # triggers for on attack declaration
    deal_damage(target, attacker.strength, combat, attacker)
    deal_damage(attacker, target.strength, combat, target)


def deal_damage(target, damage, cause=None, cause_card=None):
    if isinstance(target, Card.Creature):
        # triggers for before damage
        target.strength -= damage
        # triggers for after damage
        if target.strength <= 0:
            destroy(target, cause, cause_card)
    elif isinstance(target, Player.Player):
        mill(1, target)


def destroy(cards, cause=None, cause_card=None):
    # triggers for before destruction
    for card in cards:
        for player in players:
            if card in player.board:
                player.board_remove((card,))
                player.graveyard_add((card,))
    # triggers for after destruction


def mill(num, player):
    # triggers for before mill
    player.graveyard_add(player.deck_get_top(num))
    # triggers for after mill


def play_card(player, card, position):
    # triggers for before playing card
    player.hand_remove((card,))
    if card.trigger:
        # triggers for before trigger effects
        player.trigger(card.trigger)
        # triggers for after trigger effects
    if isinstance(card, Card.Creature):
        player.board_add(card, position)
    # add continuous and trigger effects to continuous and trigger lists
    # triggers for after playing card


def discard(player, cards):
    # triggers for before discard
    player.hand_remove(cards)
    # triggers for before send to graveyard
    player.graveyard_add(cards)
    # triggers for after send to graveyard
    # triggers for after discard


def discardRandom(player, num):
    cards = random.sample(player.hand_get(), num)
    # triggers for before discard
    player.hand_remove(cards)
    # triggers for before send to graveyard
    player.graveyard_add(cards)
    # triggers for after send to graveyard
    # triggers for after discard
