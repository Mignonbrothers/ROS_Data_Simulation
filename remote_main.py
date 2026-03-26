import roslibpy
import mysql.connector
import json
import time
from datetime import datetime

# 1. MySQL 연결 (본인의 비밀번호로 수정하세요)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="ros"
)
cursor = db.cursor()

client = roslibpy.Ros(host='192.168.81.129', port=9090)
client.run()

scan_sub = roslibpy.Topic(client, '/scan', 'sensor_msgs/LaserScan')
cmd_vel_pub = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/Twist')


def handler(message):
    ranges = message['ranges']
    front_dist = ranges[0]

    # [3번 항목] 액션 결정
    if front_dist < 1.0:
        action = "TURN_LEFT"
        move_msg = {'linear': {'x': 0.0}, 'angular': {'z': 2.0}}
    else:
        action = "GO_STRAIGHT"
        move_msg = {'linear': {'x': 2.0}, 'angular': {'z': 0.0}}

    # 거북이에게 명령 전송 (Publish)
    cmd_vel_pub.publish(roslibpy.Message(move_msg))

    # [4번 항목] MySQL에 데이터 쌓기 (INSERT)
    sql = "INSERT INTO lidardata (ranges, action, `when`) VALUES (%s, %s, %s)"
    # 리스트를 JSON 문자열로 변환하고 현재 시간을 함께 저장
    val = (json.dumps(ranges), action, datetime.now())

    cursor.execute(sql, val)
    db.commit()

    print(f"✅ 저장 완료 | 거리: {front_dist:.2f}m | 액션: {action}")


scan_sub.subscribe(handler)

try:
    while client.is_connected:
        time.sleep(1)
except KeyboardInterrupt:
    cursor.close()
    db.close()
    client.terminate()