# 15. Формула Эйлера-Маклорена и ζ(z) функция (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [9hUfPCZF1sA](https://www.youtube.com/watch?v=9hUfPCZF1sA). Получено: 2026-10-08T17:42:51+01:00.

[00:00:01] Hello everyone! Welcome to the channel "Mathematical Experiments."

[00:00:05] I'm Artem Vorozhtsov.

[00:00:07] And today I want to continue the topic of the formula: the sum of the s-th powers of the first "x" natural numbers.

[00:00:16] The thing is, I forgot to mention one important thing.

[00:00:19] The Euler-Maclaurin formula.

[00:00:22] Well, not just one thing, I forgot to mention many important things.

[00:00:25] In particular, in that video, I forgot to mention the actual answer.

[00:00:30] What the Bernoulli polynomials look like when written explicitly, in the form of a formula.

[00:00:37] Also, today I want to show you some tricks.

[00:00:42] Today's video has two stars,

[00:00:46] where I will cover elements of advanced math.

[00:00:51] These are tricks that you won't often find in textbooks, but they are mentioned there.

[00:00:59] Inevitably in proper textbooks.

[00:01:03] You won't find them often in textbooks because they are not related to proving formulas.

[00:01:10] They are related to the process of finding answers.

[00:01:15] And they are, let's say, not entirely fair.

[00:01:19] Sneaky.

[00:01:20] To strictly justify them, you need to write a lot of words,

[00:01:24] but textbooks, you know, don't have that much space.

[00:01:29] And our intermediate goal will be the formula 1/√n. The sum up to x.

[00:01:39] I will need the Taylor series formula for the exponential function in this video.

[00:01:46] Here it is.

[00:01:47] I covered it in my previous video.

[00:01:50] About how this series of basic functions (x^n)/n! has this remarkable property

[00:01:59] that their derivatives give the same series.

[00:02:04] Alright.

[00:02:05] So, let's fill in the gap from the previous video and write out the formula.

[00:02:12] Here it is.

[00:02:15] The resulting polynomials have the following formula.

[00:02:18] These polynomials are equal to the sum of the s-th powers of the first x natural numbers.

[00:02:31] These polynomials include the first term,

[00:02:36] which many recognize as an integral, those who studied calculus,

[00:02:40] and the second part, the sum over k of binomial coefficients,

[00:02:48] multiplied by certain constants Zeta[-k].

[00:02:54] Let's just call them constants.

[00:02:55] Magical constants, numbered by the natural number k.

[00:03:01] And these constants appear for various values of s.

[00:03:07] For 1, 2, and 3, the same constants Zeta[-k] appear.

[00:03:12] We simply discovered them, and we still don't understand the values of the zeta function.

[00:03:17] We haven't proven it.

[00:03:19] And by the way, maybe today we will finally gain some intuition,

[00:03:26] that most likely it is the analytic continuation of some function, which I will define today.

[00:03:36] But not a proof, just intuition.

[00:03:38] We don't have proofs on our channel, as you know, as you have probably noticed.

[00:03:45] Yes. In fact, the formula we obtained sums up to s-1.

[00:03:52] But here, we really want to extend this sum up to s.

[00:03:57] It's not so scary to add the last term for k = s,

[00:04:01] because that term is the constant term.

[00:04:05] When s = k, we get x^0.

[00:04:09] Which is just some number.

[00:04:11] Let's see...

[00:04:14] Slap!

[00:04:16] Here, for example, Hr[x, 4].

[00:04:22] This is what the sum of the fourth powers of the natural numbers from 1 to x looks like. This is the result.

[00:04:33] Let's write down these magical coefficients,

[00:04:36] which are hidden in the coefficients of all these Bernoulli polynomials.

[00:04:42] They start with -1/2, -1/12,

[00:04:45] and then there are zeros every other number,

[00:04:50] and strange, mysterious numbers.

[00:04:55] The formula for the sum of the s-th powers of the first x natural numbers

[00:04:59] in Mathematica is known as HarmonicNumber.

[00:05:12] But you see, there is a discrepancy for odd HR[x, 5],

[00:05:17] because I added this constant term that is actually absent.

[00:05:22] Well, indeed, when you sum up the s-th powers of the natural numbers where x = 0, it should be 0.

[00:05:31] But mine is not 0.

[00:05:33] Well, you understand, it's not a big deal.

[00:05:35] The main thing is that this polynomial of mine,

[00:05:40] when x is increased by 1, x^s is added to it.

[00:05:52] The Bernoulli polynomials defined in Mathematica,

[00:05:57] how are they different from the polynomial HR that I defined?

[00:06:06] Stop... Let me input the number 6.

[00:06:12] First, they need to be divided by "s". By what I call "s".

[00:06:20] Second, we need to take a higher power.

[00:06:23] I have 5, while Bernoulli has 6.

[00:06:27] The arguments are swapped, and there's also a difference in the sign here.

[00:06:35] That's not so important.

[00:06:36] Simply put, Bernoulli polynomials sum the natural numbers up to x - 1, not up to x. That's the only difference.

[00:06:47] What's important here?

[00:06:48] The main thing is that the difference between my polynomials for x and x-1 gives x^5,

[00:06:55] while for Bernoulli, the same thing gives (x-1)^5.

[00:06:59] That's the main property of the polynomials we were looking for.

[00:07:05] And of course, for this property, the constant term is simply not important.

[00:07:11] Moving on...

[00:07:14] This formula,

[00:07:16] that the difference of two HR polynomials is simply the sum of the s-th powers of natural numbers from a+1 to b.

[00:07:26] Very reminiscent of the Leibniz formula.

[00:07:30] Reminiscent only to those who have studied the Leibniz formula.

[00:07:35] So... It's a direct analogy, as you understand.

[00:07:41] Except here, it's not integration, but discrete integration.

[00:07:45] Essentially, it's also an area, but the area of columns, not the area under a smooth curve.

[00:07:53] I will show you this visualization with the columns.

[00:07:58] Let's go back a bit now and for those who missed it, let's show how the HR formula was derived.

[00:08:09] It wasn't derived, as always.

[00:08:12] It was discovered.

[00:08:13] We don't derive, we don't prove, we just suddenly discover some beautiful formula.

[00:08:21] It all starts innocently.

[00:08:23] We write down Pascal's Triangle in this form.

[00:08:26] We move this leading term x^s to the left.

[00:08:32] Here are the first rows of Pascal's Triangle.

[00:08:36] And let's denote this difference as yₖ[x].

[00:08:45] It's unclear how this idea came to mind,

[00:08:54] but forgive me for that.

[00:08:55] In fact, you can reach this idea independently. I won't focus on that.

[00:09:02] It's not some kind of magic.

[00:09:03] When a person thinks about the sum of k-th powers,

[00:09:06] this idea appears in their mind at some point.

[00:09:12] You just have to think, think, think for a few weeks, and this idea will come to your mind.

[00:09:19] It could have come up, but it's too late now.

[00:09:21] Now you already have the answer, and the experiment would be unfair.

[00:09:26] So, the idea arises:

[00:09:29] to write down Pascal's Triangle

[00:09:31] and then try to express x^k in terms of y's.

[00:09:40] The first answers are given easily.

[00:09:43] x^0 is y1.

[00:09:45] And x1,

[00:09:47] which is x^1,

[00:09:49] is expressed in terms of y2 and 1,

[00:09:52] and 1 is y1.

[00:09:57] It gets harder from here.

[00:10:01] What do we need to do to obtain the formula for x^2?

[00:10:08] We need to take the third equation,

[00:10:14] multiply it by 2, and subtract 3 times the second equation from it.

[00:10:19] Then these 3x and 2x will cancel out.

[00:10:25] Then we need to determine the constant term and eliminate it using the third term.

[00:10:33] Here's what we get.

[00:10:35] Pause and think.

[00:10:37] Amazingly, this expression is the polynomial HR of x-1.

[00:10:47] Moving on.

[00:10:50] Now let's take the 4th rows of Pascal's Triangle

[00:10:55] and do the same thing for x^3.

[00:10:59] What do we need to do to obtain x^3?

[00:11:02] We need to subtract 2 times the penultimate equation from the last equation.

[00:11:08] Then these 6x^2 and 3x^2 will cancel out.

[00:11:11] Well, then you'll see x's and constant terms.

[00:11:14] The constant terms actually turn out to be zero.

[00:11:19] And here, y1 is absent.

[00:11:22] Alright.

[00:11:23] Amazingly, this coincides with HR for s = 3.

[00:11:29] Except for that additional constant term, which is added for the beauty of the final formula.

[00:11:39] Well, why did this work? The answer is quite simple.

[00:11:43] Here, for example, we obtained this equality.

[00:11:48] And now we sum this equality over x from 0 to n.

[00:11:56] We sum it.

[00:11:58] On the left, we get the desired result...

[00:12:02] More precisely, we obtain the formula for which we want to find the answer.

[00:12:07] The sum of squares of the first x natural numbers.

[00:12:11] And here, such sums are obtained.

[00:12:14] These sums are interesting because they contain terms that cancel out when you sum them.

[00:12:22] Think about this formula

[00:12:25] and understand that when you sum it, only ((1+n)^1)/6 remains.

[00:12:34] Well, the same thing here.

[00:12:37] This is one way to obtain the formula for the sum of squares of the first n natural numbers.

[00:12:45] And for those who are familiar with matrices, everything looks somewhat easier.

[00:12:54] The first n rows of Pascal's Triangle is expressed as a single, but matrix equation.

[00:13:03] And all we need to do is invert this matrix.

[00:13:07] We calculate the inverse of this matrix, examine it,

[00:13:11] and with surprise, we discover zeros on these diagonals.

[00:13:17] We call this the discovered pattern.

[00:13:26] If we calculate this matrix, choosing a larger size n,

[00:13:34] we see that not only zeros become visible to us,

[00:13:40] but the non-zero diagonals are also structured in a particular way.

[00:13:45] This number 691, which mathematicians know by heart,

[00:13:53] suggests to us that the numbers on the diagonals consist of one particular number multiplied by something.

[00:14:05] And how can we discover what that something is?

[00:14:10] Well, it's very simple.

[00:14:11] Let's divide the entire diagonal by 1/30.

[00:14:15] Let's divide the entire diagonal by 5/66 and so on...

[00:14:20] These are the things we do.

[00:14:22] Binomial coefficients are discovered there.

[00:14:25] And then after dividing by binomial coefficients, we understand how our matrix is structured.

[00:14:36] Let me skip some steps here.

[00:14:38] If you don't understand, I refer you to my video.

[00:14:42] In short, we see that the coefficients in this inverse matrix consist of the product

[00:14:50] of binomial coefficients

[00:14:52] and a number that is written here.

[00:14:58] Each diagonal consists of a number

[00:15:02] which we denote as Zeta[-k],

[00:15:04] and a binomial coefficient.

[00:15:07] And this part simply corresponds to the main diagonal of this matrix.

[00:15:17] Now we have an explicit formula.

[00:15:20] Yes, here we sum up to s-1, but I always add just s everywhere.

[00:15:30] Let's take a look at this formula.

[00:15:36] Binomial coefficient [s, k] multiplied by x^(s-k).

[00:15:43] Oh, how I wish there was something raised to the power of k here.

[00:15:47] Then it would be exactly the formula of Newton's binomial.

[00:15:54] Let's allow ourselves to do that and replace Zeta[-k] with z^k.

[00:16:02] Then this expression becomes the following.

[00:16:10] z is not a number. It's just a little hack, a trick.

[00:16:17] Let's allow ourselves to replace the sequence Zeta[-k] with z^k.

[00:16:24] To see the structure of the formula.

[00:16:29] Of course, such z does not exist.

[00:16:32] It's impossible to imagine such z that would satisfy these equations.

[00:16:39] But nevertheless, let's take a closer look at the result.

[00:16:45] And we'll see something interesting here,

[00:16:49] that this

[00:16:52] is simply the integral of this.

[00:16:56] And let's allow ourselves to generalize this equation

[00:17:01] to this equation.

[00:17:05] As if here, instead of t^s, you could take any function of t.

[00:17:13] This idea naturally arises for those who know that functions can be expanded into Taylor series.

[00:17:22] If you obtained something for t^s,

[00:17:28] then perhaps it is true for any other function that can be expanded into a sum of powers of t.

[00:17:38] But here we need to go back to the fact that z is not just some number, but a tricky thing.

[00:17:48] Here, we take that very Taylor series and write z^k through Zeta[-k].

[00:17:56] This trick, this cleverness, allowed us to quickly go from Pascal's Triangle and the formula for s-powers

[00:18:07] to the Euler-Maclaurin formula.

[00:18:13] What is written here is an incorrect formula.

[00:18:17] You have to forgive me for now.

[00:18:22] We will reach the correct formula soon.

[00:18:27] But for now, we simply hope that it is true.

[00:18:31] And we wonder: what then?

[00:18:36] Let's assume it's true.

[00:18:38] Then it states the following:

[00:18:42] that the sum of the function f at different points k

[00:18:49] can be expressed through an integral,

[00:18:52] and the values of different derivatives of the function f, but at one point, as if this knowledge about the function at one point,

[00:19:02] can determine the sum over this function at different points k.

[00:19:09] As if.

[00:19:13] Let's rewrite it in another way.

[00:19:20] The Euler-Maclaurin formula talks about the difference between the sum (discrete integral) and the actual integral.

[00:19:32] This difference is determined by the values of the derivatives at one point "x".

[00:19:41] Oops.. there's a little mistake here. We integrate not up to 1, but up to x, of course.

[00:19:50] It's strange that there's no dependence on the values of derivatives at point 0.

[00:19:58] What is the difference between "0" and "x" in this formula?

[00:20:02] Seemingly nothing.

[00:20:04] And that's a good discovering.

[00:20:07] In fact, this formula is not correct and needs to be generalized. We'll understand how in a moment.

[00:20:13] Let me more  illustrate this difference.

[00:20:21] Let's take √x as the function f[x].

[00:20:29] Then this sum - it's the sum of these columns.

[00:20:38] And this integral - it's the area under the blue smooth curve.

[00:20:46] There's a subtle point: from which number do we sum to which.

[00:20:52] And accordingly, it turns out that the sum is either the columns above the curve,

[00:21:00] or the columns that fit inside the curve.

[00:21:04] Let's not delve into that for now,

[00:21:07] but it's as if this formula, it's a formula for the areas

[00:21:13] of these triangles.

[00:21:14] Either yellow triangles or gray triangles.

[00:21:22] Curvilinear triangles. They have one curved side.

[00:21:27] By the way, it's clear that the sum of yellow and gray triangles is a simple thing.

[00:21:32] Because we can just shift these squares entirely to the left,

[00:21:36] and then the sum of all triangles, both gray and yellow,

[00:21:41] is simply: 1 multiplied by the height of the column, which is f[x].

[00:21:49] So, if you know the sum of the yellow ones, you know the sum of the gray ones.

[00:21:53] Alright.

[00:21:56] So, let's write down the formula (which we think is true, but actually it's not) twice,

[00:22:05] when "x" equals "a" and when "x" equals "b",

[00:22:07] then subtract one from the other and here's what we'll get.

[00:22:12] The sum from a+1 to b equals this difference.

[00:22:18] And this formula already looks more symmetric.

[00:22:22] The points a and b are symmetrically included in this formula.

[00:22:29] And now it's clear that the sum of the areas of the triangles depends on the derivatives at point "a" and the derivatives at point "b".

[00:22:41] Okay.

[00:22:45] If we look at Wikipedia, we'll find the following formula:

[00:22:50] "S" is the sum, "I" is the integral.

[00:22:53] And instead of Zeta[-k], there are Bernoulli numbers.

[00:23:01] The sum there is not to infinity, but to "p", and that's correct. Infinity here is a mistake.

[00:23:07] And there's a certain remainder term here.

[00:23:11] Here I want to show that Zeta[-k] is simply Bernoulli numbers divided by k+1 with a minus sign.

[00:23:21] Furthermore, if you look into the "Euler-Maclaurin formula" section on Wikipedia,

[00:23:26] you'll find another formula.

[00:23:29] Here, the summation over "k", where "k" is multiplied by 2 inside the formula.

[00:23:35] Not surprisingly, because there's Zeta[-k] there.

[00:23:40] You see, those are numbers that are equal to zero. Every other number is equal to zero, except the first one.

[00:23:47] And the first term is taken out of the sum,

[00:23:51] and then, roughly speaking, you can only take the odd values of "k" in this formula.

[00:24:02] I actually prefer this notation of mine,

[00:24:05] where, on the contrary, this term is inside the sum.

[00:24:11] Moreover, I really want to put this term inside the formula.

[00:24:17] And I'll do it now.

[00:24:22] This "F" is the antiderivative of "f".

[00:24:27] What is an antiderivative?

[00:24:30] It's the k-th derivative, where k is equal to -1.

[00:24:36] Let's write the summation from k = -1

[00:24:40] and remove this term.

[00:24:43] This is another trick of the advanced math.

[00:24:48] What will happen when we do this?

[00:24:53] Here's what we'll get:

[00:24:56] we want Zeta[-k] (where k = -1), divided by k!, to be equal to -1.

[00:25:08] Here awaits us an unpleasantness.

[00:25:13] Zeta[1] and (-1)! are equal to infinity.

[00:25:19] But what's interesting is that if we let "s" approach -1 for this ratio,

[00:25:26] we'll get a limit equal to -1.

[00:25:36] We need exactly -1, not 1.

[00:25:39] Because there's a minus sign in front of the sum here.

[00:25:45] And this limit gives us a right to write this formula

[00:25:53] with this caveat,

[00:25:55] that for k = -1, this ratio should be considered equal to -1.

[00:26:03] So, as some joke, it turned into the Euler-Maclaurin formula.

[00:26:10] And all of this can be turned into a rigorous proof using phrases such as

[00:26:19] the sum and the integral are linear operators,

[00:26:23] the summation signs can be interchanged,

[00:26:26] and that transforming Zeta[-k] into z^k was only temporary in our reasoning and can be avoided.

[00:26:36] Here, I wrote these thoughts as equalities.

[00:26:46] Moving on.

[00:26:48] This formula,

[00:26:50] where the sum goes to infinity,

[00:26:54] actually doesn't work.

[00:26:56] It doesn't work even if you replace infinity with some finite value for the case

[00:27:03] where the function f has some peculiarity, an unpleasantness, at point "a".

[00:27:15] To avoid this unpleasantness at point "a" equal to zero for some functions f[t],

[00:27:23] we will apply the following trick.

[00:27:25] Here we have a graph of the function 1/√t,

[00:27:29] or more precisely, not the function itself, but these steps.

[00:27:34] And the sum of the reciprocals of the first n natural numbers is the blue area.

[00:27:42] So, the blue area can be calculated as the entire area under all the bars minus the yellow area.

[00:27:50] This simple idea allows us to write the formula even for the case when s is equal to -1/2,

[00:27:59] that is, when you sum the reciprocals of square roots.

[00:28:04] And that's the whole idea.

[00:28:06] But let's live in the world of the problem of summing the reciprocals of cubed natural numbers for now.

[00:28:14] It will be easier for us to start with.

[00:28:17] So, let's dwell in this problem for now.

[00:28:20] When we sum the reciprocals of cubed numbers, the area turns out to be finite. The total area.

[00:28:29] But when we choose 1/√n, the green area and the area under all the bars become infinite.

[00:28:40] Those who know calculus know this fact.

[00:28:47] Let's not think about this unpleasantness for now.

[00:28:50] Let's write that the blue area is the blue plus yellow minus yellow.

[00:28:59] And another thing we'll understand...

[00:29:02] We'll understand that the antiderivative for 1/(t^3) is this thing.

[00:29:09] And using the antiderivative, we can calculate the entire area under the smooth curve.

[00:29:16] And we can also calculate the area of all the triangles,

[00:29:24] these ones here,

[00:29:26] as the addition to the green area.

[00:29:32] We know the green area when the function f[t] is 1/(t^3).

[00:29:38] But how do we calculate the sum of the areas of all the triangles, both blue and yellow?

[00:29:45] The answer is as follows:

[00:29:47] like this.

[00:29:50] What is a triangle?

[00:29:52] It's the area of a bar minus the green area within that bar.

[00:30:06] It is computed as the difference between the antiderivatives at the points t+1 and t.

[00:30:14] This is the area of the triangles for other values of s.

[00:30:20] Let's define it.

[00:30:23] The entire green area under the smooth curve for s = 3.

[00:30:28] It's written in another way here.

[00:30:32] Next, I finally want to define the function Zeta[s].

[00:30:37] It is the sum of the reciprocals of the s-th powers.

[00:30:41] Let's define the function Zeta[s] in this way when "s" is greater than one,

[00:30:49] then the sum converges.

[00:30:54] And then the area of all the triangles, Mathematica knows,

[00:31:00] is equal to the area of all the bars minus the area under the smooth curve.

[00:31:09] I still want to write the areas of the triangles and work with the areas of the triangles.

[00:31:15] So, what do we do...

[00:31:17] We define the function Zeta[s] in this way, where "s" is greater than one.

[00:31:24] And we discover these moments,

[00:31:34] that

[00:31:37] the sum of the triangles is the sum of the bars minus the area under the smooth curve.

[00:31:46] Here again, the sum of the bars minus the area under the smooth curve.

[00:31:51] This is what the area of all the triangles is equal to.

[00:31:59] Zeta[4] - the sum of the reciprocals of the fourth powers, Mathematica knows.

[00:32:04] The sum of the fifth powers is unknown to Mathematica.

[00:32:08] In general, here's what we have, what Mathematica knows.

[00:32:13] Starting from the second power, it says there are numbers.

[00:32:18] And for even cases, it even knows the sum of the bars.

[00:32:25] For the case when we take the hyperbola,

[00:32:29] the sum of the bars is equal to this sum.

[00:32:33] And Mathematica writes that it diverges.

[00:32:39] So... now it will become clear what I want to do.

[00:32:44] Here is this moment!

[00:32:46] What I want to do.

[00:32:48] I want to write down this formula:

[00:32:51] Zeta[s], the sum of the bars, is equal to the sum of the triangles plus the area under the smooth curve.

[00:33:02] Is idea clear?

[00:33:04] Here's what I couldn't tell you for so long.

[00:33:09] I want to write it like this.

[00:33:12] And here's the catch:

[00:33:16] if I take this sum (the sum of reciprocals),

[00:33:21] Mathematica says: I don't understand.

[00:33:27] Although it says this sum is the Zeta function,

[00:33:32] for s = 1/2, it says: the sum diverges.

[00:33:39] But if we take Zeta2[1/2]...

[00:33:46] So... we need to define it.. I'm forgetting to do that..

[00:33:51] What does it say?

[00:33:54] It says there is an answer.

[00:33:58] It's not quite clear what's happening here.

[00:34:01] It simply says that this sum converges.

[00:34:09] The sum of areas of triangles is a converging thing.

[00:34:17] And this formula, which gave valid answers for s > 1,

[00:34:25] we simply extended it for the case of s = 1/2.

[00:34:31] So, I showed you one formula that was true, obvious, and proven for s > 1,

[00:34:40] and then I allowed myself to insert s = 1/2 into it

[00:34:47] and say: before, this was equal to Zeta[s],

[00:34:55] so let this thing be called Zeta[s] now.

[00:34:59] Let it be a series and diverge,

[00:35:04] but before, this formula gave the value of this series,

[00:35:08] so let this thing be a generalization of this analytic function of "s" for the case when s = 1/2.

[00:35:19] Not just 1/2.

[00:35:21] This series (the sum of triangle areas) will converge for s = 1/3, 1/4.

[00:35:30] For different numbers from 0 (greater than 0) to 1. Not just for s > 1.

[00:35:39] That's how it is.

[00:35:41] Zeta2[3] gives the expected answer, Zeta[3].

[00:35:49] And for s = 1/2, it gives some new value,

[00:35:55] which Mathematica knows and it can do it too, and it calls it Zeta[1/2].

[00:36:04] To be continued...
