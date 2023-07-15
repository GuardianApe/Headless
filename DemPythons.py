#A function that approximates the Harmonic Series up to the n-th term.
def Harmonic(n):
  k = 1
  HarmonicSum = 0
  while k < n:
    HarmonicSum = 1/k + HarmonicSum
    k = k+1
  return HarmonicSum
  
