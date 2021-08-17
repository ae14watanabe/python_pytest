import pytest
from int_closed_range import IntClosedRange

# @pytest.fixture(scope='module')
# def range37():
# 	self.closed_range = IntClosedRange(3, 7)

class Test_整数閉区間を表現するクラス:
	
	class Test_コンストラクタは閉区間の下端と上端をセットする:
		def test_引数として受け取った上端点をインスタンス変数に格納する(self):
			int_closed_range = IntClosedRange(3, 7)
			assert int_closed_range.upper_endpoint == 7

		def test_引数として受け取った下端点をインスタンス変数に格納する(self):
			int_closed_range = IntClosedRange(3, 7)
			assert int_closed_range.lower_endpoint == 3

	class Test_メソッドstrはセットされている整数閉区間について数式likeな文字列を返す:
		def test_閉区間下端3上端7を与えたとき数式likeな文字列を返す(self):
			int_closed_range = IntClosedRange(3, 7)
			assert int_closed_range.str() == "[3,7]"

	class Test_メソッドis_includeは引数が閉区間に含まれるか判定する:

		# constructor を定義するとwarningを吐かれて途中で止まる
		# def __init__(self) -> None:
		# 	self.int_closed_range = IntClosedRange(3,7)

		class Test_閉区間が下端3上端7のとき:
			def test_2は含まないのでFalseを返す(self):
				int_closed_range = IntClosedRange(3, 7)
				assert int_closed_range.is_include(2) == False

			def test_3は含むのでTrueを返す(self):
				int_closed_range = IntClosedRange(3, 7)
				assert int_closed_range.is_include(3)

			def test_5は含むのでTrueを返す(self):
				int_closed_range = IntClosedRange(3, 7)
				assert int_closed_range.is_include(5)

			def test_7は含むのでTrueを返す(self):
				int_closed_range = IntClosedRange(3, 7)
				assert int_closed_range.is_include(7)

			def test_8は含まないのでFalseを返す(self):
				int_closed_range = IntClosedRange(3, 7)
				assert int_closed_range.is_include(8) == False

