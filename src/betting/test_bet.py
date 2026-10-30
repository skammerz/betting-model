from odds import american_to_implied_probability
from ev import expected_value, bet_recommendation

sportsbook_odds = -110
model_win_probability = 0.58

break_even_probability = american_to_implied_probability(sportsbook_odds)
ev = expected_value(model_win_probability, sportsbook_odds)
edge = model_win_probability - break_even_probability
recommendation = bet_recommendation(model_win_probability, sportsbook_odds)

print("Sportsbook break-even probability: ", f"{break_even_probability:.2%}")
print("Model win probability: ", f"{model_win_probability:.2%}")
print("Expected value: ", f"{ev:.2%}")
print("Edge: ", f"{edge:.2%}")
print("Recommendation: ", recommendation)