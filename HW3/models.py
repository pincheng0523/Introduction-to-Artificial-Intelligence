import nn


class PerceptronModel(object):
    def __init__(self, dimensions):
        """
        Initialize a new Perceptron instance.

        A perceptron classifies data points as either belonging to a particular
        class (+1) or not (-1). `dimensions` is the dimensionality of the data.
        For example, dimensions=2 would mean that the perceptron must classify
        2D points.
        """
        self.w = nn.Parameter(1, dimensions)

    def get_weights(self):
        """
        Return a Parameter instance with the current weights of the perceptron.
        """
        return self.w

    def run(self, x):
        """
        Calculates the score assigned by the perceptron to a data point x.

        Inputs:
            x: a node with shape (1 x dimensions)
        Returns: a node containing a single number (the score)
        """
        "*** YOUR CODE HERE ***"
        return nn.DotProduct(self.w,x)

    def get_prediction(self, x):
        """
        Calculates the predicted class for a single data point `x`.

        Returns: 1 or -1
        """
        "*** YOUR CODE HERE ***"
        if nn.as_scalar(self.run(x)) >=0:
            return 1
        else:
            return -1

    def train(self, dataset):
        """
        Train the perceptron until convergence.
        """
        "*** YOUR CODE HERE ***"
        while True:
            error = False
            for x,y in dataset.iterate_once(1):
                predict = self.get_prediction(x)
                if predict != nn.as_scalar(y):
                    error = True
                    self.w.update(x,nn.as_scalar(y))
            if error != True:
                break



class RegressionModel(object):
    """
    A neural network model for approximating a function that maps from real
    numbers to real numbers. The network should be sufficiently large to be able
    to approximate sin(x) on the interval [-2pi, 2pi] to reasonable precision.
    """

    def __init__(self):
        # Initialize your model parameters here
        "*** YOUR CODE HERE ***"
        self.LR = 0.01

        self.lay1 = nn.Parameter(1, 128)
        self.bias1 = nn.Parameter(1, 128)
        self.lay2 = nn.Parameter(128, 64)
        self.bias2 = nn.Parameter(1, 64)
        self.lay3 = nn.Parameter(64, 1)
        self.bias3 = nn.Parameter(1, 1)
        self.param = [self.lay1, self.bias1, self.lay2, self.bias2, self.lay3, self.bias3]

    def run(self, x):
        """
        Runs the model for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
        Returns:
            A node with shape (batch_size x 1) containing predicted y-values
        """
        "*** YOUR CODE HERE ***"

        l = nn.Linear(x,self.lay1)
        l = nn.AddBias(l,self.bias1)
        l = nn.ReLU(l)
        l = nn.Linear(l, self.lay2)
        l = nn.AddBias(l, self.bias2)
        l = nn.ReLU(l)
        l = nn.Linear(l, self.lay3)
        l = nn.AddBias(l, self.bias3)
        return l



    def get_loss(self, x, y):
        """
        Computes the loss for a batch of examples.

        Inputs:
            x: a node with shape (batch_size x 1)
            y: a node with shape (batch_size x 1), containing the true y-values
                to be used for training
        Returns: a loss node
        """
        "*** YOUR CODE HERE ***"

        loss = self.run(x)
        return nn.SquareLoss(loss,y)

    def train(self, dataset):
        """
        Trains the model.
        """
        "*** YOUR CODE HERE ***"
        batch = 0.2
        batchsize = int(batch * dataset.x.shape[0])
        loss = float('inf')
        while loss >= 0.015:
            for x, y in dataset.iterate_once(batchsize):
                loss = self.get_loss(x, y)
                print(nn.as_scalar(loss))
                grad = nn.gradients(loss, self.param)
                loss = nn.as_scalar(loss)
                for i in range(len(self.param)):
                    self.param[i].update(grad[i], -self.LR)