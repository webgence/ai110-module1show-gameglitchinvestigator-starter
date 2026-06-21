from logic_utils import check_guess

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_message_says_go_lower():
    # Bug fix: when guess > secret, message must direct the player downward (Go LOWER),
    # not upward. The original code returned "Go HIGHER!" for a too-high guess.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message for Too High, got: {message!r}"
    assert "HIGHER" not in message, f"Message for Too High must not say HIGHER, got: {message!r}"

def test_too_low_message_says_go_higher():
    # Bug fix: when guess < secret, message must direct the player upward (Go HIGHER),
    # not downward. The original code returned "Go LOWER!" for a too-low guess.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message for Too Low, got: {message!r}"
    assert "LOWER" not in message, f"Message for Too Low must not say LOWER, got: {message!r}"
