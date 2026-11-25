import streamlit as st

# 1. 페이지 기본 설정 (모바일 및 데스크탑 반응형)
st.set_page_config(
    page_title="mongle-stay | Guest Guidebook",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 커스텀 CSS (크림 아이보리 & 세이지 그린 감성 디자인)
st.markdown("""
<style>
    .stApp {
        background-color: #FAF9F6;
        color: #3C4043;
    }
    .hero-box {
        background: linear-gradient(135deg, #2E5A44 0%, #4A7C62 100%);
        color: #FFFFFF;
        padding: 26px 22px;
        border-radius: 20px;
        margin-top: 8px;
        margin-bottom: 18px;
        box-shadow: 0 8px 20px rgba(46, 90, 68, 0.15);
        text-align: center;
    }
    .hero-title {
        font-size: 25px;
        font-weight: 700;
        margin: 0 0 6px 0;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 13.5px;
        opacity: 0.92;
        margin: 0;
    }
    .info-card {
        background-color: #FFFFFF;
        border: 1px solid #E8E4DC;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
    }
    .card-title {
        font-size: 16.5px;
        font-weight: 700;
        color: #2E5A44;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .card-text {
        font-size: 14.5px;
        line-height: 1.65;
        color: #4A4E52;
        margin: 0;
    }
    .story-quote {
        border-left: 3px solid #4A7C62;
        padding-left: 12px;
        margin: 10px 0;
        color: #3C4043;
        font-size: 14px;
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
        font-size: 11.5px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        margin-bottom: 8px;
    }
    .map-btn {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #2E5A44;
        color: #FFFFFF !important;
        text-decoration: none;
        padding: 12px 0;
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
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #EFECE6;
        padding: 6px;
        border-radius: 14px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 8px 10px;
        font-size: 13px;
        font-weight: 600;
        color: #5F6368;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF !important;
        color: #2E5A44 !important;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    div[role="radiogroup"] {
        justify-content: center;
        gap: 8px;
    }
</style>
""", unsafe_allow_html=True)

# 3. 4개 국어 다국어 콘텐츠 사전 (한국어 / 영어 / 일본어 / 중국어)
CONTENT = {
    "🇰🇷 한국어": {
        "title": "mongle-stay (몽글스테이)",
        "subtitle": "6호선 안암역 도보 5분 · 따뜻한 쉼과 서울의 로컬 감성이 머무는 공간",
        "tabs": ["🏡 스토리", "🗺️ 오시는 길", "🔑 체크인·Wi-Fi", "✨ 로컬·교통"],
        # TAB 1: 스토리 & 공간 안내
        "t1_story_title": "🎨 Mongle Stay Story (Curated by miel Yi)",
        "t1_story_body": """
        몽글스테이는 서로 다른 나라와 도시에서 온 여행자들이 서울의 일상을 편안하게 경험할 수 있도록 만든 집입니다. 좋아하는 음악과 문화는 달라도, 여행지에서 느끼는 설렘과 새로운 이야기를 발견하는 기쁨은 서로 닮아 있습니다. 몽글스테이에 머무는 시간이 단순한 숙박을 넘어, 자신만의 서울 취향과 기억을 발견하는 시간이 되기를 바랍니다.
        <div class='story-quote'>
            <b>• 취향:</b> 각기 다른 색과 분위기를 가진 공간에서 나에게 가장 편안한 방식으로 머물러보세요.<br>
            <b>• 연결:</b> K컬처와 안암의 일상, 서울의 오래된 시장과 새로운 문화를 함께 만나보세요.<br>
            <b>• 안심:</b> 낯선 도시에서도 내 집처럼 편안하게 머물 수 있도록 깨끗한 공간과 세심한 안내를 준비했습니다.
        </div>
        """,
        "t1_rooms_title": "🛏️ 세 개의 방 이야기 & 인원별 객실 안내",
        "t1_rooms_body": """
        • <b>Palette Room:</b> 서로 다른 색과 취향이 자연스럽게 어우러지는 방<br>
        • <b>Amber Room:</b> 따뜻한 빛처럼 편안하게 하루를 마무리하는 방<br>
        • <b>Cozy Room:</b> 작지만 온전히 나만의 시간을 보낼 수 있는 아늑한 방<br><br>
        <span style='font-size: 13.5px; color: #8C5A3C;'>※ <b>인원별 객실 세팅 안내:</b> 예약 인원에 맞춰 객실이 준비됩니다.<br>
        &nbsp;&nbsp;- <b>4인 이하:</b> 침실 2개 개방 (Palette Room / Amber Room)<br>
        &nbsp;&nbsp;- <b>5인 이상:</b> 침실 3개 전체 개방 (Palette / Amber / Cozy Room)</span>
        """,
        "t1_floorplan_caption": "📐 몽글스테이 3D 공간 구조 및 객실 배치도",
        # TAB 2: 오시는 길
        "t2_loc_title": "📍 숙소 주소 및 지도 앱 열기",
        "t2_loc_body": "<b>도로명 주소:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br><b>영문 주소:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br><b>가까운 역:</b> 지하철 6호선 <b>안암역(Anam Station) 3번 출구</b> 도보 5분",
        "t2_btn_naver": "🟢 네이버 지도로 길찾기 (한국 내 가장 정확)",
        "t2_btn_google": "🗺️ Google Maps로 열기",
        "t2_sub_title": "🚉 지하철 6호선 안암역에서 오시는 법",
        "t2_sub_body": "• <b>지하철 6호선 안암역(고대병원앞) 3번 출구</b>로 나오세요.<br>• 3번 출구에서 안암오거리·제기시장 방면으로 직진 후 <b>안암로18길</b> 골목으로 진입하시면 <b>도보 약 5분</b> 거리에 '고려맨션' 건물이 위치해 있습니다. (2층 203호)",
        "t2_air_title": "✈️ 공항에서 오시는 방법",
        "t2_air_body": "<b>1. 인천국제공항 (ICN) 출발 (약 75~85분 소요)</b><br>• <b>공항철도 + 지하철 (추천):</b> 공항철도 탑승 ➔ <b>공덕역</b> 또는 <b>디지털미디어시티(DMC)역</b>에서 <b>6호선(신내 방면)</b> 환승 ➔ <b>안암역</b> 하차 (3번 출구 도보 5분)<br>• <b>공항리무진 버스:</b> 6002번 탑승 ➔ '제기동역.서울약령시' 하차 후 택시 기본요금 이동 (약 5분)<br><br><b>2. 김포국제공항 (GMP) 출발 (약 55분 소요)</b><br>• 공항철도 탑승 ➔ <b>디지털미디어시티(DMC)역</b>에서 <b>6호선</b> 환승 ➔ <b>안암역</b> 하차",
        # TAB 3: 체크인 · 도어락 · Wi-Fi
        "t3_time_title": "⏰ 입·퇴실 및 현관 도어락 출입 안내",
        "t3_time_body": """
        • <b>체크인 (Check-in):</b> 오후 3:00 (15:00) 이후<br>
        • <b>체크아웃 (Check-out):</b> 오전 11:00 (11:00) 이전<br>
        <div class='doorlock-box'>
            <b>🔐 현관 도어락 여는 법 (셀프 체크인)</b><br>
            1. 체크인 당일 예약 플랫폼(에어비앤비/트립닷컴/부킹닷컴) 메시지로 발송된 <b>개별 비밀번호</b>를 확인해 주세요.<br>
            2. 도어락 화면을 손바닥으로 터치해 불을 켠 뒤 ➔ <b><code>*</code> + <code>비밀번호</code> + <code>*</code></b> 순서대로 누르시면 문이 열립니다.<br>
            <span style='font-size: 12.5px; color: #5F6368;'>※ 앞뒤로 별표(*)를 꼭 함께 눌러주세요. 외출 시 문이 닫히면 자동으로 잠깁니다.</span>
        </div>
        """,
        "t3_wifi_title": "📶 초고속 무선 인터넷 연결",
        "t3_wifi_body": "원하시는 Wi-Fi와 비밀번호 우측의 복사 아이콘을 눌러 연결하세요.",
        "t3_wifi_ssid": "네트워크 이름 (SSID)",
        "t3_wifi_pw": "비밀번호 (5G · 2.4G 공통)",
        "t3_rules_title": "🌿 쾌적한 머무름을 위한 약속",
        "t3_rules_body": "1. <b>실내 절대 금연:</b> 건물 전체 및 객실 내 흡연(전자담배 포함)은 엄격히 금지됩니다.<br>2. <b>실내화 착용:</b> 현관에서 신발을 벗고 비치된 실내화를 착용해 주세요.<br>3. <b>정숙 시간:</b> 밤 10시(22:00) 이후에는 이웃을 위해 TV 볼륨과 대화를 낮춰주시고, 세탁기 사용을 자제해 주세요.<br>4. <b>요리 및 분리수거:</b> 냄새가 강한 요리는 삼가주시고, 쓰레기는 주방 옆 전용함에 분리배출해 주세요.<br>5. <b>외출 시 전원 확인:</b> 외출하실 때는 냉난방기 및 인덕션 전원을 꼭 꺼주세요.",
        "t3_contact_title": "🐶 호스트 긴급 연락처",
        "t3_contact_body": "머무시는 동안 도움이 필요하시면 언제든 편하게 연락해 주세요.<br>• <b>예약 플랫폼 메시지:</b> 에어비앤비 / 트립닷컴 / 부킹닷컴 앱 내 채팅 (가장 빠름)<br>• <b>메신저 문의:</b> WeChat: <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>",
        # TAB 4: 로컬 명소 & 교통 꿀팁
        "t4_walk_title": "☕ 도보권 핫플레이스 (안암·제기 로컬)",
        "t4_walk_body": "<b>1. 고려대학교 캠퍼스 & 안암동 대학가 맛집 (도보 5~10분)</b><br>• 유럽 고딕 양식의 아름다운 석조 건축물로 유명한 고려대 캠퍼스 산책과, 대학가 특유의 가성비 넘치는 로컬 맛집·카페 거리를 도보로 즐겨보세요.<br><br><b>2. 스타벅스 경동1960점 & 경동시장 (도보 15분 / 버스 5분)</b><br>• 1960년대 폐극장(경동극장)을 개조한 압도적 분위기의 스타벅스 스페셜 매장과, 활기찬 한국 전통시장(경동시장·서울약령시) 먹거리 투어를 추천합니다.<br><br><b>3. 성북천 산책로 (도보 8분)</b><br>• 저녁 식사 후 조명이 예쁘게 켜진 성북천 물길을 따라 여유롭게 산책해 보세요.",
        "t4_city_title": "🏯 서울 핵심 관광지 초간단 이동 루트 (안암역 출발)",
        "t4_city_body": "<b>1. 동대문 디자인 플라자(DDP) & 쇼핑타운 (약 10분)</b><br>• 6호선 안암역 ➔ 2정거장 뒤 <b>동묘앞역</b>에서 1호선 환승 ➔ <b>동대문역</b> 하차<br><br><b>2. 이태원 · 한강진(한남동) · 망원 · 합정 (환승 없이 6호선 직통!)</b><br>• 6호선 안암역에서 한 번에 쭉 이동합니다:<br>&nbsp;&nbsp;- <b>한강진역 (약 18분):</b> 한남동 감성 카페거리 & 리움미술관<br>&nbsp;&nbsp;- <b>이태원역 (약 20분):</b> 이태원 경리단길 & 해방촌<br>&nbsp;&nbsp;- <b>망원역 · 합정역 (약 32분):</b> 망리단길 & 망원시장 & 홍대<br><br><b>3. 광장시장 · 익선동 · 성수동 (약 15~25분)</b><br>• <b>광장시장·익선동:</b> 6호선 안암역 ➔ <b>동묘앞역(1호선 환승)</b> ➔ 종로5가역(광장시장) / 종로3가역(익선동)<br>• <b>성수동 카페거리:</b> 6호선 안암역 ➔ <b>신당역(2호선 환승)</b> ➔ <b>성수역</b> 하차 (약 20분)",
        "t4_trans_title": "💳 서울 대중교통 & 택시 이용 꿀팁",
        "t4_trans_body": "• <b>기후동행카드 (무제한 패스):</b> 1일권(5,000원)~5일권(15,000원)으로 서울 지하철·버스·따릉이를 무제한 이용할 수 있습니다. (안암역 고객안전실 및 편의점 구매)<br>• <b>티머니(T-money) 환승 할인:</b> 버스 하차 시 단말기에 카드를 한 번 더 태그해야 30분 이내 지하철/버스 무료 환승이 적용됩니다.<br>• <b>택시 호출 앱:</b> <b>카카오 T (Kakao T)</b> 또는 <b>Uber</b> 앱에서 '기사님께 직접 결제'를 선택하면 해외 카드 등록 없이도 바로 호출 가능합니다."
    },
    "🇺🇸 English": {
        "title": "mongle-stay Seoul",
        "subtitle": "5-min walk from Anam Stn (Line 6) · Cozy Local Stay in Seoul",
        "tabs": ["🏡 Story", "🗺️ Directions", "🔑 Check-in·Wi-Fi", "✨ Local·Transit"],
        # TAB 1
        "t1_story_title": "🎨 Mongle Stay Story (Curated by miel Yi)",
        "t1_story_body": """
        Mongle Stay is a home created so travelers from different countries and cities can comfortably experience everyday life in Seoul. Even if our favorite music and cultures differ, the excitement of traveling and the joy of discovering new stories connect us all. We hope your time here goes beyond a simple stay—becoming a moment to discover your own taste and memories of Seoul.
        <div class='story-quote'>
            <b>• Taste:</b> Stay in the way that feels most comfortable to you, surrounded by spaces of distinct colors and moods.<br>
            <b>• Connection:</b> Experience K-culture alongside the daily rhythm of Anam, where Seoul's historic markets meet new culture.<br>
            <b>• Peace of Mind:</b> We prepared a spotless home and thoughtful guidance so you feel right at home in an unfamiliar city.
        </div>
        """,
        "t1_rooms_title": "🛏️ Story of Three Rooms & Room Setup",
        "t1_rooms_body": """
        • <b>Palette Room:</b> A room where different colors and personal tastes naturally blend together<br>
        • <b>Amber Room:</b> A room to unwind and end your day peacefully, like a warm glow<br>
        • <b>Cozy Room:</b> A snug, intimate room where you can enjoy quiet time all to yourself<br><br>
        <span style='font-size: 13.5px; color: #8C5A3C;'>※ <b>Room Setup by Guest Count:</b> Rooms are prepared according to your reservation.<br>
        &nbsp;&nbsp;- <b>1–4 Guests:</b> 2 Bedrooms open (Palette Room / Amber Room)<br>
        &nbsp;&nbsp;- <b>5+ Guests:</b> All 3 Bedrooms open (Palette / Amber / Cozy Room)</span>
        """,
        "t1_floorplan_caption": "📐 Mongle Stay 3D Floor Plan & Room Layout",
        # TAB 2
        "t2_loc_title": "📍 Address & Navigation",
        "t2_loc_body": "<b>English Address:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br><b>Korean Address:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br><b>Nearest Subway:</b> <b>Anam Station (Line 6), Exit 3</b> (5-minute walk)",
        "t2_btn_naver": "🟢 Open in Naver Map (Most Accurate in Korea)",
        "t2_btn_google": "🗺️ Open in Google Maps",
        "t2_sub_title": "🚉 From Anam Station (Subway Line 6)",
        "t2_sub_body": "• Come out of <b>Anam Station (Line 6), Exit 3</b>.<br>• Walk straight toward Anam Ogeori / Jegi Market and turn into the <b>Anam-ro 18-gil</b> alley. You will find <b>'Goryeo Mansion'</b> within a <b>5-minute walk</b> (2nd floor, Room 203).",
        "t2_air_title": "✈️ From the Airport",
        "t2_air_body": "<b>1. From Incheon Int'l Airport (ICN) (~75–85 mins)</b><br>• <b>AREX Train + Subway (Recommended):</b> Take AREX All-stop train ➔ Transfer at <b>Gongdeok</b> or <b>Digital Media City (DMC)</b> to <b>Line 6 (Sinnae bound)</b> ➔ Get off at <b>Anam Station</b> (Exit 3, 5-min walk).<br>• <b>Airport Limousine Bus:</b> Take Bus #6002 ➔ Get off at 'Jegi-dong Station / Seoul Yangnyeongsi' ➔ 5-min taxi ride.<br><br><b>2. From Gimpo Int'l Airport (GMP) (~55 mins)</b><br>• Take AREX train ➔ Transfer at <b>DMC Station</b> to <b>Line 6</b> ➔ Get off at <b>Anam Station</b>.",
        # TAB 3
        "t3_time_title": "⏰ Check-in, Check-out & Door Lock Guide",
        "t3_time_body": """
        • <b>Check-in:</b> After 3:00 PM (15:00)<br>
        • <b>Check-out:</b> Before 11:00 AM (11:00)<br>
        <div class='doorlock-box'>
            <b>🔐 How to Unlock the Front Door (Self Check-in)</b><br>
            1. Check your <b>unique passcode</b> sent via booking platform message (Airbnb / Trip.com / Booking.com) on your check-in day.<br>
            2. Touch the keypad with your palm to wake the screen ➔ Enter <b><code>*</code> + <code>Passcode</code> + <code>*</code></b> to unlock.<br>
            <span style='font-size: 12.5px; color: #5F6368;'>※ Be sure to press the asterisk (*) both before and after the passcode. The door locks automatically when closed.</span>
        </div>
        """,
        "t3_wifi_title": "📶 Free High-Speed Wi-Fi",
        "t3_wifi_body": "Tap the copy icon next to your preferred Wi-Fi and password to connect.",
        "t3_wifi_ssid": "Network Name (SSID)",
        "t3_wifi_pw": "Password (Shared for 5G & 2.4G)",
        "t3_rules_title": "🌿 House Rules",
        "t3_rules_body": "1. <b>No Smoking:</b> Smoking (including e-cigarettes) is strictly prohibited inside the room and building.<br>2. <b>Shoes Off Indoors:</b> Please take off your shoes at the entrance and wear the provided indoor slippers.<br>3. <b>Quiet Hours:</b> Please keep noise down after 10:00 PM (22:00) and avoid using the washing machine late at night.<br>4. <b>Cooking & Recycling:</b> Please avoid strong-smelling cooking and separate waste into the bins next to the kitchen.<br>5. <b>Save Energy:</b> Please turn off the A/C, heater, and induction stove when leaving the room.",
        "t3_contact_title": "🐶 Host Contact",
        "t3_contact_body": "Feel free to reach out anytime if you need assistance during your stay.<br>• <b>Booking Platform Chat:</b> Airbnb / Trip.com / Booking.com in-app message (Fastest)<br>• <b>Messenger ID:</b> WeChat: <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>",
        # TAB 4
        "t4_walk_title": "☕ Walking Distance Gems (Anam & Jegi)",
        "t4_walk_body": "<b>1. Korea University Campus & Anam Food Street (5–10 min walk)</b><br>• Stroll through the stunning European Gothic stone architecture of Korea University and enjoy affordable, vibrant local student eateries and cafes.<br><br><b>2. Starbucks Gyeongdong 1960 & Gyeongdong Market (15-min walk / 5-min bus)</b><br>• Visit the viral Starbucks built inside an abandoned 1960s theater, right inside Seoul's largest traditional herbal & food market.<br><br><b>3. Seongbukcheon Stream Trail (8-min walk)</b><br>• Enjoy a peaceful evening walk along the illuminated waterside path.",
        "t4_city_title": "🏯 Direct Routes to Seoul Hotspots (From Anam Stn)",
        "t4_city_body": "<b>1. Dongdaemun Design Plaza (DDP) & Shopping (~10 mins)</b><br>• Take Line 6 to <b>Dongmyo Station</b> (2 stops) ➔ Transfer to Line 1 ➔ <b>Dongdaemun Station</b>.<br><br><b>2. Itaewon · Hannam-dong · Mangwon · Hongdae (Direct on Line 6!)</b><br>• No transfers needed from Anam Station:<br>&nbsp;&nbsp;- <b>Hangangjin Stn (~18 mins):</b> Hannam-dong trendy cafes & Leeum Museum<br>&nbsp;&nbsp;- <b>Itaewon Stn (~20 mins):</b> Itaewon & Haebangchon<br>&nbsp;&nbsp;- <b>Mangwon / Hapjeong Stn (~32 mins):</b> Mangwon Market & Hongdae<br><br><b>3. Gwangjang Market · Ikseon-dong · Seongsu-dong (~15–25 mins)</b><br>• <b>Gwangjang Market / Ikseon-dong:</b> Transfer at <b>Dongmyo Stn</b> to Line 1 ➔ Jongno 5-ga / Jongno 3-ga Stn.<br>• <b>Seongsu-dong (Brooklyn of Seoul):</b> Transfer at <b>Sindang Stn</b> to Line 2 ➔ <b>Seongsu Stn</b> (~20 mins).",
        "t4_trans_title": "💳 Seoul Public Transit & Taxi Tips",
        "t4_trans_body": "• <b>Climate Card (Unlimited Pass):</b> Unlimited rides on Seoul subways, buses, and public bikes (1-Day 5,000 KRW to 5-Day 15,000 KRW). Available at Anam Station office or convenience stores.<br>• <b>T-money Transfer Tip:</b> Always tap your card again when exiting a bus to get free transfers to subways/other buses within 30 minutes!<br>• <b>Taxi Apps:</b> Both <b>Kakao T</b> and <b>Uber</b> work seamlessly. Select 'Pay to the driver' in Kakao T if you don't have a Korean card."
    },
    "🇯🇵 日本語": {
        "title": "mongle-stay (モングルステイ)",
        "subtitle": "地下鉄6号線「安岩(アナム)駅」徒歩5分 · ソウルのローカル感性あふれる空間",
        "tabs": ["🏡 ストーリー", "🗺️ アクセス", "🔑 チェックイン", "✨ 周辺·交通"],
        # TAB 1
        "t1_story_title": "🎨 Mongle Stay Story (Curated by miel Yi)",
        "t1_story_body": """
        モングルステイは、異なる国や都市から訪れた旅人たちがソウルの日常を心地よく体験できるようにつくられた家です。好きな音楽や文化は違っても、旅先で感じるときめきや新しい物語に出会う喜びは同じです。ここでの滞在が単なる宿泊を超え、あなただけのソウルの好みと記憶を見つける時間になることを願っています。
        <div class='story-quote'>
            <b>• 好み (Taste):</b> それぞれ異なる色と雰囲気を持つ空間で、自分にとって一番心地よいスタイルでお過ごしください。<br>
            <b>• つながり (Connection):</b> Kカルチャーと安岩の日常、ソウルの歴史ある伝統市場と新しい文化を一緒に体験してください。<br>
            <b>• 安心 (Peace of Mind):</b> 見知らぬ街でも自宅のようにリラックスできるよう、清潔な空間と丁寧なご案内を用意しました。
        </div>
        """,
        "t1_rooms_title": "🛏️ 3つのお部屋の物語＆人数別のお部屋案内",
        "t1_rooms_body": """
        • <b>Palette Room:</b> 異なる色と好みが自然に調和するお部屋<br>
        • <b>Amber Room:</b> 温かい光のように穏やかに一日を締めくくるお部屋<br>
        • <b>Cozy Room:</b> コンパクトながらも自分だけの時間をゆっくり過ごせる居心地の良いお部屋<br><br>
        <span style='font-size: 13.5px; color: #8C5A3C;'>※ <b>人数別のお部屋セッティング:</b> ご予約人数に合わせてお部屋をご用意いたします。<br>
        &nbsp;&nbsp;- <b>4名以下:</b> 寝室2部屋開放 (Palette Room / Amber Room)<br>
        &nbsp;&nbsp;- <b>5名以上:</b> 寝室3部屋すべて開放 (Palette / Amber / Cozy Room)</span>
        """,
        "t1_floorplan_caption": "📐 モングルステイ 3D間取り図・お部屋レイアウト",
        # TAB 2
        "t2_loc_title": "📍 住所および地図アプリを開く",
        "t2_loc_body": "<b>韓国語住所:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br><b>英語住所:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br><b>最寄り駅:</b> 地下鉄6号線 <b>安岩(アナム)駅 3番出口</b> 徒歩5分",
        "t2_btn_naver": "🟢 NAVERマップでルート検索（韓国で最も正確）",
        "t2_btn_google": "🗺️ Google マップで開く",
        "t2_sub_title": "🚉 地下鉄6号線「安岩駅」からの行き方",
        "t2_sub_body": "• <b>地下鉄6号線 安岩(アナム)駅 3番出口</b>を出ます。<br>• 3番出口から安岩五叉路・祭基市場方面へ直進し、<b>安岩路18ギル(안암로18길)</b>の路地に入ると<b>徒歩約5分</b>で「高麗マンション(고려맨션)」に到着します。（2階 203号室）",
        "t2_air_title": "✈️ 空港からのアクセス",
        "t2_air_body": "<b>1. 仁川国際空港 (ICN) から（約75〜85分）</b><br>• <b>空港鉄道 + 地下鉄（おすすめ）:</b> 空港鉄道(一般列車)に乗車 ➔ <b>孔徳(コンドク)駅</b> または <b>デジタルメディアシティ(DMC)駅</b>で<b>6号線(新内方面)</b>に乗換 ➔ <b>安岩(アナム)駅</b>下車（3番出口 徒歩5分）<br>• <b>空港リムジンバス:</b> 6002番バス乗車 ➔「祭基洞駅・ソウル薬令市」下車後、タクシーで初乗り距離（約5分）<br><br><b>2. 金浦国際空港 (GMP) から（約55分）</b><br>• 空港鉄道に乗車 ➔ <b>DMC駅</b>で<b>6号線</b>に乗換 ➔ <b>安岩駅</b>下車",
        # TAB 3
        "t3_time_title": "⏰ チェックイン・チェックアウト＆ドアロック案内",
        "t3_time_body": """
        • <b>チェックイン:</b> 15:00以降<br>
        • <b>チェックアウト:</b> 11:00まで<br>
        <div class='doorlock-box'>
            <b>🔐 玄関ドアロックの開け方（セルフチェックイン）</b><br>
            1. チェックイン当日に予約サイト（Airbnb / Trip.com / Booking.com）のメッセージでお送りする<b>個別暗証番号</b>をご確認ください。<br>
            2. ドアロック画面を手のひらでタッチして点灯させた後 ➔ <b><code>*</code> + <code>暗証番号</code> + <code>*</code></b> の順に押すと解錠されます。<br>
            <span style='font-size: 12.5px; color: #5F6368;'>※ 暗証番号の前後両方にアスタリスク(*)を押してください。ドアが閉まると自動で施錠されます。</span>
        </div>
        """,
        "t3_wifi_title": "📶 無料高速Wi-Fi",
        "t3_wifi_body": "ご希望のWi-Fiとパスワード右側のコピーアイコンを押して接続してください。",
        "t3_wifi_ssid": "ネットワーク名 (SSID)",
        "t3_wifi_pw": "パスワード（5G・2.4G共通）",
        "t3_rules_title": "🌿 快適にお過ごしいただくためのお願い",
        "t3_rules_body": "1. <b>室内完全禁煙:</b> 建物全体および客室内での喫煙（電子タバコ含む）は固くお断りいたします。<br>2. <b>室内履き着用:</b> 玄関で靴を脱ぎ、備え付けのスリッパをご利用ください。<br>3. <b>お静かに:</b> 22時以降は近隣住民への配慮のためお静かにお過ごしいただき、洗濯機の使用はお控えください。<br>4. <b>調理＆ゴミ分別:</b> 匂いの強い調理はご遠慮いただき、ゴミはキッチン横の専用ゴミ箱へ分別をお願いします。<br>5. <b>外出時の電源オフ:</b> お出かけの際はエアコン・暖房・IHコンロの電源を必ずお切りください。",
        "t3_contact_title": "🐶 ホスト連絡先",
        "t3_contact_body": "ご滞在中に何かお困りの際は、いつでもお気軽にご連絡ください。<br>• <b>予約サイトメッセージ:</b> Airbnb / Trip.com / Booking.com アプリ内チャット（最速）<br>• <b>メッセンジャーID:</b> LINE: <code>mongle-stay</code> / WeChat: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>",
        # TAB 4
        "t4_walk_title": "☕ 徒歩圏内の人気スポット（安岩・祭基ローカル）",
        "t4_walk_body": "<b>1. 高麗大学キャンパス＆安岩グルメ通り（徒歩5〜10分）</b><br>• ヨーロッパのゴシック建築のような美しい石造りのキャンパス散策や、学生街ならではのコスパ抜群のローカルグルメ・カフェ通りをお楽しみください。<br><br><b>2. スターバックス京東1960店＆京東市場（徒歩15分 / バス5分）</b><br>• 1960年代の廃劇場をリノベーションした話題のスターバックスと、活気あふれる韓国最大級の伝統市場（京東市場・ソウル薬令市）の食べ歩きがおすすめです。<br><br><b>3. 城北川(ソンブクチョン)散策路（徒歩8分）</b><br>• 夕食後、ライトアップされた川辺の遊歩道をゆったりお散歩してみてください。",
        "t4_city_title": "🏯 ソウル主要観光地への簡単ルート（安岩駅出発）",
        "t4_city_body": "<b>1. 東大門デザインプラザ(DDP)＆ショッピング街（約10分）</b><br>• 6号線 安岩駅 ➔ 2駅先の<b>東廟前(トンミョアプ)駅</b>で1号線に乗換 ➔ <b>東大門(トンデムン)駅</b>下車<br><br><b>2. 梨泰院・漢南洞・望遠・合井（乗り換えなし・6号線直通！）</b><br>• 6号線 安岩駅から一本でアクセスできます：<br>&nbsp;&nbsp;- <b>漢江鎮(ハンガンジン)駅（約18分）:</b> 漢南洞のおしゃれカフェ通り＆リウム美術館<br>&nbsp;&nbsp;- <b>梨泰院(イテウォン)駅（約20分）:</b> 梨泰院＆解放村<br>&nbsp;&nbsp;- <b>望遠(マンウォン)・合井(ハプチョン)駅（約32分）:</b> 望遠市場＆弘大(ホンデ)<br><br><b>3. 広蔵市場・益善洞・聖水(ソンス)洞（約15〜25分）</b><br>• <b>広蔵市場・益善洞:</b> <b>東廟前駅</b>で1号線に乗換 ➔ 鍾路5街駅（広蔵市場）／鍾路3街駅（益善洞）<br>• <b>聖水洞カフェ通り:</b> <b>新堂(シンダン)駅</b>で2号線に乗換 ➔ <b>聖水(ソンス)駅</b>下車（約20分）",
        "t4_trans_title": "💳 ソウル公共交通＆タクシー利用ガイド",
        "t4_trans_body": "• <b>気候同行カード（乗り放題パス）:</b> 1日券(5,000ウォン)〜5日券(15,000ウォン)でソウル市内の地下鉄・バス・公共自転車が乗り放題。（安岩駅事務室・コンビニで購入）<br>• <b>T-money乗り換え割引:</b> バス降車時に必ず端末へカードをタッチしてください。30分以内の地下鉄・バス乗換が無料になります！<br>• <b>タクシー配車アプリ:</b> <b>Kakao T</b> または <b>Uber</b> で「運転手に直接支払い」を選べば日本のカード登録なしでも利用可能です。"
    },
    "🇨🇳 中文": {
        "title": "mongle-stay 首尔民宿",
        "subtitle": "地铁6号线安岩站步行5分钟 · 感受首尔本地烟火气的温馨居所",
        "tabs": ["🏡 民宿故事", "🗺️ 交通路线", "🔑 入住·Wi-Fi", "✨ 周边·出行"],
        # TAB 1
        "t1_story_title": "🎨 Mongle Stay Story (Curated by miel Yi)",
        "t1_story_body": """
        Mongle Stay 是为了让来自不同国家和城市的旅行者都能舒适地体验首尔日常生活而打造的家。即使喜欢的音乐与文化各不相同，在旅途中感受到的心动与发现新故事的喜悦却是相通的。希望您在 Mongle Stay 停留的时光不仅是一次简单的住宿，更是一段发现属于自己首尔品味与美好回忆的旅程。
        <div class='story-quote'>
            <b>• 品味 (Taste):</b> 在拥有不同色彩与氛围的空间里，以最让自己感到自在的方式停留。<br>
            <b>• 连接 (Connection):</b> 感受 K-Culture 与安岩的日常烟火气，邂逅首尔古老的传统市场与新潮文化。<br>
            <b>• 安心 (Peace of Mind):</b> 即使身处陌生的城市也能像在家一样安心，我们为您准备了整洁的空间与细致贴心的指引。
        </div>
        """,
        "t1_rooms_title": "🛏️ 三间卧室的故事 & 入住人数房型配置",
        "t1_rooms_body": """
        • <b>Palette Room:</b> 不同色彩与个人品味自然交融的房间<br>
        • <b>Amber Room:</b> 如温暖灯光般伴您舒适结束一天旅程的房间<br>
        • <b>Cozy Room:</b> 小巧却能完全享受独处时光的温馨房间<br><br>
        <span style='font-size: 13.5px; color: #8C5A3C;'>※ <b>按入住人数配置客房:</b> 客房将根据您的预订人数提前准备。<br>
        &nbsp;&nbsp;- <b>4人及以下:</b> 开放 2 间卧室 (Palette Room / Amber Room)<br>
        &nbsp;&nbsp;- <b>5人及以上:</b> 开放全部 3 间卧室 (Palette / Amber / Cozy Room)</span>
        """,
        "t1_floorplan_caption": "📐 Mongle Stay 3D 空间结构与房间布局图",
        # TAB 2
        "t2_loc_title": "📍 民宿地址与地图导航",
        "t2_loc_body": "<b>韩文地址:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br><b>英文地址:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br><b>最近地铁站:</b> 地铁6号线 <b>安岩站 (Anam Station) 3号出口</b> 步行5分钟",
        "t2_btn_naver": "🟢 打开 Naver 地图导航（韩国境内最准确）",
        "t2_btn_google": "🗺️ 打开 Google 地图",
        "t2_sub_title": "🚉 从地铁6号线「安岩站」步行路线",
        "t2_sub_body": "• 请从<b>地铁6号线安岩站（高大医院前）3号出口</b>出站。<br>• 出站后朝安岩五岔路口·祭基市场方向直行，拐入 <b>안암로18길 (Anam-ro 18-gil)</b> 小巷，<b>步行约5分钟</b>即可看到“고려맨션 (Goryeo Mansion)”建筑。（2楼 203室）",
        "t2_air_title": "✈️ 从机场出发路线",
        "t2_air_body": "<b>1. 仁川国际机场 (ICN) 出发（约 75–85 分钟）</b><br>• <b>机场铁路 + 地铁（推荐）:</b> 乘坐机场铁路普通列车 ➔ 在<b>孔德站 (Gongdeok)</b> 或 <b>数码媒体城站 (DMC)</b> 换乘<b>地铁6号线（往新内方向）</b> ➔ <b>安岩站</b>下车（3号出口步行5分钟）。<br>• <b>机场大巴:</b> 乘坐 6002 路大巴 ➔ 在“祭基洞站·首尔药令市”下车后打车起步价即到（约5分钟）。<br><br><b>2. 金浦国际机场 (GMP) 出发（约 55 分钟）</b><br>• 乘坐机场铁路 ➔ 在 <b>DMC站</b> 换乘<b>6号线</b> ➔ <b>安岩站</b>下车。",
        # TAB 3
        "t3_time_title": "⏰ 入住退房时间 & 门锁密码开锁指南",
        "t3_time_body": """
        • <b>入住时间 (Check-in):</b> 下午 3:00 (15:00) 以后<br>
        • <b>退房时间 (Check-out):</b> 上午 11:00 (11:00) 以前<br>
        <div class='doorlock-box'>
            <b>🔐 大门电子密码锁开锁方法（自助入住）</b><br>
            1. 入住当天请查看预订平台（Airbnb / 携程 Trip.com / Booking.com）私信发送给您的<b>专属密码</b>。<br>
            2. 用手掌轻触门锁屏幕唤醒灯光 ➔ 依次输入 <b><code>*</code> + <code>专属密码</code> + <code>*</code></b> 即可开锁。<br>
            <span style='font-size: 12.5px; color: #5F6368;'>※ 请务必在密码前后都按星号(*)。关门后门锁会自动上锁。</span>
        </div>
        """,
        "t3_wifi_title": "📶 免费高速 Wi-Fi",
        "t3_wifi_body": "请点击所需Wi-Fi及密码右侧的复制图标进行连接。",
        "t3_wifi_ssid": "网络名称 (SSID)",
        "t3_wifi_pw": "密码（5G与2.4G通用）",
        "t3_rules_title": "🌿 住宿公约",
        "t3_rules_body": "1. <b>室内绝对禁烟:</b> 整栋建筑及房间内严禁吸烟（包括电子烟）。<br>2. <b>室内更换拖鞋:</b> 请在玄关脱鞋并换穿室内拖鞋。<br>3. <b>保持安静:</b> 晚上10点（22:00）以后请调低音量，并请勿使用洗衣机。<br>4. <b>烹饪与垃圾分类:</b> 请避免油烟或气味较大的烹饪；垃圾请分类投放到厨房旁的专用垃圾桶内。<br>5. <b>外出断电:</b> 外出时请务必关闭空调、地暖及电磁炉电源。",
        "t3_contact_title": "🐶 房东紧急联系方式",
        "t3_contact_body": "入住期间如需任何帮助，请随时联系我们。<br>• <b>预订平台消息:</b> Airbnb / 携程(Trip.com) / Booking.com 应用内聊天（最快）<br>• <b>即时通讯账号:</b> 微信(WeChat): <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>",
        # TAB 4
        "t4_walk_title": "☕ 步行可达热门打卡点（安岩·祭基本地）",
        "t4_walk_body": "<b>1. 高丽大学校园 & 安岩大学街美食（步行 5–10 分钟）</b><br>• 漫步于充满欧式哥特风情的石造建筑校园，打卡大学街性价比超高的本地美食店与咖啡馆。<br><br><b>2. 星巴克京东1960店 & 京东市场（步行 15 分钟 / 公交 5 分钟）</b><br>• 强烈推荐由1960年代老剧场改造而成的网红星巴克，顺便逛逛首尔最具烟火气的传统市场（京东市场·首尔药令市）。<br><br><b>3. 城北川散步路（步行 8 分钟）</b><br>• 晚饭后沿着灯光璀璨的溪边步道悠闲散步，感受首尔本地人的慢生活。",
        "t4_city_title": "🏯 首尔核心景点快捷路线（安岩站出发）",
        "t4_city_body": "<b>1. 东大门设计广场 (DDP) & 购物商圈（约 10 分钟）</b><br>• 地铁6号线安岩站 ➔ 2站后在<b>东庙前站</b>换乘1号线 ➔ <b>东大门站</b>下车。<br><br><b>2. 梨泰院 · 汉南洞 · 望远 · 合井（6号线直达无需换乘！）</b><br>• 从安岩站乘坐6号线即可一线直达：<br>&nbsp;&nbsp;- <b>汉江镇站（约18分钟）:</b> 汉南洞潮流咖啡街 & 三星美术馆 Leeum<br>&nbsp;&nbsp;- <b>梨泰院站（约20分钟）:</b> 梨泰院经理团路 & 解放村<br>&nbsp;&nbsp;- <b>望远站 · 合井站（约32分钟）:</b> 望理团路 & 望远市场 & 弘大商圈<br><br><b>3. 广藏市场 · 益善洞 · 圣水洞（约 15–25 分钟）</b><br>• <b>广藏市场·益善洞:</b> 在<b>东庙前站</b>换乘1号线 ➔ 钟路5街站（广藏市场）/ 钟路3街站（益善洞）。<br>• <b>圣水洞咖啡街:</b> 在<b>新堂站</b>换乘2号线 ➔ <b>圣水站</b>下车（约20分钟）。",
        "t4_trans_title": "💳 首尔公共交通 & 打车贴士",
        "t4_trans_body": "• <b>气候同行卡（无限次交通卡）:</b> 1日券(5,000韩元)至5日券(15,000韩元)，可无限次搭乘首尔地铁、公交及公共自行车（安岩站客服中心及便利店有售）。<br>• <b>T-money 换乘优惠:</b> 下公交车时务必在后门刷卡机再次刷卡，30分钟内换乘地铁或公交可享免费换乘优惠！<br>• <b>打车软件:</b> 使用 <b>Kakao T</b> 或 <b>Uber</b>，在 Kakao T 中选择“向司机直接付款（现场支付）”，无需绑定韩国银行卡也能轻松叫车。"
    }
}

# 4. 상단 언어 선택 바 (한국어 / 영어 / 일본어 / 중국어)
selected_lang = st.radio(
    "Language",
    options=list(CONTENT.keys()),
    horizontal=True,
    label_visibility="collapsed"
)
t = CONTENT[selected_lang]

# 5. 상단 웰컴 헤더
st.markdown(f"""
<div class="hero-box">
    <div style="font-size: 30px; margin-bottom: 4px;">🐾</div>
    <h1 class="hero-title">{t['title']}</h1>
    <p class="hero-subtitle">{t['subtitle']}</p>
</div>
""", unsafe_allow_html=True)

# 6. 게스트 여정 맞춤형 4대 탭 구성 (1.스토리 ➔ 2.오시는 길 ➔ 3.체크인·Wi-Fi ➔ 4.로컬·교통)
tab_story, tab_way, tab_checkin, tab_local = st.tabs(t["tabs"])

# TAB 1: 몽글스테이 스토리 & 공간/객실 안내
with tab_story:
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

# TAB 2: 숙소에 찾아오는 방법
with tab_way:
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
        <p class="card-text">{t['t2_air_body']}</p>
    </div>
    """, unsafe_allow_html=True)

# TAB 3: 체크인 · 도어락 · Wi-Fi · 하우스 룰
with tab_checkin:
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
        st.code("U+Net1825_5G", language=None)
        st.code("U+Net1825", language=None)
    with col2:
        st.caption(t['t3_wifi_pw'])
        st.code("42155551M#", language=None)

    st.markdown(f"""
    <div class="info-card" style="margin-top: 16px;">
        <span class="badge">HOUSE RULES</span>
        <div class="card-title">{t['t3_rules_title']}</div>
        <p class="card-text">{t['t3_rules_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card" style="background-color: #F4F7F5; border-color: #C8D6CE;">
        <div class="card-title">{t['t3_contact_title']}</div>
        <p class="card-text">{t['t3_contact_body']}</p>
    </div>
    """, unsafe_allow_html=True)

# TAB 4: 로컬 명소 & 교통 꿀팁
with tab_local:
    st.markdown(f"""
    <div class="info-card">
        <span class="badge">WALKING 5~15 MIN</span>
        <div class="card-title">{t['t4_walk_title']}</div>
        <p class="card-text">{t['t4_walk_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">SUBWAY 10~30 MIN</span>
        <div class="card-title">{t['t4_city_title']}</div>
        <p class="card-text">{t['t4_city_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">TRANSIT TIPS</span>
        <div class="card-title">{t['t4_trans_title']}</div>
        <p class="card-text">{t['t4_trans_body']}</p>
    </div>
    """, unsafe_allow_html=True)

# 7. 하단 푸터
st.markdown("""
<div style="text-align: center; padding: 24px 0 10px 0; color: #8C857B; font-size: 12.5px;">
    © 2026 <b>mongle-stay Seoul (Anam · Jegi-dong)</b>. All rights reserved.<br>
    Have a cozy and wonderful stay in Seoul 🐾
</div>
""", unsafe_allow_html=True)
