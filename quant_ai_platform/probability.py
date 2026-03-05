def profit_probability(score):
    if score > 1.7:
        return 0.75
    elif score > 1.4:
        return 0.65
    elif score > 1.0:
        return 0.55
    else:
        return 0.45
