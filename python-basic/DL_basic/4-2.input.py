import streamlit as st
import pandas as pd
from datetime import datetime  

st.header('날짜 구간으로 데이터 조회하기')

# streamlit//data_subway_in_seoul.csv
# encoding='cp949'  읽어오고 확인하기 
df = pd.read_csv('data_subway_in_seoul.csv', encoding='cp949')
st.write('날짜 필드 형식: ', df['날짜'].dtypes)
st.write( df  )

# 날짜 컬럼을 string에서 datetime으로 변환하고 확인하기
df['날짜'] = pd.to_datetime( df['날짜'], format='%Y-%m-%d' )
st.write('날짜 필드 형식: ', df['날짜'].dtypes)
st.write(df)

# slider를 사용하여 날짜 구간 설정하기
slider_date = st.slider(
    '날짜 구간을 선택하세요 ',
    datetime(2021, 1, 1), datetime(2021, 12, 31),
    value=(datetime(2021, 7, 1), datetime(2021, 7, 31)),
    format='YY/MM/DD')
st.write('slider_date[0]: ', slider_date[0], 'slider_date[1]: ', slider_date[1] )
start_date = slider_date[0]
end_date = slider_date[1]

    
    

    


# slider 날짜 구간으로 df를 읽어서 새 sel_df 으로 저장하고 확인하기
sel_df = df.loc[df['날짜'].between(start_date, end_date)]
st.dataframe(sel_df)


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-2.input.py