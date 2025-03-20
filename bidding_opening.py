import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🏆 개찰정보 입력", layout="wide")

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

# ✅ 데이터 저장 함수
def save_data(df, year):
    file_name = get_data_file(year)
    df.to_csv(file_name, index=False)

st.title("🏆 개찰정보 입력")

# ✅ 연도 선택 드롭다운
year = st.selectbox("연도 선택", ["2024", "2025", "2026", "2027"])

# ✅ 기존 데이터 불러오기
df = load_data(year)

if len(df) > 0:
    selected_index = st.number_input("개찰할 입찰 번호 선택", min_value=0, max_value=len(df)-1, step=1)

    num_companies = st.number_input("참여업체 수", min_value=1, max_value=10, value=1)

    companies = []
    scores = []
    bids = []
    
    for i in range(num_companies):
        col1, col2, col3 = st.columns(3)
        with col1:
            company_name = st.text_input(f"업체 {i+1} 이름")
        with col2:
            company_score = st.number_input(f"업체 {i+1} 기술점수", min_value=0, max_value=100, step=1, value=0)
        with col3:
            bid_price = st.number_input(f"업체 {i+1} 투찰금액 (원)", min_value=0, step=100000, value=0)
        
        companies.append(company_name)
        scores.append(company_score)
        bids.append(bid_price)

    # ✅ 가격점수 계산
    lowest_bid = min(bids)
    price_scores = [(lowest_bid / bid) * 20 for bid in bids]
    total_scores = [s + p for s, p in zip(scores, price_scores)]
    winner = companies[total_scores.index(max(total_scores))]

    if st.button("개찰 정보 저장"):
        df.at[selected_index, "참여업체"] = ", ".join(companies)
        df.at[selected_index, "낙찰업체"] = winner
        save_data(df, year)
        st.success("✅ 개찰 정보가 저장되었습니다!")
