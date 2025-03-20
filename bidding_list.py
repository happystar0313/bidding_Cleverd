import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="📜 입찰 목록 조회", layout="wide")

# ✅ 연도별 데이터 파일 생성 함수
def get_data_file(year):
    return f"bidding_data_{year}.csv"

# ✅ 연도별 데이터 로드
def load_data(year):
    file_name = get_data_file(year)
    if os.path.exists(file_name):
        return pd.read_csv(file_name)
    else:
        return pd.DataFrame(columns=[
            "입찰공고번호", "입찰명", "공고일", "마감일", "사업기간", "사업예산", "과업내용", "입찰조건",
            "기술점수", "가격점수", "참여업체", "업체점수", "투찰금액", "낙찰업체", "개찰자",
            "제출방법", "제출지역", "비고", "클레버디 투찰여부"
        ])

st.title("📜 입찰 목록 조회")

# ✅ 연도 선택 드롭다운
year = st.selectbox("연도 선택", ["2024", "2025", "2026", "2027"])

# ✅ 기존 데이터 불러오기
df = load_data(year)

# ✅ 데이터가 있을 경우만 표시
if len(df) > 0:
    # 🔍 검색 기능 (입찰공고번호 & 입찰명)
    search_term = st.text_input("🔍 검색 (입찰공고번호 또는 입찰명 입력)")

    # 🔍 필터링 기능 (클레버디 투찰 여부)
    status_filter = st.selectbox("📌 클레버디 투찰 여부 필터", ["전체", "예", "아니오", "보류"])

    # ✅ 필터 적용
    if search_term:
        df = df[df["입찰공고번호"].astype(str).str.contains(search_term) | df["입찰명"].str.contains(search_term, na=False)]

    if status_filter != "전체":
        df = df[df["클레버디 투찰여부"] == status_filter]

    # 📋 필터링된 데이터 표시
    st.write(f"📌 {year}년 입찰 목록")
    st.dataframe(df, use_container_width=True)
    
else:
    st.write("🚨 아직 등록된 입찰 정보가 없습니다.")
