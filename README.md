# 📱 QR 코드 리더기 & 생성기

Deep Blue 테마의 클린하고 직관적인 Streamlit 기반 QR 코드 올인원 도구

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

## ✨ 주요 기능

### 📱 세 가지 기능 (탭 UI)

| 탭 | 아이콘 | 기능 | 설명 |
|---|---|---|---|
| **파일 업로드** | 📤 | QR 코드 읽기 | PNG, JPG, JPEG 파일을 드래그 앤 드롭으로 QR 코드 스캔 |
| **카메라 촬영** | 📷 | QR 코드 읽기 | 실시간 카메라로 QR 코드 즉시 촬영 및 인식 |
| **QR 생성기** | ✨ | QR 코드 생성 | URL/텍스트를 입력하여 커스텀 QR 코드 제작 |

### 🔍 리더기 기능

- ✅ **자동 QR 스캔**: 이미지 입력 즉시 QR 코드 자동 인식
- 🔗 **스마트 URL 처리**: URL 감지 시 '사이트 방문하기' 버튼 자동 제공
- 📝 **텍스트 처리**: 일반 텍스트는 복사 용이한 코드 블록으로 표시
- 📜 **히스토리 관리**: 현재 세션의 스캔 기록 자동 저장 (최대 10개)
- 🗑️ **히스토리 삭제**: 원클릭으로 전체 기록 초기화
- 🎯 **다중 QR 인식**: 하나의 이미지에서 여러 QR 코드 동시 인식

### ✨ 생성기 기능

- ⚡ **실시간 생성**: 입력값 변경 시 즉시 QR 코드 생성 및 미리보기
- 🎨 **완벽한 커스터마이징**:
  - 🎨 **색상 선택**: 전경색 및 배경색 자유 선택 (컬러 피커)
  - 📏 **크기 조정**: 박스 크기 5~20px 슬라이더 조정
  - 🖼️ **테두리 설정**: 테두리 두께 1~10px 조정
  - 🛡️ **오류 복구**: L(7%), M(15%), Q(25%), H(30%) 4단계 선택
- 💾 **유연한 다운로드**: PNG 또는 JPEG 형식, 사용자 지정 파일명
- 📊 **상세 정보 표시**: 생성된 QR 코드의 모든 설정값 실시간 표시
- 🔗 **URL/텍스트 지원**: 웹사이트 주소, 연락처, 메시지 등 다양한 데이터 인코딩

## 🛠️ 기술 스택

| 분류 | 라이브러리 | 버전 | 용도 |
|---|---|---|---|
| **프레임워크** | Streamlit | ≥1.31.0 | 웹 애플리케이션 프레임워크 |
| **이미지 처리** | Pillow | ≥10.0.0 | 이미지 로딩 및 편집 |
| **이미지 처리** | OpenCV | ≥4.8.0.74 | 이미지 전처리 및 변환 |
| **QR 디코딩** | pyzbar | ≥0.1.9 | QR 코드 읽기 (리더기) |
| **QR 생성** | qrcode[pil] | ≥7.4.2 | QR 코드 생성 (생성기) |
| **스타일링** | Custom CSS | - | Deep Blue Clean Theme |

## 📦 설치 방법

### 1. 저장소 클론 또는 다운로드

```bash
# Git을 사용하는 경우
git clone <repository-url>
cd qr_reader

# 또는 ZIP 파일 다운로드 후 압축 해제
```

### 2. 의존성 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. Windows 사용자 추가 설정 (pyzbar 전용)

Windows에서 pyzbar를 사용하려면 **zbar 라이브러리**가 필요합니다:

#### 방법 1: vcpkg 사용 (권장)
```bash
vcpkg install zbar:x64-windows
```

#### 방법 2: 수동 설치
1. [zbar 다운로드 페이지](http://zbar.sourceforge.net/download.html)에서 Windows용 바이너리 다운로드
2. `libiconv.dll`과 `libzbar-64.dll`을 Python 실행 경로 또는 시스템 PATH에 추가

💡 **참고**: 자세한 내용은 [pyzbar 공식 문서](https://github.com/NaturalHistoryMuseum/pyzbar#installation)를 참고하세요.

## 🚀 실행 방법

### 애플리케이션 시작

```bash
streamlit run qr_reader.py
```

실행 후 브라우저에서 자동으로 열립니다:
- **로컬 URL**: http://localhost:8501
- **네트워크 URL**: http://[your-ip]:8501

### 종료 방법

터미널에서 `Ctrl + C` 누르기

## 📖 사용 방법

### 📤 방법 1: 파일 업로드로 QR 코드 읽기

1. 브라우저에서 앱 열기 (http://localhost:8501)
2. **"📤 파일 업로드" 탭** 선택
3. QR 코드가 포함된 이미지를 업로드 영역에 **드래그 앤 드롭** 또는 클릭하여 선택
4. 업로드 즉시 QR 코드가 자동으로 분석됩니다
5. **결과 확인**:
   - 🔗 URL인 경우: `🌐 사이트 방문하기` 버튼으로 바로 접속
   - 📝 텍스트인 경우: 코드 블록에서 복사 가능
6. 여러 개의 QR 코드가 있으면 모두 인식되어 표시됩니다

### 📷 방법 2: 카메라로 QR 코드 촬영하기

1. 브라우저에서 앱 열기
2. **"📷 카메라 촬영" 탭** 선택
3. 브라우저에서 카메라 권한 요청 시 **"허용"** 클릭
4. QR 코드를 카메라 화면에 맞추기
5. **"Take Photo"** 버튼 클릭하여 촬영
6. 촬영 즉시 QR 코드가 자동으로 분석됩니다
7. **결과 확인**:
   - 🔗 URL인 경우: `🌐 사이트 방문하기` 버튼으로 바로 접속
   - 📝 텍스트인 경우: 코드 블록에서 복사 가능

### ✨ 방법 3: QR 코드 생성하기

1. 브라우저에서 앱 열기
2. **"✨ QR 생성기" 탭** 선택
3. **사이드바에서 디자인 커스터마이징** (선택사항):
   
   **색상 설정**
   - 🎨 **전경색**: QR 코드의 메인 색상 선택 (기본: 검정)
   - 🎨 **배경색**: QR 코드의 배경 색상 선택 (기본: 흰색)
   
   **크기 설정**
   - 📏 **박스 크기**: 5~20px 조정 (기본: 10px)
   - 🖼️ **테두리 두께**: 1~10px 조정 (기본: 4px)
   
   **오류 복구 수준**
   - L: 약 7% 복구 (가장 빠름)
   - M: 약 15% 복구 (권장, 기본값)
   - Q: 약 25% 복구
   - H: 약 30% 복구 (가장 안전)

4. **메인 화면에서 데이터 입력**:
   - 🔗 **URL**: 웹사이트 주소 입력 (예: https://example.com)
   - 📝 **텍스트**: 일반 텍스트 입력 (최대 4296자)

5. **실시간 미리보기**: 입력 즉시 QR 코드 자동 생성 및 표시
   - 🖼️ 생성된 QR 코드 이미지
   - 📊 상세 정보 (데이터 길이, 설정값 등)

6. **다운로드**:
   - 파일명 입력 (기본: `my_qrcode`)
   - 형식 선택: **PNG** (투명 배경 지원) 또는 **JPEG**
   - `📥 다운로드` 버튼 클릭

### 📜 히스토리 확인 및 관리

페이지 하단에서 현재 세션의 **스캔 히스토리**를 확인할 수 있습니다:
- ⏰ 스캔 시각 표시
- 📄 스캔한 데이터 미리보기 (최대 100자)
- 🗑️ `히스토리 전체 삭제` 버튼으로 기록 초기화
- 자동으로 최신 10개만 유지

## 🎨 디자인 특징

### 테마
- **메인 색상**: Deep Blue (#1e3a8a ~ #3b82f6)
- **배경**: Clean White (#FFFFFF)
- **강조색**: Accent Blue (#60a5fa)

### UI/UX
- ✅ **반응형 레이아웃**: 중앙 집중형 디자인으로 시선 분산 방지
- ✅ **탭 기반 인터페이스**: 3개 탭으로 기능 분리
- ✅ **사이드바 활용**: 생성기 설정을 사이드바에 배치하여 메인 화면 깔끔하게 유지
- ✅ **컬러 시스템**: 컬러 피커로 직관적인 색상 선택
- ✅ **실시간 피드백**: 스피너, 성공/오류 메시지로 상태 명확히 표시

### 주요 컴포넌트
- 🎯 **그라데이션 헤더**: 눈에 띄는 Deep Blue 그라데이션
- 📤 **대시 보더 업로드 영역**: 드래그 앤 드롭 명확히 표시
- 📷 **실시간 카메라 프리뷰**: 카메라 피드 즉시 확인
- 🎨 **컬러 피커 & 슬라이더**: 생성기 커스터마이징 UI
- 📊 **결과 카드**: 색상으로 구분된 결과 표시 영역
- 📜 **히스토리 타임라인**: 간결한 시간순 기록

## 🔧 주요 함수

### 리더기 관련 함수

```python
is_url(text: str) -> bool
```
- **기능**: 텍스트가 URL 형식인지 정규식으로 검증
- **반환**: URL이면 True, 아니면 False

```python
decode_qr_code(image: PIL.Image) -> list
```
- **기능**: PIL 이미지에서 QR 코드를 디코딩
- **처리**: RGB → BGR → 그레이스케일 변환 후 pyzbar로 디코딩
- **반환**: 디코딩된 QR 코드 객체 리스트

```python
add_to_history(data: str) -> None
```
- **기능**: 스캔 결과를 세션 히스토리에 추가
- **처리**: 타임스탬프와 함께 저장, 최대 10개 유지

```python
display_qr_results(decoded_objects: list) -> None
```
- **기능**: 디코딩된 QR 코드 결과를 화면에 표시
- **처리**: URL/텍스트 자동 구분, 적절한 UI 컴포넌트 렌더링

### 생성기 관련 함수

```python
generate_qr(
    data: str, 
    fill_color: str = 'black', 
    back_color: str = 'white', 
    box_size: int = 10, 
    border: int = 4, 
    error_correction: str = 'M'
) -> PIL.Image
```
- **기능**: 커스터마이징된 QR 코드 생성
- **매개변수**:
  - `data`: 인코딩할 데이터 (URL 또는 텍스트)
  - `fill_color`: 전경색 (Hex 코드)
  - `back_color`: 배경색 (Hex 코드)
  - `box_size`: 박스 픽셀 크기 (5~20)
  - `border`: 테두리 두께 (1~10)
  - `error_correction`: 복구 수준 ('L'|'M'|'Q'|'H')
- **반환**: 표준 PIL Image 객체 (RGB 모드)
- **특징**: `.convert('RGB')` 처리로 바이트 스트림 저장 호환성 확보

## ⚠️ 예외 처리

### 리더기 예외 처리

| 상황 | 처리 방법 |
|---|---|
| QR 코드 없음 | ❌ 명확한 안내 메시지 + 개선 제안 (조명, 각도, 선명도) |
| 잘못된 파일 형식 | ⚠️ 지원 형식 안내 (PNG, JPG, JPEG) |
| 이미지 처리 오류 | 🔧 상세한 오류 메시지 및 디버깅 정보 제공 |
| 카메라 권한 거부 | 📷 권한 허용 안내 표시 |

### 생성기 예외 처리

| 상황 | 처리 방법 |
|---|---|
| 데이터 길이 초과 | 📏 에러 복구 수준 조정 제안 |
| 특수 문자 인코딩 문제 | 🔤 문제 해결 팁 제공 |
| 이미지 생성 실패 | 🔧 상세 오류 메시지 및 원인 설명 |
| 빈 입력 | 💡 입력 대기 안내 메시지 표시 |

## 📂 프로젝트 구조

```
qr_reader/
│
├── qr_reader.py          # 메인 애플리케이션 (리더기 + 생성기 통합)
│   ├── [Import 섹션]
│   ├── [페이지 설정]
│   ├── [Custom CSS - Deep Blue Theme]
│   ├── [세션 상태 초기화]
│   ├── [유틸리티 함수들]
│   │   ├── is_url()
│   │   ├── decode_qr_code()
│   │   ├── add_to_history()
│   │   ├── generate_qr()          ✨ 신규
│   │   └── display_qr_results()
│   ├── [메인 UI]
│   │   ├── 헤더
│   │   ├── 탭 1: 파일 업로드
│   │   ├── 탭 2: 카메라 촬영
│   │   └── 탭 3: QR 생성기       ✨ 신규
│   ├── [히스토리 섹션]
│   └── [푸터]
│
├── requirements.txt      # 의존성 패키지 목록
│   ├── streamlit         # 웹 프레임워크
│   ├── Pillow            # 이미지 처리
│   ├── opencv-python-headless  # 이미지 변환
│   ├── pyzbar            # QR 디코딩 (리더기)
│   └── qrcode[pil]       # QR 생성 (생성기) ✨ 신규
│
└── README.md             # 프로젝트 문서 (이 파일)
```

## 🐛 문제 해결 (Troubleshooting)

### 일반적인 문제

#### 1. pyzbar 관련 오류 (Windows)

**증상**:
```
ImportError: Unable to find zbar shared library
```

**해결 방법**:
- vcpkg로 zbar 설치: `vcpkg install zbar:x64-windows`
- 또는 [zbar 공식 사이트](http://zbar.sourceforge.net/download.html)에서 DLL 다운로드

#### 2. QR 코드 생성 시 "bytes-like object is required" 오류

**증상**:
```
TypeError: a bytes-like object is required, not 'PilImage'
```

**해결 방법**:
- ✅ **이미 수정됨**: `qr_img.convert('RGB')` 추가로 해결
- 최신 코드 사용 시 이 문제 발생하지 않음

#### 3. QR 코드 인식 실패

**개선 방법**:
- ✅ 이미지가 선명한지 확인
- ✅ QR 코드가 잘 보이는지 확인 (전체가 포함되어야 함)
- ✅ 조명이 충분한 환경에서 촬영
- ✅ 다른 각도나 거리에서 재촬영

#### 4. Streamlit 실행 안 됨

**해결 방법**:
```bash
# Streamlit 재설치
pip uninstall streamlit
pip install streamlit

# 또는 가상환경 재생성
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 💡 활용 예시

### QR 코드 리더기로 할 수 있는 것
- ✅ 명함에 있는 QR 코드에서 연락처 정보 추출
- ✅ 포스터의 QR 코드로 이벤트 페이지 바로 접속
- ✅ 제품 패키지의 QR 코드로 제품 정보 확인
- ✅ 여러 QR 코드가 있는 문서 일괄 스캔

### QR 코드 생성기로 할 수 있는 것
- ✅ 개인 웹사이트/블로그 주소를 QR 코드로 제작
- ✅ Wi-Fi 비밀번호를 QR 코드로 공유
- ✅ 이벤트 초대장에 넣을 위치 정보 QR 코드 생성
- ✅ 브랜드 색상에 맞춘 커스텀 QR 코드 제작
- ✅ SNS 계정, 연락처, 이메일 주소 등을 QR 코드화

## 🔄 업데이트 내역

### v2.0 (2026-02-05) ✨ 최신
- ✅ QR 코드 생성기 기능 추가
- ✅ 3탭 UI로 확장 (파일 업로드 / 카메라 / 생성기)
- ✅ 사이드바 커스터마이징 옵션 추가
- ✅ 실시간 QR 코드 미리보기
- ✅ PNG/JPEG 다운로드 기능
- ✅ PIL Image 변환 이슈 수정

### v1.0 (2026-02-05)
- ✅ QR 코드 리더기 기본 기능 구현
- ✅ 파일 업로드 및 카메라 촬영 지원
- ✅ URL/텍스트 자동 구분
- ✅ 히스토리 관리 기능
- ✅ Deep Blue 테마 적용

## 📝 라이선스

이 프로젝트는 **개인 및 상업적 용도로 자유롭게 사용**할 수 있습니다.

## 🤝 기여

버그 리포트, 기능 제안, Pull Request는 언제든 환영합니다!

### 기여 방법
1. 이 저장소를 Fork
2. 새로운 브랜치 생성 (`git checkout -b feature/AmazingFeature`)
3. 변경사항 커밋 (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 Push (`git push origin feature/AmazingFeature`)
5. Pull Request 생성

## 📧 연락처

프로젝트에 대한 문의사항이 있으시면 이슈를 생성해주세요.

---

<div align="center">

**Made with ❤️ using Streamlit**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](http://localhost:8501)

**QR 코드로 세상을 연결하세요! 🌐**

</div>
