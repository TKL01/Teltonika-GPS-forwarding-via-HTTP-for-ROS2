import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import pynmea2
import os

class GPSPublisher(Node):
    def __init__(self):
        super().__init__('gps_publisher')
        self.publisher_ = self.create_publisher(NavSatFix, 'gps_data', 10)      # /gps_data topic
        self.timer = self.create_timer(2.0, self.timer_callback)  # send every 2s

    def timer_callback(self):
        file_path = '/tmp/gps_data.nmea'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as file:
                nmea_data = file.read()
                for line in nmea_data.splitlines():
                    try:
                        msg = pynmea2.parse(line)
                        if isinstance(msg, pynmea2.types.talker.GGA):  # GGA message contains GPS data
                            navsat_msg = NavSatFix()
                            navsat_msg.header.stamp = self.get_clock().now().to_msg()
                            navsat_msg.header.frame_id = 'gps'
                            navsat_msg.latitude = msg.latitude
                            navsat_msg.longitude = msg.longitude
                            navsat_msg.altitude = msg.altitude
                            self.publisher_.publish(navsat_msg)
                            self.get_logger().info(f"Published GPS data: {navsat_msg}")
                    except pynmea2.ParseError as e:
                        self.get_logger().error(f"Failed to parse NMEA line: {line} with error: {e}")
            os.remove(file_path)

def main(args=None):
    rclpy.init(args=args)
    gps_publisher = GPSPublisher()
    rclpy.spin(gps_publisher)
    gps_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

