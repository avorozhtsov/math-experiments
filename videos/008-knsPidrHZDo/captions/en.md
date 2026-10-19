# 8. От треугольника Паскаля до Дзета-функции (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [knsPidrHZDo](https://www.youtube.com/watch?v=knsPidrHZDo). Получено: 2026-10-08T17:43:19+01:00.

[00:00:01] Hello everyone!

[00:00:02] This is the channel "Math experiments".

[00:00:04] Today we have an ambitious task:

[00:00:06] to run a hundred meters from Pascal's triangle to the value of the zeta (ζ) function.

[00:00:12] We will run at a great speed... like Usain Bolt.

[00:00:16] But in truth, we will not run for 10 seconds, because I'm not Usain Bolt.

[00:00:22] And the distance is not 100 meters. It's more like ten kilometers. Look at how much scrolling is needed...

[00:00:28] Well, actually, it's not that much...

[00:00:30] I tried to find the shortest path

[00:00:33] from the simple and understandable Pascal's triangle to the great and incomprehensible zeta (ζ) function.

[00:00:40] Why is it great and incomprehensible?

[00:00:43] There are many interesting videos about the zeta function

[00:00:48] and, of course, you should start with the value of the zeta function at 2.

[00:00:54] Calculating the value of the zeta function at 2 is a separate task.

[00:00:58] Calculating the value of the zeta function at 3 is another task.

[00:01:02] Calculating the zeros of the zeta function is also a serious task.

[00:01:07] Proving that they are located here and there is the greatest task of modern times.

[00:01:11] But I digress...

[00:01:15] The value of the zeta function is defined as follows:

[00:01:19] it is the sum of the reciprocals of the k-th powers.

[00:01:21] This is the value of the zeta function at point k.

[00:01:23] The sum of the reciprocals of the k-th powers of natural numbers.

[00:01:27] Hence, the sum of the reciprocals of the squares is the value of the zeta function at point 2.

[00:01:33] And this value is Pi^2/6.

[00:01:36] This problem, to calculate the sum of inverse squares, is known as the Basel problem.

[00:01:41] Interestingly, it was posed to mathematicians for 45 years.

[00:01:48] For 45 years, people couldn't find what this sum equaled.

[00:01:51] It's amusing to think about this in our days.

[00:01:54] Apparently, in mathematics, as in computer science, there's an acceleration of progress.

[00:01:59] Every year, acceleration increases and speed increases.

[00:02:02] Everything increases, and what happened 100 or 200 years ago seems amusing.

[00:02:13] In general, in those times people didn't know what Fourier transforms were.

[00:02:16] They didn't know enough about the series... How to properly deal with them.

[00:02:22] And they couldn't calculate this sum.

[00:02:26] They had to be tricky about it.

[00:02:29] And there are many interesting videos about how to calculate this sum of inverse squares and get that coveted Pi^2/(6).

[00:02:36] You have to find some connection to the circle, to trigonometric functions, to make Pi^2/(6) appear.

[00:02:45] And I recommend looking at the channel, for example, zetamath.

[00:02:51] It's in English, though...

[00:02:53] If your English isn't good enough to watch lectures in English,

[00:02:57] I recommend installing Yandex Browser, opening YouTube, hovering over the video, and finding the icon with hieroglyphs.

[00:03:03] Click on it and you will get synchronized translation in Russian.

[00:03:07] This is cool. It greatly expands the amount of mathematical educational content

[00:03:14] that you can consume for self-improvement.

[00:03:17] This is really... this is ridiculously cool.

[00:03:19] Well, you can also learn English. That's also an option.

[00:03:24] Today, I'm not talking about the function Zeta[2] = Pi^2/(6),

[00:03:32] but about how we suddenly, completely accidentally, stumble upon the values of the zeta function -1, -2, -3,

[00:03:43] solving some simple problem.

[00:03:45] By doing some simple exercises, summing this series.

[00:03:51] Our task is to find the sum of this finite series of k-th powers of natural numbers.

[00:03:56] Not all of them, but up to the number n.

[00:03:58] In mathematics, by the way, this sum is known as HarmonicNumber[m, -k].

[00:04:07] And...

[00:04:09] Maybe some of you have already thought about it.

[00:04:12] What is Zeta[-2]? This is when k = -2, which means the sum of the squares of all natural numbers.

[00:04:19] This is a very large number, namely - infinity.

[00:04:24] Indeed, it's somewhat incomprehensible until you learn what analytic continuation of a function is.

[00:04:30] But I won't talk about it now either.

[00:04:32] We'll just accidentally stumble upon some numbers that will be called Zeta[-1], Zeta[-2], Zeta[-3]...

[00:04:39] and someday I might be able to tell you more about it.

[00:04:43] And now, let's start again...

[00:04:45] Pascal's triangle. Finally!

[00:04:47] We return to simple and understandable things for us - Pascal's triangle.

[00:04:52] It arises when you expand (a+b)^n.

[00:04:55] Or like here (1+x)^n.

[00:05:00] I want to make a small transformation.

[00:05:02] Let's move this highest power of x^5 to the left.

[00:05:05] Move x^4 to the left.

[00:05:07] This is what we get.

[00:05:10] On the right, we have this truncated Pascal's triangle with the right slope cut off.

[00:05:17] And what I want to do here is...

[00:05:19] I want to take these three equations...

[00:05:26] The arrow means "equals."

[00:05:27] Three equations and name them, give them names a3, a2, a1.

[00:05:34] And I want to sum them with certain coefficients.

[00:05:38] I want only x^2 to remain on the right, and all other terms (constant terms and terms with x) to disappear.

[00:05:46] This is done very simply:

[00:05:47] Take the first equation, multiply by 2. Multiply the second equation by 3.

[00:05:50] And subtract the second equation from the first.

[00:05:52] Here it is written like this: 2a3 - 3a2...

[00:05:57] It turns out that 3x^2 becomes 6x^2,

[00:06:02] and 3x becomes 6x, 2x becomes 6x, they cancel out.

[00:06:06] And we're left with 2 - 3. And we need to eliminate the remaining -1 term. And for this we add a1.

[00:06:16] This is the linear combination of three equations that we're interested in.

[00:06:21] And this is what we get.

[00:06:24] On the right, we get what is written here.

[00:06:29] 6x^2. That's correct!

[00:06:31] Only x^2 remains on the right.

[00:06:33] Let's divide by 6 and this is what we have.

[00:06:38] Of course, you might ask: why to do all this?

[00:06:44] I don't like when viewers don't understand what happens on the screen.

[00:06:45] It is important that all actions that are taken are understood for why they are being done.

[00:06:52] And I had started telling you about some manipulations with three equations for some reason.

[00:07:01] But wait... you'll understand it all soon.

[00:07:05] In short...

[00:07:06] Actually, what I want to do is find the sum of 1^2 + 2^2 + 3^2 ... + n^2

[00:07:14] And there are many ways to obtain this result.

[00:07:20] I'm just telling you one of them.

[00:07:22] Here it is: take Pascal's triangle and do some manipulations to make only x^2 remain on the right.

[00:07:30] And look at what we get afterwards:

[00:07:33] I take the obtained equation, one, and add it to itself by substituting x = 1, 2, 3, 4, 5 ... n

[00:07:42] Then on the right, I'll have the sum of the squares of the first n natural numbers.

[00:07:47] And on the left... What will be on the left?

[00:07:49] You probably guessed already.

[00:07:50] This bracket will be repeated several times for different values of x.

[00:07:58] There. I added this equation to itself four times

[00:08:02] and you can see how the terms cancel out when we sum up this column.

[00:08:06] 1^3 - 0^3

[00:08:08] 2^3 - 1^3

[00:08:09] 3^3 - 2^3

[00:08:11] 4^3 - 3^3

[00:08:12] and when they cancel out, we're left with just (1 + 3)^3

[00:08:17] Similarly here.

[00:08:18] When we sum up these terms with -3,

[00:08:22] we'll just get -3(1+3)^2

[00:08:28] In short, when we add this equation to itself n times... In short, when we add this equation to itself n times...

[00:08:35] n plus 1 times, starting from zero,

[00:08:37] we get the following equation,

[00:08:39] that the sum of the squares of the natural numbers from 0 to n

[00:08:45] equals this quantity.

[00:08:49] Let's expand this expression. This is what it's equal to.

[00:08:54] This is a formula for the sum of the first n squares of natural numbers.

[00:08:59] Remarkably, this sum coincides with the third degree Bernoulli polynomial.

[00:09:05] Well, because Bernoulli polynomials are defined that way.

[00:09:10] More precisely, not quite, but for the number three they coincide completely...

[00:09:19] However, you need to divide by 3.

[00:09:22] For four...

[00:09:24] For four there is some difference.

[00:09:26] Let's see...

[00:09:33] HarmonicNumber for the value (n, -2) is precisely the 3-degree Bernoulli polynomial.

[00:09:39] But let's take a look, for example, if this is true for the sum of fourth powers.

[00:09:43] Mathematics knows what the sum of fourth powers is.

[00:09:48] Is it true that it's the fifth degree Bernoulli polynomial?

[00:09:56] Yes, that's correct.

[00:09:58] Only you have to divide it by k.

[00:10:01] And for the third degree...

[00:10:03] If we sum up the third degree, we get the fourth degree polynomial,

[00:10:08] and the fourth degree Bernoulli polynomial is a different expression.

[00:10:12] It coincides in the leading terms, but differs in the lower ones.

[00:10:17] What is this connected to? It's connected to the fact that Bernoulli polynomials are normalized in a certain way,

[00:10:21] namely, they are normalized so that the integral from 0 to 1 is equal to zero for all Bernoulli polynomials.

[00:10:26] But that's not important. Let's talk later about it.

[00:10:30] Bernoulli polynomials allow us to calculate sums of k-th powers of consecutive natural numbers from one arbitrary number to another.

[00:10:39] This is how it's done.

[00:10:42] Mathematica is great at computing these polynomials.

[00:10:47] You can ask it to factor them.

[00:10:50] Like this, you can compute the roots directly.

[00:10:54] Or you can compute them numerically.

[00:10:56] And our roots turn out to be complex.

[00:11:00] At first we got lucky and all roots were real, although irrational,

[00:11:08] but as n increases, starting from k = 6, we already get complex roots.

[00:11:21] These roots can be visualized...

[00:11:25] like this.

[00:11:28] Let me delete...

[00:11:30] These roots.

[00:11:31] I add two slashes "//" and get a list consisting of two lists.

[00:11:40] The first one is the real parts of the roots.

[00:11:44] The second one is the imaginary parts of the roots.

[00:11:47] Well, we need to do Transpose to get a list of pairs instead of a list of two lists.

[00:11:54] Real coordinate and imaginary coordinate.

[00:11:57] And let's add "//" and ListPlot here.

[00:12:04] "//" in Mathematica language means to compute what's on the left and apply the function described on the right to it.

[00:12:15] We did that here.

[00:12:16] N - means to obtain the numerical value of what's on the left.

[00:12:23] This function that I've constructed by myself.

[00:12:26] In programming, such constructs are known as lambda(λ) expressions.

[00:12:35] Here instead of the hash sign (#) comes everything on the left, and on the left is a list.

[00:12:39] The function "Re" applied to a list becomes a list of "Re" applied to individual components of the list.

[00:12:45] Therefore, what we get is two lists,

[00:12:48] but when we transpose them, we get a list of pairs.

[00:12:52] There we go. We have drawn it! Beauty rules, doesn't it?

[00:12:57] We just need some grid lines.

[00:13:00] I don't like plots without grid lines.

[00:13:06] And of course, we need "Manipulate." Since we're in Mathematica, we might as well run "Manipulate."

[00:13:13] Beauty rules!

[00:13:16] We have got such two forms.

[00:13:21] So there you have it!

[00:13:22] In reality, we've been digressing. We haven't been running straight towards our goal.

[00:13:26] We've been zig-zagging towards the roots of the Bernoulli polynomials.

[00:13:32] So here's our Pascal's Triangle.

[00:13:36] What did we do when we looked for the Bernoulli polynomial of degree three?

[00:13:42] Actually, we took a certain row from some inverse matrix, and now I'll explain what all of this means.

[00:13:53] This Pascal's Triangle, written in this form, can be turned into a matrix.

[00:14:00] An n-by-n matrix.

[00:14:04] Where n here is equal to 10.

[00:14:08] There you have it. This is Pascal's Triangle with its right slope cut off.

[00:14:14] And...

[00:14:16] Another representation is the more traditional one, with round brackets.

[00:14:20] That's how matrices are usually depicted. With big round brackets on either side.

[00:14:27] And this equality...

[00:14:29] Well, not just one equality, but a set of equalities.

[00:14:31] ...can be represented as a single equality.

[00:14:36] Formally as a single equality, the meaning of which is as follows:

[00:14:42] A column matrix equals a square matrix multiplied by a column.

[00:14:48] This is the formal notation for the following:

[00:14:50] We take this column and multiply it element-wise by the first row.

[00:14:58] Just like that.

[00:14:59] 1 goes here

[00:15:00] x goes here

[00:15:01] x^2 goes here.

[00:15:03] And we multiply,

[00:15:06] and then we replace the spaces here with a plus sign and add them up.

[00:15:11] And this should be equal to this value.

[00:15:15] This value is equal to this thing:

[00:15:17] We take this column,

[00:15:22] put it this time on the second row,

[00:15:29] multiply element-wise,

[00:15:31] and then add up, replacing these spaces with a plus sign, and so on.

[00:15:37] That is...

[00:15:39] It's not magic, it's just a formal notation for what is shown above.

[00:15:43] No more than that.

[00:15:44] Just a short way to write what is on top.

[00:15:50] But in addition to being a formal notation, it's also an interesting problem.

[00:15:56] We have this formal notation, and I want to get a formal notation in the other direction.

[00:16:01] I want to represent this column as a certain square matrix multiplied by this column.

[00:16:09] In the other direction. Reverse.

[00:16:11] Here, this column is expressed through this one,

[00:16:13] and I want to go in the other direction.

[00:16:15] This operation is called matrix inversion.

[00:16:19] And what have we done?

[00:16:20] Essentially, we have found the value of this inverse matrix in this row.

[00:16:26] We know that its values are 1/6, -1/2, 1/3.

[00:16:31] Why?

[00:16:32] Because this expression...

[00:16:37] No, not that...

[00:16:40] Because our Bernoulli polynomial is 1/6 before n, -1/2 before n^2, and 1/3 before n^3.

[00:16:53] Let's do...

[00:16:55] matrix inversion.

[00:16:57] For this, Mathematica has the Inverse function, and we got our values of 1/6, -1/2, 1/3.

[00:17:06] So...

[00:17:07] First of all, trust me, you can do the fourth line yourself,

[00:17:12] since we did it for the third line, you can try to find the fourth line yourself and you'll succeed.

[00:17:21] You will need to take not...

[00:17:27] not these three equations, but four.

[00:17:32] And your task will be to find a linear combination of four equations

[00:17:38] and get x^3 on the right.

[00:17:41] At first, you'll understand how to eliminate x^2.

[00:17:44] For this, you need to multiply this by 2...

[00:17:47] and subtract it from this.

[00:17:50] Then you can forget about this equation

[00:17:54] and work on subtracting this equation from that one,

[00:17:56] which resulted here and eliminate the x component.

[00:18:00] Well, and then eliminate the constant term by subtracting the required amount of this equation.

[00:18:05] In short, clear.

[00:18:07] Okay.

[00:18:09] You are capable of taking and calculating this matrix yourself.

[00:18:14] Completely.

[00:18:15] With a bit effort.

[00:18:17] Let's take a closer look at this matrix.

[00:18:21] So, I wanted to make it look beautiful here. I drew faint borders.

[00:18:26] Well, okay...

[00:18:28] Let's see what's drawn here, for example, in the 9th row.

[00:18:36] -1/30, 2/9, -7/15

[00:18:40] These are actually the coefficients of the Bernoulli polynomial divided by 9.

[00:18:46] Alright!

[00:18:48] Here...

[00:18:49] Here I decided to draw more.

[00:18:52] On this picture, you can already look for patterns.

[00:18:56] Let's see who is faster.

[00:18:58] I, for example, can continue this diagonal.

[00:19:03] I can also continue the diagonal with -1/2.

[00:19:06] Further It gets harder...

[00:19:09] We haven't proven that this diagonal equals -1/2, we just discovered it.

[00:19:14] We also discovered that this diagonal consists of zeros.

[00:19:18] And I have a very high confidence that there will also be zeros further, if we continue.

[00:19:27] Not zeros here,

[00:19:28] zeros again,

[00:19:29] not zeros, zeros, and so on.

[00:19:32] I sometimes like to look at complex cases

[00:19:36] and it becomes clear that these diagonals

[00:19:43] are made up of some one number and neighboring numbers differ slightly, just like that.

[00:19:51] What I decided to do here.

[00:19:53] I decided to take each diagonal and divide it by the value with which this diagonal starts.

[00:20:03] But some diagonals actually start with zero but don't continue with zeros, so it's not a problem.

[00:20:07] For example, the diagonal that starts with 1/42, I decided to divide it by 42.

[00:20:11] 1, 2, 3, 4, 5, 6, 7

[00:20:14] Next up is number 1/12. If I divide 1/12 by 42, what do I get?

[00:20:24] So...

[00:20:32] As a result of this division, when I just took the inverse matrix mi - that's m Inverse - and divided it by the value...

[00:20:42] by some value that is in the first column of this matrix.

[00:20:44] This first column of this matrix, it's... there's a one written there.

[00:20:49] And then, to figure out from (i, j) which element the diagonal, that passes through the (i, j) point, rests against,

[00:21:00] I have to do this manipulation.

[00:21:03] Basically, I found the value k for each number,

[00:21:10] the ordinal number in the first column, and this expression,

[00:21:16] and divided it by that.

[00:21:20] And this is what I got.

[00:21:22] I got Bi Definitioon in the first column. Zeros and ones.

[00:21:26] And then things got a lot better.

[00:21:31] -1/2 turned into ones.

[00:21:34] Okay.

[00:21:37] Here we have 1/8, and here we have 2, 4, 2.

[00:21:40] Here we have 1/9, and here we have a three.

[00:21:43] Here we have 1/10, and here we have a two in the denominator.

[00:21:49] Here we have 1/11, and there's nothing in the denominator.

[00:21:52] Here we have 1/12, and there are 2, 4, 2 in the denominator.

[00:21:58] 1/13 and there's nothing in the denominator.

[00:22:03] Well, we can try multiplying by i.

[00:22:07] There we go. And now we have some whole numbers.

[00:22:12] Yes.

[00:22:15] So, who recognizes these numbers?

[00:22:19] We encounter these numbers in Pascal's Triangle:

[00:22:21] 3, 6, 10, 15, 21, 28.

[00:22:25] 3, 6, 10, 15, 21, 28.

[00:22:28] m is the original matrix that contains Pascal's Triangle.

[00:22:31] So.

[00:22:31] We have discovered that after inverting the triangular matrix,

[00:22:41] which is a truncated Pascal's Triangle,

[00:22:45] we obtain a matrix in which these numbers from Pascal's Triangle are also hidden, but they are hidden there cleverly.

[00:22:55] But they are there.

[00:22:57] What we will do is take these binomial coefficients that are hidden there and divide by them,

[00:23:10] to clean them up.

[00:23:12] They've popped up here. Some of them are punctured with zeros.

[00:23:16] We will divide by them, here I divided by the value in the first column,

[00:23:22] but now I want to divide by the binomial coefficients that I see here.

[00:23:28] Each i-th, j-th element is to be divided by the binomial coefficient that I see here.

[00:23:33] And to see what will left.

[00:23:35] And conversely, now that I've divided by the binomial coefficients,

[00:23:40] I see identical numbers on the diagonals.

[00:23:43] Absolutely identical numbers.

[00:23:47] Well, now we need to draw this answer.

[00:23:56] Here are the values of the zeta function at 10 points.

[00:24:00] -1, -2, and so on.

[00:24:05] And, lo and behold!

[00:24:08] They match!

[00:24:13] Only the signs differ.

[00:24:17] But that's exactly what we need.

[00:24:22] So we've just discovered some patterns and some interesting numbers.

[00:24:31] And I've just told you the answer: these numbers are the values of the zeta function.

[00:24:39] In the next videos, I'll try to prove that these are the values of the zeta function at negative points.

[00:24:49] But for that, we'll have to go a long way.

[00:24:53] I recommend checking out the links I've attached to the video from the channel zetamath.

[00:24:59] There, it's very well explained about analytic continuation

[00:25:03] and about how to use almost school-level methods...

[00:25:06] ...well, not exactly school-level methods...

[00:25:08] ... with nearly school-level methods to get the value of the zeta function at the point 2.

[00:25:14] That's all for today. Bye!
