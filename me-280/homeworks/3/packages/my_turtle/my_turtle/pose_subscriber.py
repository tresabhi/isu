import rclpy
from rclpy.node import Node

# Import the Pose message from turtlesim
from turtlesim.msg import Pose


class PoseSubscriber(Node):
    def __init__(self):
        super().__init__("sub_node")
        self.subscriber_ = self.create_subscription(
            Pose, "/turtle1/pose", self.pose_callback, 10
        )

    def pose_callback(self, msg):
        self.get_logger().info("Turtle pose: x={:0.6f}, y={:0.6f}".format(msg.x, msg.y))


def main(args=None):
    rclpy.init(args=args)
    sub_node = PoseSubscriber()
    rclpy.spin(sub_node)
    sub_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
