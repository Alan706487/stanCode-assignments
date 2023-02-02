"""
File: largest_digit.py
Name: Alan
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	# print(find_largest_digit(12345))      # 5
	# print(find_largest_digit(281))        # 8
	# print(find_largest_digit(6))          # 6
	# print(find_largest_digit(-111))       # 1
	# print(find_largest_digit(-9453))      # 9

	print(find_largest_digit(-8493))


def find_largest_digit(n):  # 舊值大於新值，取代新值並少一位數 再遞迴  反之 直接少一位 再遞迴
	"""
	:param n:
	:return:
	"""
	# if n < 0:  # 都轉成正整數
	# 	n *= -1
	# largest_digit = int(n % 10)  # 令largest_digit儲存n的末位數字
	# n = (n - n % 10) * 0.1  # 令n變為去除自己末位數後的新數字(位數少1)
	# if n == 0:  # 新數字為0 代表前次輸入的數字n只剩一位數 也會是遞迴後剩的largest_digit
	# 	return largest_digit
	# else:  # 新數字不為0 代表前次輸入的n有兩位數以上 則繼續遞迴判斷
	# 	if largest_digit > n % 10:  # n的末位數字大於新數字的末位數字 代表n的末位數是目前較大數字
	# 		n = (n - n % 10)+largest_digit  # 將新數字(位數少1)的末位數以n的末位數字取代 把largest_digit的值保留進新數字再遞迴判斷
	# 	return find_largest_digit(n)

	n = abs(n)
	largest_digit = n % 10
	if n == 0:
		return largest_digit
	else:
		return max(largest_digit, find_largest_digit(n//10))


if __name__ == '__main__':
	main()
