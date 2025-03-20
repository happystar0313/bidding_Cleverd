import streamlit as st
import pandas as pd
import os
import datetime

st.set_page_config(page_title="📌 입찰정보 입력", layout="wide")

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

st.title("📌 입찰정보 입력")

# ✅ 연도 선택 드롭다운
year = st.selectbox("연도 선택", ["2024", "2025", "2026", "2027"])

# ✅ 기존 데이터 불러오기
df = load_data(year)

# ✅ 신규 입찰정보 입력
st.write("### ➕ 신규 입찰 정보 입력")
bid_number = st.text_input("입찰공고번호")
bidding_name = st.text_input("입찰명")

# ✅ 📅 날짜 입력
start_date = st.date_input("공고일", value=datetime.date.today())
end_date = st.date_input("마감일", value=datetime.date.today())

# ✅ 날짜 한글 변환
start_date_kor = start_date.strftime("%Y년 %m월 %d일")
end_date_kor = end_date.strftime("%Y년 %m월 %d일")

project_duration = st.text_input("사업기간")
budget = st.number_input("사업예산 (숫자만 입력)", min_value=0, step=100000)
scope = st.text_area("과업내용")
conditions = st.text_area("입찰조건")

# ✅ 제출 방법 선택
st.write("### 📤 제출 방법 선택")
submit_method = st.radio("제출 방법", ["온라인 제출", "직접 제출"])

submit_location = ""
if submit_method == "직접 제출":
    submit_location = st.text_input("제출 지역 (예: 서울시 종로구 조달청)")

# ✅ 클레버디 투찰 여부 선택
st.write("### 📌 클레버디 투찰 여부")
cleverbid_status = st.radio("클레버디 투찰 여부", ["예", "아니오", "보류"])

# ✅ 비고 입력
notes = st.text_area("📌 비고 (기타 메모)")

# ✅ 저장 버튼
if st.button("저장"):
    new_data = pd.DataFrame([{
        "입찰공고번호": bid_number,
        "입찰명": bidding_name,
        "공고일": start_date_kor,
        "마감일": end_date_kor,
        "사업기간": project_duration,
        "사업예산": budget,
        "과업내용": scope,
        "입찰조건": conditions,
        "기술점수": "",
        "가격점수": "",
        "참여업체": "",
        "업체점수": "",
        "투찰금액": "",
        "낙찰업체": "",
        "개찰자": "",
        "제출방법": submit_method,
        "제출지역": submit_location,
        "비고": notes,
        "클레버디 투찰여부": cleverbid_status
    }])
    import streamlit as st

st.set_page_config(page_title="📑 입찰 관리 시스템", layout="wide")

st.title("📑 입찰 관리 시스템")

st.write("📌 좌측 사이드바에서 원하는 페이지를 선택하세요.")

# ✅ Streamlit 멀티페이지 기능 자동 활성화됨

    df = pd.concat([df, new_data], ignore_index=True)
    save_data(df, year)
    st.success(f"{year}년 입찰 정보가 저장되었습니다!")
