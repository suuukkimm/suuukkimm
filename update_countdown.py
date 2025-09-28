from datetime import datetime

# 목표 날짜 (ADsP 시험)
target_date = datetime(2025, 11, 2, 0, 0, 0)

# 오늘 날짜
now = datetime.utcnow()

# 남은 시간 계산
delta = target_date - now

days = delta.days
hours, remainder = divmod(delta.seconds, 3600)
minutes, _ = divmod(remainder, 60)

countdown_text = f"{days}일 {hours}시간 {minutes}분"

# README 파일 업데이트
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace("{{COUNTDOWN}}", countdown_text)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
