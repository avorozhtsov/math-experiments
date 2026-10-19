# 22.  Распределение простых чисел и числа Каталана. Неравенства Чёбышева (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [VeLbvkEJrn0](https://www.youtube.com/watch?v=VeLbvkEJrn0). Получено: 2026-10-08T17:41:56+01:00.

[00:00:00] Hello! Welcome to "Mathematical Adventures".

[00:00:03] Today, we're diving deep into the prime number theorem,

[00:00:06] which goes something like this:

[00:00:08] The number of primes less than n

[00:00:11] is roughly n divided by Log[n].

[00:00:15] In fancy math talk, it sounds like this:

[00:00:18] The limit of this ratio equals 1.

[00:00:22] Now, we won't be proving this theorem today; it's quite the mathematical odyssey.

[00:00:26] Instead, we'll prove a pair of these nifty inequalities.

[00:00:28] We want to prove that this expression is sandwiched between two positive numbers, a and b.

[00:00:32] Concrete, real-deal positive numbers.

[00:00:36] This problem has occupied the minds of some mathematical legends, including Pafnuty Chebyshev.

[00:00:39] Yes, the same fellow who brought us those polynomials we talked about recently.

[00:00:43] He came up with this result back in 1852.

[00:00:46] The constants a and b he found were pretty darn close to 1.

[00:00:53] But he couldn't prove the existence of the limit, even though he was on the right track.

[00:00:58] He did prove, however, that if there is a limit, it's equal to 1.

[00:01:03] A rather intriguing claim.

[00:01:07] The actual proof of this limit's existence came 45 years later.

[00:01:12] And it was based on the Riemann zeta function.

[00:01:17] Specifically, the fact that it has a pole at 1,

[00:01:20] and all of its zeros reside to the left of a vertical line with a real part of 1.

[00:01:28] But, my friends, that's getting into some serious mathematical territory...

[00:01:31] Far easier to derive these nifty inequalities instead.

[00:01:35] This one on the right is a walk in the park to get.

[00:01:40] We'll be using school methods and those Catalan numbers we learnt about recently.

[00:01:45] In general, I'd like this video to be more than just a proof.

[00:01:52] I want it to be a mathematical journey.

[00:01:57] You see, we stumbled upon Catalan numbers.

[00:02:00] We noticed some fascinating prime-related properties hiding within these Catalans.

[00:02:05] So, we decided to explore further.

[00:02:07] By pure chance, we stumbled upon one inequality and then another.

[00:02:12] The goal of this video is to showcase this mathematical adventure as a way of the Samurai.

[00:02:20] When there's no fixed destination, just new mathematical terrain to explore and intriguing observations to make.

[00:02:27] We follow the mathematical path illuminated by curiosity.

[00:02:31] We gather important observations along the way.

[00:02:35] And these accumulated insights will surely come in handy when tackling specific mathematical puzzles on our journey.

[00:02:40] These observations will be our guiding light as we continue on this mathematical adventure.

[00:02:47] In addition to these inequalities, we'll uncover more mathematical gems.

[00:02:50] And some visually stunning plots...

[00:02:53] Like this one, for instance. What does it mean?

[00:02:56] Let me try to explain right away.

[00:02:59] Take the Catalan numbers and look at the powers of 2 within them.

[00:03:05] In the Catalan numbers c1, c2, c3, and so on.

[00:03:08] Apply Accumulate to this series of numbers.

[00:03:13] Then subtract (n+1)Log[n + 1] from it.

[00:03:18] And voilà, you've got yourself this beautiful fractal function.

[00:03:23] And if we divide it by n, we get this intriguing result.

[00:03:27] In essence, it depicts the function of the power of the prime number 2 in the product of the first n Catalan numbers.

[00:03:37] Also minus a certain base function of (n+1)Log[n+1].

[00:03:43] Alright, let's keep this mathematical journey rolling.

[00:03:45] So, we've uncovered the Catalan numbers (c_n) and their explicit formula.

[00:03:52] But today, we'll find it more convenient to work with numbers that are n + 1 times larger.

[00:03:59] In other words, with the binomial coefficient 2n/n.

[00:04:02] Let's define it.

[00:04:04] Here are our Catalan numbers.

[00:04:07] And here are the first 10 centered binomial coefficients.

[00:04:10] I'll call them centered binomial coefficients because these numbers, 2, 6, 20, 70...

[00:04:20] They are these numbers: 2, 6, 20, 70...

[00:04:26] Let's enclose them in a frame.

[00:04:30] In general, today we'll be studying these binomial coefficients,

[00:04:36] investigating the powers of prime numbers within them,

[00:04:39] and making interesting observations.

[00:04:43] Here's observation №1.

[00:04:44] The remainders when dividing these binomial coefficients by 5 look like this.

[00:04:52] Some remainders go on, and then there's a long sequence of zeros.

[00:04:56] Again, non-zeros,

[00:05:00] then another long sequence of zeros.

[00:05:03] This holds true for both 7 and 11...

[00:05:08] We keep encountering these long sequences of zeros all the time.

[00:05:13] Let's delve into these zeros.

[00:05:16] A zero signifies divisibility by a prime number, p.

[00:05:19] But to what power, precisely, does the number b divide by p?

[00:05:25] To understand this, we'll define the function vp, which represents the exponent of the prime number p in the integer x.

[00:05:36] For instance, let's consider the case of 5.

[00:05:40] Here, we have remainders "2, 1".

[00:05:46] This implies that the number isn't divisible by 5.

[00:05:48] Then "0, 0".

[00:05:50] This indicates that the number is divisible by 5, and specifically, it's divisible by the first power of 5.

[00:05:55] Then it's not divisible again, and then it is...

[00:05:57] We encounter numbers that are divisible by 5^2,

[00:06:00] and 5^3.

[00:06:02] In fact, if desired, you can find numbers that are divisible by any power of 5.

[00:06:07] However, the maximum power of 5 in binomial coefficients increases very slowly.

[00:06:13] This is an interesting observation.

[00:06:16] What's also interesting is that we periodically encounter zeros here.

[00:06:20] So, no matter how far we go in these binomial coefficients,

[00:06:24] numbers that are not divisible by 5 will still appear.

[00:06:30] So...

[00:06:31] We expand using the formula b_n and get something such,

[00:06:37] that the exponent of the prime number p in b_n is equal to the difference between these two expressions.

[00:06:45] The function vp is an entirely additive arithmetic function.

[00:06:50] vp[a * b] = vp[a] + vp[b]

[00:06:55] And when we divide, we get the difference.

[00:06:59] In essence, today we'll try to express this equation.

[00:07:03] I've called it the vp-identity, but that's an unofficial name. It's incorrect.

[00:07:09] What we want to write down is that x can be expressed as a product of prime powers in the following way.

[00:07:16] We simply take the Log[x].

[00:07:19] Then, instead of a product, we have the sum of Log[p] times the power of the prime number p within x.

[00:07:26] And we'll apply this elementary equation to various expressions to get what we need.

[00:07:34] But let's start with something very simple for now.

[00:07:38] Let's immediately derive a fascinating result by school methods.

[00:07:44] The result is as follows:

[00:07:47] It's clear that the central binomial coefficient is less than 2^2n.

[00:07:56] So, let's consider this expansion.

[00:08:00] The 10th row of Pascal's triangle.

[00:08:03] Let's take this central binomial coefficient...

[00:08:06] And it's entirely obvious that it's less than 2^10.

[00:08:11] Simply because the sum of all coefficients (this is x = 1) yields 2^10.

[00:08:18] So, on one hand, we have obvious inequalities,

[00:08:22] and on the other hand, from the formula, we can see that in b_n, prime numbers greater than n are in the numerator.

[00:08:33] And they cannot be canceled by what's in the denominator.

[00:08:39] (2n)! is the product of numbers from 1 to 2n.

[00:08:43] n! is the product of all numbers from 1 to n, and there are two of them.

[00:08:49] Prime numbers greater than n cannot appear in the denominator.

[00:08:54] This means that b_n is definitely greater than the product of all prime numbers from n + 1 (inclusive) to 2n.

[00:09:06] So, this is what we want to write down.

[00:09:10] 2^2n is greater than the product of prime numbers from n + 1 to 2n.

[00:09:18] A result suitable for school.

[00:09:21] Let's introduce a definition...

[00:09:23] Alright... let's call this function θ[n].

[00:09:26] And let it be the product of all prime numbers less than n, along with the logarithm.

[00:09:36] The logarithm of a product is expressed as the sum of logarithms.

[00:09:40] So, when we take the logarithm of both sides,

[00:09:45] it gives us...

[00:09:48] Well... this 4^n here.

[00:09:51] This means Log[4n] ≥ (θ[2n] - θ[n]).

[00:10:02] Let's write this down several times for n, n/2, n/4, n/8, and so on.

[00:10:09] Let's write down Log₂[n] lines here.

[00:10:14] And let's sum up these inequalities.

[00:10:16] What will we get?

[00:10:18] On the left, we get Log[4] * 2n.

[00:10:23] 2n is the sum of all these factors plus one.

[00:10:29] Here, we get cancellation.

[00:10:31] This cancels out with this, and so on.

[00:10:36] And we are left with just the first part.

[00:10:39] In the end, Log[4]2n ≥ θ[2n]

[00:10:44] Now, when we substitute n/2 here, we get θ[n] ≤ Log[4]n.

[00:10:53] Approximately ≈ 1.386 * n

[00:10:58] By the way, we've already dealt with this function in one of our videos.

[00:11:02] And got this experimental result.

[00:11:05] That θ[n] is actually ≈ n.

[00:11:08] And it becomes slightly less than n asymptotically.

[00:11:14] So, the truth is that θ[n] has an asymptote.

[00:11:21] If we divide θ[n] by n, in the limit, we get 1.

[00:11:24] This theorem is, in fact, equivalent to the Prime Number Theorem.

[00:11:29] We saw it through numerical experimentation, but we didn't prove it.

[00:11:37] In short, the truth is that instead of 1.386, we should write 1, but it's not that simple.

[00:11:45] So far, we've got this upper bound.

[00:11:50] Let's move on.

[00:11:52] This result can be further developed.

[00:11:59] Somehow, the idea comes to us...

[00:12:02] Let's take the product of prime numbers from √n to n.

[00:12:08] How does this idea come to our minds?

[00:12:12] Well... just think about it.

[00:12:15] This idea actually comes to mind when you think about this result.

[00:12:21] You start to understand that if we take θ[√n], it's asymptotically smaller than θ[n].

[00:12:31] So, we can study prime numbers from √n to n.

[00:12:41] What will we get?

[00:12:43] We'll get that this logarithm is equal to the difference.

[00:12:48] We can get a lower estimate like this:

[00:12:55] how many of these numbers from √n to n?

[00:12:58] This difference is already the Pi function.

[00:13:01] That's the number of prime numbers in this range.

[00:13:08] So, we take their products and logarithms.

[00:13:14] It's like we're taking the sum of the logarithms of these prime numbers.

[00:13:18] And each of these terms is definitely greater than Log[√n].

[00:13:23] So, we write down this expression and say that it's less.

[00:13:26] We've got a lower estimate for this thing.

[00:13:30] Next, we divide by Log[√n] and get this.

[00:13:38] Then we move Pi[√n] to the right and make a very rough estimate.

[00:13:46] The number of prime numbers less than √n is definitely less than √n.

[00:13:51] And in the end, we can discard this term by rounding up the "α" coefficient.

[00:14:00] And say that, starting from some large n, we can neglect this term

[00:14:08] due to a slight increase in this constant.

[00:14:12] In the end, we've got an upper estimate for Pi[n].

[00:14:17] But the truth is, instead of 1.1 (like Chebyshev), we got 2.78, much cruder. But it was a complete giveaway.

[00:14:29] That's how we quickly got two results.

[00:14:34] One for the θ[n] function,

[00:14:37] and the other for the Pi[n] function.

[00:14:40] Okay...

[00:14:43] Let's move on.

[00:14:45] Let's write down this vp - identity for n! and the binomial coefficient b_n.

[00:15:01] Let's start with the function vp[n], where n ranges from 1 to 128.

[00:15:08] Take the prime number 2.

[00:15:11] This is what the powers of the prime number 2 in the number n look like.

[00:15:18] A simple function like this.

[00:15:19] Every second number isn't divisible by 2, so vp = 0.

[00:15:24] Every second number is divisible by 2. Here...

[00:15:29] Every fourth number is divisible by 2^2.

[00:15:34] Every eighth number is divisible by 2^3, and so on.

[00:15:39] And vp[n!] is actually the sum of all these columns.

[00:15:50] Moving on...

[00:15:52] We can calculate the sum of these columns like this:

[00:15:56] We can calculate it horizontally.

[00:16:02] Let me explain...

[00:16:05] Let's mentally imagine that there are points at the intersections with the horizontals as well.

[00:16:12] Then, the sum of the heights of these columns equals the number of points in this region.

[00:16:21] In other words, above horizontal 0.

[00:16:25] So, vp[n!] can be calculated like this:

[00:16:31] the number of points on horizontal 1,

[00:16:34] the number of points on horizontal 2,

[00:16:36] including these intersections.

[00:16:39] The number of points on horizontal 3, and so on.

[00:16:44] If n = p^k, then the number of points on the first horizontal equals (p^k)/p, which is p^k-1.

[00:16:58] The number of points on the second horizontal equals n/(p^2), which is p^k - 2 if n = p^k.

[00:17:08] And so on...

[00:17:10] So, for a specific value of n = p^k

[00:17:15] vp[n!] becomes a geometric progression with q = p.

[00:17:24] Moving on...

[00:17:25] Now let's think about b_n.

[00:17:29] There we have vp[(2n)!] equal to this.

[00:17:35] vp[n!] equals this.

[00:17:38] And we need to subtract two of these. We get 0.

[00:17:44] At these points, the remainder of division by p isn't zero for n = p^k.

[00:17:53] For other n that are not equal to p^k,

[00:17:57] the number of points on the k-th horizontal equals n/p^k, rounded down.

[00:18:04] These square brackets represent rounding down of a real number.

[00:18:12] You can consider this variant where n = (p^k) plus some small a.

[00:18:19] And then we get this expression for vp[n!]

[00:18:27] and this expression for vp[(2n)!].

[00:18:32] When we subtract one from the other,

[00:18:37] these first parts cancel out

[00:18:41] and only the second parts remain,

[00:18:44] and we can group them further like this.

[00:18:48] We end up with a sum of such brackets.

[00:18:51] Well... instead of a, you could write n here. It's not that important.

[00:18:57] So, this function can be represented as the sum of such functions,

[00:19:05] which are essentially the same function f[x],

[00:19:08] but for x it's first a/p, then a/(p^2), then a/(p^3).

[00:19:21] By the way, these square brackets work directly in Mathematica.

[00:19:27] Here's the function I'm talking about.

[00:19:30] Floor[2x] - 2Floor[x]

[00:19:36] Let's define it.

[00:19:40] And, for example, for the prime number 3, we'll have this option for the first bracket.

[00:19:48] Such a thing for the sum of the first two brackets. And so on...

[00:19:56] Look... we get a kind of fractal function.

[00:20:02] Let's see how it's structured.

[00:20:05] First, we have these three platforms.

[00:20:08] Then, we divide each platform into triangles.

[00:20:13] Here the triangle goes up,

[00:20:15] while here the triangle goes down,

[00:20:16] and then the triangle goes up again.

[00:20:19] We essentially break down each platform into three subplatforms.

[00:20:25] Here, the middle one goes up,

[00:20:29] while here, the two edges go up.

[00:20:32] Here, the middle one goes up again.

[00:20:35] And the same process continues.

[00:20:37] Next, we again divide each of these subplatforms into three parts,

[00:20:40] and again, every other one is lifted up.

[00:20:49] For five, the same concept applies.

[00:20:52] Only there, each platform is divided into five pieces, and two subplatforms go up

[00:21:02] or three subplatforms go up.

[00:21:07] Here, it's two again.

[00:21:11] And so on.

[00:21:12] In short, it's quite understandable how the function vp for the number b_n is structured.

[00:21:22] Here, each point x holds b_x,

[00:21:28] and the Y-axis represents the value of vp,

[00:21:31] the power of the prime number p within b_x.

[00:21:36] We get exactly what we analytically predicted.

[00:21:44] The next observation.

[00:21:46] When we take a large number of b_n values,

[00:21:50] we see that the function vp for them can be bounded from above by the logarithm of n base p.

[00:21:59] Plus some constant, which is unique for each prime but small (<1).

[00:22:07] When we take the logarithmic X-axis,

[00:22:11] plot the logarithm of n here,

[00:22:14] and here, just vp of the number b_n,

[00:22:18] we get such a linear boundary.

[00:22:22] I added 0.1 here to show these blue dots, which are located directly below the yellow line if you don't add 0.1.

[00:22:40] So...

[00:22:41] For two, you get a very precise approximation of the maximum value of the vp function.

[00:22:48] But you need use Log[n+1] instead of Log[n].

[00:22:51] That extra 1 is added, I'll explain where it comes from later.

[00:22:58] For five, and for nineteen.

[00:23:01] Everywhere, you get a simple linear function if you take the logarithmic X-axis.

[00:23:12] Alright...

[00:23:16] vp grows slowly, logarithmically.

[00:23:20] And it takes on values 0, 1, 2, 3, ..., whole numbers.

[00:23:24] The question arises: "How many blue dots are there on this line,

[00:23:29] on this one, on this one, and so on?"

[00:23:32] That's exactly what we'll deal with today. And we'll get the following answers.

[00:23:38] The average value of Y for n = p^k is equal to this.

[00:23:47] Approximately k/2 minus a small adjustment for p > 2.

[00:23:53] And for two, it's a different result.

[00:23:56] We'll prove it directly.

[00:23:59] Let's go...

[00:24:03] You can count the number of different Y values using the Tally function.

[00:24:10] Look... Tally counts frequencies.

[00:24:16] 1 occurs 5 times.

[00:24:18] 2 occurs 3 times.

[00:24:20] 101 occurs 2 times.

[00:24:22] And here it's the same.

[00:24:25] But I prefer to use the IntTally function.

[00:24:29] How it works.

[00:24:30] It gives you the same frequencies but not as pairs, just as an array of frequencies.

[00:24:37] The i-th position contains how many times the number i occurs.

[00:24:47] Look at what we have...

[00:24:50] How many times is vp[b[n]] for p = 2 equal to zero?

[00:24:56] Answer: 0 times.

[00:24:58] How many times is vp[b[n]] equal to 1?

[00:25:02] 7 times.

[00:25:03] How many times is it equal to 2?

[00:25:05] And so on...

[00:25:08] We consider all b_i, where i ranges from 1

[00:25:13] to such an n.

[00:25:18] Clearly, these are simply binomial coefficients.

[00:25:23] Interesting, right?

[00:25:27] So, in different binomial coefficients from b_1 to b_n,

[00:25:31] the frequencies of different values form a row from Pascal's Triangle.

[00:25:37] In other words, they are also binomial coefficients.

[00:25:42] Let's draw the frequencies of these powers of b_1 to b_n for different values of m, where n = (p^m) - 1.

[00:25:55] Here's Pascal's Triangle.

[00:25:58] Only with the ones detached in the first column.

[00:26:04] This triangle has a generating function.

[00:26:10] Like this.

[00:26:11] More precisely, it's the generating function of Pascal's Triangle itself without the detached ones.

[00:26:17] To detach the ones,

[00:26:18] you need to subtract 1/(1-y) here, 1 from here, 1 from here, and so on...

[00:26:23] So, in reality, you need to subtract 1/(1-y).

[00:26:31] This comes from the formula for an infinite geometric series.

[00:26:38] If you're not familiar with this, you'll have to look it up on your own.

[00:26:45] In general, the generating function for Pascal's Triangle is simple.

[00:26:49] For y^k, we want to see the k-th row.

[00:26:54] In other words, (1 + x)^k.

[00:26:57] We want to see the generating function for the kth row in terms of the variable x.

[00:27:03] The generating function for the triangle is a function of two variables: x and y.

[00:27:10] And it's structured like this.

[00:27:12] For y^k, we want to see a polynomial in x, whose coefficients are the numbers in the k-th row of Pascal's Triangle.

[00:27:22] Some triangle. Whichever you prefer.

[00:27:27] Here's the generating function for a triangle with the first column detached.

[00:27:36] Let's make sure of that.

[00:27:38] I divided by y again here because our triangle starts from the second row.

[00:27:44] Okay... Checking...

[00:27:46] Yes, indeed...

[00:27:48] There's no 1 here,

[00:27:50] no 1 here...

[00:27:51] The 1 is detached.

[00:27:53] Okay.

[00:27:55] We need to get a similar generating function for other prime numbers.

[00:28:00] 3, 5 and so on...

[00:28:02] Then, we might come across something interesting.

[00:28:08] We'll get this result soon.

[00:28:10] It will be like this.

[00:28:14] And for p = 3, we'll have a generating function like this.

[00:28:22] And here are the rows of this triangle.

[00:28:25] Each row represents the frequencies of different values of vp

[00:28:31] when we consider vp[b1], vp[b2], ..., vp[bn],

[00:28:36] where n is equal to (p^k) - 1 (or not -1, we'll see).

[00:28:43] Alright...

[00:28:44] I must postpone the proof of this statement until the end of the video.

[00:28:49] For now, let's look at the experimental results.

[00:28:55] Let's experimentally study our vp function some more.

[00:29:01] And very often, when you have a sequence of numbers, it makes sense to consider partial sums of that sequence.

[00:29:11] To compute partial sums in Wolfram Mathematica, you use the Accumulate function.

[00:29:18] Accumulate turns a sequence of numbers into a sequence of partial sums, where the k-th element is the sum of the first k.

[00:29:30] Here's what Accumulate looks like for p = 2.

[00:29:35] Accumulate of vp[b_i] is vp of the product b1, b2, b3, ..., b_n.

[00:29:45] We get this plot...

[00:29:48] And it's evident that it has some small "peaks",

[00:29:53] which are more noticeable for 3.

[00:29:57] There are such points. Maxima.

[00:30:01] For them, you can get the exact value of Accumulate[vp[b_i]].

[00:30:09] For two, in particular, it's simply 0.5Log[n+1] * (n+1).

[00:30:18] And when we subtract this function,

[00:30:23] at the points where there were peaks (these are powers of two minus one),

[00:30:31] we get exactly 0 at these points.

[00:30:36] When n equals 2^(k-1), this expression becomes 2^k.

[00:30:45] And here, I multiplied it by Log[p],

[00:30:50] to get the contribution of the prime number p to vp of the product of b_i's.

[00:30:59] The contribution to the logarithm of the product of b_i's.

[00:31:06] I'm just giving you the answer.

[00:31:10] We'll try to derive it below.

[00:31:13] Basically, you wouldn't have to guess it,

[00:31:16] you could find it through trial and error.

[00:31:22] If everything is clear with the maxima,

[00:31:27] it's much more complicated with the minima (these points at the bottom).

[00:31:33] Let's take a look at them...

[00:31:39] For this, we will divide the expression we had by n.

[00:31:44] This is a very natural desire when you see such a plot, to divide it by n.

[00:31:51] Here's what we get.

[00:31:53] It appears that this entire plot resides within a certain band.

[00:31:59] Both the upper and lower bounds will eventually give us

[00:32:03] upper and lower estimates for Pi[n] or some other prime-related function.

[00:32:11] We'll see this later.

[00:32:13] Right now, we're interested in studying this fractal function and understanding how it behaves.

[00:32:19] Here, I've written down the values of n for all these minima.

[00:32:29] If for points of maximum, we have (2^k)-1

[00:32:33] and the binary representation looks like this,

[00:32:37] then for minima, the answer is like this:

[00:32:39] The binary representation of n looks like 1010101, and so on.

[00:32:49] Well... there's a mistake here...

[00:32:52] In general, it alternates between 1 and 0.

[00:32:56] And sometimes at the end, you encounter an irregularity.

[00:32:58] Sometimes this final "1" is omitted.

[00:33:03] Lets make sure of this

[00:33:07] Here we go...

[00:33:09] So it ends either with (1, 0, 0) or (0, 1, 0).

[00:33:14] Essentially, each subsequent number is either 2 times the previous one

[00:33:19] or 2 times the previous one plus 2.

[00:33:22] Like for example 42 is 20 * 2 + 2.

[00:33:26] This is how the points of minima are arranged.

[00:33:30] This x. And what is y at the points of minima?

[00:33:35] Well, here we get expressions, the structure of which is somewhat clear.

[00:33:44] Firstly, we see that everything tends to some limit -0.14...

[00:33:53] This is a complex matter.

[00:33:55] These numbers are not easy to decipher right away.

[00:33:59] We'll skip studying these numbers.

[00:34:02] Let it be for your independent study.

[00:34:09] So, for powers of two, the upper bound is this,

[00:34:15] and the lower bound is this.

[00:34:19] Here, 0.20744

[00:34:23] is actually this number, but you need to divide it by Log[2].

[00:34:32] Because here, 0.14 is got after multiplying by Log[p].

[00:34:40] And here, I didn't multiply by Log[p].

[00:34:45] For other prime numbers, you get an upper bound like this.

[00:34:49] This is also an analytical result that we will prove below.

[00:34:55] And this result is not proven, but it's somewhat visible.

[00:35:03] You see, this 0.5 – it's an estimate that simply can't be improved upon.

[00:35:10] This value emerges in the very first minimum when p approaches infinity.

[00:35:22] Now, the first minimum looks quite simple.

[00:35:25] It's a scenario where vp[b1, b2, b3, ..., b_n0] doesn't contain the prime number p at all.

[00:35:34] Because there's no prime number p in either the numerator or the denominator as long as n ≤ n0.

[00:35:43] So, let's take n = (p - 1)/2.

[00:35:49] First we need to define...

[00:35:52] Then set...

[00:35:55] Then calculate the limit.

[00:35:57] There we have it. It equals 0.5.

[00:36:00] Of course, this isn't a proof; it's just how the first minimum is structured.

[00:36:04] It's quite possible that the second and third minima will be even smaller.

[00:36:09] This isn't proven here.

[00:36:12] Of course, the number 0.5 for each individual prime number can be replaced by something smaller modulo.

[00:36:19] Now, I'll draw a plot, and hopefully, it'll all become clearer.

[00:36:25] Here, we calculate the minimum for a specific prime number in the range from 0 to 16000.

[00:36:38] Here, you can see the first 15 prime numbers and the number 71.

[00:36:44] For some reason, I did it this way...

[00:36:46] Initially, for two -> 0.20

[00:36:50] Then, it gets closer to 0.5

[00:36:57] For example, this is what the plot looks like for p = 5.

[00:37:05] The first minimum is found right here.

[00:37:08] The second and third minima are at approximately the same level, around -0.4.

[00:37:15] If we take 7... it sort of looks like this.

[00:37:20] Let's create a Manipulate.

[00:37:22] And visualize our difference.

[00:37:26] True minus our approximation (n+1)*Log[n+1].

[00:37:33] This function is simply 0. A horizontal line.

[00:37:38] And this is another horizontal line, which is derived...

[00:37:46] right here.

[00:37:48] Some unique constant for each prime number.

[00:37:52] And this constant is determined simply as the actual minimum among the first 16000 n values.

[00:38:03] Let's experiment... p equals 2. The first prime number.

[00:38:12] Three... Already -0.4...

[00:38:18] Then, smaller modulo...

[00:38:23] Even smaller modulo...

[00:38:25] So, p = 7 is the smallest.

[00:38:32] And then it gradually starts increasing again.

[00:38:38] As p increases, this minimum grows very slowly.

[00:38:44] The first minimum increases very slowly and approaches -0.5 as p tends to infinity.

[00:38:52] And as we can see from examples of small prime numbers,

[00:38:58] the second, third and subsequent minima don't deviate much from the first minimum.

[00:39:07] A similar study of minima can be done for p = 3 and other values of p.

[00:39:15] Maxima are found at points (p^k) - 1.

[00:39:20] In these n values.

[00:39:25] And the pi-notation of these numbers looks like a sequence of twos for p = 3.

[00:39:35] For p = 5, it would be fours.

[00:39:39] Minima are a more complex matter.

[00:39:42] I zoomed in here once again,

[00:39:46] looked at what n equals,

[00:39:49] and wrote down the initial values. 13, 40, 121, etc.

[00:39:56] Let's see how they are structured. They are structured very simply.

[00:39:59] This number, in pi-notation, consists of nothing but ones.

[00:40:04] Here is where the minimum is located.

[00:40:10] You can see that the numerical values are slowly increasing modulo,

[00:40:18] and most likely, they have some limit

[00:40:21] that is less than 0.5 modulo.

[00:40:27] Studying these minima is a complex matter.

[00:40:30] In short, one can delve into the study of minima for different p

[00:40:36] and try to guess what this limit of minima is.

[00:40:42] What I want to draw your attention to

[00:40:44] I want to draw your attention to the fact that the contributions of different prime numbers to Accumulate[vp[b[i]],

[00:40:52] these contributions are roughly the same.

[00:40:55] At first, the contributions from different prime numbers to the logarithm of Accumulate[vp]

[00:41:01] They sort of keep overtaking each other.

[00:41:06] I'm not sure if this is a correct statement...

[00:41:07] The statement that for any two prime numbers, their contributions constantly overtake each other.

[00:41:13] And no contribution ever dominates the other completely, to infinity.

[00:41:19] The number p = 2, it seems, is a special case after all.

[00:41:24] But the others...

[00:41:26] With the others, it's complicated.

[00:41:30] Now, let me explain.

[00:41:34] Going back a bit.

[00:41:35] Look at what we've got.

[00:41:39] We've got that the contribution from the prime number p is equal to its vp multiplied by the logarithm.

[00:41:48] Let's take this value.

[00:41:51] Multiply it by Log[p].

[00:41:54] And what do we get when we bring this logarithm of p inside the brackets?

[00:42:00] Let's bring it in...

[00:42:01] Here, p disappears and it becomes a simple natural logarithm.

[00:42:06] And here, multiplication takes place.

[00:42:08] So, the contribution of the prime number p,

[00:42:12] it's mostly (n + 1) * Log[n+1] for any prime number p.

[00:42:18] In other words, the contributions from all prime numbers are asymptotically the same, (n + 1) Log[n+1],

[00:42:25] if we ignore this small addition, which does depend on p,

[00:42:30] but it's noticeably smaller than this.

[00:42:33] So, we can kind of disregard it and roughly say that the contributions are the same.

[00:42:42] And maybe even the statement that they constantly overtake each other is true for large p.

[00:42:46] Because this number appears to approach zero.

[00:42:51] I'm talking about the limit of Log[p] / (p - 1) -> 0 as p -> infinity (without the n multiplier).

[00:42:57] Because this number approaches zero

[00:43:00] and against the backdrop of this number, 0.5 or 0.4, whatever it is,

[00:43:05] it diminishes to zero for large p.

[00:43:09] And large prime numbers, they definitely behave this way, overtaking each other within the b_i's.

[00:43:19] Alright... Let's move on.

[00:43:24] Let's now move on to our other important statement.

[00:43:30] To this first statement.

[00:43:33] And now, let's write that the contribution of the prime number p to the logarithm of b1, b2, b3, ..., bn

[00:43:46] is less than or equal to this.

[00:43:52] Because b_i has an estimate like this, what can do?

[00:44:00] We can write this inequality, simplifying b_i to an estimate of 2^2n.

[00:44:06] There's an error here. We should use Stirling's formula and estimate it in the other direction. Instead of an upper estimate b[n] < 4^n we need a lower estimate like b[n] > 3.9^n, starting from some n. Or work with O[n], as done below.

[00:44:14] Let's go through with it.

[00:44:17] From this statement about the approximation of b_n

[00:44:21] and from what I call the vp-identity,

[00:44:26] we get:

[00:44:29] the logarithm of the product is equal to n(n+1)Log[2].

[00:44:36] This follows from the approximation that b_i equals 4^i.

[00:44:42] And from this statement, by replacing Log[p] * vp

[00:44:52] with this expression, multiplied by 1/2,

[00:44:56] we get this answer.

[00:45:00] Since the contribution of each prime number is approximately the same,

[00:45:05] we end up with the count of prime numbers

[00:45:08] that enter into the products of b_i from 1 to n

[00:45:15] multiplied by the size of this contribution.

[00:45:18] We have these two things, and now we write the inequality.

[00:45:23] We need to figure out which way it's directed.

[00:45:26] It turns out that Pi[2n] is greater than or equal to

[00:45:31] this estimate

[00:45:37] divided by this estimate,

[00:45:40] which came from here.

[00:45:42] And we get that Pi[2n] is greater than or equal to this thing.

[00:45:48] Or greater than or equal to 0.69n/Log[n].

[00:45:53] That's how we made a step towards the prime number theorem.

[00:46:00] We didn't prove that this limit exists,

[00:46:02] but we did prove that this quantity is bounded from below by the number 0.69.

[00:46:11] I'll skip this part, it seems like some nonsense is written here...

[00:46:16] What else I want to tell you here...

[00:46:20] Well, okay... Let's move on to the attempt to prove that the maximum approaches (n + 1) Logₚ[n+1].

[00:46:35] For this, we'll need to draw generating functions for triangles.

[00:46:43] We've already drawn a triangle for the frequency values of vp[b[i]] for p = 2.

[00:46:55] It turns out that this is, indeed, Pascal's Triangle.

[00:46:59] So...

[00:47:04] The triangles for p = 3, 5 and 7 look like this.

[00:47:17] A very interesting puzzle is to try to crack this triangle.

[00:47:20] To figure out if there are any recurrent dependencies here.

[00:47:25] The answer is: "There are!"

[00:47:28] Moreover, we can choose different options for the recurrent formula.

[00:47:33] For example, we can represent any number in this triangle as a linear combination of numbers

[00:47:40] that are right here.

[00:47:43] The coefficients in this linear combination turn out to be:

[00:47:46] 2, 1, 2, 4, 8, 16, and so on.

[00:47:50] Let me demonstrate how this works.

[00:47:53] 1072 – this is a sum of these numbers with coefficients 2, 1, 2, 4, 8, 16.

[00:48:03] In Mathematica, the dot corresponds to scalar multiplication.

[00:48:06] And you get exactly linear combinations of numbers from this series

[00:48:11] with coefficients from this series.

[00:48:16] You can choose a different option for the recurrent formula.

[00:48:19] You can write that this number

[00:48:20] depends as the sum of these numbers.

[00:48:22] And, oddly enough, the coefficients will be the same powers of two.

[00:48:27] At first, some irregularity (2), and then there are powers of two.

[00:48:33] You can choose this option.

[00:48:35] And write this number

[00:48:36] as a linear combination of these numbers.

[00:48:39] The number 312 should have been included in the yellow strip - into the set of numbers, a linear combination of which gives the number 1072.

[00:48:47] But there, the dependence is more complex.

[00:48:51] You can come up with a recurrent formula like this.

[00:48:55] By the way, the same applies to Pascal's Triangle.

[00:48:59] Just, for example, in this version, it will have...

[00:49:02] It will simply have: the sum of two numbers above with coefficients 1, like [1072] = [312] + [419].

[00:49:10] For instance, here it seems like there will be all ones as coefficients.

[00:49:14] In Pascal's Triangle, you can also choose different options for the recurrent formula.

[00:49:20] Not just the sum of the two above.

[00:49:25] Take a look at this moment.

[00:49:28] In general, here I'm showing that there are different options for the recurrent formula.

[00:49:33] And the simplest one to guess is this formula.

[00:49:37] Here, there are simply powers of two for p = 3.

[00:49:41] And for p = 5...

[00:49:44] Let's see what we get for p = 5...

[00:49:50] We get this 6-th row of the triangle.

[00:49:55] By the way, you can try to derive an explicit formula using some factorials.

[00:50:00] And for this, you can break down these numbers into prime exponents.

[00:50:05] But here, there's nothing interesting to see.

[00:50:08] You can see simple things, like 3^6 – the first number, and 3^5 * 2 – the last number.

[00:50:15] But inside... it's not obvious.

[00:50:20] Here's the triangle for p = 5.

[00:50:23] And here, something interesting happens.

[00:50:26] For example, the number 3970 is written as

[00:50:34] a linear combination of this, this, this, and this number

[00:50:41] with coefficients of 3, and then there's a geometric progression with q = 3.

[00:50:50] Each subsequent number is three times larger than the previous one and starts with 4.

[00:50:57] For p = 7...

[00:50:59] In general, these recurrent formulas are guessed, and then proved.

[00:51:04] And we get the following:

[00:51:08] from these recurrent formulas, we can derive generating functions for the triangles.

[00:51:15] From this generating function, we can get an estimate of the mean value.

[00:51:21] It's very simple.

[00:51:22] So, we have a triangle.

[00:51:25] Let's take a specific fifth row.

[00:51:28] What is the average value of the exponent within this row?

[00:51:37] We take the coefficients from this row as weights.

[00:51:43] So, the total number of elements in the row is the sum of the coefficients.

[00:51:50] This is also the number of indices i that we traverse.

[00:51:56] And in the numerator, we need to write that we get a power of 2 ten times.

[00:52:03] We get a power of 3 ten times.

[00:52:06] We get a power of 4 five times.

[00:52:08] And we get a power of 5 once.

[00:52:12] Here's the manually calculated average exponent of two within b_i.

[00:52:23] How could we express this (this expression)

[00:52:26] using the generating function of the row?

[00:52:30] Like this.

[00:52:31] We can take the derivative of this polynomial, and it will do what we need.

[00:52:38] This 10 will be multiplied by 2.

[00:52:40] This 10 will be multiplied by 3.

[00:52:42] This 5 will be multiplied by 4.

[00:52:44] And this 1 will be multiplied by 5.

[00:52:51] Just remember to substitute x with 1.

[00:52:56] It matches.

[00:52:58] This with this.

[00:53:01] This expression, when we take the derivative of the function and divide by the function itself,

[00:53:07] it's the same as taking the derivative of the logarithm of that function.

[00:53:11] It's all simple.

[00:53:13] Our k-th row (the coefficient at y^k) is this thing.

[00:53:20] ((1 + x)^k) - 1

[00:53:23] And we can simply calculate what this expression equals.

[00:53:28] The logarithmic derivative at the point x = 1.

[00:53:31] So, we've got the answer for 2.

[00:53:34] And it's clear that gradually it all approaches 0.5.

[00:53:41] Good. Now for 3.

[00:53:45] Here's our triangle.

[00:53:48] Here's the recurrent formula we chose.

[00:53:53] How to get the generating function of the triangle from the recurrent formula?

[00:54:05] Let's introduce the notation f_i.

[00:54:07] Let f_k be the coefficient at y^k.

[00:54:11] It is claimed that from the recurrent formula...

[00:54:15] This one. It's written for a specific case, but it's more convenient in a sense.

[00:54:22] It turns out that f_n[x] can be gotten from 2 * f_n-1[x].

[00:54:35] That's this two.

[00:54:39] Plus...

[00:54:41] We take the same power of x, the same vertical, but the previous row,

[00:54:47] and the previous row is n - 1.

[00:54:50] Then we take the pre-previous row, n - 2.

[00:54:54] But here, we need to shift to the left, so here we have a multiplication by x.

[00:55:00] To make this number appear as a power of x,

[00:55:02] which is this, you need to multiply f_n-2 by x.

[00:55:11] Next, here comes the 2. It's from the pre-previous row already.

[00:55:16] Then 4, then 8 and so on.

[00:55:20] So, it turns out that F[x, y] (now we're thinking about F[x, y]) can be gotten from F[x, y] in the following way:

[00:55:33] 2y means we take the previous row.

[00:55:38] In other words, we multiply by "y".

[00:55:41] This means that now something from y^k-1 from the same triangle will contribute to y^k.

[00:55:52] Then, we take from the n - 2 row by multiplying the same function F[x, y] by y^2.

[00:56:03] And we also need to shift to the left, so the multiplication by x occurs.

[00:56:09] What's here?

[00:56:11] That's a good question.

[00:56:13] It's just found by trial and error to figure out what to substitute here.

[00:56:17] In the end, we get this expression.

[00:56:24] Here are calculations where I was specifically finding this expression that needs to be substituted in the numerators.

[00:56:32] And the denominator follows from the recurrent formula.

[00:56:39] Thus, for p = 3, we get the generating function of the frequency triangle as follows.

[00:56:52] Here, I'm just making sure the answer is correct.

[00:56:55] And these coefficients are exactly what I saw in the triangle,

[00:57:00] computed explicitly by hand in the real triangle.

[00:57:06] Okay... This is all very complicated and will take forever if I don't skip ahead.

[00:57:12] Similar things can be done for p = 5, 7, 11 and we get the answer.

[00:57:21] The answer is written here.

[00:57:23] We find that for the binomial coefficients triangle of prime frequencies for n = p^k,

[00:57:36] it can be expressed by this generating function.

[00:57:41] So how do we proceed from here? How do we get the mean value of the exponent from this answer?

[00:57:51] We take the denominator and study its roots with respect to y.

[00:57:58] Knowing the roots, we can expand it into a combination of two such simple fractions.

[00:58:07] 1 divided by y minus the first root.

[00:58:11] This scary root here.

[00:58:13] 1 divided by y minus y2. The second scary root.

[00:58:19] And when you expand such an expression,

[00:58:22] you get some linear combination of simple fractions like 1/(y - y_i).

[00:58:32] The coefficients depend on the situation here.

[00:58:35] Here, we have coefficients of 1 and -1.

[00:58:38] And then we divide by this thing, independent of y.

[00:58:44] Lets check...

[00:58:47] It's true.

[00:58:50] This is just 1 divided by the denominator.

[00:58:54] And if we have some numerator, we simply add it.

[00:58:58] Based on this expansion, we will now get the answer.

[00:59:02] It’s clear what these things are equal to.

[00:59:07] These are basically formulas of infinite geometric progressions.

[00:59:12] So here, we write:

[00:59:14] one geometric progression minus the second geometric progression.

[00:59:20] We take this coefficient.

[00:59:23] Checking...

[00:59:25] Okay. I wrote this for 5. Let's go back to 5...

[00:59:32] Checking...

[00:59:36] Fourth row for p = 5.

[00:59:39] 81, 189

[00:59:42] Here I got the answer for this thing.

[00:59:51] To get the answer for this thing, you need to do a simple thing.

[01:00:00] The coefficients b_n, which are here at y^n,

[01:00:09] are gotten by this formula

[01:00:13] from the coefficients of this thing.

[01:00:18] Let's check...

[01:00:20] And indeed, this thing equals

[01:00:23] this expression

[01:00:24] minus x times this expression.

[01:00:29] 162 = 189 - 27

[01:00:35] First, we manually calculate the number we believe in.

[01:00:43] Then, we verify.

[01:00:46] Yes... the correct answer.

[01:00:52] And here comes the moment of truth.

[01:00:55] What is the average value of the degree in the k-th row of the triangle for prime number p > 2?

[01:01:05] It all simplifies to this form.

[01:01:08] And here are the answers.

[01:01:11] The average value for n = p^k.

[01:01:16] The average value for n = (p^k) - 1, which is more accurate, as it turns out, it's different.

[01:01:23] We need to multiply this by p^k and divide by (p^k) - 1.

[01:01:29] Because, as we remember, vp of b^n, where n = p^k, equals 0.

[01:01:37] So, we can either include b_n or not.

[01:01:41] It doesn't matter.

[01:01:42] For this n, b_n has a zero power of the prime number p inside.

[01:01:49] Oh... this is probably quite hard to follow just by listening.

[01:01:54] Next... This is for 2. For n = (2^k) - 1.

[01:02:00] And here is not the average but the sum of the powers of prime number p inside b_i's.

[01:02:08] Similar expressions are gotten.

[01:02:10] Only for p > 2, this adjustment comes into play.

[01:02:17] Here below, I explain what I said verbally.

[01:02:20] That vp[b_p^k] = 0. We discussed this earlier.

[01:02:27] And that vp of this product

[01:02:29] matches vp of this product as the results.

[01:02:32] And these are the functions I wrote down at the bottom.

[01:02:38] And here's what we get for these specific n.

[01:02:42] Such answer. Absolute equality when n = (p^k) - 1.

[01:02:50] Why is it a maximum?

[01:02:58] Alright... Let's make this a homework question: Why do we need to use the ≤ sign here?

[01:03:03] Why are these n the points of maximum

[01:03:08] of the powers of prime number p inside the product?

[01:03:13] We started with quite elementary methods.

[01:03:17] We simply became interested in the powers of prime numbers inside Catalan numbers.

[01:03:23] And then we went in the direction where the road opened up to us.

[01:03:29] Of course, you need some experience to just ask yourself such a question,

[01:03:37] to make such an observation about prime numbers.

[01:03:40] "Let's look at the product of all prime numbers in the range from n to 2n".

[01:03:47] Or "let's examine the contributions of different prime numbers inside the product of b_i's".

[01:03:55] You need to know how to ask such questions, and that's the main secret of mathematical creativity.

[01:04:04] Then, it's a matter of technique and perseverance.

[01:04:09] As it turned out, Catalan numbers and central binomial coefficients

[01:04:15] can shed light on the asymptotics of these functions, to both lower and upper bounds.

[01:04:26] We used the simple fact that any number x is the product of prime numbers.

[01:04:32] But after taking logarithms, it's expressed in this more complex form.

[01:04:40] And based on the triangle of frequency of powers of the prime number p inside b_i's, we derived some estimates.

[01:04:53] And an important intermediate step was getting the generating function for the frequency triangles.

[01:05:01] And now we know how to bound this A[n], which is part of the formula for Pi[n].

[01:05:11] Pi[n] is approximately n/Log[n].

[01:05:14] And we have proven that the multiplier A[n], which is determined simply by this equation,

[01:05:21] at some point, starting from some n, begins to fluctuate within this range.

[01:05:25] The truth lies in the fact that the limit of A[n] is 1. And this is the fundamental prime number theorem.

[01:05:34] It was proven in 1896 using the Riemann zeta function.

[01:05:44] And essentially, this theorem is equivalent to proving that the Riemann zeta function has a pole at 1.

[01:05:55] A pole of degree 1.

[01:05:58] And that all zeros of this function are to the left of the vertical line with real part equal to 1.

[01:06:07] Chebyshev proved a very interesting statement.

[01:06:10] He was close to this limit.

[01:06:12] He proved that if the limit exists, it is equal to 1.

[01:06:17] But the existence of this limit turned out to be a big question.

[01:06:21] And it turns out that now we have proofs based on the theory of complex variables.

[01:06:28] It's quite unusual that theorems about prime numbers require knowledge of all this.

[01:06:38] Analytic continuations and the theory of complex variables.

[01:06:43] Now it's no longer a surprise.

[01:06:45] Perhaps, back then, it was such an interesting connection between two areas of mathematics.

[01:06:54] We have many unanswered questions about the exact value of this lower bound δ_p.

[01:07:03] And about the average value of this fractal function.

[01:07:12] In some sense, a simpler approach to proving these inequalities.

[01:07:19] You can find it online here, for example.

[01:07:22] An excellent course on analytic number theory.

[01:07:27] It's such... systematic. It starts with the theorem.

[01:07:30] You have to prove the theorem, and somehow, you start pulling lemmas out of thin air

[01:07:37] to reach the theorem you need.

[01:07:40] But it happens much faster. Much clearer.

[01:07:45] Everything there is based on Abel's summation formula.

[01:07:51] Stirling's formula is also a special case of Abel's summation formula.

[01:07:57] I recommend you study this course.

[01:08:02] I watched it myself. I liked it a lot!

[01:08:05] However, it's funny that on the second lecture, the sound disappears halfway through.

[01:08:11] You watch the most important part with prove with no sound.

[01:08:15] That's it for today! Good luck to everyone! Goodbye!
