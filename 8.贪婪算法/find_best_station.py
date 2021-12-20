#近似算法
#集合覆盖问题
#假设你办了个广播节目，想让全美50个州的人都听得到。为此，你需要决定在哪些广播电台播出。在每个广播电台播出都需要支付费用，此时你力图在尽可能少的广播台播出。
#每个广播台覆盖特定的州，不同广播台覆盖的区域可能重叠。
#实现：
# 1. 选出这样一个广播台，即它覆盖了最多未覆盖州。即便这个广播台已经覆盖了一些已覆盖州，也没有关系
# 2. 重复第一步，直到覆盖了所有的州

#用set存储所有需要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

#用散列表来表示广播台和覆盖州的对应关系
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#储存最终选择出来的广播台
final_stations = set()

while states_needed:
    #遍历广播台，选出覆盖最多未覆盖州的广播台
    best_station = None
    #best_station覆盖的未覆盖的州
    states_covered = set()
    #station->广播台    states->每个广播台覆盖的州
    for station, states in stations.items():
        covered = states_needed & states  #取交集 -> 当前电台覆盖的一系列还未覆盖的州
        if len(covered) > len(states_covered):  #如果该电台覆盖的州 > best_station覆盖的州
            best_station = station  #将该电台设置为best_station
            states_covered = covered  #它覆盖的州设置为states_covered

    states_needed -= states_covered  #更还未覆盖的州
    final_stations.add(best_station)  #将best_station加入最终的结果

print(final_stations)
