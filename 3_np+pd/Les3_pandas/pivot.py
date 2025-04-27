import pandas as pd
data = {
    'Date': ['2025-03-01', '2025-03-01', '2025-03-02', '2025-03-02', '2025-03-02', '2025-03-03'],
    'City': ['Genk', 'As', 'Hasselt', 'Genk', 'As','Hasselt', ],
    'Gebied' : ['Wei', 'Centrum', 'Industrie','Wei', 'Centrum', 'Industrie'],
    'Temperature' : [15.22, 14.33, 16.44, 13.55, 17.66, 14.77]
}
df = pd.DataFrame(data)
print(df)

# In onderstaande kan columns geen 'Gebied' zijn omdat die geen unieke combinaties kolom-index bevat. Gebruik dan pivot_table
pivoted_df = df.pivot(index='City', columns='Date', values='Temperature')
print(pivoted_df)

# Nu wel aggregatie mogelijk op kolim-index-combinaties. Tevens wiskunde erop mogelijk.
aggregatiemethode = ("mean", "count", "max", "min")
pivoted_df2 = df.pivot_table(index='City', columns='Gebied', values='Temperature', aggfunc=aggregatiemethode[1], fill_value=0)

print(pivoted_df2.round(1))
print(df)
