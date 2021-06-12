#!/usr/bin/env python
"""
This is a calss to clean rosbag

python clean_rosbag.py  /home/vahid/.../ .bag

"""
from __future__ import print_function
from __future__ import division

import sys
import rosbag

class CleanRosbag(object):
    """
    This class subscriber to
    """
    def __init__(self):
        self.unwanted_topic = ['/cam_left_left/image_raw/compressed',                               
                               '/cam_right_center/camera_info',
                               '/cam_right_center/image_raw/compressed',                               
                               '/cam_right_right/camera_info',                               
                               '/cam_right_right/image_raw/compressed',
                               '/cam_left_center/camera_info',                               
                               '/cam_left_left/camera_info',
                               '/plc_cas_raw',
                               '/tf',
                               '/cam_left_right/camera_info',
                               '/cam_left_right/image_raw/compressed',
                               '/cam_right_left/camera_info',
                               '/cam_right_left/image_raw/compressed',
                               '/rs_bperl_right/rslidar_packets_difop',
                               '/rs_bperl_left/rslidar_packets_difop',
                               '/rs_bperl_left/rslidar_packets', 
                               '/rs_bperl_right/rslidar_packets'                              
                              ]

        self.wanted_topic = [
                             '/points_raw',
                             '/cam_right_center/image_raw/compressed',
                             '/cam_left_center/image_raw/compressed'
                            ]

    def filter_topics(self, in_bag):
        """
        This function read the wnated topic and write them in to a new bag file
        """
        print('Keeping Topics : \n')
        for item in self.wanted_topic:
            print('\t {}'.format(item))
        out_bag = in_bag[:-4] + '_.bag'
        with rosbag.Bag(out_bag, 'w') as outbag:
            print("\nReading from \n" + in_bag)
            print("\nWriting to \n" + out_bag)
            
            for topic, msg, t in rosbag.Bag(in_bag).read_messages():
                if topic in self.wanted_topic:
                    # print('topic    : {}'.format(topic))
                    outbag.write(topic, msg, t)
 
def main():
    """
    This is the main file
    """
    in_bag = sys.argv[1]

    clean_rosbag = CleanRosbag()
    clean_rosbag.filter_topics(in_bag)
    print("Done")

if __name__ == '__main__':
    try:
        main()
    except rosbag.ROSInterruptException:
        print(rosbag.ROSInterruptException)