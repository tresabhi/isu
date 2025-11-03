import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np


class VelPublisher(Node):
    def __init__(self):
        super().__init__("pub_node")
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        # initialize (could initialize angular values to numpy random numbers)
        vel_msg = Twist()
        # tell the turtle to do random things
        vel_msg.linear.x = np.random.uniform(low=-1, high=1)
        vel_msg.angular.z = np.random.uniform(low=-1, high=1)
        self.publisher_.publish(vel_msg)
        self.get_logger().info(
            "Publish turtle velocity command: {:0.3f} m/s, {:0.3f} rad/s".format(
                vel_msg.linear.x, vel_msg.angular.z
            )
        )


def main(args=None):
    rclpy.init(args=args)
    pub_node = VelPublisher()
    rclpy.spin(pub_node)
    pub_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
