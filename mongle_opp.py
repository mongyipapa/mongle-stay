import streamlit as st

# =========================================================
# [설정 영역] 실제 숙소 Wi-Fi 및 연락처 정보
# =========================================================
WIFI_5G = "U+Net1825_5G"
WIFI_24G = "U+Net1825"
WIFI_PW = "42155551M#"

WECHAT_ID = "mongle-stay"
LINE_ID = "mongle-stay"
KAKAO_ID = "mongle0607"

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
# 2. 커스텀 CSS
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
        margin-bottom: 0.38rem;
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
        line-height: 1.55;
    }
    .tip-box {
        background-color: #F2F7F4;
        border-left: 4px solid #2D4A3E;
        padding: 0.75rem 0.95rem;
        border-radius: 8px;
        margin: 0.6rem 0;
        font-size: 0.88rem;
        color: #264035;
        line-height: 1.55;
    }

    /* 방 소개 & 연락처 미니 그리드 */
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
# 3. 다국어 데이터 (노션 이용 안내 내용 100% 반영 · 별표 기호 복원)
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
        "tabs": ["🗺️ 오시는 길", "🔑 체크인·이용안내", "🏡 공간 스토리", "✨ 로컬·교통"],
        "location": {
            "taxi_tag": "🚖 택시 기사님께 이 화면을 보여주세요",
            "taxi_sub": "게스트 안내: 택시나 길 안내가 필요할 때 아래 한국어 주소를 기사님께 그대로 보여주세요.",
            "address_title": "숙소 주소 (우측 아이콘 클릭 시 복사)",
            "address_road": "서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "address_jibun": "지번: 서울특별시 동대문구 제기동 137-273, 고려맨션 203호",
            "airport_title": "✈️ 인천공항에서 오시는 길",
            "airport_limo": (
                "<b>공항리무진 6002번 (가장 편리):</b> 인천공항 승차 ➔ "
                "<b>'신설동역' 또는 '동대문역'</b> 하차 ➔ 택시로 약 5~7분 이동"
            ),
            "airport_arex": (
                "<b>공항철도(AREX):</b> 서울역 또는 홍대입구역 하차 ➔ "
                "지하철 1호선(제기동역) 또는 6호선(안암역) 환승"
            ),
            "map_note": "아래 버튼으로 지도를 바로 열 수 있습니다."
        },
        "checkin": {
            "contact_title": "0. 문의 및 비상 연락처",
            "contact_desc": "머무시는 동안 도움이 필요하시면 언제든 아래 메신저 또는 에어비앤비 메시지로 연락해 주세요.",
            "door_title": "1. 현관 도어락 & Wi-Fi 안내",
            "door_alert": (
                "⚠️ <b>비밀번호 앞과 뒤에 반드시 별표(*)를 눌러주세요!</b><br>"
                "입력 순서: <b>[ * ] + [ 비밀번호 4자리 ] + [ * ]</b>"
            ),
            "door_desc": "보안을 위해 개별 비밀번호는 체크인 전 에어비앤비 메시지로 보내드립니다. 우측 복사 아이콘을 누르면 Wi-Fi 정보가 복사됩니다.",
            "rules_title": "2. 함께 지켜주세요 (이용 수칙)",
            "rules": [
                "<b>정숙 시간 (22:00 ~ 07:00):</b> 밤 10시 이후에는 이웃을 위해 소음을 줄여주세요.",
                "<b>실내에서는 신발 벗기:</b> 현관에서 실외화를 벗고 실내화를 착용해 주세요.",
                "<b>숙소 전체 금연:</b> 전자담배 포함 건물 전체 절대 금연입니다.",
                "<b>냄새가 강한 요리 금지:</b> 다음 게스트를 위해 생선구이, 청국장 등 냄새가 배는 조리는 삼가주세요.",
                "<b>세탁기 22시 이후 사용 금지:</b> 야간 진동 및 소음 방지를 위해 밤 10시 이후 세탁기 작동을 멈춰주세요.",
                "<b>예약 인원 외 방문과 숙박 금지:</b> 사전 등록된 인원 외 외부인 출입은 불가합니다.",
                "<b>복도와 계단에서도 조용히 이동하기:</b> 공동주택이므로 출입 시 계단과 복도에서 대화를 자제해 주세요."
            ],
            "trash_title": "3. 쓰레기 분리수거 안내 🗑️",
            "trash_alert": (
                "🚫 <b>음식물 쓰레기와 다른 쓰레기를 절대 섞지 마세요!</b><br>"
                "한국의 쓰레기 분리수거는 매우 엄격하며, 혼합 배출 시 과태료(벌금) 부과 대상이 됩니다."
            ),
            "trash_basic": [
                "<b>① 음식물 쓰레기:</b> 싱크대 위에 비치된 <b>음식물 쓰레기 전용통(그린컬러)</b> 안에 버려주세요.",
                "<b>② 재활용 쓰레기 (종이/비닐/캔/유리병/플라스틱):</b> <b>냉장고 앞 분리수거함</b>에 종류별로 넣어주세요. <i>(※ 음식물이 묻은 용기는 반드시 물로 깨끗이 헹군 후 배출해 주세요.)</i>",
                "<b>③ 일반 쓰레기:</b> 그 외 일반 쓰레기는 <b>trash 수거함</b>에 버려주세요.",
                "<b>⚠️ 벌레 예방 주의:</b> 음식물이 묻은 쓰레기를 실내에 오래 방치하면 벌레가 생길 수 있습니다. 장기 숙박이나 쓰레기가 많을 때는 반드시 외부 배출 장소에 버려주세요. <i>(미분리 및 장기 방치로 인한 벌레 문제는 숙소에서 책임지기 어렵습니다.)</i>"
            ],
            "trash_long_title": "📦 장기숙박(5박 이상) & 수거함이 가득 찼을 때 외부 배출 방법",
            "trash_long": [
                "<b>1. 음식물 쓰레기:</b> 작은 음식물 전용 봉투(<b>노랑 2ℓ 또는 초록 3ℓ</b>)에 담아 배출해 주세요.",
                "<b>2. 재활용 쓰레기:</b> 수거함에 세팅되어 있는 <b>투명 봉투 그대로</b> 묶어서 밖에 배출하시면 됩니다.",
                "<b>3. 일반 쓰레기 (화장실 쓰레기 포함):</b> <b>흰색 종량제 비닐봉투(20ℓ 또는 50ℓ)</b>에 담아 묶어서 배출해 주세요.",
                "<b>4. 쓰레기 배출 요일:</b> <b>화요일, 목요일, 일요일</b> (건물 앞 입구 <b>전봇대 밑</b>에 놓아주세요.)",
                "<b>5. 봉투 비치 위치:</b> 모든 쓰레기 봉투는 <b>싱크볼 하부 수납장</b>에 준비되어 있습니다."
            ],
            "checkout_title": "4. 체크아웃 전 확인 체크리스트 (11:00까지)",
            "checkout_items": [
                "사용한 식기 세척 및 정리",
                "쓰레기 분리수거 확인",
                "에어컨 · 보일러 · 모든 조명 끄기",
                "창문과 현관 출입문 잠금 확인",
                "잊은 물건(충전기, 여권 등)이 없는지 확인"
            ]
        },
        "story": {
            "welcome_title": "몽글스테이에 오신 것을 환영합니다 🐾",
            "welcome_p1": (
                "<b>mongle-stay</b>는 호스트 부부와 사랑스러운 4살 비숑 <b>'몽이(mongyi)'</b>의 이름에서 "
                "시작된 따뜻한 쉼터입니다. 인테리어 디자이너 호스트 <b>미엘(Miel)</b>이 여행자의 시선으로 직접 설계하고 가꾸었습니다."
            ),
            "welcome_p2": (
                "고려대학교와 경희대학교의 활기, 경동시장의 정겨운 로컬 감성이 어우러진 제기동에서 "
                "서울의 진짜 일상을 경험해 보세요."
            ),
            "rooms_title": "예약 인원별 객실 오픈 안내 (최대 6인)",
            "room_rule_tip": (
                "🛏️ <b>예약 인원에 맞춰 객실이 준비됩니다:</b><br>"
                "• <b>4인 이하 예약:</b> 침실 2개 오픈 (<b>팔레트룸 · 앰버룸</b>)<br>"
                "• <b>5인 이상 예약:</b> 침실 3개 전체 오픈 (<b>팔레트룸 · 앰버룸 · 코지룸</b>)"
            ),
            "rooms": [
                ("🎨 Room 1 · Palette (팔레트룸)", "부드러운 색감과 아늑한 조명이 어우러진 메인 침실입니다."),
                ("🕯️ Room 2 · Amber (앰버룸)", "따뜻한 우드 톤과 차분한 휴식에 집중한 침실입니다."),
                ("☁️ Room 3 · Cozy (코지룸 · 5인 이상 오픈)", "구름처럼 포근한 침구로 깊은 숙면을 돕는 침실입니다.")
            ],
            "note": (
                "※ 본 숙소는 호스트 부부가 직접 관리하는 합법 외국인관광 도시민박업 등록 숙소입니다. "
                "(반려견 몽이는 호스트 자택에서 지내며 숙소 내에는 출입하지 않으니 알레르기 걱정은 하지 않으셔도 됩니다.)"
            )
        },
        "local": {
            "card_title": "💳 서울 대중교통 카드 필수 팁",
            "card_alert": (
                "⚠️ <b>인천공항에서는 기후동행카드(무제한 패스)를 사용할 수 없습니다!</b><br>"
                "공항에서는 일반 <b>티머니(T-money)</b>를 쓰시고, 서울 시내 도착 후 편의점에서 기후동행카드를 구매·충전해 사용하세요."
            ),
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
        "tabs": ["🗺️ Directions", "🔑 Check-in·Guide", "🏡 Story", "✨ Local·Transit"],
        "location": {
            "taxi_tag": "🚖 SHOW THIS TO YOUR TAXI DRIVER",
            "taxi_sub": "Tip: Show the large Korean address below directly to your taxi driver.",
            "address_title": "Property Address (Tap Copy Icon)",
            "address_road": "203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul",
            "address_jibun": "Korean: 서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "airport_title": "✈️ From Incheon Airport (ICN)",
            "airport_limo": (
                "<b>Airport Limousine Bus #6002 (Easiest):</b> Board at ICN ➔ "
                "Get off at <b>Sinseol-dong Stn.</b> or <b>Dongdaemun Stn.</b> ➔ Take a 5–7 min taxi ride."
            ),
            "airport_arex": (
                "<b>AREX Airport Train:</b> Transfer at Seoul Stn. (Line 1 to Jegi-dong Stn.) "
                "or Gongdeok Stn. (Line 6 to Anam Stn.)."
            ),
            "map_note": "Open directly in your preferred map app:"
        },
        "checkin": {
            "contact_title": "0. Host Contact & Emergency",
            "contact_desc": "Feel free to reach out anytime via Airbnb message or the messengers below if you need assistance:",
            "door_title": "1. Smart Door Lock & Wi-Fi",
            "door_alert": (
                "⚠️ <b>You MUST press Asterisk (*) before and after your PIN!</b><br>"
                "Sequence: <b>[ * ] + [ 4-Digit PIN ] + [ * ]</b>"
            ),
            "door_desc": "Your unique PIN is sent via Airbnb message before check-in. Tap the copy icon below to copy the Wi-Fi password.",
            "rules_title": "2. House Rules (Please Respect)",
            "rules": [
                "<b>Quiet Hours (22:00 – 07:00):</b> Please keep noise down after 10:00 PM for our neighbors.",
                "<b>Shoes Off Indoors:</b> Please take off outdoor shoes at the entrance and wear indoor slippers.",
                "<b>Strictly No Smoking:</b> No smoking or vaping anywhere inside the building.",
                "<b>No Strong-Smelling Cooking:</b> Please refrain from grilling fish or cooking strong-odored foods.",
                "<b>No Washing Machine After 22:00:</b> Please avoid using the washer after 10:00 PM due to vibration/noise.",
                "<b>Registered Guests Only:</b> Unregistered visitors or extra overnight guests are strictly prohibited.",
                "<b>Quiet in Hallways & Stairs:</b> Please keep your voice down when walking through common stairs/hallways."
            ],
            "trash_title": "3. Garbage & Recycling Guide 🗑️",
            "trash_alert": (
                "🚫 <b>NEVER mix food waste with general or recyclable trash!</b><br>"
                "South Korea enforces strict waste sorting laws; improper disposal is subject to fines."
            ),
            "trash_basic": [
                "<b>① Food Waste:</b> Dispose into the <b>green food waste bin</b> located on the kitchen sink counter.",
                "<b>② Recyclables (Paper / Vinyl / Cans / Glass / Plastic):</b> Sort into the <b>recycling bins in front of the refrigerator</b>. <i>(Please rinse off any food residue cleanly first.)</i>",
                "<b>③ General Waste:</b> Put all other non-recyclable trash into the <b>Trash bin</b>.",
                "<b>⚠️ Pest Prevention:</b> Leaving food-stained trash indoors can attract bugs. For long stays or full bins, please take trash to the outdoor collection point. <i>(The host is not responsible for pests caused by unseparated or unemptied trash.)</i>"
            ],
            "trash_long_title": "📦 Long Stays (5+ Nights) & When Bins Are Full",
            "trash_long": [
                "<b>1. Food Waste:</b> Tie up in a small designated food waste bag (<b>Yellow 2L or Green 3L</b>).",
                "<b>2. Recyclables:</b> Tie the <b>clear plastic bag</b> inside the recycling bin as-is and take it outside.",
                "<b>3. General Waste (incl. bathroom trash):</b> Place inside a <b>White Volume-Based Trash Bag (20L or 50L)</b> and tie tightly.",
                "<b>4. Collection Days:</b> <b>Tuesday, Thursday, and Sunday</b> (Place neatly <b>under the utility pole in front of the building entrance</b>).",
                "<b>5. Extra Bags Location:</b> All trash bags are stocked inside the <b>cabinet under the kitchen sink</b>."
            ],
            "checkout_title": "4. Pre-Checkout Checklist (By 11:00 AM)",
            "checkout_items": [
                "Wash and put away used dishes/cookware",
                "Sort and dispose of garbage properly",
                "Turn off A/C, floor heating (boiler), and all lights",
                "Close and lock all windows and the front door",
                "Double-check that no personal belongings are left behind"
            ]
        },
        "story": {
            "welcome_title": "Welcome to mongle-stay 🐾",
            "welcome_p1": (
                "<b>mongle-stay</b> is a warm, thoughtfully curated retreat named after our beloved "
                "4-year-old Bichon Frise, <b>Mongyi</b>. Designed by interior designer host <b>Miel</b>, "
                "every corner is crafted for comfort and calm."
            ),
            "welcome_p2": (
                "Located in Jegi-dong—where university energy meets authentic traditional markets—"
                "experience the real rhythm of Seoul."
            ),
            "rooms_title": "Bedroom Allocation by Guest Count (Up to 6 Guests)",
            "room_rule_tip": (
                "🛏️ <b>Bedrooms are prepared based on your reserved guest count:</b><br>"
                "• <b>Up to 4 Guests:</b> 2 Bedrooms Open (<b>Palette · Amber</b>)<br>"
                "• <b>5 to 6 Guests:</b> All 3 Bedrooms Open (<b>Palette · Amber · Cozy</b>)"
            ),
            "rooms": [
                ("🎨 Room 1 · Palette", "Our main bedroom featuring soft pastel tones and cozy ambient lighting."),
                ("🕯️ Room 2 · Amber", "Designed with warm wood accents for deep, peaceful rest."),
                ("☁️ Room 3 · Cozy (Open for 5+ Guests)", "Cloud-soft bedding tailored for a restful night's sleep.")
            ],
            "note": (
                "※ Officially licensed Foreign Tourist Urban Homestay. "
                "(Our dog Mongyi lives at our separate residence and never enters the guest house—no allergy worries!)"
            )
        },
        "local": {
            "card_title": "💳 Seoul Transit Card Essential Tip",
            "card_alert": (
                "⚠️ <b>Climate Card (Unlimited Pass) CANNOT be used from Incheon Airport!</b><br>"
                "Use a standard <b>T-money card</b> from the airport, then buy/top up a Climate Card at any Seoul convenience store."
            ),
            "bus_title": "🚌 Direct Buses to Top Seoul Attractions",
            "bus_intro": "Reach major spots without subway transfers from bus stops right near the house. Tap each area to view routes:",
            "areas": [
                ("🛍️ Myeongdong · Euljiro · Namsan (~20–25 min)", "<b>Buses:</b> 105, 147, 202, 261<br>• Direct access to Myeongdong shopping, Euljiro hip alleys, and N Seoul Tower shuttle."),
                ("🎨 Seongsu-dong · Seoul Forest (~20–25 min)", "<b>Buses:</b> 2012, 2222, 2416 (or Subway Line 2 to Seongsu)<br>• Trendy cafes, pop-up stores, and Seoul Forest Park."),
                ("🏯 Gyeongbokgung Palace · Bukchon · Gwanghwamun (~25–30 min)", "<b>Buses:</b> 101, 152, 272, 7211<br>• Direct to Royal Palaces, Hanbok rental streets, and Bukchon Hanok Village."),
                ("🎸 Hongdae · Yeonnam-dong · Sinchon (~35–40 min)", "<b>Bus:</b> 273 (Golden direct route from Anam/Jegi to Hongik Univ.!)<br>• Zero transfers straight to Hongdae street performances and Yeonnam cafes."),
                ("🏙️ Gangnam · Apgujeong · Jamsil (~35–45 min)", "<b>Buses:</b> 147, 421 (Gangnam/Sinsa) / 2416 or Line 2 (Jamsil Lotte World Tower)")
            ],
            "spot_title": "🍜 Walking-Distance Local Gems",
            "spots": [
                ("Gyeongdong Market & Starbucks Gyeongdong 1960 (8–10 min walk)", "Explore Seoul's largest traditional market and the famous retro theater-converted Starbucks."),
                ("Anam University Food Alley (7–10 min walk)", "Lively local restaurants, Korean BBQ, fried chicken, and cozy study cafes.")
            ]
        }
    },
    "日本語": {
        "subtitle": "ソウル東大門 祭基洞 · 最大6名様 プライベートステイ",
        "badge": "IN 15:00 · OUT 11:00",
        "quick": [
            ("📍 アクセス", "祭基洞・安岩駅 徒歩圏"),
            ("🔐 ドアロック", "* + 暗証番号 + *"),
            ("📶 Wi-Fi", f"PW: {WIFI_PW}")
        ],
        "tabs": ["🗺️ アクセス", "🔑 利用案内・Wi-Fi", "🏡 ストーリー", "✨ 周辺・交通"],
        "location": {
            "taxi_tag": "🚖 タクシー運転手さんにこの画面を見せてください",
            "taxi_sub": "ご案内：タクシーに乗車する際は、下の韓国語住所をそのまま運転手さんにお見せください。",
            "address_title": "宿泊施設 住所（右上アイコンでコピー）",
            "address_road": "서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "address_jibun": "英語表記: 203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul",
            "airport_title": "✈️ 仁川国際空港からのアクセス",
            "airport_limo": (
                "<b>空港リムジンバス 6002番（一番おすすめ）：</b>仁川空港乗車 ➔ "
                "<b>「新設洞駅」または「東大門駅」</b>下車 ➔ タクシーで約5〜7分"
            ),
            "airport_arex": (
                "<b>空港鉄道(AREX)：</b>ソウル駅（1号線・祭基洞駅へ）"
                "または孔徳駅（6号線・安岩駅へ）で乗り換え。"
            ),
            "map_note": "地図アプリで開く："
        },
        "checkin": {
            "contact_title": "0. お問い合わせ・緊急連絡先",
            "contact_desc": "ご滞在中に何かございましたら、Airbnbメッセージまたは下記メッセンジャーよりいつでもご連絡ください。",
            "door_title": "1. 玄関スマートロック & Wi-Fi",
            "door_alert": (
                "⚠️ <b>暗証番号の前後に必ずアスタリスク(*)を押してください！</b><br>"
                "入力順：<b>[ * ] + [ 4桁の暗証番号 ] + [ * ]</b>"
            ),
            "door_desc": "暗証番号はチェックイン前にAirbnbメッセージでお送りします。右上のコピーアイコンでWi-Fi情報をコピーできます。",
            "rules_title": "2. ハウスルール（お守りください）",
            "rules": [
                "<b>お静かに（22:00〜07:00）：</b>夜22時以降は近隣住民へのご配慮をお願いいたします。",
                "<b>室内では靴を脱ぐ：</b>玄関で靴を脱ぎ、備え付けのスリッパをご利用ください。",
                "<b>建物内完全禁煙：</b>電子タバコを含め、建物内はすべて禁煙です。",
                "<b>匂いの強い料理の禁止：</b>焼き魚や匂いの強い調理はご遠慮ください。",
                "<b>22時以降の洗濯機使用禁止：</b>夜間の振動・騒音防止のため、22時以降は洗濯機を使用しないでください。",
                "<b>予約人数以外の立ち入り・宿泊禁止：</b>登録されたゲスト以外の入室は禁止です。",
                "<b>廊下・階段でもお静かに：</b>集合住宅のため、共用階段・廊下ではお静かにご移動ください。"
            ],
            "trash_title": "3. ゴミの分別方法 🗑️",
            "trash_alert": (
                "🚫 <b>生ゴミと他のゴミを絶対に混ぜないでください！</b><br>"
                "韓国のゴミ分別は非常に厳しく、混ぜて捨てると罰金（過怠料）の対象となります。"
            ),
            "trash_basic": [
                "<b>① 生ゴミ（食物残渣）：</b>シンクの上に置かれた<b>生ゴミ専用容器（グリーンカラー）</b>に入れてください。",
                "<b>② 資源ゴミ（紙・ビニール・缶・瓶・プラスチック）：</b><b>冷蔵庫前の分別ゴミ箱</b>へ種類ごとに入れてください。<i>（※食べ残しや汚れは必ず水で綺麗に洗い流してから捨ててください。）</i>",
                "<b>③ 一般ゴミ：</b>その他の一般ゴミは<b>Trashゴミ箱</b>へ捨ててください。",
                "<b>⚠️ 害虫防止のご注意：</b>汚れがついたゴミを室内に長時間放置すると虫が発生する原因になります。長期滞在やゴミが多い場合は必ず屋外の排出場所へお出しください。<i>（未分別・長期放置による虫の発生については責任を負いかねます。）</i>"
            ],
            "trash_long_title": "📦 長期滞在（5泊以上）& ゴミ箱がいっぱいになった時の屋外排出方法",
            "trash_long": [
                "<b>1. 生ゴミ：</b>小さな生ゴミ専用袋（<b>黄色2ℓ または 緑色3ℓ</b>）に入れてお出しください。",
                "<b>2. 資源ゴミ：</b>ゴミ箱にセットされている<b>透明の袋のまま</b>口を縛って外へお出しください。",
                "<b>3. 一般ゴミ（トイレのゴミ含む）：</b><b>白色の従量制ゴミ袋（20ℓ または 50ℓ）</b>に入れて縛り、外へお出しください。",
                "<b>4. ゴミ出し曜日：</b><b>火曜日・木曜日・日曜日</b>（建物前の入り口、<b>電柱の下</b>に置いてください。）",
                "<b>5. ゴミ袋の保管場所：</b>すべてのゴミ袋は<b>シンク下の収納棚</b>にご用意しています。"
            ],
            "checkout_title": "4. チェックアウト前の確認事項（11:00まで）",
            "checkout_items": [
                "使用した食器の洗浄・片付け",
                "ゴミの分別確認",
                "エアコン・オンドル（床暖房）・照明の電源オフ",
                "窓と玄関ドアの施錠確認",
                "お忘れ物（充電器・パスポートなど）がないか確認"
            ]
        },
        "story": {
            "welcome_title": "mongle-stay へようこそ 🐾",
            "welcome_p1": (
                "<b>mongle-stay（モングルステイ）</b>は、ホスト夫婦と愛犬の4歳のビションフリーゼ"
                "<b>「モンイ（mongyi）」</b>の名前から生まれた温かい空間です。"
                "インテリアデザイナーのホスト<b>ミエル（Miel）</b>が自ら空間をデザインしました。"
            ),
            "welcome_p2": (
                "高麗大学エリアの活気と京東市場のローカルな情緒が溶け合う祭基洞で、"
                "暮らすようなソウル旅をお楽しみください。"
            ),
            "rooms_title": "ご予約人数別の寝室ご案内（最大6名）",
            "room_rule_tip": (
                "🛏️ <b>ご予約人数に合わせて寝室をご用意いたします：</b><br>"
                "• <b>4名様以下：</b>寝室2部屋オープン（<b>パレットルーム · アンバールーム</b>）<br>"
                "• <b>5名様以上：</b>寝室3部屋すべてオープン（<b>パレット · アンバー · コージールーム</b>）"
            ),
            "rooms": [
                ("🎨 Room 1 · Palette（パレット）", "柔らかな色合いと心地よい照明が調和するメイン寝室です。"),
                ("🕯️ Room 2 · Amber（アンバー）", "温かみのあるウッド調で落ち着いた休息にぴったりの寝室です。"),
                ("☁️ Room 3 · Cozy（コージー · 5名以上でオープン）", "雲のようにふわふわの寝具で深い眠りをサポートする寝室です。")
            ],
            "note": (
                "※ 正式認可を受けた外国人観光都市民泊施設です。"
                "（愛犬モンイはホストの自宅におり、宿には入りませんのでアレルギーの方もご安心ください。）"
            )
        },
        "local": {
            "card_title": "💳 ソウル交通カードの重要ポイント",
            "card_alert": (
                "⚠️ <b>仁川空港からは「気候同行カード（乗り放題パス）」は利用できません！</b><br>"
                "空港からは通常の<b>T-moneyカード</b>を利用し、ソウル市内到着後にコンビニで気候同行カードを購入・チャージしてください。"
            ),
            "bus_title": "🚌 宿近くのバス停から主要観光地へ直通アクセス",
            "bus_intro": "地下鉄の乗り換えなしで主要スポットへ直行できます。エリアをタップして路線をご確認ください：",
            "areas": [
                ("🛍️ 明洞・乙支路・Nソウルタワー（約20〜25分）", "<b>おすすめバス：</b>105番, 147番, 202番, 261番<br>• 明洞ショッピング、乙支路カフェ街へ乗り換えなしで直通"),
                ("🎨 聖水洞（ソンス）・ソウルの森（約20〜25分）", "<b>おすすめバス：</b>2012番, 2222番, 2416番（または地下鉄2号線 聖水駅）<br>• 最新ポップアップストアやおしゃれカフェ巡りに便利"),
                ("🏯 景福宮・北村韓屋村・光化門（約25〜30分）", "<b>おすすめバス：</b>101番, 152番, 272番, 7211番<br>• チマチョゴリ体験や古宮、韓屋村へ直通アクセス"),
                ("🎸 弘大（ホンデ）・延南洞・新村（約35〜40分）", "<b>おすすめバス：</b>273番（祭基洞・安岩 ➔ 弘大入口 直通の黄金路線！）<br>• 乗り換えなしで弘大エリアへ一本で到着します"),
                ("🏙️ 江南・狎鴎亭・蚕室（約35〜45分）", "<b>おすすめバス：</b>147番, 421番（江南・新沙）/ 2416番・2号線（ロッテワールドタワー）")
            ],
            "spot_title": "🍜 徒歩圏内のローカルおすすめスポット",
            "spots": [
                ("京東市場 & スターバックス京東1960店（徒歩8〜10分）", "ソウル最大級の伝統市場と、古い劇場をリノベーションした話題のスターバックスは必見です。"),
                ("安岩（アナム）大学街グルメ通り（徒歩7〜10分）", "コスパ抜群の韓国料理、チキン、ローカルカフェが夜遅くまで賑わっています。")
            ]
        }
    },
    "中文": {
        "subtitle": "首尔东大门 祭基洞 · 最多可住6人 独享民宿",
        "badge": "入住 15:00 · 退房 11:00",
        "quick": [
            ("📍 位置", "近安岩站 · 祭基洞站"),
            ("🔐 密码锁", "* + 密码 + *"),
            ("📶 Wi-Fi", f"PW: {WIFI_PW}")
        ],
        "tabs": ["🗺️ 交通路线", "🔑 入住·使用指南", "🏡 空间故事", "✨ 周边·公交"],
        "location": {
            "taxi_tag": "🚖 请向出租车司机出示此屏幕",
            "taxi_sub": "温馨提示：搭乘出租车时，直接将下方韩文地址展示给司机即可。",
            "address_title": "民宿地址（点击右上角复制）",
            "address_road": "서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "address_jibun": "英文地址: 203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul",
            "airport_title": "✈️ 仁川国际机场出发路线",
            "airport_limo": (
                "<b>机场大巴 6002路（最推荐）：</b>仁川机场上车 ➔ "
                "<b>“新设洞站”或“东大门站”</b>下车 ➔ 换乘出租车约5~7分钟即达。"
            ),
            "airport_arex": (
                "<b>机场快线(AREX)：</b>在首尔站换乘地铁1号线（祭基洞站）"
                "或孔德站换乘6号线（安岩站）。"
            ),
            "map_note": "点击下方按钮直接打开地图导航："
        },
        "checkin": {
            "contact_title": "0. 咨询及紧急联系方式",
            "contact_desc": "入住期间如有任何需要，请随时通过Airbnb私信或以下社交软件联系我们：",
            "door_title": "1. 智能门锁与 Wi-Fi 指南",
            "door_alert": (
                "⚠️ <b>输入密码前后，请务必按下星号键 (*)！</b><br>"
                "正确顺序：<b>[ * ] + [ 4位数字密码 ] + [ * ]</b>"
            ),
            "door_desc": "专属门锁密码将在入住前通过Airbnb私信发送。点击下方复制图标即可一键复制Wi-Fi信息。",
            "rules_title": "2. 请共同遵守（住宿守则）",
            "rules": [
                "<b>安静时间 (22:00 ~ 07:00)：</b>晚上22:00后请降低音量，以免打扰邻里休息。",
                "<b>室内请脱鞋：</b>进门后请在玄关脱下室外鞋，换穿室内拖鞋。",
                "<b>整栋建筑全面禁烟：</b>包括电子烟在内，室内及整栋楼严禁吸烟。",
                "<b>禁止烹饪气味强烈的食物：</b>为保持室内空气清新，请勿煎烤鱼类或烹制重油烟食物。",
                "<b>22:00后禁止使用洗衣机：</b>为防止夜间震动与噪音扰民，晚上10点后请勿运行洗衣机。",
                "<b>禁止非预订人员访问或留宿：</b>严禁未经登记的访客入内或留宿。",
                "<b>走廊和楼梯也请保持安静：</b>本建筑为居民楼，进出经过楼梯和走廊时请轻声慢行。"
            ],
            "trash_title": "3. 垃圾分类指南 🗑️",
            "trash_alert": (
                "🚫 <b>切勿将厨余垃圾与其他垃圾混合投放！</b><br>"
                "韩国垃圾分类法规非常严格，违规混合投放将面临罚款。"
            ),
            "trash_basic": [
                "<b>① 厨余垃圾：</b>请倒入水槽上方放置的<b>绿色厨余垃圾专用桶</b>内。",
                "<b>② 可回收垃圾（纸类/塑料袋/易拉罐/玻璃瓶/塑料瓶）：</b>请按类别放入<b>冰箱前方的分类垃圾桶</b>。<i>（※沾有食物残渣的容器，请务必用水冲洗干净后再投放。）</i>",
                "<b>③ 一般垃圾：</b>其他不可回收垃圾请放入 <b>Trash 垃圾桶</b>。",
                "<b>⚠️ 防虫提示：</b>沾有食物的垃圾若长时间留在室内极易滋生虫害。长住或垃圾较多时请务必及时丢弃至室外指定地点。<i>（因未分类或长期放置导致的虫害问题，民宿恕不负责。）</i>"
            ],
            "trash_long_title": "📦 长住客人（5晚以上）及垃圾桶装满时的室外投放方法",
            "trash_long": [
                "<b>1. 厨余垃圾：</b>请装入小型厨余专用袋（<b>黄色2ℓ 或 绿色3ℓ</b>）中扎紧丢弃。",
                "<b>2. 可回收垃圾：</b>直接将分类桶内套好的<b>透明塑料袋</b>扎紧拿到室外丢弃即可。",
                "<b>3. 一般垃圾（含卫生间垃圾）：</b>请装入<b>白色计量垃圾袋（20ℓ 或 50ℓ）</b>扎紧后拿到室外丢弃。",
                "<b>4. 垃圾投放日：</b><b>每周二、周四、周日</b>（请放置于<b>建筑正门入口处的电线杆下方</b>。）",
                "<b>5. 垃圾袋存放位置：</b>所有备用垃圾袋均存放在<b>厨房水槽下方的橱柜内</b>。"
            ],
            "checkout_title": "4. 退房前确认清单（11:00前）",
            "checkout_items": [
                "清洗并整理使用过的餐具",
                "确认已完成垃圾分类",
                "关闭空调、地暖（锅炉）及所有灯光",
                "确认门窗已关好并锁好大门",
                "检查是否有遗漏的随身物品（充电器、护照等）"
            ]
        },
        "story": {
            "welcome_title": "欢迎来到 mongle-stay 🐾",
            "welcome_p1": (
                "<b>mongle-stay</b> 源于房东夫妇与4岁可爱比熊犬 <b>“Mongyi（蒙伊）”</b> 的名字。"
                "由室内设计师房东 <b>Miel</b> 亲自设计与布置，为您提供家一般的温暖休憩空间。"
            ),
            "welcome_p2": (
                "坐落于高丽大学青春活力与京东市场烟火气交融的祭基洞，"
                "带您体验最地道的首尔生活。"
            ),
            "rooms_title": "按入住人数开放卧室说明（最多6人）",
            "room_rule_tip": (
                "🛏️ <b>我们将根据您的预订人数准备相应卧室：</b><br>"
                "• <b>4人及以下预订：</b>开放2间卧室（<b>调色盘房 · 琥珀房</b>）<br>"
                "• <b>5人及以上预订：</b>开放全部3间卧室（<b>调色盘房 · 琥珀房 · 惬意房</b>）"
            ),
            "rooms": [
                ("🎨 Room 1 · Palette（调色盘房）", "柔和色彩与温馨灯光交织的主卧室。"),
                ("🕯️ Room 2 · Amber（琥珀房）", "温暖木质色调，专注于安静放松的独立卧室。"),
                ("☁️ Room 3 · Cozy（惬意房 · 5人以上开放）", "云朵般柔软亲肤的床品，助您一夜好眠。")
            ],
            "note": (
                "※ 本民宿为政府正式注册的合法外国人观光城市民宿。"
                "（爱犬Mongyi住在房东家中，绝不会进入民宿，易过敏客人请放心入住。）"
            )
        },
        "local": {
            "card_title": "💳 首尔交通卡实用贴士",
            "card_alert": (
                "⚠️ <b>从仁川机场出发时无法使用“气候同行卡（无限次通票）”！</b><br>"
                "机场进市区请先使用普通 <b>T-money卡</b>，抵达首尔市区后可在便利店购买并充值气候同行卡。"
            ),
            "bus_title": "🚌 门口公交直达首尔各大热门景点",
            "bus_intro": "无需换乘地铁，步行至附近公交站即可一线直达各大商圈。点击下方区域查看路线：",
            "areas": [
                ("🛍️ 明洞 · 乙支路 · N首尔塔（约20~25分钟）", "<b>推荐公交：</b>105路, 147路, 202路, 261路<br>• 一线直达明洞购物街、乙支路网红咖啡巷及南山塔接驳站"),
                ("🎨 圣水洞 · 首尔林（约20~25分钟）", "<b>推荐公交：</b>2012路, 2222路, 2416路（或地铁2号线圣水站）<br>• 轻松打卡圣水潮流快闪店与首尔林公园"),
                ("🏯 景福宫 · 北村韩屋村 · 光化门（约25~30分钟）", "<b>推荐公交：</b>101路, 152路, 272路, 7211路<br>• 直达景福宫韩服体验区、北村韩屋村及光化门广场"),
                ("🎸 弘大入口 · 延南洞 · 新村（约35~40分钟）", "<b>推荐公交：</b>273路（祭基洞·安岩 ➔ 弘大入口直达黄金线路！）<br>• 零换乘直达弘大街头表演区与延南洞咖啡街"),
                ("🏙️ 江南 · 狎鸥亭 · 蚕室（约35~45分钟）", "<b>推荐公交：</b>147路, 421路（江南/新沙）/ 2416路或地铁2号线（乐天世界大厦）")
            ],
            "spot_title": "🍜 步行可达的本地宝藏去处",
            "spots": [
                ("京东市场 & 星巴克京东1960店（步行8~10分钟）", "必打卡首尔规模最大的传统市场，以及由老剧场改造的复古网红星巴克。"),
                ("安岩大学街美食巷（步行7~10分钟）", "性价比超高的韩式烤肉、炸鸡与特色咖啡馆营业至深夜。")
            ]
        }
    }
}

# ---------------------------------------------------------
# 4. 상단 언어 선택 & 슬림 헤더 + 퀵 바
# ---------------------------------------------------------
lang = st.radio(
    "Language",
    ["한국어", "English", "日本語", "中文"],
    horizontal=True,
    label_visibility="collapsed"
)
t = CONTENT[lang]

# 슬림 히어로 헤더
st.markdown(f"""
<div class="hero-slim">
    <div>
        <h1>🐾 mongle-stay</h1>
        <p>{t['subtitle']}</p>
    </div>
    <div class="hero-badge">{t['badge']}</div>
</div>
""", unsafe_allow_html=True)

# 상단 3열 퀵 바
q1, q2, q3 = t["quick"]
st.markdown(f"""
<div class="quick-grid">
    <div class="quick-item">
        <div class="quick-label">{q1[0]}</div>
        <div class="quick-val">{q1[1]}</div>
    </div>
    <div class="quick-item">
        <div class="quick-label">{q2[0]}</div>
        <div class="quick-val">{q2[1]}</div>
    </div>
    <div class="quick-item">
        <div class="quick-label">{q3[0]}</div>
        <div class="quick-val">{q3[1]}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. 메인 4개 탭 구성
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(t["tabs"])

# [TAB 1] 오시는 길 + 택시 기사님용 큰 글씨 카드
with tab1:
    loc = t["location"]

    st.markdown(f"""
    <div class="taxi-card">
        <div class="taxi-tag">{loc['taxi_tag']}</div>
        <div class="taxi-kr-main">
            “기사님, 동대문구 안암로18길 3<br>고려맨션으로 가주세요.”
        </div>
        <div class="taxi-kr-sub">
            📍 서울 동대문구 제기동 137-273 (안암오거리 · 고대앞삼거리 인근)
        </div>
        <p style="font-size:0.82rem; color:#7A746E; margin-top:0.6rem; margin-bottom:0;">
            {loc['taxi_sub']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <h3>{loc['address_title']}</h3>
        <p style="margin-bottom:0.2rem;">{loc['address_road']}</p>
        <p style="font-size:0.84rem; color:#7A746E;">{loc['address_jibun']}</p>
    </div>
    """, unsafe_allow_html=True)
    st.code("서울특별시 동대문구 안암로18길 3, 고려맨션 203호", language="text")

    st.markdown(f"""
    <div class="info-card">
        <h3>{loc['airport_title']}</h3>
        <p>• {loc['airport_limo']}</p>
        <p>• {loc['airport_arex']}</p>
        <div class="tip-box">{loc['map_note']}</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🟢 Naver Map", "https://map.naver.com/v5/search/%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EB%8F%99%EB%8C%80%EB%AC%B8%EA%B5%AC%20%EC%95%88%EC%95%94%EB%A1%9C18%EA%B8%B8%203", use_container_width=True)
    with col2:
        st.link_button("🔵 Google Maps", "https://www.google.com/maps/search/?api=1&query=3+Anam-ro+18-gil+Dongdaemun-gu+Seoul", use_container_width=True)

# [TAB 2] 체크인 · 이용안내 · 분리수거 · 체크아웃
with tab2:
    c = t["checkin"]

    # 0. 비상 연락처
    st.markdown(f"""
    <div class="info-card">
        <h3>{c['contact_title']}</h3>
        <p>{c['contact_desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    st.code(f"WeChat ID   : {WECHAT_ID}\nLINE ID     : {LINE_ID}\nKakaoTalk ID: {KAKAO_ID}", language="text")

    # 1. 도어락 & Wi-Fi
    st.markdown(f"""
    <div class="info-card">
        <h3>{c['door_title']}</h3>
        <div class="alert-box">{c['door_alert']}</div>
        <p>{c['door_desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    st.code(f"5G Wi-Fi  : {WIFI_5G}\n2.4G Wi-Fi: {WIFI_24G}\nPassword  : {WIFI_PW}", language="text")

    # 2. 함께 지켜주세요
    rules_html = "".join([f"<li>{item}</li>" for item in c["rules"]])
    st.markdown(f"""
    <div class="info-card">
        <h3>{c['rules_title']}</h3>
        <ul style="padding-left: 1.2rem; margin: 0;">{rules_html}</ul>
    </div>
    """, unsafe_allow_html=True)

    # 3. 쓰레기 분리수거 & 장기숙박 외부 배출 아코디언
    trash_basic_html = "".join([f"<p>{item}</p>" for item in c["trash_basic"]])
    st.markdown(f"""
    <div class="info-card" style="margin-bottom:0.5rem;">
        <h3>{c['trash_title']}</h3>
        <div class="alert-box">{c['trash_alert']}</div>
        {trash_basic_html}
    </div>
    """, unsafe_allow_html=True)

    trash_long_html = "".join([f"<li>{item}</li>" for item in c["trash_long"]])
    with st.expander(c["trash_long_title"]):
        st.markdown(f"<ul style='padding-left:1.2rem; margin:0; font-size:0.9rem; line-height:1.6;'>{trash_long_html}</ul>", unsafe_allow_html=True)

    # 4. 체크아웃 전 확인
    checkout_html = "".join([f"<li>☑️ {item}</li>" for item in c["checkout_items"]])
    st.markdown(f"""
    <div class="info-card" style="margin-top:0.85rem;">
        <h3>{c['checkout_title']}</h3>
        <ul style="list-style:none; padding-left:0.2rem; margin:0;">{checkout_html}</ul>
    </div>
    """, unsafe_allow_html=True)

# [TAB 3] 공간 스토리 & 인원별 객실 안내
with tab3:
    s = t["story"]
    st.markdown(f"""
    <div class="info-card">
        <h3>{s['welcome_title']}</h3>
        <p>{s['welcome_p1']}</p>
        <p>{s['welcome_p2']}</p>
        <div class="tip-box">{s['note']}</div>
    </div>
    """, unsafe_allow_html=True)

    rooms_html = "".join([
        f'<div class="room-pill"><strong>{r[0]}</strong><p style="margin:0.2rem 0 0 0; font-size:0.88rem;">{r[1]}</p></div>'
        for r in s["rooms"]
    ])
    st.markdown(f"""
    <div class="info-card">
        <h3>{s['rooms_title']}</h3>
        <div class="tip-box">{s['room_rule_tip']}</div>
        {rooms_html}
    </div>
    """, unsafe_allow_html=True)

# [TAB 4] 로컬 · 교통
with tab4:
    l = t["local"]
    st.markdown(f"""
    <div class="info-card">
        <h3>{l['card_title']}</h3>
        <div class="alert-box">{l['card_alert']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card" style="margin-bottom:0.5rem;">
        <h3>{l['bus_title']}</h3>
        <p style="margin-bottom:0;">{l['bus_intro']}</p>
    </div>
    """, unsafe_allow_html=True)

    for area_title, area_desc in l["areas"]:
        with st.expander(area_title):
            st.markdown(f"<p style='font-size:0.9rem; line-height:1.6; margin:0;'>{area_desc}</p>", unsafe_allow_html=True)

    spots_html = "".join([
        f'<div class="room-pill"><strong>{sp[0]}</strong><p style="margin:0.2rem 0 0 0; font-size:0.88rem;">{sp[1]}</p></div>'
        for sp in l["spots"]
    ])
    st.markdown(f"""
    <div class="info-card" style="margin-top:0.85rem;">
        <h3>{l['spot_title']}</h3>
        {spots_html}
    </div>
    """, unsafe_allow_html=True)
