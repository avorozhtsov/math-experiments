00:00 Introduction
00:14 Prime numbers
00:54 Let’s crack primes counting Pi function
01:25 PrimePi function introduction 
01:58 PrimePi function learning: 
  02:08 Studying how the proportion of prime 
 numbers among all numbers ≤ x changes
  03:49 Plot of the Difference PrimePi[x] - x/(Log[x] - а)
  06:10 A law for the mismatch between the PrimePi function and the approximation
  07:27 Noise
  07:51 Writting down an approximate law for the mismatch
08:49 Fitting method for more precise law
09:16 Express of the noise
09:44 QRange function
10:10 Find coeffs by minimizing of the mean value of squared noise
10:34 NMinimize function uses the simulated annealing method
10:53 PrimePiMy function definition
11:04 Plot the discrepancy between the function PrimePiMy 
 and the true function PrimePi 
13:51 Find coeffs by minimizing noise, attempt 2
14:54 Plot the noise value: PrimePiMy[#] - PrimePi[#]
16.01 Find coeffs by minimizing noise, attempt 3
17:25 LogIntegral function
19:29 Factorial in the coeffs
20:36 Compare of the coeffs
21:19 Summarize what we have
22:15 3 Approximation plots
23:25 Riemann formula
24:29 MoebiusMu function
24:56 Riemann approximation
26:04 4 Approximation plots
28:32 Takeaways

Let's do some math experiments with the prime counting function  pi(x), i.e. the number of primes less than or equal to x. Quite quickly, we come across a mysterious noise hidden inside pi(x). The size of this noise grows as sqrt(x)/log(x), and the existence of the upper bound of its modulus of the form C * sqrt(x) * log(x)  is equivalent to the Riemann hypothesis on the zeros of the zeta function.

For more information on these topics, please refer to the following links:

https://en.wikipedia.org/wiki/Prime-counting_function
https://en.wikipedia.org/wiki/Logarithmic_integral_function
https://en.wikipedia.org/wiki/Cauchy_principal_value
https://en.wikipedia.org/wiki/Riemann_hypothesis

Mathematica notebook:
https://www.wolframcloud.com/obj/artem.voroztsov/Published/017-prime_pi.nb
https://disk.yandex.ru/d/pHW8P_Q_gcc4wg

Materials, code and Mathematica notebooks: https://github.com/avorozhtsov/math-experiments/tree/main/videos/017-p4r1qaUxXgA
