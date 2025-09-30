from datetime import datetime, timedelta, timezone
import sys

# 한국 시간대 (UTC+9)
KST = timezone(timedelta(hours=9))

# 목표 날짜 (ADsP 시험, 한국 시간 자정)
target_date = datetime(2025, 11, 2, 0, 0, 0, tzinfo=KST)

# 현재 시간 (한국 시간)
now = datetime.now(KST)

# 남은 일수 (D-Day)
delta = target_date.date() - now.date()
days = delta.days

if days >= 0:
    countdown_text = f"D-{days}"
else:
    countdown_text = f"D+{abs(days)}"  # 시험일 지났을 경우

# README.md 수정
try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    if "{{COUNTDOWN}}" not in content:
        print("⚠️ README.md 안에 {{COUNTDOWN}}가 없습니다. 수정하지 않았습니다.")
        sys.exit(0)

    new_content = content.replace("{{COUNTDOWN}}", countdown_text)

    if new_content != content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ README.md 업데이트 완료: {countdown_text}")
    else:
        print("ℹ️ 변경 사항 없음")
except FileNotFoundError:
    print("❌ README.md 파일을 찾을 수 없습니다.")
    sys.exit(1)
