def analyze_stats(df):
    """Perform statistical analysis on character attributes."""
    stats = df[["Health", "Strength", "Defense", "Speed"]]
    print("\nStatistical Summary:")
    print(stats.describe())
