# M1161005_hw1.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In M1161005_hw1.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #dps在行走過程進行紀錄，若相鄰的點都走過便往回退直到有點沒走過，因此用stack的方式(LIFO)處理
    #先套用預設好util中的stack package
    eat = util.Stack()
    #用來裝已走過的點
    explorednode= []
    #起始點開始
    Startstate = problem.getStartState()
    #用來記錄走過的路線
    path = []
    #將起始點和紀錄放入stack 設置為tuple否則會出錯
    eat.push((Startstate, path, 0))

    while not eat.isEmpty():  #因前面有先丟起始點所以這邊才可以運行!!
        currentnode, actions, cost = eat.pop() #開始行動

        if currentnode not in explorednode:
            explorednode.append(currentnode) #若沒走過則做紀錄

            if problem.isGoalState(currentnode):
                return actions #如果到達終點回傳路徑

            else: #沒有則繼續行動
                success = problem.getSuccessors(currentnode) #根據其回傳值來往下個點前進

                for success_state,sussess_action,stepcost in success:  #stepcost 後面沒用到這邊卻要呼叫?
                    newaction = actions+[sussess_action]
                    newcost = cost+stepcost
                    newnode = (success_state, newaction, newcost)
                    eat.push(newnode)

    return actions

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #BFS 先選擇一個起始點 先探索起始點相鄰的點 再根據起始點相鄰點去尋找為探索的點 使用queue方法探索
    eat = util.Queue()
    # 用來裝已走過的點
    explorednode = []
    # 起始點開始
    Startstate = problem.getStartState()
    # 用來記錄走過的路線
    path = []
    # 將起始點和紀錄放入stack 設置為tuple否則會出錯
    eat.push((Startstate, path, 0))

    while not eat.isEmpty():  # 因前面有先丟起始點所以這邊才可以運行!!
        currentnode, actions, cost = eat.pop()  # 開始行動

        if currentnode not in explorednode:
            explorednode.append(currentnode)  # 若沒走過則做紀錄

            if problem.isGoalState(currentnode):
                return actions  # 如果到達終點回傳路徑

            else:  # 沒有則繼續行動
                success = problem.getSuccessors(currentnode)  # 根據其回傳值來往下個點前進

                for success_state, sussess_action, stepcost in success:  # stepcost 後面沒用到這邊卻要呼叫?
                    newaction = actions + [sussess_action]
                    newcost = cost + stepcost
                    newnode = (success_state, newaction, newcost)
                    eat.push(newnode)

    return actions

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #  uniformCostSearch 從起始點開始 計算到下個點的cost 每次選擇cost最少的路徑前進 最後到達終點可以得到最少cost 使用priority queue方法探索
    eat = util.PriorityQueue()
    # 用dict能更準確紀錄走過所需的cost
    #explorednode = []
    explorednode = {}
    # 起始點開始
    Startstate = problem.getStartState()
    # 用來記錄走過的路線
    path = []
    # 將起始點和紀錄放入stack 設置為tuple否則會出錯
    star = (Startstate, path, 0)
    eat.push(star, 0)

    while not eat.isEmpty():  # 因前面有先丟起始點所以這邊才可以運行!!
        currentnode, actions, cost = eat.pop()  # 開始行動

        if (currentnode not in explorednode) or (cost < explorednode[currentnode]):
            explorednode[currentnode] = cost  # 前面探索法式做紀錄但這邊為求最少的cost 所以每次都呼叫最少的cost

            if problem.isGoalState(currentnode):
                return actions  # 如果到達終點回傳路徑

            else:  # 沒有則繼續行動
                success = problem.getSuccessors(currentnode)  # 根據其回傳值來往下個點前進

                for success_state, sussess_action, stepcost in success:  # stepcost 後面沒用到這邊卻要呼叫?
                    newaction = actions + [sussess_action]
                    newcost = cost + stepcost
                    newnode = (success_state, newaction, newcost)
                    eat.update(newnode, newcost)  #檢查cost 並更新最小的或相等的路徑

    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #astar 有多節點路徑去求出最佳路徑 使用priority queue 演算法為f(n) = g(n)起始點到每點的距離+h(n)任意點到終點的距離
    #heuristics 為估算點到終點接近程度
    eat = util.PriorityQueue()
    # 用來裝走過的點
    explorednode = []
    # 起始點開始
    Startstate = problem.getStartState()
    # 用來記錄走過的路線
    path = []
    # 將起始點和紀錄放入stack 設置為tuple否則會出錯
    star = (Startstate, path, 0)
    #這裡的push內容與前面不一樣要注意
    heuristicpath = heuristic(Startstate, problem)
    eat.push(star, 0 + heuristicpath)

    while not eat.isEmpty():  # 因前面有先丟起始點所以這邊才可以運行!!
        currentnode, actions, cost = eat.pop()  # 開始行動
        #後面會拿來做判斷
        explorednode.append((currentnode, cost + heuristicpath))

        if problem.isGoalState(currentnode):
            return actions  # 如果到達終點回傳路徑

        else:  # 沒有則繼續行動
            success = problem.getSuccessors(currentnode)  # 根據其回傳值來往下個點前進

            for success_state, sussess_action, stepcost in success:  # stepcost 後面沒用到這邊卻要呼叫?
                newaction = actions + [sussess_action]
                newcost = cost + stepcost
                newnode = (success_state, newaction, newcost)
                #確認是否探索過
                explored = 0

                for explore in explorednode:
                    exploredstate, exploredcost = explore

                    if (success_state == exploredstate) & (newcost >= exploredcost):
                        explored = 1
                #預估到達終點還有多少
                if  explored != 1:
                    eat.push(newnode, newcost + heuristic(success_state, problem))
                    explorednode.append((success_state, newcost))

    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
