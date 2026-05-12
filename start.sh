#!/bin/bash

# kissblossom 봇 실행 스크립트 (우분투/리눅스)

# 스크립트 위치로 이동
cd "$(dirname "$0")"

echo ""
echo " ==============================="
echo "   kissblossom bot starting..."
echo " ==============================="
echo ""

# Python 명령어 자동 감지 (python3 우선)
if command -v python3 &>/dev/null; then
    PYTHON=python3
    PIP=pip3
elif command -v python &>/dev/null; then
    PYTHON=python
    PIP=pip
else
    echo " ❌ Python이 설치되어 있지 않아요!"
    echo "    sudo apt install python3 python3-pip"
    exit 1
fi

# 라이브러리 자동 설치 (처음 한 번만)
if ! $PYTHON -c "import discord" &>/dev/null; then
    echo " 📦 필요한 라이브러리 설치 중..."
    $PIP install discord.py python-dotenv
    echo ""
fi

# 봇 실행 (꺼지면 5초 후 자동 재시작)
while true; do
    $PYTHON main.py
    echo ""
    echo " 봇이 꺼졌어요. 5초 후 자동 재시작..."
    echo " (완전히 종료하려면 Ctrl+C)"
    echo ""
    sleep 5
done
