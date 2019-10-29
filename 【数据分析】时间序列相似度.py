import numpy as np

float_formatter = lambda x: "%.2f" % x
np.set_printoptions(formatter={'float_kind': float_formatter})


def TimeSeriesSimilarityImprove(s1, s2):
    # 取较大的标准差
    sdt = np.std(s1, ddof=1) if np.std(s1, ddof=1) > np.std(s2, ddof=1) else np.std(s2, ddof=1)
    # print("两个序列最大标准差:" + str(sdt))
    l1 = len(s1)
    l2 = len(s2)
    paths = np.full((l1 + 1, l2 + 1), np.inf)  # 全部赋予无穷大
    sub_matrix = np.full((l1, l2), 0)  # 全部赋予0
    max_sub_len = 0

    paths[0, 0] = 0
    for i in range(l1):
        for j in range(l2):
            d = s1[i] - s2[j]
            cost = d ** 2
            paths[i + 1, j + 1] = cost + min(paths[i, j + 1], paths[i + 1, j], paths[i, j])
            if np.abs(s1[i] - s2[j]) < sdt:
                if i == 0 or j == 0:
                    sub_matrix[i][j] = 1
                else:
                    sub_matrix[i][j] = sub_matrix[i - 1][j - 1] + 1
                    max_sub_len = sub_matrix[i][j] if sub_matrix[i][j] > max_sub_len else max_sub_len

    paths = np.sqrt(paths)
    s = paths[l1, l2]
    return s, paths.T, [max_sub_len]


def calculate_attenuate_weight(seqLen1, seqLen2, com_ls):
    weight = 0
    for comlen in com_ls:
        weight = weight + comlen / seqLen1 * comlen / seqLen2
    return 1 - weight


if __name__ == '__main__':
    # 测试数据
    s1 = np.array([1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1])
    s2 = np.array([0, 1, 1, 2, 0, 1, 1.7, 2, 0, 1, 1, 2, 0, 1, 1, 2])
    s3 = np.array([0.8, 1.5, 0, 1.2, 0, 0, 0.6, 1, 1.2, 0, 0, 1, 0.2, 2.4, 0.5, 0.4])

    # 原始算法
    distance12, paths12, max_sub12 = TimeSeriesSimilarityImprove(s1, s2)
    distance13, paths13, max_sub13 = TimeSeriesSimilarityImprove(s1, s3)

    print("更新前s1和s2距离：" + str(distance12))
    print("更新前s1和s3距离：" + str(distance13))

    # 衰减系数
    weight12 = calculate_attenuate_weight(len(s1), len(s2), max_sub12)
    weight13 = calculate_attenuate_weight(len(s1), len(s3), max_sub13)

    # 更新距离
    print("更新后s1和s2距离：" + str(distance12 * weight12))
    print("更新后s1和s3距离：" + str(distance13 * weight13))