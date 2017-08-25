from src.game import Winner
from src import card
from src.player import Player
from src import player
import random

combat = 'combat'


def draw(player, deck, num, cause=None):
    # triggers for before draw
    for x in range(num):
        if not len(player.deck):
            raise Winner(player)  # perhaps give enemy coins instead
        else:
            player.draw()
    # triggers for after draw


def attack(attacker, target):
    # triggers for on attack declaration
    deal_damage(target, attacker.strength, combat)
    # triggers for after attack


def deal_damage(source, target, damage):
    if isinstance(target, card.Creature):
        # triggers for before damage
        target.health -= damage
        # triggers for after damage
        if target.health <= 0:
            destroy(target, source)
    elif isinstance(target, player):
        gain_coins(source.player, damage)


def gain_coins(Player, coins):
    # triggers before gain coins
        Player.gain_coins(coins)
    # triggers after gain coins


def destroy(players, cards, cause=None, cause_card=None):
    # triggers for before destruction
    for card in cards:
        for player in players:
            if card in player.board:
                player.board_remove((card,))
                player.graveyard_add((card,))
    # triggers for after destruction


def mill(player, deck, num):
    # triggers for before mill
    player.graveyard_add(player.deck_get_top(deck, num))
    # triggers for after mill


def play_card(player, card, position):
    # triggers for before playing card
    player.hand_remove((card,))
    if card.trigger:
        # triggers for before trigger effects
        player.trigger(card.trigger)
        # triggers for after trigger effects
    if isinstance(card, card.Creature):
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
