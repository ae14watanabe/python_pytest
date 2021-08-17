class IntClosedRange():
	def __init__(self, lower_endpoint: int, upper_endpoint: int) -> None:
		if lower_endpoint > upper_endpoint:
			raise ValueError("lower_endpointはupper_endpoint以下にしてください")
		self.lower_endpoint = lower_endpoint
		self.upper_endpoint = upper_endpoint
	
	def str(self):
		return "[{},{}]".format(self.lower_endpoint, self.upper_endpoint)
	
	def is_include(self, target):
		if target >= self.lower_endpoint and target <= self.upper_endpoint:
			return True
		else:
			return False
