# 📤 GitHub 업로드 & Streamlit 배포 가이드

> **소요 시간**: 10분  
> **난이도**: 초급  
> **준비물**: GitHub 계정, Git 설치

---

## 📋 목차

1. [Part 1: GitHub에 프로젝트 업로드](#part-1-github에-프로젝트-업로드)
2. [Part 2: Streamlit Community Cloud 배포](#part-2-streamlit-community-cloud-배포)
3. [문제 해결](#문제-해결)

---

# Part 1: GitHub에 프로젝트 업로드

## 🎯 목표
로컬 프로젝트를 GitHub 저장소에 업로드하기

---

## 📝 Step 1: GitHub 저장소 생성

### 1-1. GitHub 웹사이트 접속
```
https://github.com
```

### 1-2. 새 저장소 생성
1. 오른쪽 상단 **"+"** 버튼 클릭
2. **"New repository"** 선택
3. 저장소 정보 입력:
   - **Repository name**: `QR` (원하는 이름)
   - **Description**: `QR코드 리더기 및 생성기`
   - **Public** 선택 (무료 배포를 위해)
   - ❌ **Initialize this repository with a README** 체크 해제
4. **"Create repository"** 클릭

### 1-3. 저장소 URL 복사
생성된 저장소 페이지에서 URL 복사:
```
https://github.com/[사용자명]/QR.git
```

---

## 💻 Step 2: 로컬 프로젝트에서 Git 초기화

### 2-1. 프로젝트 폴더로 이동
터미널(또는 PowerShell)을 열고:

```bash
cd c:\Users\ComHolic\intel_project_son\qr_reader
```

### 2-2. Git 초기화
```bash
git init
```

**예상 출력**:
```
Initialized empty Git repository in C:/Users/ComHolic/intel_project_son/qr_reader/.git/
```

---

## 🔗 Step 3: 원격 저장소 연결

```bash
git remote add origin https://github.com/[사용자명]/QR.git
```

**예시**:
```bash
git remote add origin https://github.com/LouiEll2033/QR.git
```

**확인**:
```bash
git remote -v
```

**예상 출력**:
```
origin  https://github.com/LouiEll2033/QR.git (fetch)
origin  https://github.com/LouiEll2033/QR.git (push)
```

---

## 📦 Step 4: 파일 추가 및 커밋

### 4-1. 모든 파일 스테이징
```bash
git add .
```

### 4-2. 커밋 생성
```bash
git commit -m "QR 코드 리더기 & 생성기 완성"
```

**예상 출력**:
```
[master (root-commit) 4d9a819] QR 코드 리더기 & 생성기 완성
 5 files changed, 2000 insertions(+)
 create mode 100644 README.md
 create mode 100644 TUTORIAL.md
 create mode 100644 qr_reader.py
 create mode 100644 requirements.txt
 create mode 100644 packages.txt
```

---

## 🚀 Step 5: GitHub에 푸시

```bash
git push -u origin master
```

**또는 main 브랜치를 사용하는 경우**:
```bash
git push -u origin main
```

**예상 출력**:
```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 20.07 KiB | 6.69 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/LouiEll2033/QR.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

---

## ✅ Step 6: GitHub에서 확인

브라우저에서 저장소 URL 접속:
```
https://github.com/[사용자명]/QR
```

다음 파일들이 보여야 합니다:
- ✅ `qr_reader.py`
- ✅ `requirements.txt`
- ✅ `packages.txt`
- ✅ `README.md`
- ✅ `TUTORIAL.md`

---

## 🔄 코드 수정 후 다시 업로드하기

```bash
# 1. 변경사항 스테이징
git add .

# 2. 커밋
git commit -m "UI 개선"

# 3. 푸시
git push
```

---

# Part 2: Streamlit Community Cloud 배포

## 🎯 목표
GitHub에 올린 프로젝트를 온라인 웹앱으로 배포하기

---

## 📋 사전 준비 체크리스트

배포 전 필수 파일 확인:

- [ ] `qr_reader.py` - 메인 앱 파일
- [ ] `requirements.txt` - Python 패키지 목록
- [ ] `packages.txt` - 시스템 라이브러리 (libzbar0 포함)

### requirements.txt 내용 확인
```txt
streamlit>=1.31.0
Pillow>=10.0.0
opencv-python-headless>=4.8.0.74
pyzbar>=0.1.9
qrcode[pil]>=7.4.2
```

### packages.txt 내용 확인
```txt
libzbar0
```

---

## 🌐 Step 1: Streamlit Community Cloud 회원가입

### 1-1. 웹사이트 접속
```
https://share.streamlit.io/
```

### 1-2. GitHub 계정으로 로그인
1. **"Sign in with GitHub"** 클릭
2. GitHub 계정 로그인
3. Streamlit에 권한 부여 승인

---

## 🚀 Step 2: 새 앱 배포

### 2-1. 대시보드에서 "New app" 클릭

첫 화면에 큰 버튼으로 표시됩니다.

### 2-2. 배포 정보 입력

| 항목 | 설명 | 예시 |
|------|------|------|
| **Repository** | GitHub 저장소 선택 | `LouiEll2033/QR` |
| **Branch** | 배포할 브랜치 | `master` 또는 `main` |
| **Main file path** | 메인 Python 파일 경로 | `qr_reader.py` |
| **App URL (optional)** | 원하는 앱 주소 | `qr-code-app` |

### 2-3. "Deploy!" 버튼 클릭

---

## ⏳ Step 3: 배포 진행 상황 확인

배포가 시작되면 실시간 로그를 볼 수 있습니다:

```
🔧 Preparing environment...
   ↓ Installing system packages from packages.txt
   ✓ libzbar0 installed

📦 Installing Python packages...
   ↓ pip install -r requirements.txt
   ✓ streamlit installed
   ✓ Pillow installed
   ✓ opencv-python-headless installed
   ✓ pyzbar installed
   ✓ qrcode[pil] installed

🔨 Building app...
   ↓ Loading qr_reader.py
   ✓ App loaded successfully

🚀 Starting app...
   ✅ Your app is live at: https://qr-code-app.streamlit.app
```

**예상 소요 시간**: 3~5분

---

## ✅ Step 4: 배포 완료!

### 4-1. 앱 URL 확인
배포가 완료되면 다음과 같은 URL이 제공됩니다:

```
https://[your-app-name].streamlit.app
```

**예시**:
```
https://qr-code-app.streamlit.app
```

### 4-2. 앱 테스트
1. 제공된 URL 클릭
2. QR 코드 리더기 기능 테스트
3. QR 코드 생성기 기능 테스트

---

## 🔄 Step 5: 자동 업데이트 설정 (이미 적용됨)

GitHub에 코드를 푸시하면 **자동으로 앱이 업데이트**됩니다!

```bash
# 로컬에서 코드 수정 후
git add .
git commit -m "기능 개선"
git push

# 약 1~2분 후 자동으로 배포 완료!
```

---

## 📱 Step 6: 앱 공유하기

### URL 공유
```
https://[your-app-name].streamlit.app
```

### QR 코드로 공유
1. 앱의 QR 생성기 탭 선택
2. 앱 URL 입력
3. QR 코드 생성 → 다운로드
4. 인쇄하거나 디지털로 공유

---

# 🐛 문제 해결

## ❌ GitHub 푸시 시 인증 오류

### 문제
```
remote: Support for password authentication was removed
```

### 해결 방법
Personal Access Token(PAT) 사용:

1. GitHub → Settings → Developer settings → Personal access tokens
2. "Generate new token" 클릭
3. 권한 선택: `repo` 체크
4. 토큰 생성 및 복사
5. Git 푸시 시 비밀번호 대신 토큰 입력

---

## ❌ Streamlit 배포 시 pyzbar 오류

### 문제
```
ImportError: Unable to find zbar shared library
```

### 해결 방법
`packages.txt` 파일 확인:

```bash
# packages.txt 파일 내용
echo "libzbar0" > packages.txt

# GitHub에 푸시
git add packages.txt
git commit -m "Add libzbar0 for pyzbar"
git push
```

---

## ❌ 앱이 로딩 중에 멈춤

### 원인
- 의존성 설치 시간 소요
- 또는 코드 오류

### 해결 방법
1. Streamlit Cloud 대시보드에서 **"Logs"** 확인
2. 오류 메시지 확인
3. 로컬에서 앱 실행 테스트:
   ```bash
   streamlit run qr_reader.py
   ```

---

## ❌ GitHub에 파일이 너무 큼

### 문제
```
remote: error: File too large
```

### 해결 방법
`.gitignore` 파일 생성:

```bash
# .gitignore
__pycache__/
*.pyc
.venv/
venv/
*.jpg
*.png
*.jpeg
```

---

# 📊 배포 상태 관리

## Streamlit Cloud 대시보드 기능

### 📈 Analytics
- 방문자 수 확인
- 사용 통계

### 📋 Logs
- 실시간 로그 확인
- 오류 메시지 확인

### ⚙️ Settings
- 환경 변수 설정
- Secrets 관리

### 🔄 Reboot
- 앱 수동 재시작

---

# 🎯 체크리스트

## Part 1: GitHub 업로드 체크리스트

- [ ] GitHub 저장소 생성
- [ ] Git 초기화 (`git init`)
- [ ] 원격 저장소 연결 (`git remote add`)
- [ ] 파일 추가 (`git add .`)
- [ ] 커밋 생성 (`git commit`)
- [ ] GitHub에 푸시 (`git push`)
- [ ] GitHub 웹에서 파일 확인

## Part 2: Streamlit 배포 체크리스트

- [ ] `requirements.txt` 파일 존재 확인
- [ ] `packages.txt` 파일 존재 확인
- [ ] Streamlit Community Cloud 로그인
- [ ] "New app" 클릭
- [ ] 저장소 및 브랜치 선택
- [ ] 메인 파일 경로 입력 (`qr_reader.py`)
- [ ] "Deploy!" 클릭
- [ ] 배포 완료 대기 (3~5분)
- [ ] 앱 URL 접속 및 테스트
- [ ] 모든 기능 정상 작동 확인

---

# 📚 요약

## GitHub 업로드 (5분)

```bash
# 1. Git 초기화
git init

# 2. 원격 저장소 연결
git remote add origin https://github.com/[사용자명]/QR.git

# 3. 파일 추가 및 커밋
git add .
git commit -m "QR 코드 리더기 & 생성기 완성"

# 4. 푸시
git push -u origin master
```

## Streamlit 배포 (5분)

```
1. https://share.streamlit.io/ 접속
2. GitHub 로그인
3. "New app" 클릭
4. 저장소 선택: [사용자명]/QR
5. 브랜치: master
6. 메인 파일: qr_reader.py
7. "Deploy!" 클릭
8. 3~5분 대기
9. 완료! 🎉
```

---

# 🎉 축하합니다!

이제 여러분의 QR 코드 앱이 온라인에 배포되었습니다!

**앱 URL** (예시):
```
https://qr-code-app.streamlit.app
```

전 세계 누구나 이 URL로 접속하여 앱을 사용할 수 있습니다! 🌍

---

# 📞 추가 도움말

## 공식 문서
- [Git 기초](https://git-scm.com/book/ko/v2)
- [GitHub 가이드](https://docs.github.com/ko)
- [Streamlit 배포 문서](https://docs.streamlit.io/streamlit-community-cloud)

## 커뮤니티
- [Streamlit 포럼](https://discuss.streamlit.io/)
- [Streamlit Discord](https://discord.gg/streamlit)

## 비디오 튜토리얼
- [Streamlit 배포 영상](https://www.youtube.com/watch?v=HKoOBiAaHGg)

---

<div align="center">

**만든 이**: QR 코드 프로젝트 팀  
**최종 수정**: 2026-02-05  

**질문이 있으시면 GitHub Issues에 남겨주세요!**

</div>
