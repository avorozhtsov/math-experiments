# 17. Распределение простых чисел и Гипотеза Римана (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [p4r1qaUxXgA](https://www.youtube.com/watch?v=p4r1qaUxXgA). Получено: 2026-10-08T17:42:29+01:00.

[00:00:00] Hello! Welcome to the "Math Experiments".

[00:00:03] I've been wanting to talk about the distribution of prime numbers for a while.

[00:00:06] How we can study this distribution

[00:00:08] and what connection it has with random processes.

[00:00:12] and, of course, with the Riemann hypothesis.

[00:00:14] So...

[00:00:17] How can we study prime numbers?

[00:00:19] For example, we can study the sums of powers of first prime numbers.

[00:00:23] For instance, the sum of the 1 powers, that is just sum of primes.

[00:00:26] Here we get pairs of number P and the sum of all prime numbers from 1 to P inclusive.

[00:00:36] We can study the sum of the first powers or, for instance, inverse powers, or zero powers.

[00:00:43] When you calculate  sums of zero power of prime numbers,

[00:00:46] you are, in fact, just counting prime numbers less than x.

[00:00:52] Let's start with this...

[00:00:54] It is common to start with this prime counting function.

[00:01:01] And we will do that too.

[00:01:04] Although this function is quite a die hard.

[00:01:14] Here I computed the pi function by hand.

[00:01:19] The fact is that this function is already defined in Wolfram.

[00:01:25] It is called PrimePi. No need to define it by hand.

[00:01:27] And it is amazing that it can be computed even for quite large  x values.

[00:01:33] Let's draw a plot of this function for x from 0 to 70.

[00:01:39] Here it is...

[00:01:40] For example, for 60 we have...

[00:01:43] 17 or 18 prime numbers less 60

[00:01:48] Here I wanted to show, what I can compute this using Accumulate[primes⁰],

[00:01:58] it gives the same thing as the PrimePi function.

[00:02:04] How to explore PrimePi function?

[00:02:08] Let's start by calculating proportion of prime numbers among all numbers ≤ x changes.

[00:02:16] PrimePi[x] / x.

[00:02:20] Here we see a decreasing function,

[00:02:23] and around a million it is approximately 0.08.

[00:02:28] So, 8% of the all integer numbers less than 1 million are prime.

[00:02:36] And the function continues to decrease further.

[00:02:40] Lets make it visible and draw this plot on a logarithmic axis.

[00:02:47] Here I simply took the variable lx from 2 to 20

[00:02:52] and put the exponential of lx inside the function f.

[00:02:58] The further away, the closer this function to zero,

[00:03:05] and around e³⁰ the proportion of prime numbers is already less than 5%.

[00:03:11] Next, we can come up with a formula for this decreasing function.

[00:03:19] This formula is 1/Log[x]

[00:03:23] It is just experienced eye. Or two or three guesses, and you find this answer.

[00:03:27] An easy part.

[00:03:30] So, now I am considering PrimePi[x]/x/Log[x]

[00:03:35] and I see that gradually this plot approaches one.

[00:03:42] Good. This is our first theorem.

[00:03:46] Not a theorem, but discovered experimental fact.

[00:03:49] Let's consider the difference PrimePi[x] - x/(Log[x] - a)

[00:03:54] And here we add one more parameter "a" to the denominator.

[00:04:01] Let's see what we can observe.

[00:04:04] Here we can see that by changing the parameter "a", we can reduce this difference.

[00:04:12] For small values of "a", this difference reaches 3000 and more.

[00:04:20] And when we increase the parameter "a", gradually we start to see something interesting.

[00:04:31] We can see that for a = 1.086, we can reduce this difference almost to zero.

[00:04:43] Well, not exactly zero, ofc, but to numbers like 60, 20.

[00:04:48] On the interval x ≤ 1000000.

[00:04:51] Let's remember this value as the initial value for the parameter "a".

[00:04:58] And let's increase our range of x.

[00:05:02] And what do we see?

[00:05:04] We see that...

[00:05:08] the good behavior that we saw for small values of x is significantly distorted for this parameter.

[00:05:15] If we want to get something good for big x, this parameter needs to be smaller.

[00:05:24] For example, like this.

[00:05:28] Need more time to draw...

[00:05:43] If we leave the parameter at 1.065, then as we further increase x, we will see this bend again

[00:05:50] and the function will again go down to a negative value.

[00:05:55] The optimal parameter is probably around 1.05 or even smaller.

[00:06:00] Then the function becomes steadily increasing, but nothing to worry about.

[00:06:05] Let's find a law for this steadily increasing function.

[00:06:10] So! There is idea:

[00:06:12] PrimePi has a main component – x/(log[x]-a)

[00:06:17] and we need to find a law for the residue or, i.e. mismatch between the pi-function and the  approximation.

[00:06:26] It is natural to assume that this law is a power law.

[00:06:33] And here I have already adjusted the sliders and found some values for the multiplier and for the power "c".

[00:06:45] "b" is  just  the multiplier in front of the power law.

[00:06:52] And "c" is precisely the power.

[00:06:57] When c = 0.5 we get a square root,

[00:07:01] but we need something more than a square root here.

[00:07:07] Let's assume it's something like this.

[00:07:10] Here I am already taking the difference:

[00:07:15] Between the Pi function,

[00:07:16] the main component,

[00:07:17] and the second component, which we just found.

[00:07:21] From the values of b and c from the previous adjustment.

[00:07:25] And what do we see here?

[00:07:27] We see a very important thing here - noise.

[00:07:31] Noise that pleases my eye.

[00:07:34] It grows and needs to be divided so that it does not grow.

[00:07:39] For example, by √x

[00:07:42] Here.

[00:07:43] Now it no longer grows. Its amplitude even decreases slightly with increasing x.

[00:07:49] We will fix this in the future.

[00:07:51] Let's assume that we have found such a law and it suits us.

[00:07:59] Let's write it down.

[00:08:03] Pi minus the main component,

[00:08:07] minus the second component,

[00:08:09] and the constant is not so important here...

[00:08:11] Dividing by the square root of x - that's noise.

[00:08:15] And if we express Pi from this formula, here's what we get:

[00:08:20] Pi equals: the main component + the second component + √n times the noise

[00:08:31] This is what you can get in the first ten minutes of studying the Pi function.

[00:08:35] This is the wrong answer.

[00:08:38] It's hard to get the right answer by just moving sliders.

[00:08:42] You have to think more...

[00:08:44] Think and use a different method.

[00:08:49] Namely - the fitting method.

[00:08:53] We assume that our dependence has this form.

[00:08:58] And here I clearly wrote down the noise.

[00:09:01] And allowed it to be shifted by some "b".

[00:09:05] Added a constant "e".

[00:09:08] Here are our constants "c" and "d" for the second component

[00:09:11] and constant "a" for the first component.

[00:09:16] Then I take and express noise through Pi and everything else.

[00:09:24] And define the Noise function, which depends on PrimePi.

[00:09:32] Then I want to minimize this noise.

[00:09:38] Find such parameters a, b, c, d, e, so that the noise is as small as possible.

[00:09:44] Here I use the QRange function,

[00:09:47] which generates a list of natural numbers located approximately on a geometric progression up to the first argument.

[00:09:55] The number of these numbers is determined by the second argument.

[00:10:01] Here I have defined the QRange function.

[00:10:10] So.

[00:10:12] I'm starting to minimize the mean value of squared noise

[00:10:20] at points located approximately in geometric progression from 10 to 500,000,000,010.

[00:10:34] I ask the NMinimize function to use the simulated annealing method and here's the answer it gives me:

[00:10:41] The parameter "a" -> 1.02, we had 1.05, remember, right?

[00:10:47] And it chose this power for the second component: d -> 0.78

[00:10:53] Let's define the function PrimePiMy according to this approximation

[00:11:01] that we obtained with these parameters.

[00:11:04] And let's plot the discrepancy between the function PrimePiMy and the true function PrimePi.

[00:11:13] Let's divide by √x, because, as we know, this difference grows as x increases.

[00:11:21] Yes, and here we see that when we divide by √x, this noise decreases.

[00:11:31] Actually, we need to multiply by the logarithm so that this noise doesn't decrease in amplitude.

[00:11:41] And here I specifically chose 5 trillion as the final number.

[00:11:48] That is, I was optimizing for 500 billion.

[00:11:54] And for 500 billion, I get this.

[00:11:59] And when I look at what's happening on the right.

[00:12:02] I see what the extrapolation of what I picked looks like,

[00:12:07] I see that it's getting worse and worse over there. You can't even see how bad it's getting beyond that.

[00:12:16] So what do I do?

[00:12:19] The first thing I do is fix it.

[00:12:23] My noise grows not like √n, but like √n/Log[n].

[00:12:34] I choose this expression and see what the noise looks like.

[00:12:38] I define Noise according to this expression.

[00:12:47] My Noise depends on PrimePi and the parameters a, b, c, d, e.

[00:12:51] And again, I repeat the whole process.

[00:12:54] Again, I ask to use the Simulated Annealing method.

[00:12:57] There are other interesting methods there too.

[00:13:00] For example, I recommend NelderMead.

[00:13:04] And this is also a good method: DifferentialEvolution.

[00:13:09] The answer it found is like this.

[00:13:12] Very similar, again "a" -> 1.029 and again "d" is close to 0.8.

[00:13:19] I define again my function PrimePi

[00:13:23] and look at the difference between the interpolation up to 500 billion

[00:13:28] and then I look at the extrapolation.

[00:13:33] The situation is actually the same.

[00:13:36] Not much has changed. Essentially, we have the same answer here

[00:13:41] because we haven't done anything new. We just fixed the noise amplitude error.

[00:13:48] Here's another approach.

[00:13:49] Let's assume that we need to add not " nᵈ " to the main component,

[00:13:56] but this thing: " n " divided by some higher powers of the logarithm.

[00:14:04] And the noise is still √n/Log[n].

[00:14:06] This seems to be the correct estimate of the noise amplitude.

[00:14:09] Let's go.

[00:14:11] We get an expression. And here I have already rewritten it, replacing Pi with PrimePi.

[00:14:19] Okay.

[00:14:20] Again we minimize the noise.

[00:14:26] This time my error is already 0.049, while before it was 0.07.

[00:14:33] So the error decreased.

[00:14:35] This is the criterion that the new parametric formula for a, b3, b4, b5 is better than the previous one.

[00:14:44] The average error has decreased.

[00:14:48] We define the function PrimePiMy and plot...

[00:14:54] We plot the noise value: PrimePiMy[#] - PrimePi[#]

[00:14:59] Here it is! This is what I like.

[00:15:02] Look how good everything looks.

[00:15:04] There is no more of that sine wave onto which the noise is superimposed.

[00:15:09] And it doesn't go up as much as before.

[00:15:15] Here I can stop bothering about that approximation is not ideal:

[00:15:18] Well, I just took some finite number of powers of the logarithm, and I could take some more terms,

[00:15:26] and fix the bend at the right side.

[00:15:31] The most important thing here is that there is no more of that sine wave, those additional waves.

[00:15:38] Then I realize that I'm doing something silly.

[00:15:42] This first component, if it is expanded in powers of 1/Log[n],

[00:15:47] then it turns out to be this.

[00:15:51] So in a sense, it's easier to just choose these kinds of terms

[00:15:57] rather than trying to make the first term something special.

[00:16:01] Let me explain.

[00:16:03] Instead of this and instead of the first term, which of course becomes much better when you add "-a" to it,

[00:16:12] you can take this function, bring n/Log[n] out of the parentheses, and just add all the powers of 1/Log[n].

[00:16:24] And then add noise again.

[00:16:26] See how Noise is expressed

[00:16:29] and nicely write this expression here.

[00:16:34] Repeat the same thing again.

[00:16:36] And in fact, we don't get anything new because we've just rewritten our idea in a simpler form using powers of 1/Log[n].

[00:16:56] This is what our new approximation equals.

[00:16:59] And let's look at the noise again.

[00:17:04] Add a zero to see the extrapolation up to 5 trillion.

[00:17:15] Here there is a slight increase.

[00:17:17] Most likely because the coefficients are not perfectly chosen and one can add further powers here.

[00:17:25] Naturally, the question arises, what function is hidden here in the parentheses?

[00:17:32] The answer is: all this expression actually tends to,

[00:17:38] if you continue this fitting process,

[00:17:41] to the LogIntegral function.

[00:17:45] What is LogIntegral?

[00:17:47] It's a function that equals the logarithm of the integral of 1/Log[x].

[00:17:54] More precisely, it equals the integral from 0 to y of the function LogIntegral [y],

[00:18:01] but we need to deal with the division by zero at x=1.

[00:18:06] To do this, we subtract this pole (1/(x-1)) from the function.

[00:18:12] And, accordingly,  we need to subtract the logarithm from the answer.

[00:18:19] This kind of integration of a function with a pole in the middle is called a principal value integral.

[00:18:26] Here we just surround the problematic point x=1 with a small interval and exclude it from the integration.

[00:18:42] LogIntegral is a very unusual function.

[00:18:46] You see, when I ask Mathematica to expand this function in powers of x,

[00:18:52] it says that it is equal to x/Log[x]⁹, and then there is a polynomial of the ninth degree of Log[x].

[00:19:03] Actually, if we will do this multiplication, do Normal // Expand,

[00:19:13] then we will see that LogIntegral contains x/Log[x] as the main component,

[00:19:20] and then these terms, where the power of the logarithm in the denominator grows.

[00:19:27] Perfectly.

[00:19:29] And, by the way, we can see what the coefficients are equal to: 1, 2, 6, 24, 120, 720... this is n factorial (n!).

[00:19:38] And this is a scary dependence, of course.

[00:19:41] It is clear that if we take a lot of terms,

[00:19:46] then at some point the next term will be greater and greater and exceed one in modulus.

[00:19:56] This is the same case when we should not fully expand this series,

[00:20:01] because it diverges if we take an infinite number of its terms.

[00:20:09] Here, I'm showing this fact again.

[00:20:14] I divided LogIntegral[x] by x

[00:20:17] to see only the component about the logarithms of x.

[00:20:21] Or, this is how we can see all of this and make sure that we really have n-factorial in the numerator.

[00:20:28] And what's drawn here is madness. Such a convergent series cannot exist.

[00:20:36] Okay.

[00:20:37] Up there, what were the coefficients? Let's look at them carefully.

[00:20:49] 1, 1,

[00:20:51] 1.6 (it was 2 there).

[00:20:54] Here we have 14, and there it was 6.

[00:20:57] Here we have 27, and there it was 24.

[00:21:12] I'm telling you, we need to take these coefficients to get a good approximation of the PrimePi function.

[00:21:20] Let's try to summarize what we have:

[00:21:25] First: the noise amplitude equals √x/Log[x]

[00:21:32] and the first approximation is x/(Log[x]-a).

[00:21:40] The second approximation is...

[00:21:44] Let me write it down so it's in front of us.

[00:21:49] The second approximation is this approximation,

[00:21:50] in which the main component is x/Log[x] * 1

[00:21:55] and there are these additional components.

[00:21:59] And we can ignore this.

[00:22:01] This component is much smaller than this quantity, because here we have the square root of x, and here we have x.

[00:22:10] And the next approximation is the LogIntegral.

[00:22:15] The first one is the blue. You see, it goes up.

[00:22:21] The second one is my approximation. The yellow one.

[00:22:27] And the third one is the LogIntegral approximation. The green.

[00:22:33] You can see that the yellow one is the best of these three in this range of values.

[00:22:40] But...

[00:22:41] But in reality, this approximation can be greatly improved.

[00:22:46] And let me do that right now.

[00:22:50] We can add the LogIntegral of the square root of x with a coefficient of 1/2. "1/2LogIntegral[Sqrt[x]]"

[00:23:04] Let's see how much the green graph improves.

[00:23:11] Here we go!

[00:23:15] Here we can add 1/3 of the LogIntegral of the cube root of x and get an even better green graph. "1/3LogIntegral[Sqrt[x,3]]"

[00:23:25] Riemann obtained a more accurate formula through LogIntegral.

[00:23:30] Here's what it looks like:

[00:23:32] You have to take the sum of LogIntegals of this expression multiplied by mu[i]/i.

[00:23:42] These things have to be taken with different coefficients.

[00:23:45] This is the main, first component for i=1.

[00:23:49] Then comes this component, which I have already written above.

[00:23:53] Then there's 1/3 also with a minus sign.

[00:23:56] Then there's 1/5 (we're going by prime numbers) also with a minus sign.

[00:24:02] Skipping ahead...

[00:24:03] Next is 1/7, also with a minus sign.

[00:24:05] Basically, all prime numbers here have a minus sign,

[00:24:09] while the product of two prime numbers has a plus sign.

[00:24:13] For example, 1/14 has a plus sign.

[00:24:19] Numbers that contain a square of a prime number,

[00:24:22] where the decomposition includes the square of some prime number,

[00:24:24] are absent here.

[00:24:26] For them, the MoebiusMu function is equal to zero.

[00:24:29] The MoebiusMu function is equal to 1, -1, or 0.

[00:24:35] It is equal to zero for numbers not free from squares, inside of which there is a square of a prime number.

[00:24:42] And it is equal to 1 or -1, depending on how many prime numbers need to be multiplied to obtain i.

[00:24:56] So this is the first component of R [x, n].

[00:25:00] LogIntegral and also such things. They are also LogIntegral only from the roots of x and with coefficients.

[00:25:07] The most important component in R [x, n] is this one.

[00:25:12] This component is not that important. All other components are only important for small values of x.

[00:25:20] That is, everything else is needed to converge better for small x.

[00:25:28] For the asymptotic, only this component is important.

[00:25:36] This addition is even smaller than all these additions.

[00:25:41] It is of the order of magnitude of 1/Log [x]² without the x multiplier on top.

[00:25:51] Here you can see on the LogLogPlot, that the decrease is approximately quadratic, 1/Log [x]².

[00:26:04] So, let me define this Riemann function

[00:26:11] and draw four noise plots.

[00:26:19] Pi minus the first - the simplest approximation.

[00:26:22] Pi minus my approximation, where there are powers of n/Log[x]ᵏ.

[00:26:28] LogIntegral approximation.

[00:26:32] And this is the most accurate Riemann approximation.

[00:26:38] The first approximation, the blue one, goes up.

[00:26:43] The yellow and the green...

[00:26:46] The yellow approximation, here it is, it's not visible here, it's hidden behind the red one.

[00:26:54] Hidden behind the back of the red one.

[00:26:57] This approximation - this is the green LogIntegral approximation.

[00:27:03] Yes, we need to add 1/2  here (UPDATE: not 1/2, but 1)

[00:27:06] Or maybe, as I said earlier, add 1/2LogIntegral[Sqrt[x]] here.

[00:27:22] Here, we will see how the green approximation will become better.

[00:27:28] Here we go!

[00:27:30] So all three approximations are equally good

[00:27:35] and approximately after 10⁹ they are practically indistinguishable.

[00:27:41] For common goals, this approximation can be used perfectly well.

[00:27:49] It is good after x = 100 and up to x ≈ 10¹¹.

[00:27:56] Here I drew my approximation minus the superior Riemann approximation.

[00:28:04] And you can see that mine approximation is not so good below 100 and above 10¹¹.

[00:28:11] But below 100, you can just remember the tabulated function PrimePi[x].

[00:28:17] And above 10¹¹, it might not be interesting to anyone.

[00:28:22] At such large values of x, the answer is unlikely to be needed by anyone.

[00:28:32] Takeaways.

[00:28:34] First:

[00:28:34] The prime-counting function Pi grows roughly as x/Log[x],

[00:28:40] and this limit is equal to one.

[00:28:44] We have quickly arrived at a very important and interesting thing.

[00:28:49] The noise that manifests if we subtract all the analytical components we find in the Pi function.

[00:29:03] We understand that this noise grows roughly as x/Log[x],

[00:29:09] and here's what it looks like.

[00:29:12] If you take a logarithmic x-axis, it behaves as if it doesn't change

[00:29:20] and makes more or less the same noise.

[00:29:24] And of course, physicists can attack it and study it, as they do

[00:29:29] using spectral analysis,

[00:29:32] using some autocorrelation functions of this noise,

[00:29:36] and discover many interesting facts about prime numbers.

[00:29:41] Discover experimentally. Not prove, of course.

[00:29:47] Next. The next important takeaway.

[00:29:51] When you have some conjecture about the analytic form of a function,

[00:29:58] you can use NMinimize to find and adjust the coefficients of your formula.

[00:30:07] Next up.

[00:30:08] A good approximation for the function Pi is the LogIntegral function.

[00:30:16] In its simplest form, it can be written as this equation,

[00:30:20] but more accurately, it looks like this:

[00:30:25] R[x], which is approximately equal to li[x], and a complex component, which is very, very small and only important for small x.

[00:30:38] This component is written here.

[00:30:42] Moving on.

[00:30:44] The most important thing.

[00:30:46] It turns out the following statement is true:

[00:30:51] The fact that this noise is bounded by √x*Log[x] is equivalent to the Riemann hypothesis.

[00:31:02] As a reminder, the Riemann hypothesis is the conjecture that all non-trivial zeros of the ζ-function lie on the vertical line in the complex plane with real part 1/2.

[00:31:20] The ζ[z] function is a function that is defined as an infinite sum for z > 1,

[00:31:29] and as an analytic continuation of this function in all other points.

[00:31:35] As we can see, the noise actually runs in the range from -0.5 to 5.

[00:31:41] But it is possible that sometimes it may jump up to some point in isolated areas.

[00:31:48] It is assumed that individual points in this noise

[00:31:57] run away from the x-axis up and down no more than some constant times log[x]².

[00:32:06] Although, when you look at it, it feels like it's just in some strip, and that the running away doesn't increase with the growth of x.

[00:32:20] Perhaps that's the case.

[00:32:22] This is, of course, interesting, if the stronger statement is true that there is a strip that can completely cover this noise from above.

[00:32:35] That's all for today.

[00:32:37] Good luck to everyone. Bye!
