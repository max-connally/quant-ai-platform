def pattern_probability(patterns):

    weights = {

        "double_bottom":0.65,
        "double_top":0.65,
        "head_shoulders":0.70,
        "cup_handle":0.80

    }

    score = 0

    for p in patterns:

        if p in weights:

            score += weights[p]

    return score
