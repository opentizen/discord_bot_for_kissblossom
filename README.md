<<<<<<< HEAD
<div align="center">

# 🌸 kissblossom discord bot 🌸

**kissblossom 디스코드 서버를 위한 커스텀 봇**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![discord.py](https://img.shields.io/badge/discord.py-2.3.2-5865F2?style=flat-square&logo=discord&logoColor=white)
![License](https://img.shields.io/badge/license-Private-ff9ecd?style=flat-square)

</div>

---

## 기능? 별 거 없어요.
다른 서버도 참고해서 만드셔도 됩니다.

### 환영 봇
새 멤버가 서버에 입장하면 자동으로 예쁜 임베드 메시지를 전송해요.

### 레벨 / 경험치 시스템
채팅을 할수록 경험치가 쌓이고 레벨이 올라가요.
- 메시지 전송 시 XP +15~25 랜덤 지급
- 60초 쿨다운으로 스팸 방지
- 레벨업 시 채널에 알림
- SQLite로 데이터 영구 저장

### 오늘의 질문
매일 오전 9시(KST)에 자동으로 대화 주제를 올려서 서버 활성화를 도와요.

---

## 명령어

| 명령어 | 설명 |
|--------|------|
| `!레벨` | 내 레벨과 경험치 확인 |
| `!레벨 @유저` | 다른 멤버의 레벨 확인 |
| `!순위` | 서버 레벨 TOP 10 순위표 |
| `!질문` | 오늘의 질문 수동 전송 |

---

## 기술 스택

- * Python 3.11+
- * discord.py 2.3.2
- * SQLite — 레벨 데이터 저장
- * python-dotenv — 환경변수 관리

---

## 프로젝트 구조

kissblossom-bot/
main.py                  # 봇 실행 진입점
.env                     # 봇 토큰 (비공개)
.env.example             # 환경변수 양식
  start.bat                # Windows 실행 스크립트
  start.sh                 # Linux/Ubuntu 실행 스크립트
   cogs/
   ─ welcome.py           # 환영 봇
   ─ levels.py            # 레벨/경험치 시스템
   ─ daily_question.py    # 오늘의 질문
data/
   ─ bot.db               # 레벨 데이터 (자동 생성)
```

---

# 설치 및 실행

## 1. 저장소 클론
```bash
git clone https://github.com/opentizen/discord_bot_for_kissblossom.git
cd discord_bot_for_kissblossom
```

## 2. 라이브러리 설치
```bash
pip install discord.py python-dotenv
```

## 3. 환경변수 설정
`.env.example` 파일을 복사해 `.env` 파일 생성 후 토큰 입력
```
DISCORD_TOKEN=your_token_here
```

## 4. Discord Developer Portal 설정
- SERVER MEMBERS INTENT 활성화
- MESSAGE CONTENT INTENT 활성화

## 5. 실행
```bash
# Windows
start.bat

# Linux / Ubuntu
chmod +x start.sh && ./start.sh
```

---

# 앞으로 더 해야 할 것.

- [ ] 포인트 / 칭찬 시스템
- [ ] 역할 자동 부여
- [ ] 운세 / 타로 봇
- [ ] 꽃말 봇

# 추후에 계속 업데이트 해드릴게요.

---

<div align="center">
  <sub>made with 🌸 for kissblossom 🌸</sub>
</div>
=======
# discord_bot_for_kissblossom
>>>>>>>
