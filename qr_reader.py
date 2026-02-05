"""
QR 코드 리더기 - Streamlit 기반 클린 디자인
Deep Blue 테마의 직관적인 QR 코드 스캐너
"""

import streamlit as st
from PIL import Image
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime
import re
import qrcode  # QR 코드 생성
import io  # 바이트 스트림 처리

# ============================================
# 페이지 설정 (Clean Mode - Deep Blue Theme)
# ============================================
st.set_page_config(
    page_title="QR 코드 리더기 & 생성기",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# Custom CSS - Deep Blue Clean Theme
# ============================================
st.markdown("""
    <style>
    /* 전체 배경 및 폰트 설정 */
    .main {
        background-color: #FFFFFF;
    }
    
    /* 헤더 스타일링 */
    .header-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(30, 58, 138, 0.1);
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-align: center;
    }
    
    .header-subtitle {
        color: #dbeafe;
        font-size: 1rem;
        text-align: center;
        margin-top: 0.5rem;
    }
    
    /* 업로드 영역 스타일링 */
    .upload-section {
        background-color: #f8fafc;
        padding: 2rem;
        border-radius: 12px;
        border: 2px dashed #3b82f6;
        margin: 1.5rem 0;
    }
    
    /* 결과 카드 스타일링 */
    .result-card {
        background-color: #eff6ff;
        border-left: 4px solid #1e40af;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .result-title {
        color: #1e40af;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .result-content {
        background-color: white;
        padding: 1rem;
        border-radius: 6px;
        font-family: 'Courier New', monospace;
        word-wrap: break-word;
        color: #1f2937;
    }
    
    /* 히스토리 섹션 */
    .history-item {
        background-color: #f1f5f9;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #60a5fa;
    }
    
    .history-time {
        color: #64748b;
        font-size: 0.85rem;
        margin-bottom: 0.3rem;
    }
    
    /* 버튼 스타일 커스터마이징 */
    .stButton>button {
        background-color: #1e40af;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #1e3a8a;
        box-shadow: 0 4px 12px rgba(30, 58, 138, 0.3);
    }
    
    /* 파일 업로더 스타일링 */
    [data-testid="stFileUploader"] {
        background-color: transparent;
    }
    
    /* 경고 및 정보 메시지 색상 조정 */
    .stAlert {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# 세션 상태 초기화 (히스토리 관리)
# ============================================
if 'scan_history' not in st.session_state:
    st.session_state.scan_history = []

# ============================================
# 유틸리티 함수: URL 검증
# ============================================
def is_url(text):
    """
    주어진 텍스트가 URL 형식인지 확인하는 함수
    
    Args:
        text (str): 검증할 텍스트
        
    Returns:
        bool: URL 형식이면 True, 아니면 False
    """
    url_pattern = re.compile(
        r'^(https?://|www\.)'  # http://, https://, www. 로 시작
        r'[^\s]+$'  # 공백이 없는 문자열
    )
    return bool(url_pattern.match(text))

# ============================================
# 유틸리티 함수: QR 코드 디코딩
# ============================================
def decode_qr_code(image):
    """
    업로드된 이미지에서 QR 코드를 디코딩하는 함수
    
    Args:
        image (PIL.Image): Pillow 이미지 객체
        
    Returns:
        list: 디코딩된 QR 코드 데이터 리스트 (없으면 빈 리스트)
    """
    # PIL 이미지를 OpenCV 형식으로 변환
    img_array = np.array(image)
    
    # RGB를 BGR로 변환 (OpenCV는 BGR 사용)
    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    else:
        img_bgr = img_array
    
    # 그레이스케일로 변환 (QR 코드 인식률 향상)
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
    # QR 코드 디코딩
    decoded_objects = decode(gray)
    
    return decoded_objects

# ============================================
# 유틸리티 함수: 히스토리에 추가
# ============================================
def add_to_history(data):
    """
    스캔 결과를 히스토리에 추가하는 함수
    
    Args:
        data (str): QR 코드에서 읽은 데이터
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.scan_history.insert(0, {
        'time': timestamp,
        'data': data
    })
    # 최대 10개까지만 유지
    if len(st.session_state.scan_history) > 10:
        st.session_state.scan_history = st.session_state.scan_history[:10]

# ============================================
# 유틸리티 함수: QR 코드 생성
# ============================================
def generate_qr(data, fill_color='black', back_color='white', box_size=10, border=4, error_correction='M'):
    """
    주어진 데이터로 QR 코드를 생성하는 함수
    
    Args:
        data (str): QR 코드에 인코딩할 데이터 (URL 또는 텍스트)
        fill_color (str): QR 코드 전경색 (기본: 검정)
        back_color (str): QR 코드 배경색 (기본: 흰색)
        box_size (int): 각 박스의 픽셀 크기 (기본: 10)
        border (int): 테두리 두께 (기본: 4)
        error_correction (str): 오류 복구 수준 ('L', 'M', 'Q', 'H')
        
    Returns:
        PIL.Image: 생성된 QR 코드 이미지
    """
    # 오류 복구 수준 매핑
    error_correction_map = {
        'L': qrcode.constants.ERROR_CORRECT_L,  # 약 7% 복구
        'M': qrcode.constants.ERROR_CORRECT_M,  # 약 15% 복구
        'Q': qrcode.constants.ERROR_CORRECT_Q,  # 약 25% 복구
        'H': qrcode.constants.ERROR_CORRECT_H   # 약 30% 복구
    }
    
    # QR 코드 생성기 초기화
    qr = qrcode.QRCode(
        version=1,  # 1-40 사이 값, None이면 자동 조정
        error_correction=error_correction_map.get(error_correction, qrcode.constants.ERROR_CORRECT_M),
        box_size=box_size,
        border=border,
    )
    
    # 데이터 추가 및 이미지 생성
    qr.add_data(data)
    qr.make(fit=True)
    
    # 이미지 생성 및 PIL Image로 변환
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # PIL Image로 명시적 변환 (바이트 스트림 저장을 위해)
    img = qr_img.convert('RGB')
    
    return img


# ============================================
# 유틸리티 함수: QR 코드 결과 표시
# ============================================
def display_qr_results(decoded_objects):
    """
    디코딩된 QR 코드 결과를 화면에 표시하는 함수
    
    Args:
        decoded_objects (list): 디코딩된 QR 코드 객체 리스트
    """
    if decoded_objects:
        st.success(f"✅ {len(decoded_objects)}개의 QR 코드를 찾았습니다!")
        
        for idx, obj in enumerate(decoded_objects, 1):
            # QR 코드 데이터 추출
            qr_data = obj.data.decode('utf-8')
            
            # 히스토리에 추가
            add_to_history(qr_data)
            
            # 결과 카드 표시
            st.markdown(f"""
                <div class="result-card">
                    <div class="result-title">QR 코드 #{idx} 결과</div>
                </div>
            """, unsafe_allow_html=True)
            
            # URL인 경우: 방문하기 버튼 제공
            if is_url(qr_data):
                st.info("🔗 URL이 감지되었습니다")
                st.code(qr_data, language=None)
                
                # 새 탭에서 열기 버튼
                st.link_button(
                    "🌐 사이트 방문하기",
                    qr_data,
                    use_container_width=True
                )
            
            # 일반 텍스트인 경우: 복사하기 용이하게 코드 블록으로 표시
            else:
                st.info("📝 텍스트 데이터가 감지되었습니다")
                st.code(qr_data, language=None)
                st.caption("💡 위 텍스트를 선택하여 복사할 수 있습니다")
            
            # 구분선 (여러 개일 경우)
            if idx < len(decoded_objects):
                st.divider()
    
    else:
        # QR 코드를 찾지 못한 경우
        st.error("❌ QR 코드를 찾을 수 없습니다. 다시 시도해 주세요.")
        st.info("""
        **제안:**
        - 이미지가 선명한지 확인하세요
        - QR 코드가 잘 보이는지 확인하세요
        - 다른 각도나 조명에서 촬영한 이미지를 시도해보세요
        """)

# ============================================
# 메인 UI: 헤더
# ============================================
st.markdown("""
    <div class="header-container">
        <h1 class="header-title">📱 QR 코드 리더기 & 생성기</h1>
        <p class="header-subtitle">QR 코드를 스캔하거나 생성할 수 있는 올인원 도구</p>
    </div>
""", unsafe_allow_html=True)

# ============================================
# 메인 UI: 탭 구성 (파일 업로드 / 카메라 촬영 / QR 생성기)
# ============================================
tab1, tab2, tab3 = st.tabs(["📤 파일 업로드", "📷 카메라 촬영", "✨ QR 생성기"])

# ============================================
# 탭 1: 파일 업로드
# ============================================
with tab1:
    st.markdown("### 이미지 파일 업로드")
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "PNG, JPG, JPEG 파일을 드래그 앤 드롭하거나 선택하세요",
        type=['png', 'jpg', 'jpeg'],
        help="QR 코드가 포함된 이미지를 업로드하세요",
        key="file_uploader"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 파일이 업로드된 경우 처리
    if uploaded_file is not None:
        try:
            # 이미지 로드
            image = Image.open(uploaded_file)
            
            # 이미지 미리보기
            st.markdown("### 🖼️ 업로드된 이미지")
            st.image(image, use_container_width=True, caption="업로드된 이미지")
            
            # QR 코드 디코딩
            with st.spinner('QR 코드를 분석 중입니다...'):
                decoded_objects = decode_qr_code(image)
            
            # 결과 표시
            display_qr_results(decoded_objects)
        
        except Exception as e:
            st.error(f"⚠️ 이미지 처리 중 오류가 발생했습니다: {str(e)}")
            st.info("지원되는 파일 형식(PNG, JPG, JPEG)인지 확인해주세요.")

# ============================================
# 탭 2: 카메라 촬영
# ============================================
with tab2:
    st.markdown("### 카메라로 QR 코드 촬영")
    st.info("📸 아래 버튼을 클릭하여 카메라로 QR 코드를 촬영하세요")
    
    # 카메라 입력
    camera_image = st.camera_input(
        "카메라로 QR 코드 촬영",
        key="camera_input",
        help="카메라 권한을 허용하고 QR 코드를 촬영하세요"
    )
    
    # 카메라로 이미지를 촬영한 경우 처리
    if camera_image is not None:
        try:
            # 이미지 로드
            image = Image.open(camera_image)
            
            # 이미지 미리보기
            st.markdown("### 📸 촬영된 이미지")
            st.image(image, use_container_width=True, caption="촬영된 이미지")
            
            # QR 코드 디코딩
            with st.spinner('QR 코드를 분석 중입니다...'):
                decoded_objects = decode_qr_code(image)
            
            # 결과 표시
            display_qr_results(decoded_objects)
        
        except Exception as e:
            st.error(f"⚠️ 이미지 처리 중 오류가 발생했습니다: {str(e)}")
            st.info("다시 촬영해 주세요.")

# ============================================
# 탭 3: QR 코드 생성기
# ============================================
with tab3:
    st.markdown("### ✨ QR 코드 생성하기")
    st.info("💡 URL 또는 텍스트를 입력하면 실시간으로 QR 코드가 생성됩니다")
    
    # 사이드바에 커스터마이징 옵션 배치
    with st.sidebar:
        st.markdown("## 🎨 QR 코드 커스터마이징")
        
        # 색상 설정
        st.markdown("### 색상 설정")
        fill_color = st.color_picker(
            "전경색 (QR 코드 색상)",
            "#000000",
            help="QR 코드의 색상을 선택하세요"
        )
        back_color = st.color_picker(
            "배경색",
            "#FFFFFF",
            help="QR 코드 배경 색상을 선택하세요"
        )
        
        st.divider()
        
        # 크기 및 테두리 설정
        st.markdown("### 크기 설정")
        box_size = st.slider(
            "박스 크기 (픽셀)",
            min_value=5,
            max_value=20,
            value=10,
            step=1,
            help="각 QR 코드 박스의 픽셀 크기"
        )
        
        border = st.slider(
            "테두리 두께",
            min_value=1,
            max_value=10,
            value=4,
            step=1,
            help="QR 코드 주변 여백 크기"
        )
        
        st.divider()
        
        # 오류 복구 수준
        st.markdown("### 오류 복구 수준")
        error_correction = st.selectbox(
            "에러 복구 레벨",
            options=['L', 'M', 'Q', 'H'],
            index=1,  # 기본값: M
            help="""
            오류 복구 수준이 높을수록 손상된 QR 코드도 읽을 수 있습니다
            - L: 약 7% 복구
            - M: 약 15% 복구 (권장)
            - Q: 약 25% 복구
            - H: 약 30% 복구
            """
        )
    
    # 메인 화면: 입력 필드
    st.markdown("### 📝 데이터 입력")
    
    # 입력 방식 선택 (URL / 일반 텍스트)
    input_type = st.radio(
        "입력 유형 선택",
        options=["🔗 URL", "📝 텍스트"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    # 입력창
    if input_type == "🔗 URL":
        qr_data = st.text_input(
            "URL 입력",
            placeholder="https://example.com",
            help="QR 코드로 변환할 URL을 입력하세요"
        )
    else:
        qr_data = st.text_area(
            "텍스트 입력",
            placeholder="QR 코드로 변환할 텍스트를 입력하세요",
            help="최대 4296자까지 입력 가능 (에러 복구 수준에 따라 다름)",
            height=150
        )
    
    # 입력된 데이터가 있을 때만 QR 코드 생성
    if qr_data:
        try:
            # QR 코드 생성
            with st.spinner('QR 코드 생성 중...'):
                qr_image = generate_qr(
                    data=qr_data,
                    fill_color=fill_color,
                    back_color=back_color,
                    box_size=box_size,
                    border=border,
                    error_correction=error_correction
                )
            
            # 생성 완료 메시지
            st.success("✅ QR 코드가 생성되었습니다!")
            
            # 미리보기 섹션
            st.markdown("### 🖼️ 미리보기")
            
            # 레이아웃: 미리보기 + 정보
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # QR 코드 이미지 표시
                st.image(qr_image, caption="생성된 QR 코드", use_container_width=True)
            
            with col2:
                st.markdown("**📊 QR 코드 정보**")
                st.markdown(f"- **데이터 길이:** {len(qr_data)}자")
                st.markdown(f"- **박스 크기:** {box_size}px")
                st.markdown(f"- **테두리:** {border}px")
                st.markdown(f"- **에러 복구:** {error_correction}")
                st.markdown(f"- **전경색:** {fill_color}")
                st.markdown(f"- **배경색:** {back_color}")
            
            st.divider()
            
            # 다운로드 섹션
            st.markdown("### 💾 다운로드")
            
            # 파일명 입력
            col_name, col_format = st.columns([3, 1])
            
            with col_name:
                file_name = st.text_input(
                    "파일명",
                    value="my_qrcode",
                    help="저장할 파일명을 입력하세요 (확장자 제외)"
                )
            
            with col_format:
                file_format = st.selectbox(
                    "형식",
                    options=["PNG", "JPEG"],
                    index=0
                )
            
            # 이미지를 바이트 스트림으로 변환
            img_bytes = io.BytesIO()
            qr_image.save(img_bytes, format=file_format)
            img_bytes.seek(0)
            
            # 다운로드 버튼
            st.download_button(
                label=f"📥 {file_name}.{file_format.lower()} 다운로드",
                data=img_bytes,
                file_name=f"{file_name}.{file_format.lower()}",
                mime=f"image/{file_format.lower()}",
                use_container_width=True,
                type="primary"
            )
            
            # 성공 애니메이션 (선택사항)
            # st.balloons()  # 사용자가 원하면 주석 해제
        
        except Exception as e:
            st.error(f"⚠️ QR 코드 생성 중 오류가 발생했습니다: {str(e)}")
            st.info("""
            **문제 해결 팁:**
            - 입력 데이터가 너무 길지 않은지 확인하세요
            - 특수 문자가 포함되어 있다면 인코딩 문제가 있을 수 있습니다
            - 에러 복구 수준을 낮춰보세요
            """)
    
    else:
        # 입력 대기 상태
        st.info("👆 위에 URL 또는 텍스트를 입력하면 QR 코드가 자동으로 생성됩니다")


# ============================================
# 히스토리 섹션
# ============================================
if st.session_state.scan_history:
    st.markdown("---")
    st.markdown("### 📜 스캔 히스토리")
    st.caption("현재 세션에서 스캔한 QR 코드 기록 (최대 10개)")
    
    for item in st.session_state.scan_history:
        with st.container():
            st.markdown(f"""
                <div class="history-item">
                    <div class="history-time">🕐 {item['time']}</div>
                    <div style="color: #1f2937; font-weight: 500;">
                        {item['data'][:100]}{"..." if len(item['data']) > 100 else ""}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    # 히스토리 초기화 버튼
    if st.button("🗑️ 히스토리 전체 삭제", type="secondary"):
        st.session_state.scan_history = []
        st.rerun()

# ============================================
# 푸터
# ============================================
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #64748b; padding: 1rem;">
        <p style="margin: 0;">
            💡 <strong>Tip:</strong> QR 코드가 선명하게 보이는 이미지를 사용하면 인식률이 높아집니다
        </p>
    </div>
""", unsafe_allow_html=True)
