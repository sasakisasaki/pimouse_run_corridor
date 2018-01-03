#!/usr/bin/env python
import unittest, rostest
import rosnode, rospy
import time

class WallStopTest(unittest.TestCase):
    def set_and_get(self,lf,ls,rs,rf):
        with open("/dev/rtlightsensor0","w") as f:
            f.write("%d %d %d %d\n" % (rf,rs,ls,lf))

        time.sleep(0.3)

        with open("/dev/rtmotor_raw_l0","r") as lf,\
             open("/dev/rtmotor_raw_r0","r") as rf:
            left = int(lf.readline().rstrip())
            right = int(rf.readline().rstrip())

        return left, right

    def test_io(self):
        left, right = self.set_and_get(400,0,0,100)
        self.assertTrue(left == right == 0, "cannot be stopped")

        left, right = self.set_and_get(0,5,1000,0)
        self.assertTrue(left == right != 0, "stopped wrongly by side-sensors")

        left, right = self.set_and_get(0,10,0,0)
        self.assertTrue(left < right, "do not curve to left")

        left, right = self.set_and_get(0,200,0,0)
        self.assertTrue(left > right, "do not curve to right")

        left, right = self.set_and_get(0,5,0,0)
        self.assertTrue(0 < left == right, "curved wrongly")


if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('travis_test_wall_trace')
    rostest.rosrun('pimouse_run_corridor','travis_test_wall_trace',WallStopTest)
