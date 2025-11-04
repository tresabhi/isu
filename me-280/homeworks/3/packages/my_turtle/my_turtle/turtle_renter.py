import rclpy
from rclpy.node import Node

from turtle_interfaces.msg import Person                        # CHANGE


class OwnerSubscriber(Node):

    def __init__(self):
        super().__init__('sub_node')
        self.subscription = self.create_subscription(
            Person,                                               # CHANGE
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('I heard {}  owns the turtle, I would like to borrow the simulator from them.'.format(msg.name))  # CHANGE


def main(args=None):
    rclpy.init(args=args)

    owner_subscriber = OwnerSubscriber()

    rclpy.spin(owner_subscriber)

    owner_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
