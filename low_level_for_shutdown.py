#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:EricYun

import RPi.GPIO as GPIO  
from signal import pause
from time import sleep
from subprocess import check_call,call

pin_touch = 4                                 #所触发的引脚(GPIO)

GPIO.setmode(GPIO.BCM)                        #引脚编号规则设定(GPIO.BOARD,or GPIO.BCM)
GPIO.setup(pin_touch,GPIO.IN)                 #设置引脚号
GPIO.setwarnings(False)                       #忽略警告信息

cmd_kill = 'killall x-www-browser'            #修改要关闭的程序名称:x-www-browser
cmd_poweroff = 'poweroff'

while True:
    sleep(1)
    if GPIO.input(pin_touch) == GPIO.LOW:     #按下  
        try:
            check_call(cmd_kill,shell=True)   #关闭指定程序,不管执行关闭操作是否成功，系统将会关机
            print 'shutdown'
            sleep(2)                          #延时2s
        finally:
            call(cmd_poweroff,shell=True)     #执行关机命令
        sleep(0.2)                            #延迟200毫秒，可根据实际情况修改

pause()
GPIO.cleanup()
  
 #+-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
 #| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 #+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 #|     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 #|   2 |   8 |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5v      |     |     |
 #|   3 |   9 |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | 0v      |     |     |
 #|   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 #|     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 #|  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 #|  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 #|  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
 #|     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
 #|  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
 #|   9 |  13 |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 #|  11 |  14 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
 #|     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
 #|   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 #|   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
 #|   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 #|  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 #|  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 #|  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 #|     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 #+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 #| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 #+-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
