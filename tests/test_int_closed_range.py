import pytest
from int_closed_range import IntClosedRange

# @pytest.fixture(scope='module')
# def range37():
# 	self.closed_range = IntClosedRange(3, 7)

class Test_コンストラクタで与えた区間をインスタンス変数として持つ:
	
	def test_上端点を持つ(self):
		self.int_closed_range = IntClosedRange(3, 7)
		assert self.int_closed_range.upper_endpoint == 7

	def test_下端点を持つ(self):
		self.int_closed_range = IntClosedRange(3, 7)
		assert self.int_closed_range.lower_endpoint == 3

class Test_整数閉区間について数式likeな文字列を返す:
	def test_下端3上端7のときに数式likeな文字列を返す(self):
		int_closed_range = IntClosedRange(3, 7)
		assert int_closed_range.str() == "[3,7]"

class Test_与えられた整数が閉区間に含まれるか判定しbool値を返す:
	def test_下端3上端7で5が与えられた時にTrueを返す(self):
		int_closed_range = IntClosedRange(3, 7)
		assert int_closed_range.is_in(5)

	def test_下端3上端7で3が与えられた時にTrueを返す(self):
		int_closed_range = IntClosedRange(3, 7)
		assert int_closed_range.is_in(3)

	def test_下端3上端7で7が与えられた時にTrueを返す(self):
		int_closed_range = IntClosedRange(3, 7)
		assert int_closed_range.is_in(7)

	def test_下端3上端7で8が与えられた時にFalseを返す(self):
		int_closed_range = IntClosedRange(3, 7)
		assert int_closed_range.is_in(8) == False

	def test_下端3上端7で2が与えられた時にFalseを返す(self):
		int_closed_range = IntClosedRange(3, 7)
		assert int_closed_range.is_in(2) == False
