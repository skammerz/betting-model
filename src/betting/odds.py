def american_to_decimal(odds):
    if odds < 0:
        return 1 + (100 / abs(odds))
    else:
        return 1 + (odds / 100)

def american_to_implied_probability(odds):
    if odds < 0:
        return abs(odds) / (abs(odds) + 100)
    else:
        return 100 / (odds + 100)

def remove_vig(over_odds, under_odds):
    p_over = american_to_implied_probability(over_odds)
    p_under = american_to_implied_probability(under_odds)
    total = p_over + p_under

    return {
        "over": p_over / total,
        "under": p_under / total
    }