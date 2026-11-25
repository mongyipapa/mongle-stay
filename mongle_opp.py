import streamlit as st

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
# 2. 커스텀 CSS (모바일 최적화 · 슬림 헤더 · 택시 카드 · 아코디언 스타일)
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Noto+Sans+JP:wght@400;500;700&family=Noto+Sans+SC:wght@400;500;700&display=swap');

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

    /* 언어 선택 라디오 버튼 */
    div[data-testid="stRadio"] > div {
        justify-content: center;
        gap: 0.35rem;
        margin-bottom: 0.4rem;
    }
    div[data-testid="stRadio"] label {
        background-color: #FFFFFF;
        padding: 0.25rem 0.65rem;
        border-radius: 18px;
        border: 1px solid #E0D8CE;
        font-size: 0.82rem;
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
            ("📶 Wi-Fi", "아래 탭에서 복사")
        ],
        "tabs": ["🔑 체크인·Wi-Fi", "🗺️ 오시는 길", "🏡 공간 스토리", "✨ 로컬·교통"],
        "checkin": {
            "door_title": "1. 현관 도어락 & 입실 안내",
            "door_alert": "⚠️ <b>비밀번호 앞과 뒤에 반드시 별표(*)를 눌러주세요!</b><br>입력 순서: <b>[ * ] + [ 비밀번호 4자리 ] + [ * ]</b>",
            "door_desc": "보안을 위해 예약 확정 후 에어비앤비 메시지로 개별 비밀번호를 보내드립니다. 현관에 들어서시면 실외화를 벗고 비치된 실내화를 착용해 주세요.",
            "wifi_title": "2. 무료 초고속 Wi-Fi",
            "wifi_desc": "우측 상단 복사 아이콘을 누르면 비밀번호가 바로 복사됩니다. (상세 정보는 메시지 안내와 동일)",
            "rules_title": "3. 이용 수칙 & 분리수거",
            "rules": [
                "<b>실내 절대 금연:</b> 전자담배 포함 건물 전체 금연입니다.",
                "<b>정숙 시간:</b> 밤 10시 이후에는 이웃을 위해 소음을 줄여주세요.",
                "<b>분리수거:</b> 일반쓰레기 / 재활용(플라스틱·캔·유리) / 음식물 쓰레기를 주방 옆 전용함에 나누어 담아주세요.",
                "<b>외출 시 소등:</b> 외출하실 때는 에어컨, 보일러, 조명을 꺼주시면 감사하겠습니다."
            ]
        },
        "location": {
            "taxi_tag": "🚖 택시 기사님께 이 화면을 보여주세요",
            "taxi_sub": "게스트 안내: 택시나 길 안내가 필요할 때 아래 한국어 주소를 기사님께 그대로 보여주세요.",
            "address_title": "숙소 주소 (복사용)",
            "address_road": "서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "address_jibun": "지번: 서울특별시 동대문구 제기동 137-273, 고려맨션 203호",
            "airport_title": "✈️ 인천공항에서 오시는 길",
            "airport_limo": "<b>공항리무진 6002번 (가장 편리):</b> 인천공항 승차 ➔ <b>'신설동역' 또는 '동대문역'</b> 하차 ➔ 택시로 약 5~7분 이동",
            "airport_arex": "<b>공항철도(AREX):</b> 서울역 또는 홍대입구역 하차 ➔ 지하철 1호선(제기동역) 또는 6호선(안암역) 환승",
            "map_note": "아래 버튼으로 지도를 바로 열 수 있습니다."
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
                ("홍대입구 · 연남동 · 신촌 (약 35~40분)", "<b>추천 버스:</b> 273번 (제기동·안암 ➔ 홍대입구 직통 황금노선!)<br>• 환승 없이 한 번에 홍대 쇼핑·버스킹·연남동 카페거리 도착"),
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
            ("📶 Wi-Fi", "Copy in Tab 1")
        ],
        "tabs": ["🔑 Check-in·Wi-Fi", "🗺️ Directions", "🏡 Story", "✨ Local·Transit"],
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
        "location": {
            "taxi_tag": "🚖 SHOW THIS TO YOUR TAXI DRIVER",
            "taxi_sub": "Tip: Show the large Korean address below directly to your taxi driver.",
            "address_title": "Property Address (Tap to Copy)",
            "address_road": "203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul",
            "address_jibun": "Korean: 서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "airport_title": "✈️ From Incheon Airport (ICN)",
            "airport_limo": "<b>Airport Limousine Bus #6002 (Easiest):</b> Board at ICN ➔ Get off at <b>Sinseol-dong Stn.</b> or <b>Dongdaemun Stn.</b> ➔ Take a 5–7 min taxi ride.",
            "airport_arex": "<b>AREX Airport Train:</b> Transfer at Seoul Stn. (Line 1 to Jegi-dong Stn.) or Gongdeok Stn. (Line 6 to Anam Stn.).",
            "map_note": "Open directly in your preferred map app:"
        },
        "story": {
            "welcome_title": "Welcome to mongle-stay 🐾",
            "welcome_p1": "<b>mongle-stay</b> is a warm, thoughtfully curated retreat named after our beloved 4-year-old Bichon Frise, <b>Mongyi</b>. Designed by interior designer host <b>Miel</b>, every corner is crafted for comfort and calm.",
            "welcome_p2": "Located in Jegi-dong—where university energy meets authentic traditional markets—experience the real rhythm of Seoul.",
            "rooms_title": "3 Private Bedrooms (Up to 6 Guests)",
            "rooms": [
                ("🎨 Room 1 · Palette", "Our main bedroom featuring soft pastel tones and cozy ambient lighting."),
                ("🕯️ Room 2 · Amber", "Designed with warm wood accents for deep, peaceful rest."),
                ("☁️ Room 3 · Cozy", "Cloud-soft bedding tailored for a restful night's sleep.")
            ],
            "note": "※ Officially licensed Foreign Tourist Urban Homestay. (Our dog Mongyi lives at our separate residence and never enters the guest house—no allergy worries!)"
        },
        "local": {
            "card_title": "💳 Seoul Transit Card Essential Tip",
            "card_alert": "⚠️ <b>Climate Card (Unlimited Pass) CANNOT be used from Incheon Airport!</b><br>Use a standard <b>T-money card</b> from the airport, then buy/top up a Climate Card at any Seoul convenience store.",
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
            ("📶 Wi-Fi", "タブ1でコピー")
        ],
        "tabs": ["🔑 チェックイン", "🗺️ アクセス", "🏡 ストーリー", "✨ 周辺・交通"],
        "checkin": {
            "door_title": "1. 玄関スマートロックの開け方",
            "door_alert": "⚠️ <b>暗証番号の前後に必ずアスタリスク(*)を押してください！</b><br>入力順：<b>[ * ] + [ 4桁の暗証番号 ] + [ * ]</b>",
            "door_desc": "防犯のため、暗証番号はチェックイン前にAirbnbメッセージでお送りします。玄関では靴を脱ぎ、備え付けのスリッパをご利用ください。",
            "wifi_title": "2. 無料高速 Wi-Fi",
            "wifi_desc": "枠の右上にあるコピーアイコンをタップするとパスワードがコピーされます。",
            "rules_title": "3. ハウスルール & ゴミ分別",
            "rules": [
                "<b>建物内完全禁煙：</b>電子タバコを含め、建物内はすべて禁煙です。",
                "<b>お静かに：</b>夜22時以降は近隣住民へのご配慮をお願いいたします。",
                "<b>ゴミの分別：</b>一般ゴミ・資源ゴミ（プラ・缶・瓶）・生ゴミをキッチン横の専用ゴミ箱へ分別してください。",
                "<b>節電のお願い：</b>外出時はエアコン・オンドル（床暖房）・照明をお切りください。"
            ]
        },
        "location": {
            "taxi_tag": "🚖 タクシー運転手さんにこの画面を見せてください",
            "taxi_sub": "ご案内：タクシーに乗車する際は、下の韓国語住所をそのまま運転手さんにお見せください。",
            "address_title": "宿泊施設 住所（コピー用）",
            "address_road": "서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "address_jibun": "英語表記: 203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul",
            "airport_title": "✈️ 仁川国際空港からのアクセス",
            "airport_limo": "<b>空港リムジンバス 6002番（一番おすすめ）：</b>仁川空港乗車 ➔ <b>「新設洞駅」または「東大門駅」</b>下車 ➔ タクシーで約5〜7分",
            "airport_arex": "<b>空港鉄道(AREX)：</b>ソウル駅（1号線・祭基洞駅へ）または孔徳駅（6号線・安岩駅へ）で乗り換え。",
            "map_note": "地図アプリで開く："
        },
        "story": {
            "welcome_title": "mongle-stay へようこそ 🐾",
            "welcome_p1": "<b>mongle-stay（モングルステイ）</b>は、ホスト夫婦と愛犬の4歳のビションフリーゼ<b>「モンイ（mongyi）」</b>の名前から生まれた温かい空間です。インテリアデザイナーのホスト<b>ミエル（Miel）</b>が自ら空間をデザインしました。",
            "welcome_p2": "高麗大学エリアの活気と京東市場のローカルな情緒が溶け合う祭基洞で、暮らすようなソウル旅をお楽しみください。",
            "rooms_title": "3つの独立したベッドルーム（最大6名）",
            "rooms": [
                ("🎨 Room 1 · Palette（パレット）", "柔らかな色合いと心地よい照明が調和するメイン寝室です。"),
                ("🕯️ Room 2 · Amber（アンバー）", "温かみのあるウッド調で落ち着いた休息にぴったりの寝室です。"),
                ("☁️ Room 3 · Cozy（コージー）", "雲のようにふわふわの寝具で深い眠りをサポートする寝室です。")
            ],
            "note": "※ 正式認可を受けた外国人観光都市民泊施設です。（愛犬モンイはホストの自宅におり、宿には入りませんのでアレルギーの方もご安心ください。）"
        },
        "local": {
            "card_title": "💳 ソウル交通カードの重要ポイント",
            "card_alert": "⚠️ <b>仁川空港からは「気候同行カード（乗り放題パス）」は利用できません！</b><br>空港からは通常の<b>T-moneyカード</b>を利用し、ソウル市内到着後にコンビニで気候同行カードを購入・チャージしてください。",
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
            ("📶 Wi-Fi", "第1页一键复制")
        ],
        "tabs": ["🔑 入住·Wi-Fi", "🗺️ 交通路线", "🏡 空间故事", "✨ 周边·公交"],
        "checkin": {
            "door_title": "1. 智能门锁与入住指南",
            "door_alert": "⚠️ <b>输入密码前后，请务必按下星号键 (*)！</b><br>正确顺序：<b>[ * ] + [ 4位数字密码 ] + [ * ]</b>",
            "door_desc": "为保障安全，您的专属密码将在入住前通过Airbnb私信发送。进门后请脱下室外鞋，换上玄关准备的室内拖鞋。",
            "wifi_title": "2. 免费高速 Wi-Fi",
            "wifi_desc": "点击下方框体右上角的复制图标即可一键复制密码。",
            "rules_title": "3. 住宿守则与垃圾分类",
            "rules": [
                "<b>室内严禁吸烟：</b>整栋建筑（含电子烟）全面禁烟。",
                "<b>安静时间：</b>晚上22:00后请降低音量，以免打扰邻里休息。",
                "<b>垃圾分类：</b>请将一般垃圾、可回收物（塑料/易拉罐/玻璃）及厨余垃圾分别放入厨房旁的分类桶中。",
                "<b>节约能源：</b>外出时请关闭空调、地暖（锅炉）和室内灯光。"
            ]
        },
        "location": {
            "taxi_tag": "🚖 请向出租车司机出示此屏幕",
            "taxi_sub": "温馨提示：搭乘出租车时，直接将下方韩文地址展示给司机即可。",
            "address_title": "民宿地址（点击复制）",
            "address_road": "서울특별시 동대문구 안암로18길 3, 고려맨션 203호",
            "address_jibun": "英文地址: 203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul",
            "airport_title": "✈️ 仁川国际机场出发路线",
            "airport_limo": "<b>机场大巴 6002路（最推荐）：</b>仁川机场上车 ➔ <b>“新设洞站”或“东大门站”</b>下车 ➔ 换乘出租车约5~7分钟即达。",
            "airport_arex": "<b>机场快线(AREX)：</b>在首尔站换乘地铁1号线（祭基洞站）或孔德站换乘6号线（安岩站）。",
            "map_note": "点击下方按钮直接打开地图导航："
        },
        "story": {
            "welcome_title": "欢迎来到 mongle-stay 🐾",
            "welcome_p1": "<b>mongle-stay</b> 源于房东夫妇与4岁可爱比熊犬 <b>“Mongyi（蒙伊）”</b> 的名字。由室内设计师房东 <b>Miel</b> 亲自设计与布置，为您提供家一般的温暖休憩空间。",
            "welcome_p2": "坐落于高丽大学青春活力与京东市场烟火气交融的祭基洞，带您体验最地道的首尔生活。",
            "rooms_title": "3间独立卧室布局（最多6人）",
            "rooms": [
                ("🎨 Room 1 · Palette（调色盘）", "柔和色彩与温馨灯光交织的主卧室。"),
                ("🕯️ Room 2 · Amber（琥珀）", "温暖木质色调，专注于安静放松的独立卧室。"),
                ("☁️ Room 3 · Cozy（惬意）", "云朵般柔软亲肤的床品，助您一夜好眠。")
            ],
            "note": "※ 本民宿为政府正式注册的合法外国人观光城市民宿。（爱犬Mongyi住在房东家中，绝不会进入民宿，易过敏客人请放心入住。）"
        },
        "local": {
            "card_title": "💳 首尔交通卡实用贴士",
            "card_alert": "⚠️ <b>从仁川机场出发时无法使用“气候同行卡（无限次通票）”！</b><br>机场进市区请先使用普通 <b>T-money卡</b>，抵达首尔市区后可在便利店购买并充值气候同行卡。",
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
# 5. 메인 4개 탭 구성 (여행자 동선 우선순위 정렬)
# ---------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(t["tabs"])

# [TAB 1] 체크인 · Wi-Fi
with tab1:
    c = t["checkin"]
    st.markdown(f"""
    <div class="info-card">
        <h3>{c['door_title']}</h3>
        <div class="alert-box">{c['door_alert']}</div>
        <p>{c['door_desc']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <h3>{c['wifi_title']}</h3>
        <p>{c['wifi_desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    # 실제 Wi-Fi ID와 비밀번호로 수정해서 사용하세요
    st.code("Wi-Fi ID : mongle-stay_5G\nPassword : Check Airbnb Message (메시지 확인)", language="text")

    rules_html = "".join([f"<li>{item}</li>" for item in c["rules"]])
    st.markdown(f"""
    <div class="info-card">
        <h3>{c['rules_title']}</h3>
        <ul style="padding-left: 1.2rem; margin: 0;">{rules_html}</ul>
    </div>
    """, unsafe_allow_html=True)

# [TAB 2] 오시는 길 + 택시 기사님용 큰 글씨 카드
with tab2:
    loc = t["location"]

    # 택시 기사님 보여주기 카드 (항상 한국어 큰 글씨 고정)
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

# [TAB 3] 공간 스토리
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
        {rooms_html}
    </div>
    """, unsafe_allow_html=True)

# [TAB 4] 로컬 · 교통 (아코디언 UI 적용)
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

    # 권역별 아코디언 카드
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
