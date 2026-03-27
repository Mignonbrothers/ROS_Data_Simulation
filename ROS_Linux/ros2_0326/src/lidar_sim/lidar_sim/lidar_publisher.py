import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
import random

class LidarPub(Node):
    def __init__(self):
        super().__init__('lidar_pub_node')
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 10)
        self.timer = self.create_timer(2.0, self.timer_callback) # 2초 주기

    def timer_callback(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'laser_frame'
        msg.angle_min = 0.0
        msg.angle_max = 2 * math.pi
        msg.angle_increment = (2 * math.pi) / 360
        msg.range_min = 0.12
        msg.range_max = 3.5
        
        # 360개 랜덤 거리 데이터 생성 (0.4m 벽 패턴 포함 가능)
        msg.ranges = [random.uniform(0.12, 3.5) for _ in range(360)]
        
        self.publisher_.publish(msg)
        self.get_logger().info('Lidar 데이터를 2초마다 발행 중...')

def main(args=None):
    rclpy.init(args=args)
    node = LidarPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()