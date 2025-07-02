import streamlit as st
from PIL import Image
import pandas as pd
import random

df = pd.read_csv('iron_lunchlist.csv')

image = Image.open('다운로드.jpg')
st.image(image)

st.write('아이언디바이스 점심 메뉴 추천 페이지입니다.')
st.write('메뉴가 마음에 들지 않는다면 버튼을 다시 눌러보세요.')
st.write('\n')
st.write('점심 맛있게 드세요!')
st.write('\n')
col1, col2 = st.columns(2)

with col2:
    dontcare = st.checkbox("상관없음", key="disabled")
with col1:
    menu = st.radio(
        "조건 선택 👇",
        ["한식만 추천", "중식만 추천", "일식만 추천", "양식만 추천", "분식만 추천", "베트남만 추천", "해장메뉴 추천"],
        disabled=st.session_state.disabled
    )
st.write('\n')
if st.button('점심 추천'):
    if dontcare:
        index = random.randrange(0,len(df))
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
    elif menu == "한식만 추천":
        index = random.randrange(24,len(df))
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
    elif menu == "분식만 추천":
        index = random.randrange(22,24)
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
    elif menu == "중식만 추천":
        index = random.randrange(14,22)
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
    elif menu == "일식만 추천":
        index = random.randrange(9,14)
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
    elif menu == "양식만 추천":
        index = random.randrange(3,9)
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
    elif menu == "베트남만 추천":
        index = random.randrange(0,9)
        st.write('오늘의 점심은:')
        st.write(df.iloc[index,1] + '(' + df.iloc[index,0] + ')')
    
st.write('\n')
st.write('\n')


st.write('\n')
st.write('\n')

if st.button('전체 메뉴 리스트'):
    st.write('점심 메뉴:')
    st.write(pd.DataFrame(df))
    
st.write('\n')

st.write('아이언디바이스 화이팅!')
