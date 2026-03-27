ROS_Linux는 Sublimetext에서 작성했고 ROS_Python은 Pycharm에서 작성했습니다. 


# 실행순서

## 1. Ubuntu를 열고 ros2_0326 폴더를 생성하고 그 폴더 안으로 이동해서 src 폴더를 만듭니다.

EX) (1) mkdir ros2_0326
    (2) cd ros2_0326
    (3) mkdir src
    (4) cd src
<br>
<br>
## 2. src 폴더로 이동한 후 ROS2 파이썬 패키지 생성합니다.

EX) (1) ros2 pkg create --build-type ament_python lidar_sim --dependencies rclpy sensor_msgs
<br>
<br>
## 3. lidar_sim이라는 이름의 패키지를 만든게 보이면 lidar_sim 폴더로 이동해서 파이썬 파일을 만듭니다. (필자는 여기서 sublimetext를 직접 열어서 파이썬 파일을 만들었습니다.)

EX) (1) subl / 
    (2) lidar_sim 폴더에 이동해서 그 폴더 안에서 lidar_publisher.py라는 파일을 만듭니다.
    (3) 이제 Github에 있는 코드를 가져와서 적용합니다.
<br>
<br>
## 4. 우분투가 lidar_sim인 폴더 위치에서 lidar_publisher.py을 돌려봐서 확인해봅니다.

EX) (1) python3 lidar_publisher.py
<br>
<br>
## 5. 별도의 우분투를 열어서 토픽이 있는지 확인합니다.

EX) (1) ros2 topic list
<br>
<br>
## 6. Remote PC와 연결하기 위해 Pycharm에서 데이터를 받아오는 수신용 패키지를 설치해야 합니다. 그리고 추후 mysql과 연동할 예정이여서 (2) 패키지도 설치해주세요. (터미널에서 입력)

EX) (1) pip install roslibpy
    (2) pip install mysql-connector-python
<br>
<br>
## 7. Pycharm에서 패키지를 설치했다면 우분투에서도 조치가 필요합니다. 5번에서 별도의 우분투 연거를 그대로 활용합니다. 이 곳에서는 데이터 중계 서버를 구축해야 합니다.

EX) (1) sudo apt update
    (2) sudo apt install ros-humble-rosbridge-suite
<br>
<br>
## 8. 설치가 끝나면 서버를 키면 됩니다. (이 명령어를 입력하고 터미널에 Rosbridge WebSocket server started on port 9090라는 문구가 나오면 성공입니다.) 

EX) (1) ros2 launch rosbridge_server rosbridge_websocket_launch.xml
<br>
<br>
## 9. Remote PC로 넘어가기 전 우분투 터미널에서 다음과 같은 명령어로 IP 주소를 확인하세요.

EX) (1) hostname -I
<br>
<br>
## 10. 이제 파이참을 열고 ROS_Data_Simulation 폴더 안에서 remain_main.py와 remain_out_csv.py의 코드를 가져오세요.

EX) (1) remain_main.py를 실행하기 전 UBUNTU_IP를 9번에서 입력하고 나온 결과를 써주세요.
<br>
<br>
## 11. 만약 mysql-connector-python을 설치해도 모듈을 인식할 수 없다면 파이참(PyCharm)이 사용 중인 파이썬 환경과 지금 터미널에서 패키지를 설치한 파이썬 환경이 서로 다르기 때문입니다.
<br>

## 12. 이제 패키지 문제가 해결되었다면 mysql에 대한 설정이 필요합니다.  

EX) (1) remain_main.py와 remain_out_csv.py에 있는 mysql.connector.connect 함수 안에 있는 코드를 Mysql에서 똑같이 맞춰줘야 합니다.
    (2) mysql에는 깃헙 ROS_Python 폴더 안 sql_record_ros.sql에서 참조합니다.
<br>
<br>
## 13. 따라오느라 정말 고생하셨습니다. 이제 마지막 실행 과정입니다. 우분투 터미널 3개를 열어서 다음과 같은 명령어를 실행하세요

EX) (우분투 터미널 1) ros2 run turtlesim turtlesim_node
    (우분투 터미널 2) ros2 launch rosbridge_server rosbridge_websocket_launch.xml
    (우분투 터미널 3) lidar_sim 폴더까지 이동하고 이 명령어를 실행 : python3 lidar_publisher.py
<br>
<br>
## 14. 그 다음 파이참에서  remain_main.py을 실행하면 turtle이 임의로 받은 주행 데이터로 움직입니다. 장애물을 만나면 자동으로 회피합니다.
<br>

## 15. 쌓인 sql 내역을 보고 싶다면 깃헙 ROS_Python 폴더 안 sql_record_ros.sql에 들어가서 sql workbench에서 다음과 같은 명령어를 입력해서 확인하세요.

EX) (1) SELECT * FROM lidardata;
<br>
<br>
## 16. 이제 모든 우분투 터미널과 파이참에 강제중단을 하고 remain_out_csv.py를 실행합니다.
<br>

## 17. 모든 과정이 끝났습니다. 수고하셨습니다.