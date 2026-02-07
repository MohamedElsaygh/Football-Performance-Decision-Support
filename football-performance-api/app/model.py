def make_decision(context):
    minute = context.minute
    score_diff = context.score_diff
    fatigue = context.fatigue_level
    possession = context.possession_trend

    # Simple rule-based logic
    if score_diff > 0 and minute > 70 and fatigue > 0.7:
        return {
            "recommendation": "Protect lead",
            "reason": "Winning late with high fatigue",
            "confidence": 0.85
        }

    if score_diff < 0 and possession > 0.2 and fatigue < 0.6:
        return {
            "recommendation": "Increase press",
            "reason": "Chasing the game with positive possession momentum",
            "confidence": 0.78
        }

    return {
        "recommendation": "Maintain shape",
        "reason": "Game state stable",
        "confidence": 0.70
    }
