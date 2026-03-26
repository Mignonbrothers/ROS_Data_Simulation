import pymysql
import json
import pandas as pd

# 1. DB 연결 (사용자님 설정 반영)
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='0000',
    database='ros',  # 스키마 이름 확인 필요 (아까 'ros'라고 하셨는데 'rosdb'로 맞추시면 됩니다)
    charset='utf8'
)

# 2. 데이터 불러오기
cursor = conn.cursor()
cursor.execute("SELECT ranges, action FROM lidardata")
rows = cursor.fetchall()

# 3. [응용 포인트] 효율적인 데이터 변환
# for문 안에서 concat을 반복하는 대신, 리스트에 먼저 다 담은 뒤 한 번에 DataFrame으로 만듭니다.
data_list = []

for r in rows:
    # r[0]은 JSON 문자열 -> 파이썬 리스트로 변환
    ranges = json.loads(r[0])
    action = r[1]

    # 360개 거리 데이터와 액션을 하나의 리스트로 합침
    combined_row = ranges + [action]
    data_list.append(combined_row)

# 4. 361개 칼럼을 가진 데이터프레임 생성
# 칼럼 이름: 0~359 (거리) + 'action' (주행 액션)
column_names = [i for i in range(360)] + ['action']
df = pd.DataFrame(data_list, columns=column_names)

# 5. 결과 확인 및 저장
print("-" * 50)
print(f"✅ 총 {len(df)}개의 데이터를 불러왔습니다.")
print(f"📊 데이터프레임 모양: {df.shape}")  # (데이터개수, 361) 확인!
print(df.head())  # 상단 5줄 확인
print("-" * 50)

# CSV 내보내기
df.to_csv('lidar_action_dataset.csv', index=False)
print("💾 'lidar_action_dataset.csv' 저장 완료!")

cursor.close()
conn.close()