import sys

sys.path.append("../")

from api.nnetwork import Network


n = Network((28*28, 20, 10))
n.dump()
