'''
Sum 100 even fibonacci numbers
Python 3
'''

def fibonacciSum():
  fibSum = 0
  count = 0
  evenCounter = 0
  
  def fib(num):
    if (num < 2):
      return (num)
    if (num >= 2):
      return (fib(num - 1) + fib(num - 2))
      
  while count != -1:
    if (fib(count) % 2 == 0):
      fibSum += fib(count)
      evenCounter += 1
    if (evenCounter == 100):
      break
    count += 1
    
  return(fibSum)
 
print(fibonacciSum())
