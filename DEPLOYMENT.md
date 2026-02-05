# 🚀 QR 코드 앱 배포 가이드

이 문서는 QR 코드 리더기 & 생성기를 온라인에 배포하는 방법을 설명합니다.

---

## 📋 목차

1. [Streamlit Community Cloud 배포 (무료, 권장)](#streamlit-community-cloud-배포)
2. [기타 배포 옵션](#기타-배포-옵션)
3. [문제 해결](#문제-해결)

---

## 🌐 Streamlit Community Cloud 배포

### ✅ 장점
- ✅ **완전 무료**
- ✅ GitHub 연동으로 **자동 배포**
- ✅ 코드 변경 시 **자동 업데이트**
- ✅ **HTTPS** 자동 제공
- ✅ 설정이 **매우 간단**

### 📋 사전 준비 (완료됨!)

- ✅ GitHub 계정
- ✅ GitHub 저장소 (https://github.com/LouiEll2033/QR)
- ✅ `requirements.txt` - 파이썬 패키지
- ✅ `packages.txt` - 시스템 라이브러리 (libzbar0)
- ✅ `qr_reader.py` - 메인 앱 파일

---

## 🚀 배포 단계별 가이드

### Step 1: Streamlit Community Cloud 접속

1. 브라우저에서 접속: **https://share.streamlit.io/**
2. **"Sign in with GitHub"** 클릭
3. GitHub 계정으로 로그인

![Streamlit Community Cloud 로그인](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-empty-state.png)

---

### Step 2: 새 앱 배포

1. **"New app"** 버튼 클릭
2. 다음 정보 입력:

| 필드 | 입력값 |
|------|--------|
| **Repository** | `LouiEll2033/QR` |
| **Branch** | `master` (또는 `main`) |
| **Main file path** | `qr_reader.py` |
| **App URL** | 원하는 URL (예: `qr-code-app`) |

3. **"Deploy!"** 버튼 클릭

![앱 배포 설정](https://docs.streamlit.io/images/streamlit-community-cloud/deploy-an-app.png)

---

### Step 3: 배포 확인

배포가 시작되면 다음 과정을 거칩니다:

```
📦 Installing dependencies...
   ↓ pip install -r requirements.txt
   ↓ apt-get install libzbar0

🔨 Building app...
   ↓ Loading qr_reader.py

🚀 Launching app...
   ✅ Your app is live!
```

**예상 시간**: 3~5분

---

### Step 4: 앱 URL 확인

배포가 완료되면 다음과 같은 URL이 제공됩니다:

```
https://[your-app-name].streamlit.app
```

**예시**: `https://qr-code-app.streamlit.app`

---

## 🎉 배포 완료!

이제 전 세계 누구나 이 URL로 접속하여 QR 코드 앱을 사용할 수 있습니다!

### 공유 방법
- 📱 친구에게 URL 전송
- 🌐 웹사이트에 링크 추가
- 📧 이메일 서명에 포함
- 💼 명함에 QR 코드로 인쇄

---

## 🔄 자동 업데이트

코드를 수정하고 GitHub에 푸시하면 **자동으로 앱이 업데이트**됩니다!

```bash
# 코드 수정 후
git add .
git commit -m "UI 개선"
git push

# 약 1~2분 후 자동 배포 완료!
```

---

## ⚙️ 고급 설정 (선택사항)

### 1. 커스텀 도메인 사용

Streamlit Community Cloud는 현재 커스텀 도메인을 지원하지 않습니다.
대신 다음을 사용하세요:
- URL 단축 서비스 (bit.ly, tinyurl.com)
- 리디렉션 서비스

### 2. 환경 변수 설정

API 키 등 민감한 정보를 사용하는 경우:

1. Streamlit Cloud 대시보드에서 앱 선택
2. **"Settings"** → **"Secrets"** 클릭
3. TOML 형식으로 비밀 정보 입력:

```toml
# .streamlit/secrets.toml
api_key = "your-secret-key"
db_password = "your-password"
```

앱에서 사용:
```python
import streamlit as st

api_key = st.secrets["api_key"]
```

### 3. 리소스 제한

무료 플랜의 제한:
- **메모리**: 1GB
- **CPU**: 공유 vCPU
- **앱 수**: 무제한 (공개 앱)
- **비활성 시간**: 7일 미접속 시 슬립 모드

---

## 🐛 문제 해결

### ❌ 문제 1: "ModuleNotFoundError: No module named 'pyzbar'"

**원인**: `requirements.txt`에 pyzbar 누락

**해결**:
```bash
# requirements.txt에 추가 확인
grep pyzbar requirements.txt

# 없다면 추가
echo "pyzbar>=0.1.9" >> requirements.txt
git add requirements.txt
git commit -m "Add pyzbar to requirements"
git push
```

---

### ❌ 문제 2: "ImportError: Unable to find zbar shared library"

**원인**: `packages.txt` 누락 또는 잘못된 패키지명

**해결**:
```bash
# packages.txt 내용 확인
cat packages.txt
# 출력: libzbar0

# 없다면 생성
echo "libzbar0" > packages.txt
git add packages.txt
git commit -m "Add libzbar0 for pyzbar"
git push
```

---

### ❌ 문제 3: "App is taking too long to load"

**원인**: 의존성 설치에 시간이 오래 걸림

**해결**:
- 첫 배포는 5분 정도 소요될 수 있음
- 새로고침 후 다시 확인
- Streamlit Cloud 대시보드에서 로그 확인

---

### ❌ 문제 4: 앱이 슬립 모드에 들어감

**증상**: 7일간 접속이 없으면 앱이 슬립 상태

**해결**:
- URL 접속 시 자동으로 재시작 (약 30초 소요)
- 또는: 정기적으로 앱 접속
- 또는: 유료 플랜으로 업그레이드

---

## 📊 배포 상태 모니터링

### Streamlit Cloud 대시보드에서 확인 가능한 정보:

- ✅ **Status**: 앱 실행 상태
- 📈 **Analytics**: 방문자 통계
- 📋 **Logs**: 실시간 로그
- ⚙️ **Settings**: 설정 변경
- 🔄 **Reboot**: 수동 재시작

---

## 🎯 기타 배포 옵션

### 2. Heroku (유료 전환됨)

과거에는 무료였으나 현재는 유료입니다.

**비용**: 월 $7~

**배포 방법**:
```bash
# Heroku CLI 설치 후
heroku create qr-code-app
git push heroku master
```

---

### 3. Docker + AWS/GCP/Azure

고급 사용자를 위한 옵션입니다.

**장점**:
- 완전한 제어
- 높은 성능
- 커스텀 도메인

**단점**:
- 복잡한 설정
- 유료 (월 $5~50)

---

### 4. Vercel / Netlify

정적 사이트 호스팅 서비스이므로 Streamlit 앱은 직접 배포 불가.

대신 **Streamlit → HTML 변환** 후 배포 가능하지만 권장하지 않음.

---

## 📱 모바일 최적화

Streamlit 앱은 자동으로 반응형이지만, 추가 최적화:

```python
# qr_reader.py에 추가
st.set_page_config(
    page_title="QR 코드 앱",
    page_icon="📱",
    layout="centered",  # 모바일에 최적화
    initial_sidebar_state="collapsed"  # 사이드바 기본 닫힘
)
```

---

## 🔒 보안 고려사항

### 공개 배포 시 주의할 점:

1. **API 키 노출 방지**
   - 코드에 직접 하드코딩 금지
   - `st.secrets` 사용

2. **파일 업로드 제한**
   - 악성 파일 업로드 방지
   - 파일 크기 제한 설정

```python
# 파일 크기 제한 예시
uploaded_file = st.file_uploader(
    "이미지 업로드",
    type=['png', 'jpg', 'jpeg'],
    accept_multiple_files=False,
    # 5MB 제한
)

if uploaded_file and uploaded_file.size > 5 * 1024 * 1024:
    st.error("파일 크기는 5MB 이하여야 합니다.")
```

3. **속도 제한**
   - 무분별한 요청 방지
   - Streamlit의 자동 재실행 제어

---

## 📈 다음 단계

배포 완료 후 할 수 있는 것:

### 1. 분석 추가
```python
# Google Analytics 추가
st.components.v1.html("""
    <!-- Google Analytics 코드 -->
""")
```

### 2. 사용자 피드백 수집
```python
feedback = st.text_area("피드백을 남겨주세요")
if st.button("제출"):
    # 피드백 저장 로직
    st.success("감사합니다!")
```

### 3. 소셜 공유 버튼
```python
st.markdown("""
    <a href="https://twitter.com/intent/tweet?text=QR코드앱사용해보세요!&url=your-app-url">
        트위터에 공유
    </a>
""", unsafe_allow_html=True)
```

---

## 🎓 참고 자료

### 공식 문서
- [Streamlit Community Cloud 문서](https://docs.streamlit.io/streamlit-community-cloud)
- [배포 가이드](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app)
- [문제 해결](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/app-dependencies)

### 커뮤니티
- [Streamlit 포럼](https://discuss.streamlit.io/)
- [Discord](https://discord.gg/streamlit)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

---

## ✅ 배포 체크리스트

배포 전 확인사항:

- [ ] GitHub 저장소에 코드 푸시 완료
- [ ] `requirements.txt` 파일 존재
- [ ] `packages.txt` 파일 존재 (pyzbar 사용 시)
- [ ] `qr_reader.py` 파일명 확인
- [ ] 로컬에서 정상 작동 확인
- [ ] API 키 등 민감 정보 환경 변수로 이동
- [ ] README.md에 배포 URL 추가 예정

배포 후 확인사항:

- [ ] 앱 URL 정상 접속
- [ ] 모든 기능 정상 작동
- [ ] 파일 업로드 테스트
- [ ] QR 생성 테스트
- [ ] 모바일 반응형 확인
- [ ] 성능 모니터링

---

<div align="center">

## 🚀 배포 준비 완료!

이제 **https://share.streamlit.io** 에 접속하여  
**"New app"** 버튼을 클릭하고 배포를 시작하세요!

🎉 **축하합니다! 여러분의 앱이 곧 전 세계에 공개됩니다!** 🎉

</div>
