from matplotlib import pyplot as plt

from interface import test_detector_performance


def visualize(results, types):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    # 绘制第一个子图 - "fps比较"
    ax1.bar(range(len(results['fps'])), results['fps'], color='blue')
    ax1.set_xticks(range(len(results['fps'])))
    ax1.set_xticklabels(types)
    ax1.set_ylabel("fps")
    ax1.set_title("FPS Compare")

    # 绘制第二个子图 - "准确率比较"
    ax2.bar(range(len(results['accuracy'])), results['accuracy'], color='green')
    ax2.set_xticks(range(len(results['accuracy'])))
    ax2.set_xticklabels(types)
    ax2.set_ylabel("accuracy")
    ax2.set_title("Accuracy Compare")

    # 调整子图之间的间距
    plt.tight_layout()

    # 展示图形
    plt.show()


def auto_test(video_path, detector_types):
    results = dict()
    results['fps'] = []
    results['accuracy'] = []

    used_type = []
    for detector_type in detector_types:
        used_type.append(detector_type[15:])
        result = test_detector_performance(video_path, detector_type)
        results['fps'].append(result['fps'])
        results['accuracy'].append(result['accuracy'])
    print(results)

    visualize(results, used_type)
