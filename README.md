# Artificial Intelligence Course

## 🎯 研究所人工智慧概論作業專案
此專案展示研究所 **人工智慧概論 (Introduction to AI)** 課程的作業內容與結果。

---

## 📂 專案內容
- [HW1](#hw1)：Pacman 搜索演算法實作
- [HW2](#hw2)：多智能體搜索與決策
- [HW3](#hw3)：機器學習與神經網絡

---

## 📌 HW1：Pacman 搜索演算法實作

📌 **目標**：實作 **搜尋演算法 (Search Algorithms)**，使 Pacman 能夠在迷宮中找到食物。

### 🔹 主要步驟
1. **深度優先搜索 (DFS)**
   - 在 `search.py` 實作 `depthFirstSearch`，讓 Pacman 使用 **DFS** 來找到食物點。
2. **廣度優先搜索 (BFS)**
   - 在 `search.py` 實作 `breadthFirstSearch`，確保 Pacman 使用 **最短路徑** 到達食物。
3. **均勻成本搜索 (UCS)**
   - 在 `search.py` 中實作 `uniformCostSearch`，考慮不同行動成本。
4. **A* 演算法 (A*)**
   - 在 `search.py` 補充 `aStarSearch`，並使用 **曼哈頓距離啟發式 (Manhattan Heuristic)**。

### 🔹 挑戰與解決方案
- **挑戰**：如何優化搜尋過程以提高效率？
- **解決方案**：
  - 使用 **優先佇列 (Priority Queue)** 改善 UCS 和 A* 的搜尋速度。
  - 測試不同迷宮 (Tiny, Medium, Big) 來確保演算法能夠適應不同規模的問題。

### 🔹 成果展示

![HW1 Results](https://github.com/pincheng0523/Introduction-to-Artificial-Intelligence/blob/main/HW1/Grade.png)

- **透過 `autograder.py` 測試演算法正確性。**

---

## 📌 HW2：多智能體搜索與決策

📌 **目標**：實作 **Minimax、Alpha-Beta Pruning 及 Expectimax**，讓 Pacman 可以在有鬼的情況下最佳決策。

### 🔹 主要步驟
1. **反射智能體 (Reflex Agent)**
   - 改良 `multiAgents.py` 中的 `ReflexAgent`，讓 Pacman 在 **避開鬼魂的同時最優化得分**。
2. **Minimax 決策樹**
   - 在 `multiAgents.py` 實作 `MinimaxAgent`，讓 Pacman 可以預測鬼魂行動並做出最佳策略。
3. **Alpha-Beta 剪枝**
   - 在 `multiAgents.py` 內部補充 `AlphaBetaAgent`，提升 Minimax 的效率。
4. **Expectimax 演算法**
   - 實作 `ExpectimaxAgent`，讓 Pacman **不假設鬼魂總是做最優決策，而是以機率決策**。

### 🔹 挑戰與解決方案
- **挑戰**：如何讓 Pacman 在隨機移動的鬼魂環境下取得最佳得分？
- **解決方案**：
  - **使用 Expectimax** 而非 Minimax，以機率方式預測鬼魂行為。
  - **測試不同迷宮 (Classic, Trapped) 確保 Pacman 的決策能力。**

### 🔹 成果展示
![HW2 Results](https://github.com/pincheng0523/Introduction-to-Artificial-Intelligence/blob/main/HW2/Grade.png)

- **測試不同 AI 決策模型下的 Pacman 遊戲表現。**

---

## 📌 HW3：機器學習與神經網絡

📌 **目標**：使用 **感知器 (Perceptron) 與神經網絡 (Neural Network)** 進行影像分類。

### 🔹 主要步驟
1. **實作 Perceptron 二元分類**
   - 在 `models.py` 中補充 `PerceptronModel`，並完成 `run()`、`get_prediction()` 及 `train()`。
2. **非線性回歸 (Non-Linear Regression)**
   - 訓練一個 **神經網絡 (Neural Network)** 來擬合 `sin(x)` 函數。
3. **多類別分類 (Multi-class Classification)**
   - 使用 Softmax 進行分類，並計算 **SoftmaxLoss**。
4. **調整神經網絡架構與超參數**
   - 使用 **ReLU** 非線性激活函數來提高網絡表現。
   - 設定不同的 **學習率 (Learning Rate)、隱藏層大小 (Hidden Layer Size)** 來測試模型效能。

### 🔹 挑戰與解決方案
- **挑戰**：如何選擇合適的神經網絡架構？
- **解決方案**：
  - **使用 ReLU 取代 Sigmoid**，避免梯度消失問題。
  - **調整隱藏層神經元數量**，找到最佳模型表現。

### 🔹 成果展示
![HW3 Results](https://github.com/pincheng0523/Introduction-to-Artificial-Intelligence/blob/main/HW3/Grade.png)

---

## 📌 結論
本專案涵蓋了 **搜尋演算法 (Search Algorithms)**、**多智能體決策 (Multi-Agent Decision Making)** 及 **機器學習 (Machine Learning)** 相關技術，並透過 Pacman 遊戲作為測試環境。未來可進一步研究更複雜的 AI 策略，例如 **深度強化學習 (Deep Reinforcement Learning)** 來提升 Pacman 的遊戲策略！🚀

