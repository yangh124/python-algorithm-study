#使用哈希表构建一个关系图
def init_graph():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    return graph


from collections import deque


def search(name):
    graph = init_graph()
    search_queue = deque()  #定义一个队列
    search_queue += graph[name]
    searched = []  #这个列表用来记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a magno seller!")
            else:
                search_queue += graph[person]
                searched.append(person)
    return None


def person_is_seller(person):
    return person == "thom"


search("you")