************************
- author:EricYun
- date:2017.6.19
************************

# Documentation

## 自动关机功能
1. 安装GPIO库 (命令行操作)
- 在线安装 
	sudo apt-get install python-rpi.gpio
- 离线安装 
	1. 解压  tar -xzvf RPi.GPIO-0.6.3.tar.gz
	2. 进入目录 cd RPi.GPIO-0.6.3
	3. 执行安装程序 sudo python setup.py install 
2. 将程序文件low_level_for_shutdown.py放在树莓派/home/pi/workspace/目录下。（图形界面操作）
3. 配置 (命令行操作)
   1. 进入目录  cd /home/pi/workspace/
   2. 修改权限  sudo chmod a+x low_level_for_shutdown.py 
   3. 开机启动  打开rc.local文件：sudo nano /etc/rc.local，在exit 0 前面加入一行:
	python /home/pi/workspace/low_level_for_shutdown.py,
	按Ctrl+X,输入Y，保存退出

---
注：程序文件可放在任意目录下，步骤3中的/home/pi/workspace/改为对应目录。

## 关闭程序功能（可关闭）

### 1. 查看程序名称
   - 命令行操作：ps -aux|grep '关键字'   。例如浏览器关键字 browser
   - 图形界面操作：任务管理器中查看。

### 2. 在程序中修改名称即可。
cmd_kill = 'killall x-www-browser'  #修改要关闭的程序名称:x-www-browser

20190409 根据新设计的PCB shutdown 引脚应该连接到物理引脚序号7的引脚上 bcm序号为4