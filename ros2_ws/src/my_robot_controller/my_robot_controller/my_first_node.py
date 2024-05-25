#!/usr/bin/env python3
import rclpy # rclpy is the python library for ros2
from rclpy.node import Node

class MyNode (Node):
    def __init__(self):
        super().__init__("First_Node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_) + " from Shivam's ROS-Master")
        self.counter_+=1

def main(args = None):
    rclpy.init(args=args) # To initialize the node
    
    # Code area
    node = MyNode() # Node is called
    rclpy.spin(node) # To recall the node / To keep the node running
    rclpy.shutdown # To close down the node

if __name__ == '__main__':
    main()