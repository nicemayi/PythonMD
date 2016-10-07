import multiprocessing

class Mapper(object):

	def __init__(self, map_func, num_workers=None):
		self.map_func = map_func
		self.pool = multiprocessing.Pool(num_workers)

	def __call__(self, inputs, chunksize=1):
		map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
		return map_responses

