def analyze_stats(df):
    stats = df[["Health", "Strength", "Defense", "Speed"]]
    print("\nStatistical Summary:")
    print(stats.describe())
