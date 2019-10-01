# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.
import time
import gputools.convolve as convolve
class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None
    def time_small_gputools(self):
        import numpy as np
        image = np.random.random((100, 100))
        h = np.ones((17,17))
        res = convolve(image,h,mode='constant')
    def time_gputools(self):
        import numpy as np
        image = np.random.random((400, 400))
        image[:200, :200] += 1
        image[300:, 300] += 0.5
        h = np.ones((17,17))
        res = convolve(image,h,mode='constant')

def naive_gpu_benchmark():
    start = time.time()
    import numpy as np
    image = np.random.random((400, 400))
    image[:200, :200] += 1
    image[300:, 300] += 0.5
    h = np.ones((17,17))
    res = convolve(image,h,mode='constant')
    taken = time.time() - start
    print('took',taken)

if __name__ == "__main__":
    naive_gpu_benchmark()