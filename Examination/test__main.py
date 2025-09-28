from main import Game
from player import Player


# Test 1: Testa att spelarens poäng återställs till 0 efter reset.
# Testet skapar en ny instans av objektet Player och sätter player.score till 15.
# Metoden reset_score anropas.
# Assert verifierar att det faktiska player.score är 0, dvs poängen har återställts.
def test_player_reset_score():
    player = Player()
    player.score = 15
    player.reset_score()
    assert player.score == 0


# Test 2: Testa att det blir oavgjort när både spelare och dealer har lika mycket poäng.
# Testet startar en ny instans av objektet Game och anropar determine_winner med poängen 18 för både spelare och dealer.
# Det faktiska resultatet blir "draw", dvs oavgjort.
def test_determine_winner_draw():
    game = Game()
    assert game.determine_winner(18, 18) == "draw"


# Test 3: Testa att spelaren vinner om spelaren har högre poäng än dealern (utan att gå över 21)
# Testet startar en ny instans av objektet Game och
# anropar determine_winner med poängen 20 för spelare och 19 för dealern.
# Den faktiska vinnaren är "player", dvs spelaren, då 20 är högre än 19.
def test_determine_winner_player_wins():
    game = Game()
    assert game.determine_winner(20, 19) == "player"


# Test 4: Testa att dealern vinner om dealern har högre poäng än spelaren (utan att gå över 21)
# Testet startar en ny instans av objektet Game och anropar determine_winner
# med poängen 17 för spelare och 20 för dealern.
# Den faktiska vinnaren är "dealer", då 20 är högre än 17.
def test_determine_winner_dealer_wins():
    game = Game()
    assert game.determine_winner(17, 20) == "dealer"
