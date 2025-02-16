# multiAgents.py
# --------------
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

from game import Agent
import util
from util import manhattanDistance
import random


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as 3you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        # 10 points for every food you eat
        """
        Returns a Grid of boolean food indicator variables.

        Grids can be accessed via list notation, so to check
        if there is food at (x,y), just call

        currentFood = state.getFood()
        if currentFood[x][y] == True: ...
        """
        newCapsule = successorGameState.getCapsules()
        # 200 points for every ghost you eat
        # but no point for capsule

        # For Ghost
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        # Position of ghost do not change regardless of your state
        # because you can't predict the future
        ghostPositions = [ghostState.getPosition() for ghostState in newGhostStates]
        # Count down from 40 moves
        ghostStartPos = [ghostState.start.getPosition() for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"

        mindist = 9999999999999999  # 故意設一個很大的值避免會有錯誤
        food = newFood.asList()  # 原本使用list(newFood) 測試發現好像為array 查詢後應使用aslist
        capsule = newCapsule
        for foods in food:  # 使用manhattanDistance的方法去取得最佳的距離
            mindist = min(mindist, manhattanDistance(newPos, foods))
        '''
            for cap in capsule:
                mindist = min(mindist, manhattanDistance(newPos, cap))

                for time in newScaredTimes:
                    if time > 0:
                        for ghost in ghostPositions:
                            mindist = min(mindist, manhattanDistance(newPos, ghost))
        '''
        for ghost in ghostPositions:
            if (manhattanDistance(newPos, ghost) < 2):  # 為了讓pacman 偵測到ghost 故回傳一個很大的值讓其避開 測試過0~4後發現2應該是最佳反應的距離
                return -mindist

        '''目前測試下來因為沒有去取得capsule故分數無法上去 在這裡做紀錄有空回來補足'''
        return successorGameState.getScore() + 1/ mindist  # default scoure
        # please change the return score as the score you want


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        action, score = self.minimax(gameState, 0, 0)
        return action

    # minimax: 一方要在遊戲中優勢最大化 另一方要讓對手優勢最小化 開始總和為0
    def minimax(self, gameState, agentindex, depth):
        if agentindex >= gameState.getNumAgents():  # 若開始行動且完成則重新歸零並增加深度
            agentindex = 0
            depth += 1

        if depth == self.depth or gameState.isWin() or gameState.isLose(): #如果深度到底了或是遊戲已經得出結果了
            return 0, self.evaluationFunction(gameState)
        maxscore = -99999999  # 這裡原本使用0 但因為下面做判斷時可能會出錯因此用一個很大的數值
        maxaction = -99999999  # 同上方的問題，太棒了花了1小時找到問題qq

        if agentindex == 0:  # pacman的回合
            for action in gameState.getLegalActions(agentindex):
                newstate = gameState.generateSuccessor(agentindex, action)
                actions, score = self.minimax(newstate, agentindex + 1, depth)  # agnetindex要記得+1才能換人行動 這裡要記得有兩個回傳值否則會出錯

                if maxscore == -99999999 or score > maxscore:
                    maxscore = score
                    maxaction = action

        else:  # ghost的回合基本上與pacman的行動差不多
            for action in gameState.getLegalActions(agentindex):
                newstate = gameState.generateSuccessor(agentindex, action)
                actions, score = self.minimax(newstate, agentindex + 1, depth)  # agnetindex要記得+1才能換人行動

                if maxscore == -99999999 or score < maxscore:  # 這裡要用<因為ghost為減少優勢那方
                    maxscore = score
                    maxaction = action

        if maxscore == -99999999:
            return 0, self.evaluationFunction(gameState)

        return maxaction, maxscore


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """
    '''
    AlphaBeta 的基本為minimax 新增alpha beta 為參考依據，並以交錯的方式往下層探索
    alpha: 在最小層取最小值，若發現<=alpha的值，則不再對其他分支探索
    beta: 在最大層取最大值，若發現>=beta的值，則不再對其他分支探索
    程式碼原則上與minimax相同再導入 alpha beta 參數進行判斷應該就可以了
    '''

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        action, score = self.AlphaBeta(gameState, 0, 0, -99999999, 999999999)
        return action

    def AlphaBeta(self, gameState, agentindex, depth, alpha, beta):
        if agentindex >= gameState.getNumAgents():  # 若開始行動且完成則重新歸零並增加深度
            agentindex = 0
            depth += 1

        if depth == self.depth or gameState.isWin() or gameState.isLose(): #如果深度到底了或是遊戲已經得出結果了
            return 0, self.evaluationFunction(gameState)
        maxscore = -99999999  # 這裡原本使用0 但因為下面做判斷時可能會出錯因此用一個很大的數值
        maxaction = -99999999  # 同上方的問題，太棒了花了1小時找到問題qq

        if agentindex == 0:  # pacman的回合
            for action in gameState.getLegalActions(agentindex):
                newstate = gameState.generateSuccessor(agentindex, action)
                actions, score = self.AlphaBeta(newstate, agentindex + 1, depth, alpha,beta)  # agnetindex要記得+1才能換人行動 這裡要記得有兩個回傳值否則會出錯

                if maxscore == -99999999 or score > maxscore:
                    maxscore = score
                    maxaction = action

                alpha = max(alpha, maxscore)  # 若發現分數無法超過對手則盡快放棄這條分枝尋找其他點
                if alpha > beta:
                    break
        else:  # ghost的回合基本上與pacman的行動差不多
            for action in gameState.getLegalActions(agentindex):
                newstate = gameState.generateSuccessor(agentindex, action)
                actions, score = self.AlphaBeta(newstate, agentindex + 1, depth, alpha, beta)  # agnetindex要記得+1才能換人行動

                if maxscore == -99999999 or score < maxscore:  # 這裡要用<因為ghost為減少優勢那方
                    maxscore = score
                    maxaction = action

                beta = min(beta, maxscore)
                if beta < alpha:
                    break

        if maxscore == -99999999:
            return 0, self.evaluationFunction(gameState)

        return maxaction, maxscore


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """
    '''
    expectimax 並不會像上面的演算法只求最大或最小值
    而是有機率性會去預期ghost的行動而做出不一樣的應對
    '''

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        action, score = self.Expectimax(gameState, 0, 0)
        return action

    def Expectimax(self, gameState, agentindex, depth):
        if agentindex >= gameState.getNumAgents():  # 若開始行動且完成則重新歸零並增加深度
            agentindex = 0
            depth += 1

        if depth == self.depth or gameState.isWin() or gameState.isLose(): #如果深度到底了或是遊戲已經得出結果了
            return 0, self.evaluationFunction(gameState)
        maxscore = -99999999  # 這裡原本使用0 但因為下面做判斷時可能會出錯因此用一個很大的數值
        maxaction = -99999999  # 同上方的問題，太棒了花了1小時找到問題qq

        if agentindex == 0:  # pacman的回合
            for action in gameState.getLegalActions(agentindex):
                newstate = gameState.generateSuccessor(agentindex, action)
                actions, score = self.Expectimax(newstate, agentindex + 1,
                                                 depth)  # agnetindex要記得+1才能換人行動 這裡要記得有兩個回傳值否則會出錯

                if maxscore == -99999999 or score > maxscore:
                    maxscore = score
                    maxaction = action

        else:  # ghost的回合基本上與pacman的行動差不多 但這裡要做預測鬼的行動
            ghost = gameState.getLegalActions(agentindex)  # 參考最上方的程式碼查出鬼的行動再加上機率做預測
            if len(ghost) != 0:
                pred = 1.0 / len(ghost)  # 根據pdf所述 這裡必須要使用float 否則有可能數據會被判定錯誤!!!
            for action in gameState.getLegalActions(agentindex):
                newstate = gameState.generateSuccessor(agentindex, action)
                actions, score = self.Expectimax(newstate, agentindex + 1, depth)  # agnetindex要記得+1才能換人行動

                if maxscore == -99999999:
                    maxscore = 0

                maxscore += pred * score
                maxaction = action

        if maxscore == -99999999:
            return 0, self.evaluationFunction(gameState)

        return maxaction, maxscore
