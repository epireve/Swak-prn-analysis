import streamlit as st
import pandas as pd

st.title('Sarawak State Election 2021 Analysis')

df = pd.read_csv('result_prn12_2021.csv')

# Overall Analysis
st.header('Overall Analysis')

st.markdown(f'''
- Total seats: **{df['D_name'].nunique()}**  
- GPS won: **{df[df['Parti_Pemenang']=='GPS'].shape[0]} seats**
- Opposition won: **{df[df['Parti_Pemenang']!='GPS'].shape[0]} seats**
''')

st.bar_chart(df.groupby('Parti_Pemenang').agg({'D_name':'count'}))

# Incumbent MP Analysis
st.header('Incumbent MP Analysis')

incumbents = df[df['Penyandang.Nama']!= 'Kosong']

vote_diff = incumbents['Undi_Menang'] - incumbents['Penyandang.Undi']
incumbents['Vote Difference'] = vote_diff

incumbents['Vote Share Change'] = (incumbents['Undi_Menang']/incumbents['Total Votes'] 
                                    - incumbents['Penyandang.Undi']/incumbents['Total Votes'])

swing_df = incumbents[incumbents['Parti_Pemenang'] != incumbents['Penyandang.Parti']]

st.dataframe(incumbents)
st.markdown(f'- Number of swing districts: {len(swing_df)}')

# Winning Margin Analysis
st.header('Winning Margin Analysis')

# margin analysis code
