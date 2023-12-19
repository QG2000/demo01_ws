#! /usr/bin/env python 

##指定解释器

#1 daobao
import rospy


#2 编写主入口
if __name__ == "__main__":

	#3 初始化 ros 节点
	rospy.init_node("hello_p")
	#4 输出日志
	rospy.loginfo("hello world  python wo shi gaoqian")







