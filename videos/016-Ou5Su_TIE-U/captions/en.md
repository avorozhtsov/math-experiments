# 16. Приближение многочленами. Многочлены Чёбышева (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [Ou5Su_TIE-U](https://www.youtube.com/watch?v=Ou5Su_TIE-U). Получено: 2026-10-08T17:42:32+01:00.

[00:00:00] Hey there! Welcome to "Mathematical Experiments".

[00:00:04] Today, we'll be experimenting with approximating functions using polynomials.

[00:00:10] And, of course, we'll be learning Wolfram Mathematica by diving right in, just the way I like it.

[00:00:16] Without any extra explanations.

[00:00:20] So, today I want to talk to you about Chebyshev polynomials.

[00:00:26] You'll see how we can reach them on your own by solving a specific practical problem.

[00:00:37] Let's take a look at what these polynomials look like.

[00:00:43] Here's an example of one polynomial.

[00:00:47] And here's its plot.

[00:00:51] The higher the degree, the more oscillations within the interval (-1, 1).

[00:00:56] An important property is that the minima and maxima coincide in magnitude at -1 and 1.

[00:01:06] We'll get to these polynomials by solving the approximation problem using polynomials.

[00:01:14] We'll approximate this function f, which is called the Runge function.

[00:01:22] Here is its plot.

[00:01:25] There's a peak near zero.

[00:01:30] We'll try to approximate this function with a polynomial.

[00:01:34] Here's an example of a 12th-degree polynomial.

[00:01:38] The symbol "coeffs" contains the polynomial coefficients,

[00:01:44] and the symbol "poly" contains the polynomial itself.

[00:01:49] Let's do the next.

[00:01:52] Idea number 1:

[00:01:54] We'll take points on the interval (-1, 1), 13 of them.

[00:02:01] A uniform grid of points.

[00:02:05] Let's call it like this.

[00:02:07] And...

[00:02:09] we'll ask the polynomial to pass through these points exactly,

[00:02:17] taking the values that the function f takes at these points.

[00:02:21] For example...

[00:02:23] An example of the second equation:

[00:02:26] the value of the polynomial at the point -0.833333

[00:02:31] is equal to this expression.

[00:02:35] And we equate this expression to the value of the function f at the point -0.833333

[00:02:43] We end up with 13 such equations for 13 coefficients.

[00:02:49] Mathematica easily finds the solution.

[00:02:53] Here's our polynomial.

[00:02:57] This polynomial, at the nodal points (let's call them that),

[00:03:01] passes through the same values as our function f.

[00:03:09] Our function f is the blue plot.

[00:03:12] And the result of the approximation is the yellow plot.

[00:03:15] Clearly, the yellow plot coincides with the function f at these 13 points.

[00:03:27] But we can't call this a good approximation.

[00:03:30] If it's somewhat okay near zero,

[00:03:32] even there, we see differences between the blue and yellow plots.

[00:03:37] And towards the edges, it's a complete mess.

[00:03:42] If we take the difference, we'll see that the absolute difference is greater than one at the edges,

[00:03:49] while the function itself is smaller than one in magnitude.

[00:03:52] So, this is a bad approximation.

[00:03:55] If we try the Taylor series...

[00:03:59] Okay... better to take the 12th degree...

[00:04:02] ...we still won't find anything good.

[00:04:06] In this plot, there are now

[00:04:12] three lines.

[00:04:14] The original function f is blue.

[00:04:16] Our approximation using the grid is yellow,

[00:04:19] and the Taylor series is green.

[00:04:22] The Taylor series precisely replicates our blue plot in the vicinity of zero,

[00:04:30] but beyond the interval (-0.2, 0.2), it's even worse than the yellow plot.

[00:04:42] So, two of our ideas turned out unsuccessful.

[00:04:47] Approximating the function using a grid of points is a bad idea.

[00:04:52] Using the Taylor series doesn't give a good solution either,

[00:04:58] if we need accuracy over the entire interval (-1, 1).

[00:05:03] We need some third idea.

[00:05:06] Our Idea #1, about the grid, might be successful if we arrange the nodal points in another way.

[00:05:17] For example,

[00:05:20] let's place them closer to the edges of the interval (-1, 1).

[00:05:24] The problems arise precisely at the edges of the interval, and if we place more nodal points there,

[00:05:32] where our function matches the original one,

[00:05:37] we might overcome these problems.

[00:05:42] Let me explain why the uniform grid from -1 to 1 is bad,

[00:05:48] using this polynomial as an example.

[00:05:50] Let's plot the polynomial that takes the value 0 at all nodal points.

[00:05:59] This polynomial has slight oscillations around zero,

[00:06:05] but the closer we get to the edges of the interval (-1, 1), the larger the oscillations become.

[00:06:11] That's it's problem.

[00:06:15] Here's an idea:

[00:06:17] Let's find a grid where the oscillations throughout the interval have the same amplitude.

[00:06:27] That's roughly what this idea sounds like.

[00:06:30] Next, I try to explain something complex here.

[00:06:34] I take this polynomial

[00:06:38] and remove the i-th factor from it.

[00:06:41] And I draw various polynomials, 13 of them,

[00:06:49] to show this problem that if we remove the i-th factor even from the polynomial, then at the i-th node...

[00:06:58] (in this case, I removed the factor x - 0)

[00:07:02] ...the values modulo are smaller than some intervals between nodes.

[00:07:10] That's bad.

[00:07:11] Later, you'll understand why.

[00:07:14] Now I won't specify.

[00:07:17] Here, I want to draw all our basis functions.

[00:07:26] Here's how it looks.

[00:07:29] All 13 basis functions.

[00:07:32] Or, more precisely, here it's 11.

[00:07:35] Here are the actual 13 basis functions.

[00:07:42] The problem with these basis functions is that,

[00:07:46] when we look at a specific basis function and the node that was removed from it,

[00:07:54] at this node, it takes values modulo smaller than in some intervals between others.

[00:08:05] That's one of the problems.

[00:08:07] Maybe it's a difficult and incomprehensible explanation,

[00:08:10] but let's skip it for now and move on to this idea that was mentioned.

[00:08:20] To find a polynomial that oscillates equally over the interval (-1, 1).

[00:08:27] That is, all its maxima and minima have the same value modulo.

[00:08:33] At the end of the video, I attempted to explain the idea of proving the theorem that the polynomial, which is the solution to the minmax problem, must be equioscillating, meaning the values modulo of its extreme values should coincide.

[00:08:43] This can be written as the following code.

[00:08:49] Let's describe the polynomial as a product of factors x - r[i].

[00:08:57] Table generates the list of factors.

[00:08:59] Times multiplies all these factors.

[00:09:03] And we'll ask for the maximum

[00:09:07] and the values of this polynomial on a grid of points from -1 to 1

[00:09:15] to have the maximum of all these values as small as possible.

[00:09:20] So, now it goes like this:

[00:09:20] Minimize the maximum value of the polynomial on the interval (-1, 1).

[00:09:31] Running...

[00:09:33] It's thinking for a while.

[00:09:36] Let's see...

[00:09:39] Here's the result.

[00:09:41] Let's draw this polynomial.

[00:09:45] Here it is.

[00:09:47] See?

[00:09:49] We asked the polynomial to have the smallest value modulo on the interval (-1, 1),

[00:09:58] and it produced a polynomial called "Equioscillating".

[00:10:05] So, these are the modules of the extreme points.

[00:10:13] Well... In this case, they are approximately equal.

[00:10:15] As you can see, for example, this maximum is slightly larger than this one.

[00:10:19] And this actually indicates that Mathematica found not the absolute optimum.

[00:10:26] It's not the best solution to this problem.

[00:10:31] Anyway, let's draw how the roots of this polynomial look like.

[00:10:40] Let's draw the list of roots.

[00:10:41] The X-axis here represents the i-th number,

[00:10:44] and the Y-axis represents the value of the root.

[00:10:48] You can see that the roots are denser near the edges,

[00:10:54] then the distance between the roots increases,

[00:10:57] and then it becomes denser again.

[00:11:02] Some mathematician might say, "Oh! This looks very similar to a sinusoid!"

[00:11:09] More precisely, to the function -cos[αx].

[00:11:16] Let's test this idea.

[00:11:18] To do that, we need to take the arcsine or arccosine

[00:11:22] of these values of the roots

[00:11:25] and see

[00:11:29] if the gotten points lie on a straight line.

[00:11:38] Here I drew the best-fitting line through these points

[00:11:45] and found that they almost perfectly lie on a straight line.

[00:11:52] This is the first way to approach Chebyshev polynomials

[00:11:57] and understand how they work.

[00:12:01] Although I believe that Pafnuty Chebyshev himself took a different path,

[00:12:08] which I will explain later.

[00:12:11] So, the idea is:

[00:12:12] the nodes for which we must set the equality for our polynomial and the original function f,

[00:12:21] form a cosine of some arithmetic progression on the interval (-1, 1).

[00:12:33] More precisely, on the interval from 0 to Pi.

[00:12:36] You can see that the points are located from 0 to Pi, but do not reach Pi

[00:12:44] and do not reach zero.

[00:12:47] But here, I deliberately chose the wrong variant and placed the extreme points right at zero and right at Pi.

[00:12:58] Thus, I got cos[1] and cos[-1].

[00:13:05] Let's visualize this.

[00:13:08] On the upper half-circle, I placed 13 evenly distributed points and projected them onto the X-axis.

[00:13:21] Then I wrote the product of the terms x - x[i].

[00:13:27] And I failed.

[00:13:30] It turned out to be non-equioscillating.

[00:13:35] Because I intentionally made a mistake.

[00:13:38] Since Mathematica told us not to reach 0 and not to reach Pi.

[00:13:44] So, let's listen to it this time and make thе next change.

[00:13:53] We will divide by n + 1 instead of n,

[00:13:56] and make a shift by 0.5 here.

[00:14:00] Here we go...

[00:14:02] Now we get an equioscillating polynomial.

[00:14:08] Visualization.

[00:14:10] You see? There are no points on the circle.

[00:14:13] The first point goes through half the interval,

[00:14:16] then: interval, interval, interval, and so on,

[00:14:18] and then again half the interval,

[00:14:21] and here there are no extreme points at all.

[00:14:24] These are the roots of Chebyshev polynomials.

[00:14:33] Let's see how the approximation based on these nodes looks like.

[00:14:40] Now for some reason, odd powers start to appear.

[00:14:45] By the way, they can be removed with a simple replacement rule.

[00:14:50] Let's draw...

[00:14:53] and you can see that the green approximation is much better than the yellow one we had.

[00:15:00] Alright.

[00:15:04] So, here are our wonderful nodes.

[00:15:08] They are called Chebyshev nodes.

[00:15:15] And again, we can consider a set of basis functions that are constructed as follows:

[00:15:23] we take the product of all the terms x - x[i],

[00:15:28] but exclude one of these terms.

[00:15:32] Here, for example, a term with a node located somewhere here is excluded.

[00:15:36] And here, we already see a remarkable property.

[00:15:38] The value of this basis function modulo at the node is much larger

[00:15:43] than the value of this basis function at all other points of the interval.

[00:15:49] And this holds true for any i.

[00:15:53] Okay...

[00:15:54] Let's assume you understood this idea.

[00:15:59] Here are all the basis functions for n = 30 depicted.

[00:16:10] And here I can even explain.

[00:16:13] Each of these bumps corresponds to the value of the basis function at the node that was excluded from it.

[00:16:27] And, for example, this second-level bump,

[00:16:32] it is adjacent to the node that was excluded.

[00:16:39] You can see that with increasing n, the ratio of the maximum at the excluded node

[00:16:54] to the value of the basis function at other points increases as n grows.

[00:17:00] That is...

[00:17:04] the approximation becomes better and better the more points you take.

[00:17:11] And when you try to approximate the function f using Chebyshev nodes,

[00:17:17] you are, to some approximation, solving this problem:

[00:17:22] "Find a polynomial for which the maximum modulus deviation from the original function over the interval (-1, 1) is minimal".

[00:17:34] But Chebyshev nodes do not give an exact solution to this problem.

[00:17:41] Next, what I wanted to show here...

[00:17:43] Ah! I also wanted to explain another example with this idea of a basis.

[00:17:49] Look, here I took the fifth basis function,

[00:17:51] the eighth one.

[00:17:53] I multiplied the first one by three... it doesn't matter by what.

[00:17:56] And the second one by -7.

[00:17:58] And got these modified basis functions.

[00:18:02] The yellow one,

[00:18:05] it's exactly 3b[5],

[00:18:08] and the green one is -7b[8].

[00:18:13] And the function f2 is the sum of these two basis functions, multiplied by some coefficients.

[00:18:21] And you see? The green function passes through the same point in this node where the yellow one passes through,

[00:18:30] and in this node, it passes through the same point as the green one.

[00:18:38] So, you kind of multiply each basis polynomial by the number

[00:18:43] to get the desired value at the node that was excluded from it.

[00:18:51] And when you then sum up all the basis functions with these coefficients,

[00:18:56] you get a function with the desired properties.

[00:18:58] It will pass through all the nodes at the exact same y-values that the function f takes.

[00:19:12] Okay... I probably better skip ahead...

[00:19:16] Here, I will explain how to get Chebyshev polynomials in Mathematica.

[00:19:27] There's already a ready-made function ChebyshevT.

[00:19:31] There are also Chebyshev polynomials of the second kind, ChebyshevU.

[00:19:35] They are simply the derivatives of ChebyshevT polynomials with respect to x and some other factor 1/n.

[00:19:46] The plot looks like this.

[00:19:49] Well... you already understood how it all works.

[00:19:53] Here, several Chebyshev polynomials are already plotted together.

[00:19:58] We can add the first one.

[00:20:02] And one more thing.

[00:20:03] How could you quickly get polynomials that oscillate between the values (-1, 1)?

[00:20:16] Take the polynomial t2 = 2x^2 - 1.

[00:20:19] It possesses this remarkable property.

[00:20:23] Over the interval (-1, 1), it takes values from -1 to 1.

[00:20:30] From 1, it goes to -1, then back to 1.

[00:20:35] And...

[00:20:38] You can substitute this polynomial into itself

[00:20:43] and get increasingly intricate functions with a greater number of extrema over the interval (-1, 1),

[00:20:52] and all of them will be the same in absolute value.

[00:21:02] So...

[00:21:04] However, this method allows you to generate Equioscillating polynomials with degrees of 2^k.

[00:21:14] 2, 4, 8, and so on.

[00:21:18] But it turns out that there are also all the intermediate values of n.

[00:21:23] Like these.

[00:21:25] And they are called Chebyshev polynomials.

[00:21:33] Here, I have drawn the Chebyshev polynomials of the second kind.

[00:21:43] How do I think Chebyshev came up with them.

[00:21:48] Of course, he couldn't just call the NMinimize function.

[00:21:57] He didn't have such an opportunity.

[00:22:02] So, when he called NMinimize,

[00:22:05] looked at this polynomial,

[00:22:07] looked at this plot,

[00:22:09] and then took the arccosine,

[00:22:10] that's just my imagination, of course.

[00:22:12] Most likely, it wasn't like that.

[00:22:14] It's not that simple to solve this minimization problem on paper.

[00:22:21] Most likely, another method was used.

[00:22:25] My favorite method.

[00:22:27] When you just engage in random wandering, so to speak.

[00:22:35] Or rather, you develop your thoughts in various interesting directions for you,

[00:22:42] accumulate a base of mathematical facts.

[00:22:45] And then, when you encounter a practical problem, an enlightenment suddenly comes,

[00:22:52] because you have accumulated a base of facts.

[00:22:57] Most likely, such a method worked for Chebyshev,

[00:23:00] and he probably knew because he had accumulated such an interesting fact from life that

[00:23:11] Cos[nx] can be represented as a polynomial of Cos[x].

[00:23:20] Just a moment...

[00:23:22] Let me explain it.

[00:23:24] Look...

[00:23:25] Suppose you know these two expansion formulas for Cos[a + b] and Sin[a + b].

[00:23:33] From these formulas, it immediately follows that you can transform Cos[nx] into a polynomial of Cos[x] and Sin[x].

[00:23:42] But, oh, miracle! When you do this, you find that Sin[x] appears with even powers,

[00:23:51] which means you can apply this formula

[00:23:55] and eventually write this polynomial exclusively in terms of Cos[x].

[00:24:02] I believe this mathematical fact from trigonometry was known to mathematicians 200 years ago

[00:24:11] and an enlightenment occurred.

[00:24:14] Cos[nx], in a sense, by definition - it's a number from -1 to 1.

[00:24:25] And therefore, Cos[nx] as a polynomial of Cos[x] is exactly what we need.

[00:24:32] By the way, it will indeed take values (-1, 1) multiple times,

[00:24:38] the larger n, the more frequently.

[00:24:41] Okay... Now I'll explain this on another example.

[00:24:45] Let's take this Cos[5x],

[00:24:48] then substitute -Sin[x]^n into this expression.

[00:24:57] In short...

[00:24:58] Cos[5x] as a polynomial of Cos[x] is exactly the Chebyshev polynomial.

[00:25:06] What else...

[00:25:14] How to arrive at the recurrence formula for Chebyshev polynomials?

[00:25:20] This is done as follows:

[00:25:24] Perhaps someone knows the formula Cos[a + b] + Cos[a - b],

[00:25:29] but those, who don't, can get it from these two formulas.

[00:25:34] We simply add the first and second equalities

[00:25:39] and get the following expression.

[00:25:42] And from it, it directly follows that

[00:25:50] Chebyshev polynomial [n + 1] plus Chebyshev polynomial [n - 1]

[00:25:59] equals 2 times Chebyshev polynomial of n multiplied by x.

[00:26:06] Well, or it can be written like this.

[00:26:10] The first two values are as follows.

[00:26:15] And from this definition, from these three lines,

[00:26:20] it becomes quite clear that these are indeed polynomials, not some other functions.

[00:26:27] In addition, from this recurrence formula, you can get the generating function for Chebyshev polynomials.

[00:26:35] Here's how it's defined.

[00:26:37] You need to do this once, and then you will understand

[00:26:41] how to get the generating function from the recurrence formula.

[00:26:52] We take, according to this recurrence formula,

[00:26:57] the generating function of x, t,

[00:27:01] minus 2tx,

[00:27:08] and plus (t^2) G[x, t].

[00:27:13] Let's calculate this expression.

[00:27:16] Here's what it equals.

[00:27:18] Here I just rewrote it.

[00:27:21] Next, we put t here,

[00:27:24] and we get t^n+1.

[00:27:27] We put this t^2 here.

[00:27:29] We get t^n+2.

[00:27:33] Next, we perform a renumbering.

[00:27:37] Here we sum from 1

[00:27:39] and no longer write n + 1 here, but just n.

[00:27:47] And here we write, accordingly, n - 1.

[00:27:50] And here we write t^n, but sum from 2,

[00:27:54] and here n - 2.

[00:27:58] Next, we combine these three sums into one sum and take t^n out of the brackets.

[00:28:10] However, from the first sum, only the first two terms remain,

[00:28:17] here they are,

[00:28:19] and from the second sum, only one term remains,

[00:28:22] here it is.

[00:28:25] This sum is equal to zero simply because

[00:28:30] this expression is equal to zero.

[00:28:32] This is the same recurrence formula, just written

[00:28:37] like this.

[00:28:40] With a minus sign and it still equals zero.

[00:28:47] Therefore, what we originally calculated,

[00:28:53] is equal to just this expression.

[00:28:56] That is, this

[00:28:58] equals this.

[00:29:00] So, we have got the answer.

[00:29:02] Let's check that everything is fine.

[00:29:07] Here we go...

[00:29:10] In this way, Chebyshev polynomials are gotten.

[00:29:14] With t^n, it turns out to be the Chebyshev polynomial of degree n.

[00:29:23] And this polynomial is a solution to the minmax problem

[00:29:30] with an accuracy up to the coefficient.

[00:29:32] It is a solution to this problem.

[00:29:36] Okay...

[00:29:39] Today, I also want to remind you about Bernoulli polynomials and draw them.

[00:29:44] The thing is that they, in a sense, are also equioscillating.

[00:29:50] For example, the 15th Bernoulli polynomial.

[00:29:56] See?

[00:29:58] Here the nodes are evenly spaced,

[00:30:02] but the number of oscillations is small, less than 15.

[00:30:09] Here is the 16th Bernoulli polynomial,

[00:30:12] and you can see that it's not quite Equioscillating.

[00:30:14] Look at this extremum

[00:30:16] and this one, they're kind of strange, extreme points, they have different values.

[00:30:21] Here's the 17th.

[00:30:25] Here's the 18th.

[00:30:29] Look how interesting.

[00:30:30] It's as if the Bernoulli polynomials try to fit the sine wave,

[00:30:34] but at some point, they deviate and go into a power dependence.

[00:30:40] That's really the case.

[00:30:43] Indeed, the Bernoulli polynomials, in a sense, try to approximate the sine wave

[00:30:50] as best as possible,

[00:30:52] and with each number n, they approximate this sine wave better and better,

[00:30:58] and over a larger interval.

[00:31:02] Let's draw

[00:31:05] here several Bernoulli polynomials,

[00:31:08] only we'll cleverly normalize them...

[00:31:10] Don't pay attention, this normalization doesn't have any deep meaning.

[00:31:15] ...and let's also multiply them by 1 and -1 to see

[00:31:19] these two families explicitly.

[00:31:24] Even and odd Bernoulli polynomials.

[00:31:28] And you can see that the lower-degree one (green here) deviates earlier,

[00:31:34] while the higher the degree, the later the deviation to something different from a sine wave.

[00:31:45] The higher the polynomial number, the farther it goes along the sine wave to the left and right.

[00:31:56] Alright... what else I want to show here...

[00:32:04] Example of a 25th-degree polynomial.

[00:32:07] Without normalization, its extrema oscillate between (-350000, 350000).

[00:32:20] That is, the magnitude of the oscillations increases.

[00:32:25] But what I want to draw attention to.

[00:32:30] Let's take the 15th-degree polynomial

[00:32:37] and see where the roots of the derivative

[00:32:44] of this polynomial are.

[00:32:45] In other words, find the x-values for extreme points.

[00:32:52] Here are their values.

[00:32:54] -1.22213, 0.74999

[00:33:00] Let's calculate the intervals between these roots.

[00:33:04] When you have a list of numbers and want to calculate the differences between neighboring elements, use ListConvolve.

[00:33:13] The difference between this root and this one is 0.472...

[00:33:18] Between this one and this one, it's something very close to 0.5

[00:33:25] There you go...

[00:33:26] You can see that the extrema are not strictly spaced at 0.5

[00:33:39] And the values of the extrema themselves are also not perfectly equal modulo.

[00:33:47] See?

[00:33:50] Even between this value and this one, there are differences in some distant signs.

[00:34:02] This can be shown by plotting a small piece of the plane x/y.

[00:34:10] So...

[00:34:14] Yes, here's another interesting picture.

[00:34:16] I draw the Bernoulli polynomial in blue,

[00:34:22] and on top of it, I'm plotting the cosine function.

[00:34:28] Look...

[00:34:30] See?

[00:34:31] The Bernoulli polynomials try to be equal to the cosine,

[00:34:35] but at some point, they deviate and go to infinity.

[00:34:39] This is exclusively for even numbers.

[00:34:43] A very interesting property of the Bernoulli polynomials that I hadn't heard of.

[00:34:49] I wonder if any of you know about this property.

[00:34:55] Has it been studied anywhere?

[00:34:58] The difference between the Chebyshev polynomial and the cosine is quite small.

[00:35:06] See? 10^-7 for the 24th-degree polynomial.

[00:35:15] And this difference decreases significantly with the growth of n.

[00:35:20] Such an amazing property.

[00:35:23] The Bernoulli polynomials are almost Equioscillating,

[00:35:28] and if you want to approximate a function on a uniform grid,

[00:35:33] then you should use Bernoulli polynomials,

[00:35:36] but, of course, you'll have to take higher degrees than the number of points you have.

[00:35:47] Here, I've drawn a cool picture too.

[00:35:49] These are the roots of the Bernoulli polynomial on the complex plane.

[00:36:01] I've already mentioned, that the Bernoulli polynomials have fewer oscillations

[00:36:10] than their degree.

[00:36:12] Why? Because some of their roots

[00:36:17] have non-zero imaginary parts.

[00:36:21] And here's how these roots are distributed.

[00:36:24] That is the idea that you need to place more roots at the edge.

[00:36:29] The Bernoulli polynomials are realized as follows:

[00:36:31] they placed them at the edge, but in the complex plane,

[00:36:38] and in the middle, they still made Equidistance, approximately the same distance between the roots.

[00:36:52] And if you remove one of these roots,

[00:36:58] you'll get this wonderful property again, that

[00:37:04] at this point

[00:37:09] the value of the Bernoulli polynomial is greater than anywhere else on this interval.

[00:37:16] But there's a certain unpleasantness here.

[00:37:21] There is no reduction of the ratio of the modulus value at this point

[00:37:26] and the modulus at all other points on the interval.

[00:37:33] And also, this unusual elongation of the interval itself.

[00:37:37] It's not the interval (-1, 1),

[00:37:39] but a gradually increasing interval.

[00:37:44] And one more thing I forgot to mention.

[00:37:48] The fact that there is a problem of finding a polynomial for which the maximum value of the modulus is minimal on the interval.

[00:37:58] And there's a problem of making a polynomial that has the same extreme points.

[00:38:09] And it turns out

[00:38:13] this extreme polynomial has the Equioscillation property.

[00:38:21] How to prove this theorem? Equioscillation theorem.

[00:38:25] I don't claim to have a completely rigorous proof.

[00:38:29] The idea is as follows... by contradiction:

[00:38:32] let's assume we have a polynomial that is a solution to this problem.

[00:38:38] And let's assume it's not Equioscillating.

[00:38:42] Let's say it has an extreme point whose magnitude is greater than all the others, for example.

[00:38:49] If there are several, that's a complex case. It needs to be considered separately.

[00:38:52] But let's say there's one outstanding extreme point, a maximum,

[00:38:57] that is larger in magnitude than all other maxima.

[00:39:01] Then we can do the following:

[00:39:05] let's take, say, a 13th-degree polynomial and we have 13 coefficients.

[00:39:11] More precisely, 12, because it's a monic polynomial.

[00:39:14] And let's consider this 12-dimensional space of coefficients.

[00:39:20] And let's consider a small neighborhood around the current point,

[00:39:25] around the values of these coefficients gotten by solving this problem.

[00:39:31] And let's take such a small vicinity, a 12-dimensional sphere, its interior,

[00:39:38] so that within this sphere, this property is not violated,

[00:39:41] and our max maximum is still greater than all other maxima.

[00:39:46] Let's take such a small sphere that this property holds.

[00:39:51] Next.

[00:39:52] Note that at our extreme node,

[00:40:00] the values of the polynomial are just a linear function of the coefficients.

[00:40:06] Of these 12 coefficients.

[00:40:09] This means that in our 12-dimensional sphere, there is a direction

[00:40:13] in which we can reduce the value of this maximum.

[00:40:20] Let's move to this point on the sphere,

[00:40:26] where the maximum is reduced.

[00:40:30] Then we get an answer that better solves the problem of minimizing the maximum.

[00:40:42] And we get a contradiction.

[00:40:44] So, our original polynomial is apparently not a solution to our problem,

[00:40:50] and we assumed it was.

[00:40:53] Therefore, for polynomials,

[00:40:57] which are solutions to this problem,

[00:41:01] there cannot be a situation where the extremes by modulus have different values.

[00:41:09] This is not a rigorous proof.

[00:41:13] Its lack of rigor is due to the fact that

[00:41:17] while I managed to reduce the value of the maximum at the node,

[00:41:20] there's no guarantee that a little to the right, a new maximum won't appear, even larger.

[00:41:26] And I didn't consider the case where there are several maximums of the same magnitude.

[00:41:38] But these cases can be carefully considered.

[00:41:41] It's better to just read Wikipedia and find out how this theorem is proved.

[00:41:46] That's all for today. Bye, everyone!
