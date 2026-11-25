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
    /* 라디오 버튼(언어 선택바) 가로 정렬 스타일 */
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
        "tabs": ["🏠 숙소 이용", "🗺️ 오시는 길", "🚇 교통 꿀팁", "✨ 주변 명소"],
        "t1_time_title": "⏰ 입·퇴실 시간 안내",
        "t1_time_body": "• <b>체크인 (Check-in):</b> 오후 3:00 (15:00) 이후<br>• <b>체크아웃 (Check-out):</b> 오전 11:00 (11:00) 이전<br><span style='font-size: 13px; color: #888;'>※ 다음 게스트를 위한 침구 교체 및 방역 청소를 위해 퇴실 시간을 꼭 지켜주세요.</span>",
        "t1_wifi_title": "📶 초고속 무선 인터넷 연결",
        "t1_wifi_body": "원하시는 Wi-Fi와 비밀번호 우측의 복사 아이콘을 눌러 연결하세요.",
        "t1_wifi_ssid": "네트워크 이름 (SSID)",
        "t1_wifi_pw": "비밀번호 (5G · 2.4G 공통)",
        "t1_rules_title": "🌿 쾌적한 머무름을 위한 약속",
        "t1_rules_body": "1. <b>실내 절대 금연:</b> 건물 전체 및 객실 내 흡연(전자담배 포함)은 엄격히 금지됩니다.<br>2. <b>정숙 시간:</b> 밤 10시 이후에는 이웃을 위해 TV 볼륨과 대화를 조금만 낮춰주세요.<br>3. <b>분리수거 안내:</b> 일반쓰레기, 플라스틱/캔, 음식물 쓰레기는 주방 옆 전용함에 분리해 주세요.<br>4. <b>외출 시 전원 확인:</b> 외출하실 때는 냉난방기 및 인덕션 전원을 꼭 꺼주세요.",
        "t1_contact_title": "🐶 호스트 긴급 연락처",
        "t1_contact_body": "머무시는 동안 도움이 필요하시면 언제든 편하게 연락해 주세요.<br>• <b>예약 플랫폼 메시지:</b> 에어비앤비 / 트립닷컴 / 부킹닷컴 앱 내 채팅 (가장 빠름)<br>• <b>메신저 문의:</b> WeChat: <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>",
        "t2_loc_title": "📍 숙소 주소 및 지도 앱 열기",
        "t2_loc_body": "<b>도로명 주소:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br><b>영문 주소:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br><b>가까운 역:</b> 지하철 6호선 <b>안암역(Anam Station) 3번 출구</b> 도보 5분",
        "t2_btn_naver": "🟢 네이버 지도로 길찾기 (한국 내 가장 정확)",
        "t2_btn_google": "🗺️ Google Maps로 열기",
        "t2_sub_title": "🚉 지하철 6호선 안암역에서 오시는 법",
        "t2_sub_body": "• <b>지하철 6호선 안암역(고대병원앞) 3번 출구</b>로 나오세요.<br>• 3번 출구에서 안암오거리·제기시장 방면으로 직진 후 <b>안암로18길</b> 골목으로 진입하시면 <b>도보 약 5분</b> 거리에 '고려맨션' 건물이 위치해 있습니다. (2층 203호)",
        "t2_air_title": "✈️ 공항에서 오시는 방법",
        "t2_air_body": "<b>1. 인천국제공항 (ICN) 출발 (약 75~85분 소요)</b><br>• <b>공항철도 + 지하철 (추천):</b> 공항철도 탑승 ➔ <b>공덕역</b> 또는 <b>디지털미디어시티(DMC)역</b>에서 <b>6호선(신내 방면)</b> 환승 ➔ <b>안암역</b> 하차 (3번 출구 도보 5분)<br>• <b>공항리무진 버스:</b> 6002번 탑승 ➔ '제기동역.서울약령시' 하차 후 택시 기본요금 이동 (약 5분)<br><br><b>2. 김포국제공항 (GMP) 출발 (약 55분 소요)</b><br>• 공항철도 탑승 ➔ <b>디지털미디어시티(DMC)역</b>에서 <b>6호선</b> 환승 ➔ <b>안암역</b> 하차",
        "t3_pass_title": "💳 기후동행카드 (관광객 무제한 교통패스)",
        "t3_pass_body": "서울 시내 지하철, 버스, 공공자전거(따릉이)를 무제한으로 탈 수 있는 최고의 가성비 카드입니다.<br>• <b>권종 및 가격:</b> 1일권(5,000원), 2일권(8,000원), 3일권(10,000원), 5일권(15,000원)<br>• <b>구매처:</b> 지하철 6호선 안암역 고객안전실 또는 역 인근 편의점(GS25, CU, 세븐일레븐)<br>• <b>충전 방법:</b> 지하철 역사 내 무인충전기에서 현금으로 원하는 일수만큼 충전 후 바로 사용!",
        "t3_tmoney_title": "🚌 일반 교통카드 (티머니 / 와우패스)",
        "t3_tmoney_body": "• <b>티머니(T-money):</b> 모든 편의점에서 카드 구매(약 3,000~4,000원) 후 현금 충전하여 버스·지하철·택시 결제 가능.<br>• <b>환승 할인 꿀팁:</b> 버스에서 내릴 때 반드시 단말기에 카드를 한 번 더 태그(하차 태그)하셔야 30분 이내 지하철/버스 무료 환승이 적용됩니다!",
        "t3_taxi_title": "🚕 택시 호출 & 공공자전거 따릉이",
        "t3_taxi_body": "• <b>카카오 T (Kakao T) 앱:</b> 한국에서 가장 잘 잡히는 택시 호출 앱입니다. 해외 카드 등록 또는 '기사님께 직접 결제' 선택 후 호출하세요. (Uber 앱도 동일하게 작동)<br>• <b>서울자전거 따릉이:</b> 안암역 출구 앞 대여소에서 앱으로 1시간권(1,000원)을 끊어 성북천·청계천 자전거 도로를 따라 라이딩을 즐길 수 있습니다.",
        "t4_walk_title": "☕ 도보권 핫플레이스 (안암·제기 로컬)",
        "t4_walk_body": "<b>1. 고려대학교 캠퍼스 & 안암동 대학가 맛집 (도보 5~10분)</b><br>• 유럽 고딕 양식의 아름다운 석조 건축물로 유명한 고려대 캠퍼스 산책과, 대학가 특유의 가성비 넘치는 로컬 맛집·카페 거리를 도보로 즐겨보세요.<br><br><b>2. 스타벅스 경동1960점 & 경동시장 (도보 15분 / 버스 5분)</b><br>• 1960년대 폐극장(경동극장)을 개조한 압도적 분위기의 스타벅스 스페셜 매장과, 활기찬 한국 전통시장(경동시장·서울약령시) 먹거리 투어를 추천합니다.<br><br><b>3. 성북천 산책로 (도보 8분)</b><br>• 저녁 식사 후 조명이 예쁘게 켜진 성북천 물길을 따라 여유롭게 산책해 보세요.",
        "t4_city_title": "🏯 서울 핵심 관광지 초간단 이동 루트 (안암역 출발)",
        "t4_city_body": "<b>1. 동대문 디자인 플라자(DDP) & 쇼핑타운 (약 10분)</b><br>• <b>지하철:</b> 6호선 안암역 ➔ 2정거장 뒤 <b>동묘앞역</b>에서 1호선 환승 ➔ <b>동대문역</b> 하차<br>• <b>버스:</b> 안암역 정류장에서 간선버스(144, 273번 등) 탑승 후 동대문 방면 하차<br><br><b>2. 이태원 · 한강진(한남동) · 망원 · 합정 (환승 없이 6호선 직통!)</b><br>• 6호선 안암역에서 한 번에 쭉 이동합니다:<br>&nbsp;&nbsp;- <b>한강진역 (약 18분):</b> 한남동 감성 카페거리 & 리움미술관<br>&nbsp;&nbsp;- <b>이태원역 (약 20분):</b> 이태원 경리단길 & 해방촌<br>&nbsp;&nbsp;- <b>망원역 · 합정역 (약 32분):</b> 망리단길 & 망원시장 & 홍대<br><br><b>3. 광장시장 · 익선동 · 경복궁 · 성수동 (약 15~25분)</b><br>• <b>광장시장·익선동:</b> 6호선 안암역 ➔ <b>동묘앞역(1호선 환승)</b> ➔ 종로5가역(광장시장) / 종로3가역(익선동)<br>• <b>성수동 카페거리:</b> 6호선 안암역 ➔ <b>신당역(2호선 환승)</b> ➔ <b>성수역</b> 하차 (약 20분)"
    },
    "🇺🇸 English": {
        "title": "mongle-stay Seoul",
        "subtitle": "5-min walk from Anam Stn (Line 6) · Cozy Local Stay in Seoul",
        "tabs": ["🏠 House Info", "🗺️ Directions", "🚇 Transport", "✨ Local Guide"],
        "t1_time_title": "⏰ Check-in & Check-out",
        "t1_time_body": "• <b>Check-in:</b> After 3:00 PM (15:00)<br>• <b>Check-out:</b> Before 11:00 AM (11:00)<br><span style='font-size: 13px; color: #888;'>※ Please adhere to check-out time for thorough cleaning and fresh bedding preparation.</span>",
        "t1_wifi_title": "📶 Free High-Speed Wi-Fi",
        "t1_wifi_body": "Tap the copy icon next to your preferred Wi-Fi and password to connect.",
        "t1_wifi_ssid": "Password (Shared for 5G & 2.4G)",
        "t1_wifi_pw": "Password",
        "t1_rules_title": "🌿 House Rules",
        "t1_rules_body": "1. <b>No Smoking:</b> Smoking (including e-cigarettes) is strictly prohibited inside the room and building.<br>2. <b>Quiet Hours:</b> Please keep noise levels down after 10:00 PM out of respect for neighbors.<br>3. <b>Recycling:</b> Please separate general waste, plastics/cans, and food waste into the bins next to the kitchen.<br>4. <b>Save Energy:</b> Please turn off the A/C, heater, and induction stove when leaving the room.",
        "t1_contact_title": "🐶 Host Contact",
        "t1_contact_body": "Feel free to reach out anytime if you need assistance during your stay.<br>• <b>Booking Platform Chat:</b> Airbnb / Trip.com / Booking.com in-app message (Fastest)<br>• <b>Messenger ID:</b> WeChat: <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>",
        "t2_loc_title": "📍 Address & Navigation",
        "t2_loc_body": "<b>English Address:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br><b>Korean Address:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br><b>Nearest Subway:</b> <b>Anam Station (Line 6), Exit 3</b> (5-minute walk)",
        "t2_btn_naver": "🟢 Open in Naver Map (Most Accurate in Korea)",
        "t2_btn_google": "🗺️ Open in Google Maps",
        "t2_sub_title": "🚉 From Anam Station (Subway Line 6)",
        "t2_sub_body": "• Come out of <b>Anam Station (Line 6), Exit 3</b>.<br>• Walk straight toward Anam Ogeori / Jegi Market and turn into the <b>Anam-ro 18-gil</b> alley. You will find <b>'Goryeo Mansion'</b> within a <b>5-minute walk</b> (2nd floor, Room 203).",
        "t2_air_title": "✈️ From the Airport",
        "t2_air_body": "<b>1. From Incheon Int'l Airport (ICN) (~75–85 mins)</b><br>• <b>AREX Train + Subway (Recommended):</b> Take AREX All-stop train ➔ Transfer at <b>Gongdeok</b> or <b>Digital Media City (DMC)</b> to <b>Line 6 (Sinnae bound)</b> ➔ Get off at <b>Anam Station</b> (Exit 3, 5-min walk).<br>• <b>Airport Limousine Bus:</b> Take Bus #6002 ➔ Get off at 'Jegi-dong Station / Seoul Yangnyeongsi' ➔ 5-min taxi ride.<br><br><b>2. From Gimpo Int'l Airport (GMP) (~55 mins)</b><br>• Take AREX train ➔ Transfer at <b>DMC Station</b> to <b>Line 6</b> ➔ Get off at <b>Anam Station</b>.",
        "t3_pass_title": "💳 Climate Card (Unlimited Tourist Transit Pass)",
        "t3_pass_body": "Unlimited rides on Seoul subways, buses, and Ttareungi public bikes!<br>• <b>Passes:</b> 1-Day (5,000 KRW), 2-Day (8,000 KRW), 3-Day (10,000 KRW), 5-Day (15,000 KRW)<br>• <b>Where to buy:</b> Anam Station Customer Safety Office or nearby convenience stores (GS25, CU, 7-Eleven)<br>• <b>How to top up:</b> Load cash for your desired pass duration at any subway ticket machine.",
        "t3_tmoney_title": "🚌 T-money / WOWPASS Card",
        "t3_tmoney_body": "• <b>T-money:</b> Purchase at any convenience store (~3,000–4,000 KRW) and top up with cash for subways, buses, and taxis.<br>• <b>Transfer Tip:</b> Always tap your card again when exiting a bus to get free transfers to subways/other buses within 30 minutes!",
        "t3_taxi_title": "🚕 Taxi Apps & Public Bikes",
        "t3_taxi_body": "• <b>Kakao T / Uber:</b> Both apps work seamlessly in Seoul! In Kakao T, you can select 'Pay to the driver' if you don't have a Korean card.<br>• <b>Seoul Bike (Ttareungi):</b> Rent a bike right outside Anam Station (1,000 KRW/hr) and ride along the scenic Seongbukcheon & Cheonggyecheon streams.",
        "t4_walk_title": "☕ Walking Distance Gems (Anam & Jegi)",
        "t4_walk_body": "<b>1. Korea University Campus & Anam Food Street (5–10 min walk)</b><br>• Stroll through the stunning European Gothic stone architecture of Korea University and enjoy affordable, vibrant local student eateries and cafes.<br><br><b>2. Starbucks Gyeongdong 1960 & Gyeongdong Market (15-min walk / 5-min bus)</b><br>• Visit the viral Starbucks built inside an abandoned 1960s theater, right inside Seoul's largest traditional herbal & food market.<br><br><b>3. Seongbukcheon Stream Trail (8-min walk)</b><br>• Enjoy a peaceful evening walk along the illuminated waterside path.",
        "t4_city_title": "🏯 Direct Routes to Seoul Hotspots (From Anam Stn)",
        "t4_city_body": "<b>1. Dongdaemun Design Plaza (DDP) & Shopping (~10 mins)</b><br>• Take Line 6 to <b>Dongmyo Station</b> (2 stops) ➔ Transfer to Line 1 ➔ <b>Dongdaemun Station</b>.<br><br><b>2. Itaewon · Hannam-dong · Mangwon · Hongdae (Direct on Line 6!)</b><br>• No transfers needed from Anam Station:<br>&nbsp;&nbsp;- <b>Hangangjin Stn (~18 mins):</b> Hannam-dong trendy cafes & Leeum Museum<br>&nbsp;&nbsp;- <b>Itaewon Stn (~20 mins):</b> Itaewon & Haebangchon<br>&nbsp;&nbsp;- <b>Mangwon / Hapjeong Stn (~32 mins):</b> Mangwon Market & Hongdae<br><br><b>3. Gwangjang Market · Ikseon-dong · Seongsu-dong (~15–25 mins)</b><br>• <b>Gwangjang Market / Ikseon-dong:</b> Transfer at <b>Dongmyo Stn</b> to Line 1 ➔ Jongno 5-ga / Jongno 3-ga Stn.<br>• <b>Seongsu-dong (Brooklyn of Seoul):</b> Transfer at <b>Sindang Stn</b> to Line 2 ➔ <b>Seongsu Stn</b> (~20 mins)."
    },
    "🇯🇵 日本語": {
        "title": "mongle-stay (モングルステイ)",
        "subtitle": "地下鉄6号線「安岩(アナム)駅」徒歩5分 · ソウルのローカル感性あふれる空間",
        "tabs": ["🏠 宿泊案内", "🗺️ アクセス", "🚇 交通ガイド", "✨ 周辺スポット"],
        "t1_time_title": "⏰ チェックイン・チェックアウト",
        "t1_time_body": "• <b>チェックイン:</b> 15:00以降<br>• <b>チェックアウト:</b> 11:00まで<br><span style='font-size: 13px; color: #888;'>※ 次のゲストのための清掃・寝具交換のため、チェックアウト時間をお守りください。</span>",
        "t1_wifi_title": "📶 無料高速Wi-Fi",
        "t1_wifi_body": "ご希望のWi-Fiとパスワード右側のコピーアイコンを押して接続してください。",
        "t1_wifi_ssid": "ネットワーク名 (SSID)",
        "t1_wifi_pw": "パスワード（5G・2.4G共通）",
        "t1_rules_title": "🌿 快適にお過ごしいただくためのお願い",
        "t1_rules_body": "1. <b>室内完全禁煙:</b> 建物全体および客室内での喫煙（電子タバコ含む）は固くお断りいたします。<br>2. <b>お静かに:</b> 22時以降は近隣住民への配慮のため、お静かにお過ごしください。<br>3. <b>ゴミの分別:</b> 一般ゴミ、プラスチック・缶、生ゴミはキッチン横の専用ゴミ箱へ分別をお願いします。<br>4. <b>外出時の電源オフ:</b> お出かけの際はエアコン・暖房・IHコンロの電源を必ずお切りください。",
        "t1_contact_title": "🐶 ホスト連絡先",
        "t1_contact_body": "ご滞在中に何かお困りの際は、いつでもお気軽にご連絡ください。<br>• <b>予約サイトメッセージ:</b> Airbnb / Trip.com / Booking.com アプリ内チャット（最速）<br>• <b>メッセンジャーID:</b> LINE: <code>mongle-stay</code> / WeChat: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>",
        "t2_loc_body": "<b>韓国語住所:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br><b>英語住所:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br><b>最寄り駅:</b> 地下鉄6号線 <b>安岩(アナム)駅 3番出口</b> 徒歩5分",
        "t2_btn_naver": "🟢 NAVERマップでルート検索（韓国で最も正確）",
        "t2_btn_google": "🗺️ Google マップで開く",
        "t2_sub_title": "🚉 地下鉄6号線「安岩駅」からの行き方",
        "t2_sub_body": "• <b>地下鉄6号線 安岩(アナム)駅 3番出口</b>を出ます。<br>• 3番出口から安岩五叉路・祭基市場方面へ直進し、<b>安岩路18ギル(안암로18길)</b>の路地に入ると<b>徒歩約5分</b>で「高麗マンション(고려맨션)」に到着します。（2階 203号室）",
        "t2_air_title": "✈️ 空港からのアクセス",
        "t2_air_body": "<b>1. 仁川国際空港 (ICN) から（約75〜85分）</b><br>• <b>空港鉄道 + 地下鉄（おすすめ）:</b> 空港鉄道(一般列車)に乗車 ➔ <b>孔徳(コンドク)駅</b> または <b>デジタルメディアシティ(DMC)駅</b>で<b>6号線(新内方面)</b>に乗換 ➔ <b>安岩(アナム)駅</b>下車（3番出口 徒歩5分）<br>• <b>空港リムジンバス:</b> 6002番バス乗車 ➔「祭基洞駅・ソウル薬令市」下車後、タクシーで初乗り距離（約5分）<br><br><b>2. 金浦国際空港 (GMP) から（約55分）</b><br>• 空港鉄道に乗車 ➔ <b>DMC駅</b>で<b>6号線</b>に乗換 ➔ <b>安岩駅</b>下車",
        "t3_pass_title": "💳 気候同行カード（外国人観光客向け乗り放題パス）",
        "t3_pass_body": "ソウル市内の地下鉄・バス・公共自転車（タルンイ）が乗り放題になるお得なカードです。<br>• <b>券種・料金:</b> 1日券(5,000ウォン)、2日券(8,000ウォン)、3日券(10,000ウォン)、5日券(15,000ウォン)<br>• <b>購入場所:</b> 地下鉄6号線 安岩駅の駅事務室、または駅周辺のコンビニ（GS25、CU、セブンイレブン）<br>• <b>チャージ方法:</b> 地下鉄駅構内の券売機で現金にて希望の日数分をチャージしてすぐ利用可能！",
        "t3_tmoney_title": "🚌 一般交通カード（T-money / WOWPASS）",
        "t3_tmoney_body": "• <b>T-money:</b> コンビニでカード購入（約3,000〜4,000ウォン）後、現金チャージで地下鉄・バス・タクシーが利用できます。<br>• <b>乗り換え割引のコツ:</b> バスを降りる際、必ず降車口の端末にカードをタッチしてください。30分以内の地下鉄・バスへの乗り換えが無料になります！",
        "t3_taxi_title": "🚕 タクシー配車アプリ＆公共自転車",
        "t3_taxi_body": "• <b>Kakao T / Uber:</b> 韓国で最も捕まりやすい配車アプリです。Kakao Tでは「運転手に直接支払い(現地決済)」を選べば日本のクレジットカード登録なしでも利用可能です。<br>• <b>ソウル自転車 タルンイ:</b> 安岩駅出口前のポートからアプリで1時間券(1,000ウォン)を購入し、城北川・清渓川沿いのサイクリングを楽しめます。",
        "t4_walk_title": "☕ 徒歩圏内の人気スポット（安岩・祭基ローカル）",
        "t4_walk_body": "<b>1. 高麗大学キャンパス＆安岩グルメ通り（徒歩5〜10分）</b><br>• ヨーロッパのゴシック建築のような美しい石造りのキャンパス散策や、学生街ならではのコスパ抜群のローカルグルメ・カフェ通りをお楽しみください。<br><br><b>2. スターバックス京東1960店＆京東市場（徒歩15分 / バス5分）</b><br>• 1960年代の廃劇場をリノベーションした話題のスターバックスと、活気あふれる韓国最大級の伝統市場（京東市場・ソウル薬令市）の食べ歩きがおすすめです。<br><br><b>3. 城北川(ソンブクチョン)散策路（徒歩8分）</b><br>• 夕食後、ライトアップされた川辺の遊歩道をゆったりお散歩してみてください。",
        "t4_city_title": "🏯 ソウル主要観光地への簡単ルート（安岩駅出発）",
        "t4_city_body": "<b>1. 東大門デザインプラザ(DDP)＆ショッピング街（約10分）</b><br>• 6号線 安岩駅 ➔ 2駅先の<b>東廟前(トンミョアプ)駅</b>で1号線に乗換 ➔ <b>東大門(トンデムン)駅</b>下車<br><br><b>2. 梨泰院・漢南洞・望遠・合井（乗り換えなし・6号線直通！）</b><br>• 6号線 安岩駅から一本でアクセスできます：<br>&nbsp;&nbsp;- <b>漢江鎮(ハンガンジン)駅（約18分）:</b> 漢南洞のおしゃれカフェ通り＆リウム美術館<br>&nbsp;&nbsp;- <b>梨泰院(イテウォン)駅（約20分）:</b> 梨泰院＆解放村<br>&nbsp;&nbsp;- <b>望遠(マンウォン)・合井(ハプチョン)駅（約32分）:</b> 望遠市場＆弘大(ホンデ)<br><br><b>3. 広蔵市場・益善洞・聖水(ソンス)洞（約15〜25分）</b><br>• <b>広蔵市場・益善洞:</b> <b>東廟前駅</b>で1号線に乗換 ➔ 鍾路5街駅（広蔵市場）／鍾路3街駅（益善洞）<br>• <b>聖水洞カフェ通り:</b> <b>新堂(シンダン)駅</b>で2号線に乗換 ➔ <b>聖水(ソンス)駅</b>下車（約20分）"
    },
    "🇨🇳 中文": {
        "title": "mongle-stay 首尔民宿",
        "subtitle": "地铁6号线安岩站步行5分钟 · 感受首尔本地烟火气的温馨居所",
        "tabs": ["🏠 入住指南", "🗺️ 交通路线", "🚇 出行贴士", "✨ 周边游玩"],
        "t1_time_title": "⏰ 入住与退房时间",
        "t1_time_body": "• <b>入住时间 (Check-in):</b> 下午 3:00 (15:00) 以后<br>• <b>退房时间 (Check-out):</b> 上午 11:00 (11:00) 以前<br><span style='font-size: 13px; color: #888;'>※ 为确保下一位客人的床品更换与全面消毒，请务必准时退房。</span>",
        "t1_wifi_title": "📶 免费高速 Wi-Fi",
        "t1_wifi_body": "请点击所需Wi-Fi及密码右侧的复制图标进行连接。",
        "t1_wifi_ssid": "网络名称 (SSID)",
        "t1_wifi_pw": "密码（5G与2.4G通用）",
        "t1_rules_title": "🌿 住宿公约",
        "t1_rules_body": "1. <b>室内绝对禁烟:</b> 整栋建筑及房间内严禁吸烟（包括电子烟）。<br>2. <b>保持安静:</b> 晚上10点以后请调低音量，以免打扰周边邻居休息。<br>3. <b>垃圾分类:</b> 请将一般垃圾、塑料/易拉罐、食物残渣分类投放到厨房旁的专用垃圾桶内。<br>4. <b>外出断电:</b> 外出时请务必关闭空调、地暖及电磁炉电源。",
        "t1_contact_title": "🐶 房东紧急联系方式",
        "t1_contact_body": "入住期间如需任何帮助，请随时联系我们。<br>• <b>预订平台消息:</b> Airbnb / 携程(Trip.com) / Booking.com 应用内聊天（最快）<br>• <b>即时通讯账号:</b> 微信(WeChat): <code>mongle-stay</code> / LINE: <code>mongle-stay</code> / KakaoTalk: <code>mongle0607</code>",
        "t2_loc_title": "📍 民宿地址与地图导航",
        "t2_loc_body": "<b>韩文地址:</b> 서울특별시 동대문구 안암로18길 3 고려맨션 203호<br><b>英文地址:</b> #203, Goryeo Mansion, 3, Anam-ro 18-gil, Dongdaemun-gu, Seoul<br><b>最近地铁站:</b> 地铁6号线 <b>安岩站 (Anam Station) 3号出口</b> 步行5分钟",
        "t2_btn_naver": "🟢 打开 Naver 地图导航（韩国境内最准确）",
        "t2_btn_google": "🗺️ 打开 Google 地图",
        "t2_sub_title": "🚉 从地铁6号线「安岩站」步行路线",
        "t2_sub_body": "• 请从<b>地铁6号线安岩站（高大医院前）3号出口</b>出站。<br>• 出站后朝安岩五岔路口·祭基市场方向直行，拐入 <b>안암로18길 (Anam-ro 18-gil)</b> 小巷，<b>步行约5分钟</b>即可看到“고려맨션 (Goryeo Mansion)”建筑。（2楼 203室）",
        "t2_air_title": "✈️ 从机场出发路线",
        "t2_air_body": "<b>1. 仁川国际机场 (ICN) 出发（约 75–85 分钟）</b><br>• <b>机场铁路 + 地铁（推荐）:</b> 乘坐机场铁路普通列车 ➔ 在<b>孔德站 (Gongdeok)</b> 或 <b>数码媒体城站 (DMC)</b> 换乘<b>地铁6号线（往新内方向）</b> ➔ <b>安岩站</b>下车（3号出口步行5分钟）。<br>• <b>机场大巴:</b> 乘坐 6002 路大巴 ➔ 在“祭基洞站·首尔药令市”下车后打车起步价即到（约5分钟）。<br><br><b>2. 金浦国际机场 (GMP) 出发（约 55 分钟）</b><br>• 乘坐机场铁路 ➔ 在 <b>DMC站</b> 换乘<b>6号线</b> ➔ <b>安岩站</b>下车。",
        "t3_pass_title": "💳 气候同行卡（游客无限次交通卡）",
        "t3_pass_body": "可在有效期内无限次搭乘首尔市内地铁、公交车及公共自行车（叮铃铃）！<br>• <b>票种与价格:</b> 1日券(5,000韩元)、2日券(8,000韩元)、3日券(10,000韩元)、5日券(15,000韩元)<br>• <b>购买地点:</b> 地铁6号线安岩站客服中心，或附近便利店（GS25、CU、7-Eleven）<br>• <b>充值方式:</b> 在地铁站内自动充值机使用现金按需充值天数即可使用。",
        "t3_tmoney_title": "🚌 普通交通卡（T-money / WOWPASS）",
        "t3_tmoney_body": "• <b>T-money卡:</b> 所有便利店均可购买（约3,000–4,000韩元），现金充值后可用于地铁、公交和出租车。<br>• <b>换乘优惠贴士:</b> 下公交车时务必在后门刷卡机再次刷卡，30分钟内换乘地铁或其他公交车可享免费换乘优惠！",
        "t3_taxi_title": "🚕 打车软件与公共自行车",
        "t3_taxi_body": "• <b>Kakao T / Uber:</b> 韩国最常用的打车软件。在 Kakao T 中选择“向司机直接付款（现场支付）”，无需绑定韩国银行卡也能轻松叫车。<br>• <b>首尔公共自行车（叮铃铃）:</b> 安岩站出口前设有租车点，购买1小时券（1,000韩元）即可沿城北川、清溪川骑行。",
        "t4_walk_title": "☕ 步行可达热门打卡点（安岩·祭基本地）",
        "t4_walk_body": "<b>1. 高丽大学校园 & 安岩大学街美食（步行 5–10 分钟）</b><br>• 漫步于充满欧式哥特风情的石造建筑校园，打卡大学街性价比超高的本地美食店与咖啡馆。<br><br><b>2. 星巴克京东1960店 & 京东市场（步行 15 分钟 / 公交 5 分钟）</b><br>• 强烈推荐由1960年代老剧场改造而成的网红星巴克，顺便逛逛首尔最具烟火气的传统市场（京东市场·首尔药令市）。<br><br><b>3. 城北川散步路（步行 8 分钟）</b><br>• 晚饭后沿着灯光璀璨的溪边步道悠闲散步，感受首尔本地人的慢生活。",
        "t4_city_title": "🏯 首尔核心景点快捷路线（安岩站出发）",
        "t4_city_body": "<b>1. 东大门设计广场 (DDP) & 购物商圈（约 10 分钟）</b><br>• 地铁6号线安岩站 ➔ 2站后在<b>东庙前站</b>换乘1号线 ➔ <b>东大门站</b>下车。<br><br><b>2. 梨泰院 · 汉南洞 · 望远 · 合井（6号线直达无需换乘！）</b><br>• 从安岩站乘坐6号线即可一线直达：<br>&nbsp;&nbsp;- <b>汉江镇站（约18分钟）:</b> 汉南洞潮流咖啡街 & 三星美术馆 Leeum<br>&nbsp;&nbsp;- <b>梨泰院站（约20分钟）:</b> 梨泰院经理团路 & 解放村<br>&nbsp;&nbsp;- <b>望远站 · 合井站（约32分钟）:</b> 望理团路 & 望远市场 & 弘大商圈<br><br><b>3. 广藏市场 · 益善洞 · 圣水洞（约 15–25 分钟）</b><br>• <b>广藏市场·益善洞:</b> 在<b>东庙前站</b>换乘1号线 ➔ 钟路5街站（广藏市场）/ 钟路3街站（益善洞）。<br>• <b>圣水洞咖啡街:</b> 在<b>新堂站</b>换乘2号线 ➔ <b>圣水站</b>下车（约20分钟）。"
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

# 6. 4대 핵심 게스트 안내 탭 구성
tab_home, tab_way, tab_trans, tab_spot = st.tabs(t["tabs"])

# TAB 1: 숙소 이용 및 체크인 안내
with tab_home:
    st.markdown(f"""
    <div class="info-card">
        <span class="badge">CHECK-IN & OUT</span>
        <div class="card-title">{t['t1_time_title']}</div>
        <p class="card-text">{t['t1_time_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">FREE WI-FI</span>
        <div class="card-title">{t['t1_wifi_title']}</div>
        <p class="card-text">{t['t1_wifi_body']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.caption(t['t1_wifi_ssid'])
        st.code("U+Net1825_5G", language=None)
        st.code("U+Net1825", language=None)
    with col2:
        st.caption(t['t1_wifi_pw'])
        st.code("42155551M#", language=None)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">HOUSE RULES</span>
        <div class="card-title">{t['t1_rules_title']}</div>
        <p class="card-text">{t['t1_rules_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card" style="background-color: #F4F7F5; border-color: #C8D6CE;">
        <div class="card-title">{t['t1_contact_title']}</div>
        <p class="card-text">{t['t1_contact_body']}</p>
    </div>
    """, unsafe_allow_html=True)

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

# TAB 3: 유용한 교통수단 가이드
with tab_trans:
    st.markdown(f"""
    <div class="info-card">
        <span class="badge">BEST PASS</span>
        <div class="card-title">{t['t3_pass_title']}</div>
        <p class="card-text">{t['t3_pass_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">T-MONEY</span>
        <div class="card-title">{t['t3_tmoney_title']}</div>
        <p class="card-text">{t['t3_tmoney_body']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">
        <span class="badge">TAXI & BIKE</span>
        <div class="card-title">{t['t3_taxi_title']}</div>
        <p class="card-text">{t['t3_taxi_body']}</p>
    </div>
    """, unsafe_allow_html=True)

# TAB 4: 숙소 주변 및 서울 핵심 명소 가는 법
with tab_spot:
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

# 7. 하단 푸터
st.markdown("""
<div style="text-align: center; padding: 24px 0 10px 0; color: #8C857B; font-size: 12.5px;">
    © 2026 <b>mongle-stay Seoul (Anam · Jegi-dong)</b>. All rights reserved.<br>
    Have a cozy and wonderful stay in Seoul 🐾
</div>
""", unsafe_allow_html=True)
