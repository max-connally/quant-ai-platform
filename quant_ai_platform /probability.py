def profit_probability(score):

    if score > 1.7:
        return 0.75

    if score > 1.4:
        return 0.65

    if score > 1.0:
        return 0.55

    return 0.45
