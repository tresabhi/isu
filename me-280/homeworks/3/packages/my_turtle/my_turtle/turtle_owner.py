import rclpy
from rclpy.node import Node

from turtle_interfaces.msg import Person  # CHANGE


class OwnerPublisher(Node):

    def __init__(self):
        super().__init__("pub_node")
        self.publisher_ = self.create_publisher(Person, "topic", 10)  # CHANGE
        timer_period = 3.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.i = 0

    def timer_callback(self):
        msg = Person()  # CHANGE
        msg.name = "Abhi"
        msg.age = 20
        self.publisher_.publish(msg)
        self.get_logger().info(
            "The turtle owner is {}, age {}".format(msg.name, msg.age)
        )  # CHANGE


def main(args=None):
    rclpy.init(args=args)

    owner_publisher = OwnerPublisher()

    rclpy.spin(owner_publisher)

    owner_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
