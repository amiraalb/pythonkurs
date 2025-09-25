from main import Dice, Player, determine_winner
def test_roll_dice_should_result_in_random_value_between_1_to_6():
    dice = Dice()
    roll = dice.roll()
    assert roll > 0
    assert roll < 7

def test_player_reset_score():
    player = Player()
    player.score = 15
    player.reset_score()
    assert player.score == 0

def test_determine_winner_draw():
    assert determine_winner(18, 18) == "draw"

def test_determine_winner_player_wins():
    assert determine_winner(20, 19) == "player"

def test_determine_winner_dealer_wins():
    assert determine_winner(17, 20) == "dealer"
