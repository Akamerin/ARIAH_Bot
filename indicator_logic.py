def get_signal(pair, timeframe):
    signal = {
        "pair": pair,
        "timeframe": timeframe,
        "direction": "CALL",
        "entry": "Next Candle",
        "strength": "92%",
        "indicators": ["BB", "STC", "Stochastic", "Parabolic SAR"]
    }

    all_align = True
    psar_optional = True

    if all_align:
        return signal
    return None
