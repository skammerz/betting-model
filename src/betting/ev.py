def profit_per_dollar(odds):
    if odds > 0:
        return odds / 100
    else:
        return 100 / abs(odds)

def expected_value(win_probability, odds):
    profit = profit_per_dollar(odds)
    lose_probability = 1 - win_probability
    return (
        win_probability * profit
        - lose_probability
    )
