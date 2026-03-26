USE ros;

CREATE TABLE IF NOT EXISTS lidardata (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- 정수 타입 ID (자동 증가)
    ranges JSON NOT NULL,                     -- 360개 거리 데이터 (JSON 타입)
    `when` DATETIME DEFAULT CURRENT_TIMESTAMP, -- 데이터 수신 시간 (명칭이 예약어라 ``로 감쌉니다)
    action VARCHAR(50)                        -- 결정된 주행 액션 (직진, 좌회전 등)
);

SELECT * FROM lidardata;
