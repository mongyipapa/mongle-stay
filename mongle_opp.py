import streamlit as st
import streamlit.components.v1 as components
import time

# =========================================================
# [설정 영역] 숙소 Wi-Fi 및 연락처 정보
# =========================================================
WIFI_5G = "U+Net1825_5G"
WIFI_24G = "U+Net1825"
WIFI_PW = "42155551M#"

# 1. 페이지 기본 설정 (모바일 및 데스크탑 반응형)
st.set_page_config(
    page_title="mongle-stay | Guest Guidebook",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 현재 선택된 언어, 탭 인덱스 및 스크롤 상태 초기화
if "selected_lang" not in st.session_state:
    st.session_state.selected_lang = "한국어"
if "active_tab" not in st.session_state:
    st.session_state.active_tab = 0
if "scroll_to_top" not in st.session_state:
    st.session_state.scroll_to_top = False

def set_lang(lang_key):
    st.session_state.selected_lang = lang_key

def go_to_tab(idx):
    st.session_state.active_tab = idx
    st.session_state.scroll_to_top = True

# 2. 커스텀 CSS (모바일 1줄 고정 · 슬림 헤더 · 택시 카드 · 깔끔한 버튼)
st.markdown("""
<style>
    .stApp {
        background-color: #FAF9F6;
        color: #3C4043;
    }
    .block-container {
        padding-top: 0.9rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 680px !important;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 모바일에서도 4열 컬럼이 가로 1줄 유지되도록 강제 설정 */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 6px !important;
    }
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
        flex: 1 1 0% !important;
        min-width: 0 !important;
        width: auto !important;
    }

    /* 상단 헤더 (한 줄 고정) */
    .hero-box {
        background: linear-gradient(135deg, #2E5A44 0%, #4A7C62 100%);
        color: #FFFFFF;
        padding: 15px 18px;
        border-radius: 16px;
        margin-top: 6px;
        margin-bottom: 12px;
        box-shadow: 0 6px 16px rgba(46, 90, 68, 0.15);
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
    }
    .hero-title {
        font-size: 19px;
        font-weight: 700;
        margin: 0 0 3px 0;
        letter-spacing: -0.4px;
        color: #FFFFFF;
        white-space: nowrap;
    }
    .hero-subtitle {
        font-size: 12px;
        opacity: 0.92;
        margin: 0;
        color: #E8F2EC;
        line-height: 1.35;
    }
    .hero-badge {
        background-color: rgba(255, 255, 255, 0.18);
        padding: 5px 9px;
        border-radius: 16px;
        font-size: 11px;
        font-weight: 600;
        color: #FFFFFF;
        white-space: nowrap;
        flex-shrink: 0;
    }

    /* 택시 기사님용 큰 글씨 카드 */
    .taxi-card {
        background-color: #FFFDF7;
        border: 2px solid #D9A036;
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
        box-shadow: 0 3px 10px rgba(217, 160, 54, 0.08);
    }
    .taxi-tag {
        display: inline-block;
        background-color: #D9A036;
        color: #FFFFFF;
        font-size: 11.5px;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 6px;
        margin-bottom: 8px;
    }
    .taxi-kr-main {
        font-size: 18.5px;
        font-weight: 700;
        color: #1F1D1B;
        line-height: 1.45;
        margin: 4px 0;
        word-break: keep-all;
    }
    .taxi-kr-sub {
        font-size: 13.5px;
        font-weight: 600;
        color: #5C554E;
        margin-top: 4px;
    }

    .info-card {
        background-color: #FFFFFF;
        border: 1px solid #E8E4DC;
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
    }
    .card-title {
        font-size: 16px;
        font-weight: 700;
        color: #2E5A44;
        margin-bottom: 9px;
        display: flex;
        align-items: center;
        gap: 7px;
    }
    .card-text {
        font-size: 14px;
        line-height: 1.65;
        color: #4A4E52;
        margin: 0;
    }
    .story-quote {
        border-left: 3px solid #4A7C62;
        padding-left: 12px;
        margin: 10px 0;
        color: #3C4043;
        font-size: 13.5px;
        line-height: 1.6;
    }
    .doorlock-box {
        background-color: #F4F7F5;
        border: 1px dashed #4A7C62;
        border-radius: 10px;
        padding: 12px 14px;
        margin-top: 10px;
        font-size: 14px;
        color: #2E5A44;
    }
    .badge {
        display: inline-block;
        background-color: #F2EFE9;
        color: #8C5A3C;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 9px;
        border-radius: 20px;
        margin-bottom: 7px;
    }
    .map-btn {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #2E5A44;
        color: #FFFFFF !important;
        text-decoration: none;
        padding: 11px 0;
        border-radius: 12px;
        font-weight: 600;
        font-size: 14px;
        margin-top: 10px;
        transition: background-color 0.2s;
    }
    .map-btn:hover {
        background-color: #1E3F2F;
    }
    .map-btn-sub {
        background-color: #D1A489;
    }
    .map-btn-sub:hover {
        background-color: #B8896E;
    }

    /* 버튼 공통 스타일 */
    div.stButton > button {
        border-radius: 12px;
        font-weight: 600;
        font-size: 12.5px;
        padding: 8px 4px;
        border: 1px solid #DCD6CA;
        transition: all 0.15s;
        white-space: nowrap;
    }
    div.stButton > button[kind="primary"] {
        background-color: #2E5A44;
        color: #FFFFFF;
        border-color: #2E5A44;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #1E3F2F;
        border-color: #1E3F2F;
    }

    /* Expander(아코디언) 스타일 */
    div[data-testid="stExpander"] {
        background-color: #FFFFFF;
        border: 1px solid #E8E4DC;
        border-radius: 12px;
        margin-bottom: 8px;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.02);
    }
</style>
""", unsafe_allow_html=True)

# 3. 4개 국어 다국어 콘텐츠 사전
CONTENT = {
    "한국어": {
        "title": "mongle-stay",
        "subtitle": "6호선 안암역 도보 5분 · 서울 동대문 제기동 스테이",
        "hero_badge": "IN 15:00 · OUT 11:00",
        "tabs": ["🗺️ 오시는 길", "🔑 체크인", "🏡 스토리", "✨ 로컬·교통"],
        "next_to_checkin": "👉 다음 안내: 체크인 · 도어락 · Wi-Fi 보기",
        "next_to_story": "👉 다음 안내: 몽글스테이 스토리 & 객실 구조 보기",
        "next_to_local": "👉 다음 안내: 서울 권역별 교통 & 로컬 보기",
        "back_to_way": "🗺️ 처음으로 (숙소 오시는 길)",
        # TAXI CARD
        "taxi_tag": "🚖 택시 기사님께 이 화면을 보여주세요",
        "taxi_sub": "게스트 안내: 택시 이용 시 위 한국어 주소를 기사님께 그대로 보여주세요.",
        # TAB 1: 오시는 길
        "t2_loc_title": "📍 숙소 주소 및 지도 앱 열기",
        "t2_loc_body": (
            "<b>도로명 주소:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br>"
            "<b>영문 주소:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br>"
            "<b>가까운 역:</b> 지하철 6호선 <b>안암역(Anam Station) 3번 출구</b> 도보 5분<br>"
            "<b>가까운 버스정류장:</b> <b>안암오거리 · 고려대역(고대앞삼거리)</b> 도보 1~3분"
        ),
        "t2_btn_naver": "🟢 네이버 지도로 길찾기 (한국 내 가장 정확)",
        "t2_btn_google": "🗺️ Google Maps로 열기",
        "t2_sub_title": "🚉 지하철 6호선 안암역에서 오시는 법",
        "t2_sub_body": (
            "• <b>지하철 6호선 안암역(고대병원앞) 3번 출구</b>로 나오세요.<br>"
            "• 3번 출구에서 안암오거리·제기시장 방면으로 직진 후 <b>안암로18길</b> 골목으로 진입하시면 "
            "<b>도보 약 5분</b> 거리에 '고려맨션' 건물이 위치해 있습니다. (2층 203호)"
        ),
        "t2_air_title": "✈️ 공항에서 오시는 방법",
        "t2_air_body": (
            "<div style='background-color:#F4F7F5; border-left:3px solid #4A7C62; padding:10px 12px; "
            "margin-bottom:12px; border-radius:6px; font-size:13.5px;'>💳 <b>공항 출발 전 필수 팁:</b> "
            "입국장 편의점·자판기에서 <b>티머니(T-money)</b> 또는 <b>와우패스</b>를 먼저 구매해 충전하세요. "
            "<i>(※ 기후동행카드는 인천공항 구매·탑승 불가 → 다음 날 안암역 구매 추천)</i></div>"
            "<b>1. 인천국제공항 (ICN) 출발 (약 75~85분 소요)</b><br>"
            "• <b>공항철도 + 지하철 (추천):</b> 공항철도 탑승 ➔ <b>공덕역</b> 또는 <b>디지털미디어시티(DMC)역</b>에서 "
            "<b>6호선(신내 방면)</b> 환승 ➔ <b>안암역</b> 하차 (3번 출구 도보 5분)<br>"
            "• <b>공항리무진 버스:</b> 6002번 탑승 ➔ '제기동역.서울약령시' 하차 후 택시 기본요금 이동 (약 5분)<br><br>"
            "<b>2. 김포국제공항 (GMP) 출발 (약 55분 소요)</b><br>"
            "• 공항철도 탑승 ➔ <b>디지털미디어시티(DMC)역</b>에서 <b>6호선</b> 환승 ➔ <b>안암역</b> 하차"
        ),
        # TAB 2: 체크인 · 도어락 · Wi-Fi · 규칙 · 분리수거
        "t3_time_title": "⏰ 입·퇴실 및 현관 도어락 출입 안내",
        "t3_time_body": (
            "- <b>체크인 (Check-in):</b> 오후 3:00 (15:00) 이후 &nbsp;|&nbsp; <b>체크아웃:</b> 오전 11:00 이전<br>"
            "<div class='doorlock-box'>"
            "<b>🔐 현관 도어락 여는 법 (셀프 체크인)</b><br>"
            "1. 체크인 당일 예약 플랫폼 메시지로 발송된 <b>개별 비밀번호</b>를 확인해 주세요.<br>"
            "2. 별도의 터치 없이 바로 <b><code>*</code> + <code>비밀번호</code> + <code>*</code></b> 순서대로 누르시면 문이 열립니다.<br>"
            "<span style='font-size: 12.5px; color: #5F6368;'>※ 앞뒤로 별표(*)를 꼭 함께 눌러야 열리며, 닫히면 자동으로 잠깁니다.</span>"
            "</div>"
        ),
        "t3_wifi_title": "📶 초고속 무선 인터넷 연결",
        "t3_wifi_body": "원하시는 Wi-Fi와 비밀번호 우측의 복사 아이콘을 눌러 연결하세요.",
        "t3_wifi_ssid": "네트워크 이름 (SSID)",
        "t3_wifi_pw": "비밀번호 (5G · 2.4G 공통)",
        "t3_rules_title": "🌿 함께 지켜주세요 (House Rules)",
        "t3_rules_body": (
            "• <b>숙소 전체 금연:</b> 실내 및 건물 내 흡연(전자담배 포함) 절대 금지<br>"
            "• <b>실내화 착용:</b> 현관에서 신발을 벗고 비치된 실내화를 착용해 주세요.<br>"
            "• <b>정숙 시간 (22:00~07:00):</b> 복도·계단에서도 조용히 이동해 주시고, 밤 10시 이후 세탁기 사용은 자제해 주세요.<br>"
            "• <b>출입 및 요리:</b> 예약 인원 외 방문·숙박은 불가하며, 냄새가 강한 요리는 삼가주세요."
        ),
        "t3_trash_exp": "♻️ 쓰레기 분리수거 & 장기숙박 배출 안내 (사진 보기)",
        "t3_trash_body": (
            "한국은 쓰레기 분리수거가 엄격하며, 음식물과 일반 쓰레기를 섞어 버릴 경우 과태료가 부과됩니다.<br><br>"
            "<b>1. 실내 분리수거 방법</b><br>"
            "- <b>음식물 쓰레기:</b> 싱크대 위 <b>그린 컬러 전용통</b>에 버려주세요.<br>"
            "- <b>재활용품 (종이·비닐·캔·병·플라스틱):</b> 내용물을 깨끗이 비우고 헹군 뒤 냉장고 옆 <b>4단 분리수거함</b>에 종류별로 넣어주세요.<br>"
            "- <b>일반 쓰레기:</b> 그 외 일반 쓰레기(화장실 휴지 포함)는 <b>Trash 수거함</b>에 버려주세요.<br><br>"
            "<b>2. 장기 숙박(5박 이상) 및 수거함이 가득 찼을 때</b><br>"
            "- 여분 쓰레기봉투는 <b>싱크대 하부</b>에 준비되어 있습니다. (배출 요일: <b>화 · 목 · 일</b>)<br>"
            "- <b>음식물:</b> 노랑/초록 전용봉투(2ℓ·3ℓ) / <b>재활용:</b> 투명 비닐 그대로 / <b>일반:</b> 흰색 종량제 봉투(20ℓ·50ℓ)에 담아 묶은 뒤 "
            "<b>건물 앞 전봇대 밑</b>(아래 오른쪽 사진 파란 원 위치)에 놓아주세요."
        ),
        "t3_trash_cap1": "실내 4단 분리수거함 (냉장고 옆)",
        "t3_trash_cap2": "외부 배출 장소 (화·목·일 배출)",
        "t3_checkout_title": "✅ 체크아웃 전 10초 확인",
        "t3_checkout_body": "1. 사용한 식기 세척 및 정리 &nbsp; 2. 쓰레기 분리수거<br>3. 에어컨·보일러·조명 전원 끄기 &nbsp; 4. 창문 및 현관문 잠금 확인 &nbsp; 5. 잊은 물건 확인",
        "t3_contact_title": "🐶 호스트 긴급 연락처",
        "t3_contact_body": (
            "머무시는 동안 도움이 필요하시면 언제든 편하게 연락해 주세요.<br>"
            "• <b>예약 플랫폼 메시지:</b> 에어비앤비 / 트립닷컴 / 부킹닷컴 앱 내 채팅 (가장 빠름)<br>"
            "• <b>메신저 문의:</b> WeChat: <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>"
        ),
        # TAB 3: 스토리 & 공간 안내
        "t1_story_title": "🎨 Mongle Stay Story (Curated by miel Yi)",
        "t1_story_body": (
            "몽글스테이는 서로 다른 나라와 도시에서 온 여행자들이 서울의 일상을 편안하게 경험할 수 있도록 만든 집입니다. "
            "좋아하는 음악과 문화는 달라도, 여행지에서 느끼는 설렘과 새로운 이야기를 발견하는 기쁨은 서로 닮아 있습니다. "
            "몽글스테이에 머무는 시간이 단순한 숙박을 넘어, 자신만의 서울 취향과 기억을 발견하는 시간이 되기를 바랍니다."
            "<div class='story-quote'>"
            "<b>• 취향:</b> 각기 다른 색과 분위기를 가진 공간에서 나에게 가장 편안한 방식으로 머물러보세요.<br>"
            "<b>• 연결:</b> K컬처와 안암의 일상, 서울의 오래된 시장과 새로운 문화를 함께 만나보세요.<br>"
            "<b>• 안심:</b> 낯선 도시에서도 내 집처럼 편안하게 머물 수 있도록 깨끗한 공간과 세심한 안내를 준비했습니다."
            "</div>"
        ),
        "t1_rooms_title": "🛏️ 세 개의 방 이야기 & 인원별 객실 안내",
        "t1_rooms_body": (
            "- <b>Palette Room:</b> 서로 다른 색과 취향이 자연스럽게 어우러지는 방<br>"
            "- <b>Amber Room:</b> 따뜻한 빛처럼 편안하게 하루를 마무리하는 방<br>"
            "- <b>Cozy Room:</b> 작지만 온전히 나만의 시간을 보낼 수 있는 아늑한 방<br><br>"
            "<span style='font-size: 13.5px; color: #8C5A3C;'>※ <b>인원별 객실 세팅 안내:</b> 예약 인원에 맞춰 객실이 준비됩니다.<br>"
            "&nbsp;&nbsp;- <b>4인 이하:</b> 침실 2개 개방 (Palette Room / Amber Room)<br>"
            "&nbsp;&nbsp;- <b>5인 이상:</b> 침실 3개 전체 개방 (Palette / Amber / Cozy Room)</span>"
        ),
        "t1_floorplan_caption": "📐 몽글스테이 3D 공간 구조 및 객실 배치도",
        # TAB 4: 로컬 명소 & 권역별 버스·지하철(아코디언) & 교통카드
        "t4_walk_title": "☕ 도보권 로컬 산책 & 시장 투어 (안암 · 제기)",
        "t4_walk_body": (
            "<b>1. 고려대학교 캠퍼스 & 안암동 대학가 맛집 (도보 5~10분)</b><br>"
            "• 유럽 고딕 양식의 석조 캠퍼스 산책과 가성비 좋은 대학가 로컬 맛집·카페 거리를 도보로 즐겨보세요.<br><br>"
            "<b>2. 스타벅스 경동1960점 & 경동시장·서울약령시 (도보 12~15분)</b><br>"
            "• 1960년대 폐극장을 개조한 압도적 분위기의 스타벅스 스페셜 매장과, 활기찬 한국 전통시장 먹거리 투어를 추천합니다.<br><br>"
            "<b>3. 성북천 산책로 (도보 8분)</b><br>"
            "• 저녁 식사 후 조명이 예쁘게 켜진 성북천 물길을 따라 여유롭게 산책해 보세요."
        ),
        "t4_city_title": "🚌 서울 5대 권역별 추천 교통 (집 앞 버스 · 지하철)",
        "t4_city_intro": "숙소 도보 1~3분 거리의 <b>안암오거리 · 고려대역(고대앞삼거리)</b> 정류장에서 환승 없이 이동할 수 있습니다. 권역을 눌러 확인하세요:",
        "t4_areas": [
            ("🏯 1. 동대문 · 종로 · 고궁권 (약 10~20분)", "<b>주요 스팟:</b> DDP, 광장시장, 익선동, 경복궁<br>• <b>버스 (직통):</b> <code>101</code> · <code>144</code> · <code>273</code> · <code>111</code>번 (안암오거리 정류장)<br>• <b>지하철:</b> 6호선 안암역 ➔ 동묘앞역(1호선 환승)"),
            ("🍷 2. 한남동 · 이태원 · 용산권 (약 20~30분)", "<b>주요 스팟:</b> 한남 카페거리, 이태원, 해방촌<br>• <b>버스 (직통):</b> <b><code>110A</code>번</b> (고려대역·고대앞삼거리 탑승) ➔ 한강진역·이태원역·녹사평역 직통<br>&nbsp;&nbsp;<span style='font-size:13px; color:#8C5A3C;'>(※ 숙소 복귀 시 반대방향 <b><code>110B</code>번</b> 탑승!)</span><br>• <b>지하철 (직통):</b> 6호선 안암역 ➔ 한강진역·이태원역 환승 없이 직통"),
            ("🎨 3. 성수 · 서울숲권 (약 15~20분)", "<b>주요 스팟:</b> 성수동 팝업·카페거리, 서울숲<br>• <b>버스 (직통):</b> <code>121</code>번 (고려대역·고대앞삼거리 탑승) ➔ 서울숲·성수 방면<br>• <b>지하철:</b> 6호선 안암역 ➔ 신당역(2호선 환승) ➔ 성수역"),
            ("🎸 4. 홍대 · 연남동 · 망원권 (약 30~35분)", "<b>주요 스팟:</b> 홍대, 연트럴파크, 망원시장<br>• <b>지하철 (추천·직통):</b> 6호선 안암역 ➔ 망원역·합정역 환승 없이 직통<br>• <b>버스 (직통):</b> <code>110A</code>번 ➔ 신촌·동교동삼거리(연남동)까지 한 번에 연결"),
            ("🏙️ 5. 명동 · 남산 · 강남권 (약 25~40분)", "<b>주요 스팟:</b> 명동, N서울타워, 가로수길, 강남역<br>• <b>명동·남산:</b> 6호선 안암역 ➔ 약수역(3호선 환승) ➔ 충무로역<br>• <b>강남·신사:</b> <code>144</code>번 버스 (신사역·강남역 직통)")
        ],
        "t4_trans_title": "💳 교통카드 3종 선택법 (공항 구매 팁 포함)",
        "t4_trans_body": (
            "- <b>1. 티머니 (T-money) — 공항 도착 즉시 구매 추천!</b><br>"
            "&nbsp;&nbsp;인천공항 편의점·지하철 자판기에서 구매 후 현금 충전합니다. 공항철도·리무진 버스(6002번)·택시까지 모두 사용 가능하며, "
            "<b>버스 하차 시 뒷문 단말기에 한 번 더 태그</b>해야 30분 무료 환승이 적용됩니다.<br><br>"
            "- <b>2. 와우패스 (WOWPASS) — 환전 + 쇼핑결제 + 교통카드 올인원</b><br>"
            "&nbsp;&nbsp;공항·주요역 무인기계에서 외화를 바로 원화로 충전해 식당·매장 결제와 티머니 교통기능을 함께 씁니다. "
            "<i>(※ 교통 잔액은 지하철역 충전기에서 원화 현금으로 별도 충전)</i><br><br>"
            "- <b>3. 기후동행카드 (Climate Card) — 서울 무제한 패스</b><br>"
            "&nbsp;&nbsp;1일권(5,000원)~5일권(15,000원)으로 서울 지하철·버스 무제한 이용!<br>"
            "&nbsp;&nbsp;<span style='font-size:13px; color:#8C5A3C;'>⚠️ <b>중요:</b> 인천공항에서는 구매·탑승이 불가합니다. "
            "공항에서는 티머니로 오신 뒤, 다음 날 <b>6호선 안암역(고객안전실·충전기·편의점)</b>에서 구매해 충전하세요!</span>"
        )
    },
    "English": {
        "title": "mongle-stay",
        "subtitle": "5-min walk from Anam Stn (Line 6) · Cozy Local Stay in Seoul",
        "hero_badge": "IN 15:00 · OUT 11:00",
        "tabs": ["🗺️ Directions", "🔑 Check-in", "🏡 Story", "✨ Transit"],
        "next_to_checkin": "👉 Next: Check-in · Door Lock · Wi-Fi",
        "next_to_story": "👉 Next: Mongle Stay Story & Room Layout",
        "next_to_local": "👉 Next: Seoul Area Transit & Local Gems",
        "back_to_way": "🗺️ Back to Start (Directions)",
        "taxi_tag": "🚖 SHOW THIS TO YOUR TAXI DRIVER",
        "taxi_sub": "Tip: Show the large Korean address above directly to your taxi driver.",
        "t2_loc_title": "📍 Address & Navigation",
        "t2_loc_body": (
            "<b>English Address:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br>"
            "<b>Korean Address:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br>"
            "<b>Nearest Subway:</b> <b>Anam Station (Line 6), Exit 3</b> (5-minute walk)<br>"
            "<b>Nearest Bus Stops:</b> <b>Anam Ogeori / Korea Univ. Stn</b> (1–3 min walk)"
        ),
        "t2_btn_naver": "🟢 Open in Naver Map (Most Accurate in Korea)",
        "t2_btn_google": "🗺️ Open in Google Maps",
        "t2_sub_title": "🚉 From Anam Station (Subway Line 6)",
        "t2_sub_body": (
            "• Come out of <b>Anam Station (Line 6), Exit 3</b>.<br>"
            "• Walk straight toward Anam Ogeori / Jegi Market and turn into the <b>Anam-ro 18-gil</b> alley. "
            "You will find <b>'Goryeo Mansion'</b> within a <b>5-minute walk</b> (2nd floor, Room 203)."
        ),
        "t2_air_title": "✈️ From the Airport",
        "t2_air_body": (
            "<div style='background-color:#F4F7F5; border-left:3px solid #4A7C62; padding:10px 12px; "
            "margin-bottom:12px; border-radius:6px; font-size:13.5px;'>💳 <b>Before Leaving the Airport:</b> "
            "Buy & top up a <b>T-money</b> or <b>WOWPASS</b> card at airport convenience stores/vending machines first. "
            "<i>(※ Climate Card cannot be bought or used at Incheon Airport — buy it at Anam Stn the next day.)</i></div>"
            "<b>1. From Incheon Int'l Airport (ICN) (~75–85 mins)</b><br>"
            "• <b>AREX Train + Subway (Recommended):</b> Take AREX All-stop train ➔ Transfer at <b>Gongdeok</b> or <b>Digital Media City (DMC)</b> "
            "to <b>Line 6 (Sinnae bound)</b> ➔ Get off at <b>Anam Station</b> (Exit 3, 5-min walk).<br>"
            "• <b>Airport Limousine Bus:</b> Take Bus #6002 ➔ Get off at 'Jegi-dong Station / Seoul Yangnyeongsi' ➔ 5-min taxi ride.<br><br>"
            "<b>2. From Gimpo Int'l Airport (GMP) (~55 mins)</b><br>"
            "• Take AREX train ➔ Transfer at <b>DMC Station</b> to <b>Line 6</b> ➔ Get off at <b>Anam Station</b>."
        ),
        "t3_time_title": "⏰ Check-in, Check-out & Door Lock Guide",
        "t3_time_body": (
            "- <b>Check-in:</b> After 3:00 PM (15:00) &nbsp;|&nbsp; <b>Check-out:</b> Before 11:00 AM (11:00)<br>"
            "<div class='doorlock-box'>"
            "<b>🔐 How to Unlock the Front Door (Self Check-in)</b><br>"
            "1. Check your <b>unique passcode</b> sent via booking platform message on your check-in day.<br>"
            "2. Simply press <b><code>*</code> + <code>Passcode</code> + <code>*</code></b> directly (no need to wake the screen first) to unlock.<br>"
            "<span style='font-size: 12.5px; color: #5F6368;'>※ You must press the asterisk (*) both before and after the passcode. The door locks automatically when closed.</span>"
            "</div>"
        ),
        "t3_wifi_title": "📶 Free High-Speed Wi-Fi",
        "t3_wifi_body": "Tap the copy icon next to your preferred Wi-Fi and password to connect.",
        "t3_wifi_ssid": "Network Name (SSID)",
        "t3_wifi_pw": "Password (Shared for 5G & 2.4G)",
        "t3_rules_title": "🌿 House Rules",
        "t3_rules_body": (
            "• <b>No Smoking:</b> Strictly prohibited inside the room and building (including e-cigarettes).<br>"
            "• <b>Shoes Off Indoors:</b> Please take off your shoes at the entrance and wear the provided slippers.<br>"
            "• <b>Quiet Hours (22:00–07:00):</b> Please walk quietly in hallways/stairs and avoid using the washing machine after 10 PM.<br>"
            "• <b>Visitors & Cooking:</b> Unregistered guests are not allowed, and please avoid strong-smelling cooking."
        ),
        "t3_trash_exp": "♻️ Trash Sorting & Long-Stay Disposal Guide (View Photos)",
        "t3_trash_body": (
            "Korea enforces strict waste sorting; mixing food waste with general trash incurs fines.<br><br>"
            "<b>1. Indoor Sorting</b><br>"
            "- <b>Food Waste:</b> Dispose in the <b>green bin</b> on the kitchen sink.<br>"
            "- <b>Recycling (Paper, Vinyl, Cans, Glass, Plastic):</b> Rinse clean and place in the <b>4-tier recycling bin</b> next to the fridge.<br>"
            "- <b>General Waste:</b> Put other general trash (including bathroom tissue) in the <b>Trash bin</b>.<br><br>"
            "<b>2. Long Stays (5+ Nights) & When Bins Are Full</b><br>"
            "- Extra trash bags are stored <b>under the sink</b>. (Collection days: <b>Tue · Thu · Sun</b>)<br>"
            "- Tie bags securely—<b>Food:</b> Yellow/Green bag (2L/3L), <b>Recycling:</b> Clear bag as-is, <b>General:</b> White volume-rate bag (20L/50L)—"
            "and place them <b>under the utility pole in front of the building</b> (blue circle in the right photo)."
        ),
        "t3_trash_cap1": "Indoor 4-Tier Recycling Bin (Next to Fridge)",
        "t3_trash_cap2": "Outdoor Drop-off Spot (Tue · Thu · Sun)",
        "t3_checkout_title": "✅ 10-Second Check-out Checklist",
        "t3_checkout_body": "1. Wash & put away used dishes &nbsp; 2. Sort trash properly<br>3. Turn off A/C, heater & lights &nbsp; 4. Close windows & lock front door &nbsp; 5. Check for left items",
        "t3_contact_title": "🐶 Host Contact",
        "t3_contact_body": (
            "Feel free to reach out anytime if you need assistance during your stay.<br>"
            "• <b>Booking Platform Chat:</b> Airbnb / Trip.com / Booking.com in-app message (Fastest)<br>"
            "• <b>Messenger ID:</b> WeChat: <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>"
        ),
        "t1_story_title": "🎨 Mongle Stay Story (Curated by miel Yi)",
        "t1_story_body": (
            "Mongle Stay is a home created so travelers from different countries and cities can comfortably experience everyday life in Seoul. "
            "Even if our favorite music and cultures differ, the excitement of traveling and the joy of discovering new stories connect us all. "
            "We hope your time here goes beyond a simple stay—becoming a moment to discover your own taste and memories of Seoul."
            "<div class='story-quote'>"
            "<b>• Taste:</b> Stay in the way that feels most comfortable to you, surrounded by spaces of distinct colors and moods.<br>"
            "<b>• Connection:</b> Experience K-culture alongside the daily rhythm of Anam, where Seoul's historic markets meet new culture.<br>"
            "<b>• Peace of Mind:</b> We prepared a spotless home and thoughtful guidance so you feel right at home in an unfamiliar city."
            "</div>"
        ),
        "t1_rooms_title": "🛏️ Story of Three Rooms & Room Setup",
        "t1_rooms_body": (
            "- <b>Palette Room:</b> A room where different colors and personal tastes naturally blend together<br>"
            "- <b>Amber Room:</b> A room to unwind and end your day peacefully, like a warm glow<br>"
            "- <b>Cozy Room:</b> A snug, intimate room where you can enjoy quiet time all to yourself<br><br>"
            "<span style='font-size: 13.5px; color: #8C5A3C;'>※ <b>Room Setup by Guest Count:</b> Rooms are prepared according to your reservation.<br>"
            "&nbsp;&nbsp;- <b>1–4 Guests:</b> 2 Bedrooms open (Palette Room / Amber Room)<br>"
            "&nbsp;&nbsp;- <b>5+ Guests:</b> All 3 Bedrooms open (Palette / Amber / Cozy Room)</span>"
        ),
        "t1_floorplan_caption": "📐 Mongle Stay 3D Floor Plan & Room Layout",
        "t4_walk_title": "☕ Walking Distance Gems (Anam & Jegi)",
        "t4_walk_body": (
            "<b>1. Korea University Campus & Anam Food Street (5–10 min walk)</b><br>"
            "• Stroll through the European Gothic stone architecture of Korea University and enjoy affordable local student eateries and cafes.<br><br>"
            "<b>2. Starbucks Gyeongdong 1960 & Gyeongdong Market (12–15 min walk)</b><br>"
            "• Visit the viral Starbucks built inside an abandoned 1960s theater, right inside Seoul's largest traditional herbal & food market.<br><br>"
            "<b>3. Seongbukcheon Stream Trail (8-min walk)</b><br>"
            "• Enjoy a peaceful evening walk along the illuminated waterside path."
        ),
        "t4_city_title": "🚌 Seoul Transit by Area (Direct Buses & Subway)",
        "t4_city_intro": "Bus stops (<b>Anam Ogeori / Korea Univ. Stn</b>) are <b>1–3 mins away on foot</b>. Tap each area to see direct routes:",
        "t4_areas": [
            ("🏯 1. Dongdaemun · Jongno · Palaces (~10–20 mins)", "<b>Spots:</b> DDP, Gwangjang Market, Ikseon-dong, Gyeongbokgung<br>• <b>Direct Bus:</b> <code>101</code> · <code>144</code> · <code>273</code> · <code>111</code> (at Anam Ogeori stop)<br>• <b>Subway:</b> Line 6 Anam Stn ➔ Transfer at Dongmyo Stn (Line 1)"),
            ("🍷 2. Hannam-dong · Itaewon · Yongsan (~20–30 mins)", "<b>Spots:</b> Hannam Cafes, Itaewon, Haebangchon<br>• <b>Direct Bus:</b> <b><code>110A</code></b> (at Korea Univ. Stn stop) ➔ Direct to Hangangjin, Itaewon & Noksapyeong<br>&nbsp;&nbsp;<span style='font-size:13px; color:#8C5A3C;'>(※ Take <b><code>110B</code></b> when returning!)</span><br>• <b>Direct Subway:</b> Line 6 Anam Stn ➔ Hangangjin / Itaewon Stn (No transfer)"),
            ("🎨 3. Seongsu · Seoul Forest (~15–20 mins)", "<b>Spots:</b> Seongsu Pop-ups & Cafes, Seoul Forest<br>• <b>Direct Bus:</b> <code>121</code> (at Korea Univ. Stn stop) ➔ Seoul Forest & Seongsu<br>• <b>Subway:</b> Line 6 Anam Stn ➔ Transfer at Sindang Stn (Line 2) ➔ Seongsu Stn"),
            ("🎸 4. Hongdae · Yeonnam-dong · Mangwon (~30–35 mins)", "<b>Spots:</b> Hongdae, Yeontral Park, Mangwon Market<br>• <b>Direct Subway (Recommended):</b> Line 6 Anam Stn ➔ Mangwon / Hapjeong Stn (No transfer)<br>• <b>Direct Bus:</b> <code>110A</code> ➔ Direct to Sinchon & Yeonnam-dong"),
            ("🏙️ 5. Myeongdong · Namsan · Gangnam (~25–40 mins)", "<b>Spots:</b> Myeongdong, N Seoul Tower, Garosu-gil, Gangnam<br>• <b>Myeongdong/Namsan:</b> Line 6 ➔ Transfer at Yaksu Stn (Line 3) ➔ Chungmuro Stn<br>• <b>Gangnam/Sinsa:</b> Direct Bus <code>144</code> to Sinsa & Gangnam Stn")
        ],
        "t4_trans_title": "💳 Choosing Your Transit Card (Airport Tips)",
        "t4_trans_body": (
            "- <b>1. T-money — Best to Buy Right at Incheon Airport!</b><br>"
            "&nbsp;&nbsp;Buy & top up with cash at airport convenience stores or AREX vending machines. Works on airport trains, Limousine Bus #6002, "
            "subways, buses & taxis. <b>Always tap again when exiting a bus</b> for free 30-min transfers!<br><br>"
            "- <b>2. WOWPASS — Currency Exchange + Shopping + Transit All-in-One</b><br>"
            "&nbsp;&nbsp;Top up with foreign cash at airport/subway kiosks to pay at stores and ride transit. "
            "<i>(※ Top up T-money transit balance separately in KRW cash at subway ticket machines.)</i><br><br>"
            "- <b>3. Climate Card — Unlimited Seoul Transit Pass</b><br>"
            "&nbsp;&nbsp;1-Day (5,000 KRW) to 5-Day (15,000 KRW) unlimited rides on Seoul subways & buses!<br>"
            "&nbsp;&nbsp;<span style='font-size:13px; color:#8C5A3C;'>⚠️ <b>Note:</b> Cannot be bought or used to board at Incheon Airport. "
            "Use T-money from the airport, then buy & charge a Climate Card at <b>Anam Station (Line 6)</b> the next day!</span>"
        )
    },
    "日本語": {
        "title": "mongle-stay",
        "subtitle": "地下鉄6号線「安岩(アナム)駅」徒歩5分 · ローカル感性あふれる空間",
        "hero_badge": "IN 15:00 · OUT 11:00",
        "tabs": ["🗺️ アクセス", "🔑 チェックイン", "🏡 ストーリー", "✨ 周辺·交通"],
        "next_to_checkin": "👉 次へ：チェックイン・ドアロック・Wi-Fi",
        "next_to_story": "👉 次へ：モングルステイ物語＆お部屋案内",
        "next_to_local": "👉 次へ：エリア別交通＆周辺スポット",
        "back_to_way": "🗺️ 最初に戻る（宿へのアクセス方法）",
        "taxi_tag": "🚖 タクシー運転手さんにこの画面を見せてください",
        "taxi_sub": "ご案内：タクシーに乗車する際は、上の韓国語住所をそのまま運転手さんにお見せください。",
        "t2_loc_title": "📍 住所および地図アプリを開く",
        "t2_loc_body": (
            "<b>韓国語住所:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br>"
            "<b>英語住所:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br>"
            "<b>最寄り駅:</b> 地下鉄6号線 <b>安岩(アナム)駅 3番出口</b> 徒歩5分<br>"
            "<b>最寄りバス停:</b> <b>安岩五叉路(안암오거리) · 高麗大駅(고려대역)</b> 徒歩1〜3分"
        ),
        "t2_btn_naver": "🟢 NAVERマップでルート検索（韓国で最も正確）",
        "t2_btn_google": "🗺️ Google マップで開く",
        "t2_sub_title": "🚉 地下鉄6号線「安岩駅」からの行き方",
        "t2_sub_body": (
            "• <b>地下鉄6号線 安岩(アナム)駅 3番出口</b>を出ます。<br>"
            "• 3番出口から安岩五叉路・祭基市場方面へ直進し、<b>安岩路18ギル(안암로18길)</b>の路地に入ると"
            "<b>徒歩約5分</b>で「高麗マンション(고려맨션)」に到着します。（2階 203号室）"
        ),
        "t2_air_title": "✈️ 空港からのアクセス",
        "t2_air_body": (
            "<div style='background-color:#F4F7F5; border-left:3px solid #4A7C62; padding:10px 12px; "
            "margin-bottom:12px; border-radius:6px; font-size:13.5px;'>💳 <b>空港出発前の必須ヒント:</b> "
            "到着ロビーのコンビニや券売機で<b>T-money</b>または<b>WOWPASS</b>を先に購入・チャージしてください。"
            "<i>(※ 気候同行カードは仁川空港での購入・乗車不可 → 翌日に安岩駅での購入がおすすめです)</i></div>"
            "<b>1. 仁川国際空港 (ICN) から（約75〜85分）</b><br>"
            "• <b>空港鉄道 + 地下鉄（おすすめ）:</b> 空港鉄道(一般列車)に乗車 ➔ <b>孔徳(コンドク)駅</b> または <b>デジタルメディアシティ(DMC)駅</b>で"
            "<b>6号線(新内方面)</b>に乗換 ➔ <b>安岩(アナム)駅</b>下車（3番出口 徒歩5分）<br>"
            "• <b>空港リムジンバス:</b> 6002番バス乗車 ➔「祭基洞駅・ソウル薬令市」下車後、タクシーで初乗り距離（約5分）<br><br>"
            "<b>2. 金浦国際空港 (GMP) から（約55分）</b><br>"
            "• 空港鉄道に乗車 ➔ <b>DMC駅</b>で<b>6号線</b>に乗換 ➔ <b>安岩駅</b>下車"
        ),
        "t3_time_title": "⏰ チェックイン・チェックアウト＆ドアロック案内",
        "t3_time_body": (
            "- <b>チェックイン:</b> 15:00以降 &nbsp;|&nbsp; <b>チェックアウト:</b> 11:00まで<br>"
            "<div class='doorlock-box'>"
            "<b>🔐 玄関ドアロックの開け方（セルフチェックイン）</b><br>"
            "1. チェックイン当日に予約サイトのメッセージでお送りする<b>個別暗証番号</b>をご確認ください。<br>"
            "2. 事前のタッチなしでそのまま <b><code>*</code> + <code>暗証番号</code> + <code>*</code></b> の順に押すと解錠されます。<br>"
            "<span style='font-size: 12.5px; color: #5F6368;'>※ 前後両方にアスタリスク(*)を押してください。ドアが閉まると自動で施錠されます。</span>"
            "</div>"
        ),
        "t3_wifi_title": "📶 無料高速Wi-Fi",
        "t3_wifi_body": "ご希望のWi-Fiとパスワード右側のコピーアイコンを押して接続してください。",
        "t3_wifi_ssid": "ネットワーク名 (SSID)",
        "t3_wifi_pw": "パスワード（5G・2.4G共通）",
        "t3_rules_title": "🌿 快適にお過ごしいただくためのお願い (House Rules)",
        "t3_rules_body": (
            "• <b>室内完全禁煙:</b> 建物全体および客室内での喫煙（電子タバコ含む）は厳禁です。<br>"
            "• <b>室内履き着用:</b> 玄関で靴を脱ぎ、備え付けのスリッパをご利用ください。<br>"
            "• <b>お静かに (22:00〜07:00):</b> 廊下・階段でも静かに移動し、22時以降の洗濯機使用はお控えください。<br>"
            "• <b>入室・調理制限:</b> 予約人数以外の訪問・宿泊は禁止です。匂いの強い調理はご遠慮ください。"
        ),
        "t3_trash_exp": "♻️ ゴミの分別＆長期滞在時のゴミ出し案内（写真を見る）",
        "t3_trash_body": (
            "韓国ではゴミの分別が厳格で、生ゴミと一般ゴミを混ぜると罰金の対象となります。<br><br>"
            "<b>1. 室内の分別方法</b><br>"
            "- <b>生ゴミ:</b> シンク上の<b>グリーン色の専用容器</b>に入れてください。<br>"
            "- <b>資源ゴミ（紙・ビニール・缶・瓶・プラスチック）:</b> 中身を洗ってから冷蔵庫横の<b>4段分別ゴミ箱</b>へ種類別に入れてください。<br>"
            "- <b>一般ゴミ:</b> その他の一般ゴミ（トイレの紙を含む）は <b>Trash ゴミ箱</b>へ捨ててください。<br><br>"
            "<b>2. 長期滞在（5泊以上）＆ゴミ箱がいっぱいになった場合</b><br>"
            "- 予備のゴミ袋は<b>シンク下</b>にございます。（ゴミ出し曜日：<b>火・木・日</b>）<br>"
            "- <b>生ゴミ:</b> 黄色/緑の専用袋(2ℓ・3ℓ) / <b>資源ゴミ:</b> 透明袋のまま / <b>一般ゴミ:</b> 白色の従量制袋(20ℓ・50ℓ)に入れて口を縛り、"
            "<b>建物前の電柱の下</b>（右写真の青い丸の場所）に出してください。"
        ),
        "t3_trash_cap1": "室内4段分別ゴミ箱（冷蔵庫横）",
        "t3_trash_cap2": "屋外ゴミ出し場所（火・木・日）",
        "t3_checkout_title": "✅ チェックアウト前の10秒確認",
        "t3_checkout_body": "1. 使用した食器の洗浄・整理 &nbsp; 2. ゴミの分別<br>3. エアコン・暖房・照明の電源オフ &nbsp; 4. 窓と玄関ドアの施錠確認 &nbsp; 5. 忘れ物チェック",
        "t3_contact_title": "🐶 ホスト連絡先",
        "t3_contact_body": (
            "ご滞在中に何かお困りの際は、いつでもお気軽にご連絡ください。<br>"
            "• <b>予約サイトメッセージ:</b> Airbnb / Trip.com / Booking.com アプリ内チャット（最速）<br>"
            "• <b>メッセンジャーID:</b> LINE: <code>mongle-stay</code> / WeChat: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>"
        ),
        "t1_story_title": "🎨 Mongle Stay Story (Curated by miel Yi)",
        "t1_story_body": (
            "モングルステイは、異なる国や都市から訪れた旅人たちがソウルの日常を心地よく体験できるようにつくられた家です。"
            "好きな音楽や文化は違っても、旅先で感じるときめきや新しい物語に出会う喜びは同じです。"
            "ここでの滞在が単なる宿泊を超え、あなただけのソウルの好みと記憶を見つける時間になることを願っています。"
            "<div class='story-quote'>"
            "<b>• 好み (Taste):</b> それぞれ異なる色と雰囲気を持つ空間で、自分にとって一番心地よいスタイルでお過ごしください。<br>"
            "<b>• つながり (Connection):</b> Kカルチャーと安岩の日常、ソウルの歴史ある伝統市場と新しい文化を一緒に体験してください。<br>"
            "<b>• 安心 (Peace of Mind):</b> 見知らぬ街でも自宅のようにリラックスできるよう、清潔な空間と丁寧なご案内を用意しました。"
            "</div>"
        ),
        "t1_rooms_title": "🛏️ 3つのお部屋の物語＆人数別のお部屋案内",
        "t1_rooms_body": (
            "- <b>Palette Room:</b> 異なる色と好みが自然に調和するお部屋<br>"
            "- <b>Amber Room:</b> 温かい光のように穏やかに一日を締めくくるお部屋<br>"
            "- <b>Cozy Room:</b> コンパクトながらも自分だけの時間をゆっくり過ごせる居心地の良いお部屋<br><br>"
            "<span style='font-size: 13.5px; color: #8C5A3C;'>※ <b>人数別のお部屋セッティング:</b> ご予約人数に合わせてお部屋をご用意いたします。<br>"
            "&nbsp;&nbsp;- <b>4名以下:</b> 寝室2部屋開放 (Palette Room / Amber Room)<br>"
            "&nbsp;&nbsp;- <b>5名以上:</b> 寝室3部屋すべて開放 (Palette / Amber / Cozy Room)</span>"
        ),
        "t1_floorplan_caption": "📐 モングルステイ 3D間取り図・お部屋レイアウト",
        "t4_walk_title": "☕ 徒歩圏内のローカル散策＆市場（安岩・祭基）",
        "t4_walk_body": (
            "<b>1. 高麗大学キャンパス＆安岩グルメ通り（徒歩5〜10分）</b><br>"
            "• ヨーロッパのゴシック建築のような美しい石造りのキャンパス散策や、コスパ抜群のローカルグルメ・カフェ通りをお楽しみください。<br><br>"
            "<b>2. スターバックス京東1960店＆京東市場・ソウル薬令市（徒歩12〜15分）</b><br>"
            "• 1960年代の廃劇場をリノベーションした話題のスターバックスと、活気あふれる韓国最大級の伝統市場の食べ歩きがおすすめです。<br><br>"
            "<b>3. 城北川(ソンブクチョン)散策路（徒歩8分）</b><br>"
            "• 夕食後、ライトアップされた川辺の遊歩道をゆったりお散歩してみてください。"
        ),
        "t4_city_title": "🚌 ソウル5大エリア別おすすめ交通（徒歩1〜3分バス停・地下鉄）",
        "t4_city_intro": "宿から徒歩1〜3分の<b>安岩五叉路・高麗大駅</b>バス停から主要観光地へ直通できます。エリアをタップして確認：",
        "t4_areas": [
            ("🏯 1. 東大門・鍾路・古宮エリア（約10〜20分）", "<b>スポット:</b> DDP、広蔵市場、益善洞、景福宮<br>• <b>直通バス:</b> <code>101</code> · <code>144</code> · <code>273</code> · <code>111</code>番（安岩五叉路バス停）<br>• <b>地下鉄:</b> 6号線 安岩駅 ➔ 東廟前駅で1号線に乗換"),
            ("🍷 2. 漢南洞・梨泰院・龍山エリア（約20〜30分）", "<b>スポット:</b> 漢南カフェ通り、梨泰院、解放村<br>• <b>直通バス:</b> <b><code>110A</code>番</b>（高麗大駅バス停）➔ 漢江鎮駅・梨泰院駅・緑莎坪駅へ直通<br>&nbsp;&nbsp;<span style='font-size:13px; color:#8C5A3C;'>(※ 帰りは反対方向の<b><code>110B</code>番</b>に乗車！)</span><br>• <b>直通地下鉄:</b> 6号線 安岩駅 ➔ 漢江鎮駅・梨泰院駅（乗換なし）"),
            ("🎨 3. 聖水(ソンス)・ソウルの森エリア（約15〜20分）", "<b>スポット:</b> 聖水洞カフェ通り、ソウルの森<br>• <b>直通バス:</b> <code>121</code>番（高麗大駅バス停）➔ ソウルの森・聖水方面<br>• <b>地下鉄:</b> 6号線 安岩駅 ➔ 新堂駅(2号線乗換) ➔ 聖水駅"),
            ("🎸 4. 弘大(ホンデ)・延南洞・望遠エリア（約30〜35分）", "<b>スポット:</b> 弘大、延南洞、望遠市場<br>• <b>直通地下鉄（おすすめ）:</b> 6号線 安岩駅 ➔ 望遠駅・合井駅（乗換なし）<br>• <b>直通バス:</b> <code>110A</code>番 ➔ 新村・延南洞まで一本で直通"),
            ("🏙️ 5. 明洞・南山・江南エリア（約25〜40分）", "<b>スポット:</b> 明洞、Nソウルタワー、カロスキル、江南駅<br>• <b>明洞・南山:</b> 6号線 ➔ 薬水駅(3号線乗換) ➔ 忠武路駅<br>• <b>江南・新沙:</b> 直通バス <code>144</code>番（新沙駅・江南駅へ直通）")
        ],
        "t4_trans_title": "💳 交通カード3種の選び方（空港購入ガイド）",
        "t4_trans_body": (
            "- <b>1. T-money（ティーマネー）— 仁川空港到着後すぐの購入がおすすめ！</b><br>"
            "&nbsp;&nbsp;空港のコンビニや空港鉄道の券売機で現金購入・チャージ可能。空港鉄道・リムジンバス(6002番)・地下鉄・バス・タクシーすべてに使えます。"
            "<b>バス降車時は必ず後部ドアの端末にタッチ</b>してください（30分以内無料乗換）。<br><br>"
            "- <b>2. WOWPASS（ワウパス）— 両替＋お店決済＋交通カード一体型</b><br>"
            "&nbsp;&nbsp;空港や主要駅の専用機で日本円をそのままチャージし、飲食店でのカード決済とT-money交通機能が使えます。"
            "<i>(※ 交通残高は地下鉄駅の券売機でウォン現金にて別途チャージ)</i><br><br>"
            "- <b>3. 気候同行カード（Climate Card）— ソウル乗り放題パス</b><br>"
            "&nbsp;&nbsp;1日券(5,000ウォン)〜5日券(15,000ウォン)でソウル市内の地下鉄・バスが乗り放題！<br>"
            "&nbsp;&nbsp;<span style='font-size:13px; color:#8C5A3C;'>⚠️ <b>注意:</b> 仁川空港では購入・乗車ができません。"
            "空港からはT-moneyでお越しいただき、翌日に<b>6号線「安岩駅」</b>で購入・チャージするのが最もお得です！</span>"
        )
    },
    "中文": {
        "title": "mongle-stay",
        "subtitle": "地铁6号线安岩站步行5分钟 · 感受首尔本地烟火气的温馨居所",
        "hero_badge": "IN 15:00 · OUT 11:00",
        "tabs": ["🗺️ 交通路线", "🔑 入住指南", "🏡 民宿故事", "✨ 周边·出行"],
        "next_to_checkin": "👉 下一步：查看入住密码与 Wi-Fi",
        "next_to_story": "👉 下一步：查看民宿故事与3D户型图",
        "next_to_local": "👉 下一步：查看首尔分区公交与周边打卡",
        "back_to_way": "🗺️ 返回首页（交通路线）",
        "taxi_tag": "🚖 请向出租车司机出示此屏幕",
        "taxi_sub": "温馨提示：搭乘出租车时，直接将上方韩文地址展示给司机即可。",
        "t2_loc_title": "📍 民宿地址与地图导航",
        "t2_loc_body": (
            "<b>韩文地址:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br>"
            "<b>英文地址:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br>"
            "<b>最近地铁站:</b> 地铁6号线 <b>安岩站 (Anam Station) 3号出口</b> 步行5分钟<br>"
            "<b>最近公交站:</b> <b>安岩五岔路口 (안암오거리) · 高丽大站 (고려대역)</b> 步行1~3分钟"
        ),
        "t2_btn_naver": "🟢 打开 Naver 地图导航（韩国境内最准确）",
        "t2_btn_google": "🗺️ 打开 Google 地图",
        "t2_sub_title": "🚉 从地铁6号线「安岩站」步行路线",
        "t2_sub_body": (
            "• 请从<b>地铁6号线安岩站（高大医院前）3号出口</b>出站。<br>"
            "• 出站后朝安岩五岔路口·祭基市场方向直行，拐入 <b>안암로18길 (Anam-ro 18-gil)</b> 小巷，"
            "<b>步行约5分钟</b>即可看到“고려맨션 (Goryeo Mansion)”建筑。（2楼 203室）"
        ),
        "t2_air_title": "✈️ 从机场出发路线",
        "t2_air_body": (
            "<div style='background-color:#F4F7F5; border-left:3px solid #4A7C62; padding:10px 12px; "
            "margin-bottom:12px; border-radius:6px; font-size:13.5px;'>💳 <b>机场出发前必备贴士:</b> "
            "请先在入境大厅便利店或自助机购买并充值 <b>T-money</b> 或 <b>WOWPASS</b> 卡。"
            "<i>(※ 气候同行卡无法在仁川机场购买或进站，建议次日在安岩站购买)</i></div>"
            "<b>1. 仁川国际机场 (ICN) 出发（约 75–85 分钟）</b><br>"
            "• <b>机场铁路 + 地铁（推荐）:</b> 乘坐机场铁路普通列车 ➔ 在<b>孔德站 (Gongdeok)</b> 或 <b>数码媒体城站 (DMC)</b> "
            "换乘<b>地铁6号线（往新内方向）</b> ➔ <b>安岩站</b>下车（3号出口步行5分钟）。<br>"
            "• <b>机场大巴:</b> 乘坐 6002 路大巴 ➔ 在“祭基洞站·首尔药令市”下车后打车起步价即到（约5分钟）。<br><br>"
            "<b>2. 金浦国际机场 (GMP) 出发（约 55 分钟）</b><br>"
            "• 乘坐机场铁路 ➔ 在 <b>DMC站</b> 换乘<b>6号线</b> ➔ <b>安岩站</b>下车。"
        ),
        "t3_time_title": "⏰ 入住退房时间 & 门锁密码开锁指南",
        "t3_time_body": (
            "- <b>入住时间 (Check-in):</b> 下午 3:00 (15:00) 以后 &nbsp;|&nbsp; <b>退房时间:</b> 上午 11:00 以前<br>"
            "<div class='doorlock-box'>"
            "<b>🔐 大门电子密码锁开锁方法（自助入住）</b><br>"
            "1. 入住当天请查看预订平台私信发送给您的<b>专属密码</b>。<br>"
            "2. 无需提前触摸唤醒屏幕，直接依次输入 <b><code>*</code> + <code>专属密码</code> + <code>*</code></b> 即可开锁。<br>"
            "<span style='font-size: 12.5px; color: #5F6368;'>※ 请务必在密码前后都按星号(*)。关门后门锁会自动上锁。</span>"
            "</div>"
        ),
        "t3_wifi_title": "📶 免费高速 Wi-Fi",
        "t3_wifi_body": "请点击所需Wi-Fi及密码右侧的复制图标进行连接。",
        "t3_wifi_ssid": "网络名称 (SSID)",
        "t3_wifi_pw": "密码（5G与2.4G通用）",
        "t3_rules_title": "🌿 住宿公约 (House Rules)",
        "t3_rules_body": (
            "• <b>室内绝对禁烟:</b> 整栋建筑及房间内严禁吸烟（包括电子烟）。<br>"
            "• <b>室内更换拖鞋:</b> 请在玄关脱鞋并换穿室内拖鞋。<br>"
            "• <b>保持安静 (22:00–07:00):</b> 在走廊和楼梯也请轻声走动，晚上10点以后请勿使用洗衣机。<br>"
            "• <b>访客与烹饪限制:</b> 严禁非预订人员进入或留宿，请避免油烟或气味较大的烹饪。"
        ),
        "t3_trash_exp": "♻️ 垃圾分类与长住丢弃指南（点击查看照片）",
        "t3_trash_body": (
            "韩国垃圾分类非常严格，若将厨余垃圾与一般垃圾混装将面临罚款。<br><br>"
            "<b>1. 室内垃圾分类方法</b><br>"
            "- <b>厨余垃圾:</b> 请倒入水槽上方的<b>绿色专用厨余桶</b>内。<br>"
            "- <b>可回收垃圾（纸张·塑料袋·易拉罐·玻璃瓶·塑料瓶）:</b> 清空并冲洗干净后，放入冰箱旁的<b>四层分类垃圾桶</b>中。<br>"
            "- <b>一般垃圾:</b> 其他不可回收垃圾（含卫生间纸巾）请放入 <b>Trash 垃圾桶</b>。<br><br>"
            "<b>2. 长住客人（5晚及以上）或垃圾桶装满时</b><br>"
            "- 备用垃圾袋放在<b>水槽下方柜内</b>。（丢弃日：<b>周二 · 周四 · 周日</b>）<br>"
            "- 系紧袋口——<b>厨余:</b> 黄色/绿色专用袋(2L/3L)，<b>可回收:</b> 透明塑料袋直接丢弃，<b>一般垃圾:</b> 白色计量垃圾袋(20L/50L)——"
            "放至<b>大楼前电线杆下</b>（右图蓝色圆圈位置）。"
        ),
        "t3_trash_cap1": "室内四层分类垃圾桶（冰箱旁）",
        "t3_trash_cap2": "室外垃圾投放点（周二·周四·周日）",
        "t3_checkout_title": "✅ 退房前 10 秒检查清单",
        "t3_checkout_body": "1. 清洗并整理用过的餐具 &nbsp; 2. 完成垃圾分类<br>3. 关闭空调、地暖及灯光 &nbsp; 4. 确认关好窗户与大门 &nbsp; 5. 检查随身物品是否遗漏",
        "t3_contact_title": "🐶 房东紧急联系方式",
        "t3_contact_body": (
            "入住期间如需任何帮助，请随时联系我们。<br>"
            "• <b>预订平台消息:</b> Airbnb / 携程(Trip.com) / Booking.com 应用内聊天（最快）<br>"
            "• <b>即时通讯账号:</b> 微信(WeChat): <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>"
        ),
        "t1_story_title": "🎨 Mongle Stay Story (Curated by miel Yi)",
        "t1_story_body": (
            "Mongle Stay 是为了让来自不同国家和城市的旅行者都能舒适地体验首尔日常生活而打造的家。"
            "即使喜欢的音乐与文化各不相同，在旅途中感受到的心动与发现新故事的喜悦却是相通的。"
            "希望您在 Mongle Stay 停留的时光不仅是一次简单的住宿，更是一段发现属于自己首尔品味与美好回忆的旅程。"
            "<div class='story-quote'>"
            "<b>• 品味 (Taste):</b> 在拥有不同色彩与氛围的空间里，以最让自己感到自在的方式停留。<br>"
            "<b>• 连接 (Connection):</b> 感受 K-Culture 与安岩的日常烟火气，邂逅首尔古老的传统市场与新潮文化。<br>"
            "<b>• 安心 (Peace of Mind):</b> 即使身处陌生的城市也能像在家一样安心，我们为您准备了整洁的空间与细致贴心的指引。"
            "</div>"
        ),
        "t1_rooms_title": "🛏️ 三间卧室的故事 & 入住人数房型配置",
        "t1_rooms_body": (
            "- <b>Palette Room:</b> 不同色彩与个人品味自然交融的房间<br>"
            "- <b>Amber Room:</b> 如温暖灯光般伴您舒适结束一天旅程的房间<br>"
            "- <b>Cozy Room:</b> 小巧却能完全享受独处时光的温馨房间<br><br>"
            "<span style='font-size: 13.5px; color: #8C5A3C;'>※ <b>按入住人数配置客房:</b> 客房将根据您的预订人数提前准备。<br>"
            "&nbsp;&nbsp;- <b>4人及以下:</b> 开放 2 间卧室 (Palette Room / Amber Room)<br>"
            "&nbsp;&nbsp;- <b>5人及以上:</b> 开放全部 3 间卧室 (Palette / Amber / Cozy Room)</span>"
        ),
        "t1_floorplan_caption": "📐 Mongle Stay 3D 空间结构与房间布局图",
        "t4_walk_title": "☕ 步行可达本地漫步与传统市场（安岩·祭基）",
        "t4_walk_body": (
            "<b>1. 高丽大学校园 & 安岩大学街美食（步行 5–10 分钟）</b><br>"
            "• 漫步于欧式哥特风情石造建筑校园，打卡性价比超高的本地美食店与咖啡馆。<br><br>"
            "<b>2. 星巴克京东1960店 & 京东市场·首尔药令市（步行 12–15 分钟）</b><br>"
            "• 强烈推荐由1960年代老剧场改造的网红星巴克，顺便逛逛首尔最具烟火气的传统市场美食街。<br><br>"
            "<b>3. 城北川散步路（步行 8 分钟）</b><br>"
            "• 晚饭后沿着灯光璀璨的溪边步道悠闲散步，感受首尔本地人的慢生活。"
        ),
        "t4_city_title": "🚌 首尔五大核心商圈出行指南（门口直达公交 · 地铁）",
        "t4_city_intro": "民宿步行 1~3 分钟即到 <b>安岩五岔路口 · 高丽大站</b> 公交站，无需换乘即可直达各大商圈。点击区域查看路线：",
        "t4_areas": [
            ("🏯 1. 东大门 · 钟路 · 古宫商圈（约 10–20 分钟）", "<b>热门景点:</b> DDP、广藏市场、益善洞、景福宫<br>• <b>直达公交:</b> <code>101</code> · <code>144</code> · <code>273</code> · <code>111</code> 路（安岩五岔路口站上车）<br>• <b>地铁:</b> 6号线安岩站 ➔ 东庙前站换乘1号线"),
            ("🍷 2. 汉南洞 · 梨泰院 · 龙山商圈（约 20–30 分钟）", "<b>热门景点:</b> 汉南洞咖啡街、梨泰院、解放村<br>• <b>直达公交:</b> <b><code>110A</code> 路</b>（高丽大站上车）➔ 直达汉江镇站、梨泰院站、绿莎坪站<br>&nbsp;&nbsp;<span style='font-size:13px; color:#8C5A3C;'>(※ 返程请乘坐反方向的 <b><code>110B</code> 路</b>！)</span><br>• <b>直达地铁:</b> 6号线安岩站 ➔ 汉江镇站 / 梨泰院站（无需换乘）"),
            ("🎨 3. 圣水洞 · 首尔林商圈（约 15–20 分钟）", "<b>热门景点:</b> 圣水洞快闪店与咖啡街、首尔林<br>• <b>直达公交:</b> <code>121</code> 路（高丽大站上车）➔ 直达首尔林·圣水方向<br>• <b>地铁:</b> 6号线安岩站 ➔ 新堂站换乘2号线 ➔ 圣水站"),
            ("🎸 4. 弘大 · 延南洞 · 望远商圈（约 30–35 分钟）", "<b>热门景点:</b> 弘大、延南洞、望远市场<br>• <b>直达地铁（推荐）:</b> 6号线安岩站 ➔ 望远站 / 合井站（无需换乘）<br>• <b>直达公交:</b> <code>110A</code> 路 ➔ 一线直达新村与延南洞"),
            ("🏙️ 5. 明洞 · 南山 · 江南商圈（约 25–40 分钟）", "<b>热门景点:</b> 明洞、N首尔塔、林荫道、江南站<br>• <b>明洞·南山:</b> 6号线 ➔ 药水站换乘3号线 ➔ 忠武路站<br>• <b>江南·新沙:</b> <code>144</code> 路公交直达新沙站与江南站")
        ],
        "t4_trans_title": "💳 三种交通卡怎么选？（含机场购买贴士）",
        "t4_trans_body": (
            "- <b>1. T-money 交通卡 — 强烈建议抵达仁川机场后立即购买！</b><br>"
            "&nbsp;&nbsp;在机场便利店或地铁售票机用现金购买并充值，机场铁路、机场大巴(6002路)、地铁、公交及出租车通用。"
            "<b>下公交车时务必在后门刷卡机再刷一次卡</b>，方可享受30分钟内免费换乘！<br><br>"
            "- <b>2. WOWPASS 卡 — 外币兑换 + 商店刷卡 + 交通卡三合一</b><br>"
            "&nbsp;&nbsp;可在机场或主要地铁站橙色自助机直接存入人民币/外币兑换成韩元消费，并内置 T-money 交通功能。"
            "<i>(※ 交通卡余额需在地铁站充值机用韩元现金单独充值)</i><br><br>"
            "- <b>3. 气候同行卡 (Climate Card) — 首尔地铁公交无限次通票</b><br>"
            "&nbsp;&nbsp;1日券(5,000韩元)至5日券(15,000韩元)，首尔市内地铁公交无限次乘坐！<br>"
            "&nbsp;&nbsp;<span style='font-size:13px; color:#8C5A3C;'>⚠️ <b>重要提示:</b> 仁川机场无法购买也不能使用此卡进站。"
            "建议先用 T-money 从机场到达民宿，次日在 <b>6号线安岩站（客服中心·充值机·便利店）</b>购买并充值最划算！</span>"
        )
    }
}

# 4. 상단 언어 선택 바 (4열 가로 1줄 고정 버튼)
st.markdown('<div id="top"></div>', unsafe_allow_html=True)
lang_keys = ["한국어", "English", "日本語", "中文"]
lang_cols = st.columns(4)
for idx, l_key in enumerate(lang_keys):
    with lang_cols[idx]:
        is_selected = (st.session_state.selected_lang == l_key)
        st.button(
            l_key,
            key=f"lang_{l_key}",
            type="primary" if is_selected else "secondary",
            use_container_width=True,
            on_click=set_lang,
            args=(l_key,)
        )

t = CONTENT[st.session_state.selected_lang]

# 5. 상단 슬림 웰컴 헤더 (한 줄 고정)
st.markdown(f"""
<div class="hero-box">
    <div>
        <h1 class="hero-title">🐾 {t['title']}</h1>
        <p class="hero-subtitle">{t['subtitle']}</p>
    </div>
    <div class="hero-badge">{t['hero_badge']}</div>
</div>
""", unsafe_allow_html=True)

# 6. 상단 4대 카테고리 네비게이션 버튼 바 (가로 1줄 고정)
nav_cols = st.columns(4)
for idx, label in enumerate(t["tabs"]):
    with nav_cols[idx]:
        btn_type = "primary" if st.session_state.active_tab == idx else "secondary"
        st.button(
            label,
            key=f"nav_{idx}",
            type=btn_type,
            use_container_width=True,
            on_click=go_to_tab,
            args=(idx,)
        )

st.write("")

# TAB 1 (index 0): 숙소에 찾아오는 방법 (최우선 배치 + 택시 기사님 카드)
if st.session_state.active_tab == 0:
    st.markdown(f"""
    <div class="taxi-card">
        <div class="taxi-tag">{t['taxi_tag']}</div>
        <div class="taxi-kr-main">
            “기사님, 동대문구 안암로18길 3<br>고려맨션으로 가주세요.”
        </div>
        <div class="taxi-kr-sub">
            📍 서울 동대문구 제기동 137-273 (안암오거리 · 고대앞삼거리 인근)
        </div>
        <p style="font-size:12.5px; color:#7A746E; margin-top:8px; margin-bottom:0;">
            {t['taxi_sub']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">LOCATION</span>
        <div class="card-title">{t['t2_loc_title']}</div>
        <p class="card-text">{t['t2_loc_body']}</p>
        <a href="https://map.naver.com/p/search/서울특별시 동대문구 안암로18길 3" target="_blank" class="map-btn">{t['t2_btn_naver']}</a>
        <a href="https://maps.google.com/?q=서울특별시+동대문구+안암로18길+3" target="_blank" class="map-btn map-btn-sub">{t['t2_btn_google']}</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">SUBWAY</span>
        <div class="card-title">{t['t2_sub_title']}</div>
        <p class="card-text">{t['t2_sub_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">FROM AIRPORT</span>
        <div class="card-title">{t['t2_air_title']}</div>
        <div class="card-text">{t['t2_air_body']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.button(t["next_to_checkin"], type="primary", use_container_width=True, on_click=go_to_tab, args=(1,))

# TAB 2 (index 1): 체크인 · 도어락 · Wi-Fi · 규칙 · 분리수거(사진포함) · 체크아웃
elif st.session_state.active_tab == 1:
    st.markdown(f"""
    <div class="info-card">
        <span class="badge">CHECK-IN & DOOR LOCK</span>
        <div class="card-title">{t['t3_time_title']}</div>
        <div class="card-text">{t['t3_time_body']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">FREE WI-FI</span>
        <div class="card-title">{t['t3_wifi_title']}</div>
        <p class="card-text">{t['t3_wifi_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.caption(t['t3_wifi_ssid'])
        st.code(WIFI_5G, language=None)
        st.code(WIFI_24G, language=None)
    with col2:
        st.caption(t['t3_wifi_pw'])
        st.code(WIFI_PW, language=None)

    st.markdown(f"""
    <div class="info-card" style="margin-top: 14px;">
        <span class="badge">HOUSE RULES</span>
        <div class="card-title">{t['t3_rules_title']}</div>
        <p class="card-text">{t['t3_rules_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander(t['t3_trash_exp'], expanded=False):
        st.markdown(f"<div class='card-text'>{t['t3_trash_body']}</div>", unsafe_allow_html=True)
        st.write("")
        t_col1, t_col2 = st.columns(2)
        with t_col1:
            st.image("trash_bin.jpg", caption=t['t3_trash_cap1'], use_container_width=True)
        with t_col2:
            st.image("trash_outside.jpg", caption=t['t3_trash_cap2'], use_container_width=True)

    st.markdown(f"""
    <div class="info-card" style="margin-top: 14px;">
        <span class="badge">CHECK-OUT</span>
        <div class="card-title">{t['t3_checkout_title']}</div>
        <p class="card-text">{t['t3_checkout_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card" style="background-color: #F4F7F5; border-color: #C8D6CE;">
        <div class="card-title">{t['t3_contact_title']}</div>
        <p class="card-text">{t['t3_contact_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.button(t["next_to_story"], type="primary", use_container_width=True, on_click=go_to_tab, args=(2,))

# TAB 3 (index 2): 몽글스테이 스토리 & 공간/객실 안내 + 3D 평면도
elif st.session_state.active_tab == 2:
    st.markdown(f"""
    <div class="info-card">
        <span class="badge">MONGLE STAY STORY</span>
        <div class="card-title">{t['t1_story_title']}</div>
        <div class="card-text">{t['t1_story_body']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">THREE ROOMS</span>
        <div class="card-title">{t['t1_rooms_title']}</div>
        <div class="card-text">{t['t1_rooms_body']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.image("floorplan.png", caption=t['t1_floorplan_caption'], use_container_width=True)
    st.write("")
    st.button(t["next_to_local"], type="primary", use_container_width=True, on_click=go_to_tab, args=(3,))

# TAB 4 (index 3): 로컬 명소 & 권역별 교통(아코디언) & 교통카드
elif st.session_state.active_tab == 3:
    st.markdown(f"""
    <div class="info-card">
        <span class="badge">WALKING 5~15 MIN</span>
        <div class="card-title">{t['t4_walk_title']}</div>
        <p class="card-text">{t['t4_walk_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card" style="margin-bottom: 10px;">
        <span class="badge">BUS & SUBWAY BY AREA</span>
        <div class="card-title">{t['t4_city_title']}</div>
        <p class="card-text">{t['t4_city_intro']}</p>
    </div>
    """, unsafe_allow_html=True)

    for area_title, area_desc in t["t4_areas"]:
        with st.expander(area_title):
            st.markdown(f"<div class='card-text'>{area_desc}</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card" style="margin-top: 14px;">
        <span class="badge">TRANSIT CARDS & AIRPORT</span>
        <div class="card-title">{t['t4_trans_title']}</div>
        <div class="card-text">{t['t4_trans_body']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.button(t["back_to_way"], type="secondary", use_container_width=True, on_click=go_to_tab, args=(0,))

# 7. 하단 푸터
st.markdown("""
<div style="text-align: center; padding: 22px 0 10px 0; color: #8C857B; font-size: 12px;">
    © 2026 <b>mongle-stay Seoul (Anam · Jegi-dong)</b>. All rights reserved.<br>
    Have a cozy and wonderful stay in Seoul 🐾
</div>
""", unsafe_allow_html=True)

# 8. 페이지 전환 시 화면 맨 위로 자동 스크롤
if st.session_state.scroll_to_top:
    components.html(
        f"""
        <!-- {time.time()} -->
        <script>
            function scrollToTop() {{
                try {{
                    const parentDoc = window.parent.document;
                    const anchor = parentDoc.getElementById('top');
                    if (anchor) {{
                        anchor.scrollIntoView({{ behavior: 'instant', block: 'start' }});
                    }}
                    const containers = parentDoc.querySelectorAll(
                        '[data-testid="stAppViewContainer"], section.main, .stApp'
                    );
                    containers.forEach(el => {{ el.scrollTop = 0; }});
                    window.parent.scrollTo(0, 0);
                }} catch (e) {{}}
            }}
            scrollToTop();
            setTimeout(scrollToTop, 100);
            setTimeout(scrollToTop, 300);
        </script>
        """,
        height=0
    )
    st.session_state.scroll_to_top = False
