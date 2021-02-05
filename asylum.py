import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(layout="wide")
st.title('Human Rights First Asylum')
st.markdown('### State of Aggregated Data')
st.markdown('• Best viewed full-screen.') 
st.markdown('• Click button on the top left to expand sidebar, where cases can be filtered by selecting multiple fields.') 
st.markdown('• Hover over a field in the table below in order to see the entirety of its content. Graph and table can be viewed in fullscreen.')
st.markdown('---')

df = (
    pd.read_csv('cases.csv')
      .fillna(value='')
      .set_index('date')
      .sort_index(ascending=False)
)

df.index = pd.to_datetime(df.index).date
df = df.iloc[1:]

def getUnique(col):
    lsts = [a.split('; ') for a in df[col]]
    items = set([
        a
        for lst in lsts
        for a in lst
    ])
    items.discard('')
    return items

col1, col2 = st.beta_columns(2)

judges = getUnique('panel_members')
outcomes = getUnique('outcome')
countries = getUnique('country_of_origin')
application = getUnique('application')
protected_grounds = getUnique('protected_grounds')
based_violence = getUnique('based_violence')
keywords = getUnique('keywords')
references = getUnique('references')

judge = st.sidebar.multiselect('BIA JUDGES: ', tuple(judges))
country = st.sidebar.multiselect('APPLICANT\'S COUNTRY OF ORIGIN: ',
                        tuple(countries))
applying = st.sidebar.multiselect('APPLYING FOR: ', tuple(application))
pg = st.sidebar.multiselect('APPLICANT\'S PROTECTED GROUNDS: ',
                    tuple(protected_grounds))
bv = st.sidebar.multiselect('VIOLENCE TYPE: ',
                    tuple(based_violence))
keyword = st.sidebar.multiselect('KEYWORDS: ', tuple(keywords))
reference = st.sidebar.multiselect('REFERENCES: ', tuple(references))

ref_ = {
    'Matter of AB, 27 I&N Dec. 316 (A.G. 2018)': 'Matter of AB',
    'Matter of L-E-A-, 27 I&N Dec. 581 (A.G. 2019)': 'Matter of L-E-A-'
}

ref = [ref_[r] for r in reference]

display_df = df[
    df['panel_members'].str.contains('|'.join(judge))
    & df['country_of_origin'].str.contains('|'.join(country))
    & df['keywords'].str.contains('|'.join(keyword))
    & df['protected_grounds'].str.contains('|'.join(pg))
    & df['based_violence'].str.contains('|'.join(bv))
    & df['application'].str.contains('|'.join(applying))
    & df['references'].str.contains('|'.join(ref))
]

graphable_fields = [
    'outcome', 'country_of_origin', 
    'protected_grounds', 'based_violence',
    'references', 'panel_members', 'sex_of_applicant', 
    'year'
]

def getCount(col, normalize=False):
    if col == 'year':
        return display_df.index.year.value_counts()

    lsts = [a.split('; ') for a in display_df[col]]
    items = [
        a
        for lst in lsts
        for a in lst
    ]
    return pd.Series(items, name=col).value_counts(normalize=normalize)

with col2:
    to_graph = st.selectbox('FIELD TO GRAPH: ', graphable_fields)
    st.markdown(f'**Total Number of Cases Represented: {len(display_df)}**')
    st.write('Note: an empty value on the bar chart represents empty fields.')

with col1:
    st.bar_chart(getCount(to_graph), 
                 width=460, 
                 use_container_width=False)

display_df