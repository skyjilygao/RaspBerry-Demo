# 人体感应模块 + 无源蜂鸣器 实现人体感应报警

树莓派4B引脚：

![image](https://github.com/skyjilygao/RaspBerry-Demo/blob/main/HumanBodyInduction/demo/image-20210205230937961.png)
## 人体感应模块
模块的工作电压是5v，所以vcc接了pin02，gnd接了pin06，中间的那个是判断有没有人的需要用gpio接收感应，就用了一个gpio针，接到了pin12上

## 无源蜂鸣器
接蜂鸣器，网上很多示例是无源蜂鸣器，我买的这个是有源的蜂鸣器模块，接法跟红外人体感应模块很相似，模块也有vcc、gnd、in三个针脚，工作电压为3.3v，理所当然的vcc接了pin01，gnd接了pin09，中间的那个in接了pin11
