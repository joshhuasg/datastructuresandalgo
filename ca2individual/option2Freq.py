class option2Sort:
    def count(df):
        counts = []
        for i in range(len(df)):
            cnt = df['Equation'][i].count(')') + df['Equation'][i].count('(')
            counts.append(cnt)
        df['Bracket'] = counts
        return df

    def freq(df):
        freq = []
        for i in range(len(df)):
            count = 0
            for j in range(len(df)):
                if df['Answer'][i] == df['Answer'][j]:
                    count+=1
            freq.append(count)
        df['Frequency'] = freq
        return df
