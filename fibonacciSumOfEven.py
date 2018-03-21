'''
Sum 100 even fibonacci numbers
Python 3
'''

def fibonacciSum():
  fibSum = 0
  count = 0
  evenCounter = 0
  
  def fib(num):
    if (num == 0):
      return num
    if num > 0:
      a, b = 1, 1
      for i in range(1, num):
        a, b = b, a + b
      return a
      
  while count != -1:
    if (fib(count) % 2 == 0):
      fibSum += fib(count)
      evenCounter += 1
    if (evenCounter == 100):
      break
    count += 1
    
  return(fibSum)
 
print(fibonacciSum())
