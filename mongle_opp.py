import streamlit as st
import pandas as pd

# 몽이아빠님! 여기에 구글 시트 주소(URL)를 넣어주세요.
# 주소 양 끝의 큰따옴표(")는 지우시면 안 됩니다!
sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnwBWXxX-1anqWrcSBCrFFIC26thqAsJiM7o6a41B7sjR9eBcvDdNNUGef3A9IaQ5KCyX_9w72rxrI/pub?output=csv"

# 구글 시트 주소를 실시간 데이터 다운로드용 주소로 자동 변환하는 코드입니다.
csv_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

def get_data():
    # 구글 시트에서 데이터를 실시간으로 읽어옵니다.
    return pd.read_csv(csv_url)

st.set_page_config(page_title="mongle-stay Cloud", layout="wide")

st.title("🐾 mongle-stay Cloud Portal")

# 데이터 불러오기 및 검증
try:
    df = get_data()
    
    tab1, tab2 = st.tabs(["📊 실시간 예약 현황", "🌿 게스트 안내"])
    
    with tab1:
        st.subheader("구글 시트와 실시간 연동 중")
        st.dataframe(df, use_container_width=True)
        if st.button("🔄 새로고침"):
            st.rerun()
            
    with tab2:
        st.subheader("게스트 가이드")
        st.write("몽이가 추천하는 제기동 맛집 정보를 확인하세요!")

except Exception as e:
    st.error(f"⚠️ 주소가 올바르지 않거나 구글 시트 공유 설정('링크가 있는 모든 사용자')이 안 되어 있습니다.\n에러 내용: {e}")