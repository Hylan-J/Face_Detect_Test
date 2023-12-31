# 人脸检测算法测试框架介绍
本框架为人脸检测任务提供了**性能**测试框架，选取主要的指标为**Accuracy**和**FPS**。

通过本框架，可以将自己完成的人脸检测算法与其他人脸检测算法性能进行**比较**。

本框架目前内置的人脸检测算法为：
  - OpenCV的haar级联人脸检测算法
  - Dlib的hog正向人脸检测算法

# 主要实现方法：
实现接口的核心在于python的 **global()[function_name](inputs)** 函数可以实现任意函数的调用。

实现增量式编程的核心在于python内置函数 **dir(module_name)** 的使用，通过该内置函数，可以获取任一文件内我们所需要的function名称。

基于上述实现，我们需要对自己完成的人脸检测算法进行规范包装：**def detect_face_by_nameXXX(image)->faces:list**，由此可以实现算法的自动化性能测试。

# 待改进的点
本框架还有以下改进点可以实现：
  - 性能指标的选取及可视化部分
  - 图形化界面的使用
  - 代码部分及设计的优化
