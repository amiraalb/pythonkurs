from main import determine_winner
from player import Player


# Test 1: Testa att spelarens poäng återställs till 0 efter reset
def test_player_reset_score():
    player = Player()
    player.score = 15
    player.reset_score()
    assert player.score == 0


# Test 2: Testa att det blir oavgjort när både spelare och dealer har lika mycket poäng
def test_determine_winner_draw():
    assert determine_winner(18, 18) == "draw"


# Test 3: Testa att spelaren vinner om spelaren har högre poäng än dealern (utan att gå över 21)
def test_determine_winner_player_wins():
    assert determine_winner(20, 19) == "player"


# Test 4: Testa att dealern vinner om dealern har högre poäng än spelaren (utan att gå över 21)
def test_determine_winner_dealer_wins():
    assert determine_winner(17, 20) == "dealer"
