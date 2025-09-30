from datetime import datetime, timedelta, timezone
import sys
import re

# 한국 시간대 (UTC+9)
KST = timezone(timedelta(hours=9))

# 목표 날짜 (ADsP 시험, 한국 시간 기준 자정)
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

pattern = r"<!--COUNTDOWN-->.*?<!--/COUNTDOWN-->"

try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # HTML 코멘트 영역 안을 새로운 countdown_text로 교체
    new_content = re.sub(pattern, f"<!--COUNTDOWN-->{countdown_text}<!--/COUNTDOWN-->", content)

    if new_content != content:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ README.md 업데이트 완료: {countdown_text}")
    else:
        print("ℹ️ 변경 사항 없음")
except FileNotFoundError:
    print("❌ README.md 파일을 찾을 수 없습니다.")
    sys.exit(1)
