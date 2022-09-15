
class Calculator():
	def sum(self, num1, num2):
		return num1+num2
	def diff(self, num1, num2):
		return num1-num2
	def prd(self, num1, num2):
		return num1*num2
	def pwr(self, num1, num2):
		return num1**num2
	def div(self, num1, num2):
		return num1/num2
	def div_int(self, num1, num2):
		return num1//num2
	def modu(self, num1, num2):
		return num1%num2

c1 = Calculator()
result = c1.sum(4,5)
print("SUM : {}".format(result))

result = c1.diff(4,5)
print("DIF : {}".format(result))

result = c1.prd(4,5)
print("PRO : {}".format(result))

result = c1.pwr(4,5)
print("Power : {}".format(result))

result = c1.div(4,5)
print("DIV : {}".format(result))

result = c1.div_int(4,5)
print("Integer DIV : {}".format(result))

result = c1.modu(4,5)
print("Modulus : {}".format(result))