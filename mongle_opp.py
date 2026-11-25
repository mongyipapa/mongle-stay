import streamlit as st

# =========================================================
# [설정 영역] 실제 숙소 Wi-Fi 정보만 여기서 수정하세요
# =========================================================
WIFI_ID = "mongle-stay_5G"
WIFI_PW = "mongle1234"  # 실제 Wi-Fi 비밀번호로 변경해 주세요

# ---------------------------------------------------------
# 1. 페이지 기본 설정
# ---------------------------------------------------------
st.set_page_config(
    page_title="mongle-stay | Digital Welcome Book",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# 2. 커스텀 CSS (언어 버튼 시인성 강화 · 슬림 헤더 · 택시 카드 · 아코디언)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&family=Noto+Sans+JP:wght@400;500;700&family=Noto+Sans+SC:wght@400;500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', 'Noto Sans JP', 'Noto Sans SC', sans-serif;
        background-color: #FAF8F5;
        color: #2C2A29;
    }

    .block-container {
        padding-top: 1.1rem !important;
        padding-bottom: 3rem !important;
        max-width: 680px !important;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 상단 언어 선택 버튼 시인성 강화 */
    div[data-testid="stRadio"] > div {
        justify-content: center;
        gap: 0.45rem;
        margin-bottom: 0.65rem;
        background-color: #EFECE6;
        padding: 0.4rem;
        border-radius: 24px;
        border: 1px solid #DDD6CC;
    }
    div[data-testid="stRadio"] label {
        background-color: #FFFFFF !important;
        color: #2C2A29 !important;
        padding: 0.35rem 0.85rem !important;
        border-radius: 18px !important;
        border: 1.5px solid #C8BFB3 !important;
        font-size: 0.86rem !important;
        font-weight: 600 !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        transition: all 0.15s ease;
    }
    div[data-testid="stRadio"] label p {
        color: #2C2A29 !important;
        font-weight: 600 !important;
    }
    /* 선택된 언어 버튼 강조 */
    div[data-testid="stRadio"] label:has(input:checked) {
        background-color: #2D4A3E !important;
        border-color: #2D4A3E !important;
    }
    div[data-testid="stRadio"] label:has(input:checked) p {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }

    /* 슬림 히어로 헤더 */
    .hero-slim {
        background: linear-gradient(135deg, #2D4A3E 0%, #3E6354 100%);
        padding: 1.15rem 1.3rem;
        border-radius: 16px;
        color: #FFFFFF;
        margin-bottom: 0.9rem;
        box-shadow: 0 4px 14px rgba(45, 74, 62, 0.14);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .hero-slim h1 {
        font-size: 1.45rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.02em;
        color: #FFFFFF;
    }
    .hero-slim p {
        font-size: 0.84rem;
        margin: 0.2rem 0 0 0;
        color: #E2ECE7;
    }
    .hero-badge {
        background-color: rgba(255, 255, 255, 0.18);
        padding: 0.35rem 0.7rem;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 500;
        color: #FFFFFF;
        white-space: nowrap;
    }

    /* 상단 퀵 액션 요약 바 */
    .quick-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    .quick-item {
        background-color: #FFFFFF;
        border: 1px solid #EAE4DC;
        border-radius: 12px;
        padding: 0.65rem 0.5rem;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.02);
    }
    .quick-label {
        font-size: 0.72rem;
        color: #7A746E;
        margin-bottom: 0.15rem;
    }
    .quick-val {
        font-size: 0.85rem;
        font-weight: 700;
        color: #2D4A3E;
    }

    /* 일반 콘텐츠 카드 */
    .info-card {
        background-color: #FFFFFF;
        padding: 1.2rem 1.25rem;
        border-radius: 14px;
        border: 1px solid #EAE4DC;
        margin-bottom: 0.85rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.025);
    }
    .info-card h3 {
        font-size: 1.05rem;
        font-weight: 700;
        color: #2D4A3E;
        margin-top: 0;
        margin-bottom: 0.6rem;
    }
    .info-card p, .info-card li {
        font-size: 0.92rem;
        line-height: 1.62;
        color: #4A4642;
        margin-bottom: 0.35rem;
    }

    /* 택시 기사님용 큰 글씨 카드 */
    .taxi-card {
        background-color: #FFFDF7;
        border: 2px solid #D9A036;
        border-radius: 14px;
        padding: 1.2rem 1.25rem;
        margin-bottom: 0.9rem;
    }
    .taxi-tag {
        display: inline-block;
        background-color: #D9A036;
        color: #FFFFFF;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        margin-bottom: 0.5rem;
    }
    .taxi-kr-main {
        font-size: 1.22rem;
        font-weight: 700;
        color: #1F1D1B;
        line-height: 1.45;
        margin: 0.3rem 0;
        word-break: keep-all;
    }
    .taxi-kr-sub {
        font-size: 0.95rem;
        font-weight: 500;
        color: #5C554E;
        margin-top: 0.3rem;
    }

    /* 강조 경고 배지 (Callout) */
    .alert-box {
        background-color: #FDF3F2;
        border-left: 4px solid #D9534F;
        padding: 0.75rem 0.95rem;
        border-radius: 8px;
        margin: 0.6rem 0;
        font-size: 0.88rem;
        color: #8A2B28;
        line-height: 1.5;
    }
    .tip-box {
        background-color: #F2F7F4;
        border-left: 4px solid #2D4A3E;
        padding: 0.75rem 0.95rem;
        border-radius: 8px;
        margin: 0.6rem 0;
        font-size: 0.88rem;
        color: #264035;
        line-height: 1.5;
    }

    /* 방 소개 미니 그리드 */
    .room-pill {
        background-color: #F7F4EF;
        padding: 0.75rem 0.9rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        border: 1px solid #EAE4DC;
    }
    .room-pill strong {
        color: #2D4A3E;
        font-size: 0.95rem;
    }

    /* 탭 스타일 */
    button[data-baseweb="tab"] {
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        padding: 0.5rem 0.4rem !important;
    }

    /* Expander(아코디언) 스타일 */
    div[data-testid="stExpander"] {
        background-color: #FFFFFF;
        border: 1px solid #EAE4DC;
        border-radius: 12px;
        margin-bottom: 0.55rem;
        box-shadow: 0 1px 4px rgba(0,0,0,0.02);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. 다국어 데이터 (4개 국어)
# ---------------------------------------------------------
CONTENT = {
    "한국어": {
        "subtitle": "서울 동대문 제기동 · 최대 6인 프라이빗 스테이",
        "badge": "체크인 15:00 · 체크아웃 11:00",
        "quick": [
            ("📍 위치", "제기동 · 안암역 인근"),
            ("🔐 도어락", "* + 비번 + *"),
            ("📶 Wi-Fi", f"PW: {WIFI_PW}")
        ],
        "tabs": ["🗺️ 오시는 길", "🔑 체크인·Wi-Fi", "🏡 공간 스토리", "✨ 로컬·교통"],
        "location": {
            "taxi_tag": "🚖 택시 기사님께 이 화면을 보여주세요",
            "taxi_sub": "게스트 안내: 택시나 길 안내가 필요할 때 아래 한국어 주소를 기사님께 그대로 보여주세요.",
            "address_title": "숙소 주소 (우측 아이콘 클릭 시 복사)",
            "address_road": "서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "address_jibun": "지번: 서울특별시 동대문구 제기동 137-273, 고려맨션 203호",
            "airport_title": "✈️ 인천공항에서 오시는 길",
            "airport_limo": "<b>공항리무진 6002번 (가장 편리):</b> 인천공항 승차 ➔ <b>'신설동역' 또는 '동대문역'</b> 하차 ➔ 택시로 약 5~7분 이동",
            "airport_arex": "<b>공항철도(AREX):</b> 서울역 또는 홍대입구역 하차 ➔ 지하철 1호선(제기동역) 또는 6호선(안암역) 환승",
            "map_note": "아래 버튼으로 지도를 바로 열 수 있습니다."
        },
        "checkin": {
            "door_title": "1. 현관 도어락 & 입실 안내",
            "door_alert": "⚠️ <b>비밀번호 앞과 뒤에 반드시 별표(*)를 눌러주세요!</b><br>입력 순서: <b>[ * ] + [ 비밀번호 4자리 ] + [ * ]</b>",
            "door_desc": "보안을 위해 예약 확정 후 에어비앤비 메시지로 개별 비밀번호를 보내드립니다. 현관에 들어서시면 실외화를 벗고 비치된 실내화를 착용해 주세요.",
            "wifi_title": "2. 무료 초고속 Wi-Fi",
            "wifi_desc": "우측 상단 복사 아이콘을 누르면 비밀번호가 바로 복사됩니다.",
            "rules_title": "3. 이용 수칙 & 분리수거",
            "rules": [
                "<b>실내 절대 금연:</b> 전자담배 포함 건물 전체 금연입니다.",
                "<b>정숙 시간:</b> 밤 10시 이후에는 이웃을 위해 소음을 줄여주세요.",
                "<b>분리수거:</b> 일반쓰레기 / 재활용(플라스틱·캔·유리) / 음식물 쓰레기를 주방 옆 전용함에 나누어 담아주세요.",
                "<b>외출 시 소등:</b> 외출하실 때는 에어컨, 보일러, 조명을 꺼주시면 감사하겠습니다."
            ]
        },
        "story": {
            "welcome_title": "몽글스테이에 오신 것을 환영합니다 🐾",
            "welcome_p1": "<b>mongle-stay</b>는 호스트 부부와 사랑스러운 4살 비숑 <b>'몽이(mongyi)'</b>의 이름에서 시작된 따뜻한 쉼터입니다. 인테리어 디자이너 호스트 <b>미엘(Miel)</b>이 여행자의 시선으로 직접 설계하고 가꾸었습니다.",
            "welcome_p2": "고려대학교와 경희대학교의 활기, 경동시장의 정겨운 로컬 감성이 어우러진 제기동에서 서울의 진짜 일상을 경험해 보세요.",
            "rooms_title": "3개의 독립된 침실 구성 (최대 6인)",
            "rooms": [
                ("🎨 Room 1 · Palette (팔레트)", "부드러운 색감과 아늑한 조명이 어우러진 메인 침실입니다."),
                ("🕯️ Room 2 · Amber (앰버)", "따뜻한 우드 톤과 차분한 휴식에 집중한 침실입니다."),
                ("☁️ Room 3 · Cozy (코지)", "구름처럼 포근한 침구로 깊은 숙면을 돕는 침실입니다.")
            ],
            "note": "※ 본 숙소는 호스트 부부가 직접 관리하는 합법 외국인관광 도시민박업 등록 숙소입니다. (반려견 몽이는 호스트 자택에서 지내며 숙소 내에는 출입하지 않으니 알레르기 걱정은 하지 않으셔도 됩니다.)"
        },
        "local": {
            "card_title": "💳 서울 대중교통 카드 필수 팁",
            "card_alert": "⚠️ <b>인천공항에서는 기후동행카드(무제한 패스)를 사용할 수 없습니다!</b><br>공항에서는 일반 <b>티머니(T-money)</b>를 쓰시고, 서울 시내 도착 후 편의점에서 기후동행카드를 구매·충전해 사용하세요.",
            "bus_title": "🚌 숙소 앞 직통 버스로 서울 핵심 관광지 한 번에 가기",
            "bus_intro": "지하철 환승 없이 숙소 인근 정류장에서 버스 한 번으로 주요 스팟까지 이동할 수 있습니다. 각 권역을 눌러 노선을 확인하세요.",
            "areas": [
                ("🛍️ 명동 · 을지로 · 남산 (약 20~25분)", "<b>추천 버스:</b> 105번, 147번, 202번, 261번<br>• 명동 쇼핑거리, 을지로 힙지로 골목, N서울타워 환승 정류장 직통 연결"),
                ("🎨 성수동 · 서울숲 · 건대 (약 20~25분)", "<b>추천 버스:</b> 2012번, 2222번, 2416번 (또는 2호선 성수역)<br>• 성수 카페거리, 팝업스토어, 서울숲 산책로 이동 편리"),
                ("🏯 경복궁 · 북촌한옥마을 · 광화문 (약 25~30분)", "<b>추천 버스:</b> 101번, 152번, 272번, 7211번<br>• 한복 체험, 경복궁, 서촌·북촌 한옥마을, 광화문 광장 직통"),
                ("🎸 홍대입구 · 연남동 · 신촌 (약 35~40분)", "<b>추천 버스:</b> 273번 (제기동·안암 ➔ 홍대입구 직통 황금노선!)<br>• 환승 없이 한 번에 홍대 쇼핑·버스킹·연남동 카페거리 도착"),
                ("🏙️ 강남 · 압구정 · 잠실 (약 35~45분)", "<b>추천 버스:</b> 147번, 421번 (강남·신사) / 2416번·지하철 2호선 (잠실 롯데월드타워)")
            ],
            "spot_title": "🍜 도보권 동네 로컬 추천",
            "spots": [
                ("경동시장 & 서울약령시장 (도보 8~10분)", "한국 최대 규모의 전통 한방·식재료 시장과 MZ세대에게 인기인 '스타벅스 경동1960점'을 꼭 방문해 보세요."),
                ("안암동 대학가 먹자골목 (도보 7~10분)", "가성비 훌륭한 한식백반, 치킨, 로컬 카페가 늦은 밤까지 활기차게 열려 있습니다.")
            ]
        }
    },
    "English": {
        "subtitle": "Jegi-dong, Dongdaemun, Seoul · Up to 6 Guests",
        "badge": "Check-in 15:00 · Out 11:00",
        "quick": [
            ("📍 Location", "Near Anam & Jegi Stn."),
            ("🔐 Door Lock", "* + PIN + *"),
            ("📶 Wi-Fi", f"PW: {WIFI_PW}")
        ],
        "tabs": ["🗺️ Directions", "🔑 Check-in·Wi-Fi", "🏡 Story", "✨ Local·Transit"],
        "location": {
            "taxi_tag": "🚖 SHOW THIS TO YOUR TAXI DRIVER",
            "taxi_sub": "Tip: Show the large Korean address below directly to your taxi driver.",
            "address_title": "Property Address (Tap Copy Icon)",
            "address_road": "203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul",
            "address_jibun": "Korean: 서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "airport_title": "✈️ From Incheon Airport (ICN)",
            "airport_limo": "<b>Airport Limousine Bus #6002 (Easiest):</b> Board at ICN ➔ Get off at <b>Sinseol-dong Stn.</b> or <b>Dongdaemun Stn.</b> ➔ Take a 5–7 min taxi ride.",
            "airport_arex": "<b>AREX Airport Train:</b> Transfer at Seoul Stn. (Line 1 to Jegi-dong Stn.) or Gongdeok Stn. (Line 6 to Anam Stn.).",
            "map_note": "Open directly in your preferred map app:"
        },
        "checkin": {
            "door_title": "1. Smart Door Lock & Entry",
            "door_alert": "⚠️ <b>You MUST press Asterisk (*) before and after your PIN!</b><br>Sequence: <b>[ * ] + [ 4-Digit PIN ] + [ * ]</b>",
            "door_desc": "For your security, your unique PIN is sent via Airbnb message before check-in. Please take off outdoor shoes at the entrance and wear the indoor slippers provided.",
            "wifi_title": "2. Free High-Speed Wi-Fi",
            "wifi_desc": "Tap the copy icon on the top right of the box below to copy the password.",
            "rules_title": "3. House Rules & Recycling",
            "rules": [
                "<b>Strictly No Smoking:</b> No smoking or vaping anywhere in the building.",
                "<b>Quiet Hours:</b> Please keep noise down after 10:00 PM out of respect for neighbors.",
                "<b>Recycling:</b> Please separate General Waste, Recyclables (plastic/cans/glass), and Food Waste into the bins next to the kitchen.",
                "<b>Save Energy:</b> Please turn off the A/C, floor heating (boiler), and lights when going out."
            ]
        },
        "story": {
            "welcome_title": "Welcome to mongle-stay 🐾",
            "welcome_p1": "<b>mongle-stay</b> is a warm, thoughtfully curated retreat named after our beloved 4
