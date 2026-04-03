def add(a, b):
  res = a
  if b > 0:
      while (b - 1) >= 0:
          b -= 1
          res += 1
  elif b < 0:
      while (b + 1) <= 0:
          b += 1
          res -= 1
  return res
def subtract(a, b):
  pass
def multiply(a, b):
  res = a
  if b > 0:
      while (b - 1) >= 0:
          b -= 1
          res += a
  elif b < 0:
      while (b + 1) <= 0:
          b += 1
          res += a
          res=-res
  return res
def divide(a, b):
  pass
