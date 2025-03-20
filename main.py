import streamlit as st

st.set_page_config(page_title="📑 입찰 관리 시스템", layout="wide")

# ✅ 메인 페이지 제목
st.title("📑 입찰 관리 시스템")

# ✅ 페이지 설명 추가
st.markdown("### 🔹 이 시스템을 통해 다음 작업을 수행할 수 있습니다.")
st.write("- **[입찰정보 입력]** : 새 입찰 공고를 등록하세요.")
st.write("- **[개찰정보 입력]** : 개찰 후 참여업체 점수 및 낙찰업체를 입력하세요.")
st.write("- **[입찰정보 리스트]** : 모든 입찰 내역을 검색 및 조회하세요.")

# ✅ 사이드바 메뉴
st.sidebar.title("📌 메뉴 선택")
page = st.sidebar.radio("이동할 페이지를 선택하세요", ["🏢 입찰정보 입력", "📜 개찰정보 입력", "📋 입찰정보 리스트"])

# ✅ 각 메뉴에 대한 버튼 추가
st.write("\n\n---\n")
st.markdown("## 🔽 원하는 작업을 선택하세요!")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📢 입찰정보 입력"):
        st.switch_page("pages/bidding_entry.py")

with col2:
    if st.button("📑 개찰정보 입력"):
        st.switch_page("pages/bidding_opening.py")

with col3:
    if st.button("📋 입찰정보 리스트"):
        st.switch_page("pages/bidding_list.py")

st.write("\n\n---")
st.write("📌 좌측 사이드바에서도 페이지를 이동할 수 있습니다.")
