from datetime import datetime, timedelta, timezone
import sys

# 한국 시간대 (UTC+9)
KST = timezone(timedelta(hours=9))

# 목표 날짜 (ADsP 시험, 한국 시간 기준 자정)
target_date = datetime(2025, 11, 2, 0, 0, 0, tzinfo=KST)

# 현재 시간 (한국 시간)
now = datetime.now(KST)

# 남은 시간 계산
delta = target_date - now

days = delta.days
hours, remainder = divmod(delta.seconds, 3600)
minutes, _ = divmod(remainder, 60)

countdown_text = f"{days}일 {hours}시간 {minutes}분"

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
        print("ℹ️ 변경 사항 없음 (같은 카운트다운)")
except FileNotFoundError:
    print("❌ README.md 파일을 찾을 수 없습니다.")
    sys.exit(1)
