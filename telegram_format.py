def format_signal_message(signal):
    arrow = "🟢 BUY" if signal["direction"] == "CALL" else "🔴 SELL"
    emoji = "🧠"
    strength = signal["strength"]
    entry = signal["entry"]

    return f"""
<b>{emoji} A.R.I.A.H SIGNAL</b>

<b>Pair:</b> <code>{signal['pair']}</code>
<b>Timeframe:</b> <code>{signal['timeframe']}</code>
<b>Direction:</b> <b>{arrow}</b>
<b>Entry:</b> <code>{entry}</code>
<b>Strength:</b> <b>{strength}</b>

📊 Indicators: BB, STC, Stochastic, {'+ PSAR' if 'Parabolic SAR' in signal['indicators'] else 'No PSAR'}
"""
