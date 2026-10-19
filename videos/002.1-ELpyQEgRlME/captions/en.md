# 2. БОНУС 1. Числа Фибоначчи через матрицы (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [ELpyQEgRlME](https://www.youtube.com/watch?v=ELpyQEgRlME). Получено: 2026-10-08T17:44:11+01:00.

[00:00:01] Hello everyone! This is Artem Vorozhtsov.

[00:00:03] And in this bonus video, we're going to talk about the Fibonacci numbers and matrices.

[00:00:06] Let's recall how we defined the function F in our last video.

[00:00:10] Here are the first 20 Fibonacci numbers.

[00:00:12] They start with 1, 1

[00:00:14] Then come 2, 3, 5...

[00:00:16] Each subsequent number is the sum of the two previous ones.

[00:00:19] And this is exactly what we see in the definition:

[00:00:23] How to compute F[n_] ?

[00:00:26] We need to take F[n-1] + F[n-2],

[00:00:29] put everything into the dictionary F, and this is the memoization.

[00:00:34] Then return the resulting value.

[00:00:36] And separately in the dictionary F, values for zero and one are saved,

[00:00:41] so that this recursion is not infinite.

[00:00:43] SetAttributes[F, Listable] makes the function F "threadable over lists":

[00:00:46] if F is applied to a list, then we get a list of elements from the list,

[00:00:53] with function F applied to each element of that list.

[00:00:58] The idea of getting an explicit formula was this:

[00:01:02] Let's try to find a geometric progression

[00:01:06] that satisfies the same relation as the Fibonacci numbers.

[00:01:11] Let's define ff.

[00:01:13] This is a geometric progression.

[00:01:15] There may be some factor b0 here, but it's not that important.

[00:01:20] The identity that is true for Fibonacci numbers

[00:01:24] here turns into this identity.

[00:01:26] It can be seen that it can be reduced by b0 and λⁿ.

[00:01:30] But we'll try to solve it directly.

[00:01:34] Yes, it can be solved.

[00:01:35] And look what happened:

[00:01:36] we found two values of λ that fit.

[00:01:41] That is, there are two values of λ

[00:01:44] such that λ^n fits this identity.

[00:01:49] The second element λ is called phi – the golden ratio.

[00:01:54] And the first element, which can be checked explicitly, is -1/phi.

[00:01:58] Lets check...

[00:02:01] True.

[00:02:02] Further the reasoning goes as follows:

[00:02:03] We have two geometric progressions that satisfy this identity...

[00:02:09] ...here.

[00:02:10] Then their sum will also satisfy this identity.

[00:02:15] It's not an obvious statement, but think about it.

[00:02:19] Moving on...

[00:02:20] Let's take these two progressions.

[00:02:23] One is "a" times phi^n ...

[00:02:27] ... and the other is "b" times (-1/phi)^n.

[00:02:35] The sum of these two geometric progressions also satisfies the Fibonacci identity.

[00:02:44] So let's find values for "a" and "b" such that the zero-th element of this sum is equal to one...

[00:02:50] ...and the first element of this sum of geometric progressions is also equal to one.

[00:02:56] Solving...

[00:02:57] The first argument of the Solve function is a list of equations or inequalities.

[00:03:01] The second argument of the Solve function is a list of variables to solve for.

[00:03:10] And it successfully solves it.

[00:03:15] Here are two curly braces...

[00:03:16] ...basically, here could have been multiple pairs of "a" and "b", but we only get one pair here.

[00:03:21] We define the function F3 and verify that it works.

[00:03:26] Checking the 10th Fibonacci number, we get the familiar number 89.

[00:03:30] Moving on. What I didn't mention in the previous video...

[00:03:33] ...is that this coefficient...

[00:03:36] ...and this coefficient can be simplified ...

[00:03:39] ...or rather, more beautifully.

[00:03:41] Let's multiply the numerator and denominator by 5-√5.

[00:03:46] This is what we get for this case.

[00:03:50] Simplifying...

[00:03:52] The first coefficient is equal to this.

[00:03:55] The second coefficient is 2/(5+√5).

[00:03:58] We multiply again by 5-√5

[00:04:01] and...

[00:04:03] It's clear that we get this.

[00:04:08] Thus, here's a more elegant expression for the explicit formula of Fibonacci numbers.

[00:04:20] We check if it works or not.

[00:04:22] It works.

[00:04:23] So, Fibonacci numbers are the sum of two geometric progressions.

[00:04:29] And we know that the first number is approximately 1.618...,

[00:04:35] the second number is -0.618...

[00:04:38] The powers of these two geometric progressions are drawn here.

[00:04:44] One has a magnitude greater than one, the other less than one.

[00:04:48] This term corresponds to the geometric progression with a power of -0.618...

[00:04:57] When we raise -0.618 to the power of n, we get smaller and smaller numbers with increasing n.

[00:05:08] In the end, we know that the ratio of two adjacent large Fibonacci numbers is approximately phi.

[00:05:20] Not by chance.

[00:05:21] Because for large n we can kind of discard this term

[00:05:27] and then Fibonacci numbers are approximately equal to: some number multiplied by phiⁿ,

[00:05:32] and the ratio of two neighbors becomes equal to a number that is close to phi.

[00:05:39] The larger n is, the closer the ratio is to phi.

[00:05:43] Let's check that the function F3 correctly computes Fibonacci numbers.

[00:05:49] We've already checked that...

[00:05:55] What is a geometric progression.

[00:05:58] Example:

[00:06:00] Let the zeroth element be 3, and each subsequent one is the previous one multiplied by 2.

[00:06:07] 3, 6, 12 - here's an example of an ordinary geometric progression.

[00:06:14] And now I will write something scary and incomprehensible here...

[00:06:17] "b" is such a row vector (1 0).

[00:06:22] "Q" is a 2x2 square matrix. Two rows and two columns with elements 1 1 1 0.

[00:06:31] And we will write:

[00:06:33] b0...

[00:06:34] (Here is dot instead of multiplication)

[00:06:36] b0.(q.q)

[00:06:41] One q here, two q here, three q here, four q here, and so on.

[00:06:46] What will we see?

[00:06:47] {1, 1}, {2, 1}, {3, 2}, {5, 3}, {8, 5}

[00:06:50] yes, quite familiar ...

[00:06:52] Here.

[00:06:53] Our task is to understand what is written here.

[00:06:57] Let's step by step.

[00:06:59] First, let's pay attention that you can write this statement:

[00:07:05] a pair of neighboring Fibonacci numbers

[00:07:09] is written as a pair of such expressions.

[00:07:12] The last one is obvious.

[00:07:17] F[n-1] = F[n-1]

[00:07:19] And the first statement is simply the definition of Fibonacci numbers.

[00:07:25] This is true.

[00:07:27] But let's think about a pair of Fibonacci numbers, as about a pair of x, y.

[00:07:32] And it's as if written here that

[00:07:36] a function of the old pair x, y gives some new pair x, y.

[00:07:46] The general formula for obtaining a new pair x, y and the old one can look like this:

[00:07:54] new x = a x + b y new y = c x + d y

[00:08:05] Okay.

[00:08:08] For Fibonacci numbers, we get:

[00:08:11] if the new pair {x, y} = {F[n], F[n-1]},

[00:08:14] and the old pair {x, y} = {F[n-1], F[n-2]},

[00:08:19] then from this expression

[00:08:24] and recalling how it all looks like here,

[00:08:28] we get: a = 1, b = 1, c = 1, d = 0

[00:08:39] So...

[00:08:41] Next, we need the NewPointList function, which is applied to the list of pairs x, y.

[00:08:50] Here we write a function that converts one pair of x, y and write that it needs to be applied...

[00:08:56] It is called map (/@).

[00:09:00] The hint doesn't show up, but this is operator map (/@).

[00:09:05] We apply it to the list "l".

[00:09:09] Let's check how it works.

[00:09:13] Here...

[00:09:15] So, we passed a list of pairs as the first argument and got a list of transformed pairs.

[00:09:22] We could have added xx, yy and gotten another transformed pair.

[00:09:31] Actually, we could have avoided introducing a new function, NewPointList, and made the function NewPoint calculate for both a pair (x, y) and a list of pairs.

[00:09:36] Let's see how we can do this.

[00:09:46] Like this.

[00:09:48] This expression is quite complex and unclear.

[00:09:51] Here's what it says:

[00:09:53] We define the function NewPoint,

[00:09:55] then in square brackets we describe the arguments and prerequisites for these arguments,

[00:10:00] i.e., under what condition the arguments should satisfy,

[00:10:03] in order to expand the function definition as written to the right of the ":=" symbol.

[00:10:10] So, it says if x is not a list and y is not a list,

[00:10:16] then NewPoint is what is written here,

[00:10:19] i.e., the transformed pair.

[00:10:21] So we think of x as a number... about y.

[00:10:27] The second definition of the function NewPoint.

[00:10:31] We specify the prerequisite for the argument l.

[00:10:35] Prerequisites are written after the question mark.

[00:10:40] MatrixQ is a function that returns True when the argument l is a matrix,

[00:10:49] i.e., a list of lists.

[00:10:52] ListQ is a function that returns True when the argument is a list.

[00:11:05] So this symbol, the exclamation mark "!", means negation.

[00:11:09] That is, x_

[00:11:12] can be followed by either a type, a question mark, or a condition.

[00:11:17] Here we have a question mark and a condition.

[00:11:20] We need to describe a function that returns True or False.

[00:11:27] And if True is returned, then it's good.

[00:11:32] The definition to the right of ":=" is good for computing the NewPoint function.

[00:11:41] Let's check how this works...

[00:11:43] This works as it should.

[00:11:49] By the way, note that if (a, b, c, d) == (1, 0, 0, 1),

[00:11:55] then we get ax = x, by = 0, so just x is here.

[00:12:04] c = 0, d = 1, so just y is here.

[00:12:09] Thus, the new pair x, y is the old pair x, y.

[00:12:12] Let's remember this.

[00:12:14] This combination of parameters a, b, c, d gives us identical transformations.

[00:12:20] The next thing we will need is the Flatten function.

[00:12:23] The Flatten function erases all the curly brackets inside.

[00:12:29] It just makes a list of elements.

[00:12:33] The function F can be given a two- or three-dimensional matrix as input, and the output will be just a list.

[00:12:38] But if you specify 1 as the second argument,

[00:12:42] then you will get a list with one dimension removed.

[00:12:49] And if you specify 2, then two dimensions will be removed.

[00:12:55] Well, if you specify 3, then three dimensions will be removed.

[00:12:59] In short, I want to draw this plot here.

[00:13:06] These are sets of points.

[00:13:08] A set of blue points.

[00:13:11] A set of yellow points.

[00:13:13] And a set of green points.

[00:13:15] Here I have blue dots,

[00:13:18] yellow dots,

[00:13:20] and green ones.

[00:13:22] Points are pairs of coordinates.

[00:13:24] And here, as I'm making this matrix, what I end up with...

[00:13:28] The Table matrix.

[00:13:29] ...I end up with a two-dimensional matrix.

[00:13:32] And I want to turn it into just a list of points.

[00:13:35] Let's Flatten this matrix and we'll get a simple list of pairs.

[00:13:42] Here I have a pair of points 5i, j.

[00:13:46] In other words, "x" runs through the 5i points, and "y" runs through the "j" values.

[00:13:51] So "x" kind of jumps immediately by 5, and "y" jumps by 1.

[00:13:57] See, here are the coordinates 10, 20.

[00:14:00] Then, conversely, these become yellow points.

[00:14:04] And the third set of points this sun.

[00:14:10] Let's do the following...

[00:14:14] Here's our matrix.

[00:14:15] By the way, it's not like this.

[00:14:16] It's like this: (a, b, c, d) = (1, 1, 1, 0)

[00:14:22] And let's draw a set of transformed blue, yellow, and green points.

[00:14:30] The blue dots remain horizontal,

[00:14:34] but the yellow lines are now sloping.

[00:14:37] They were...

[00:14:40] No. Our blue dots have changed

[00:14:42] They were vertical and became horizontal.

[00:14:45] The yellow dots now go at a 45 degree angle.

[00:14:49] And as you can see, the sun has become slanted and stretched out.

[00:14:52] Let's break this down.

[00:14:55] We'll put all of this inside Manipulate.

[00:14:58] Now a, b, c, and d are numbers that we can change and observe what happens.

[00:15:08] Notice, I set a, b, c, and d equal to 1, 0, 0, 1, which is the initial value.

[00:15:14] This is the identical transformation that I talked about earlier.

[00:15:18] The letter 'a', as we can see, is responsible for horizontal compression.

[00:15:22] Compression or stretching.

[00:15:26] 'd' is responsible for vertical compression or stretching.

[00:15:31] Okay.

[00:15:33] What about 'b'? Now this is where it gets interesting.

[00:15:43] This is that slanting effect.

[00:15:45] And here's another slanting effect.

[00:15:49] You see, at some point we got a rotation.

[00:15:53] The squares remained squares.

[00:15:57] The entire plane just rotated.

[00:16:00] And also, apparently, it stretched out a bit.

[00:16:03] But if we bring "a" and "d" to numbers close to one,

[00:16:10] the image will look similar to the original, just rotated by some degrees.

[00:16:16] Okay!

[00:16:18] Let's do the following operation.

[00:16:21] We'll apply the function "t" to the point 1, 1 several times.

[00:16:28] {13, 8}

[00:16:30] We recognize the Fibonacci numbers.

[00:16:35] This thing, applying the function several times, is called Nest in Mathematica.

[00:16:41] Mathematica is a functional programming language.

[00:16:44] The function Nest takes the function h as a first argument,

[00:16:49] The second argument is x, to which the function h should be applied,

[00:16:56] and the third argument is how many times.

[00:17:00] NestList gives us the successive steps of applying the function h.

[00:17:05] There.

[00:17:06] There.

[00:17:08] Thus, we have another way of computing Fibonacci numbers.

[00:17:13] Let's draw the result of executing NestList.

[00:17:19] Here.

[00:17:22] The coordinates of these points are the adjacent Fibonacci numbers.

[00:17:27] Now let's take the logarithm.

[00:17:31] It starts from point (0, 0) – which is (log 1, log 1).

[00:17:35] Then the coordinates are equal to the (log 2, 0), then (log 3, log 2) and so on.

[00:17:43] It is evident that further points lie approximately on a straight line.

[00:17:47] This is the case of convergence to a geometric progression.

[00:17:53] And let's try to see what else we could get if we took other numbers a, b, c, d.

[00:18:01] This is exactly the case described here.

[00:18:04] So...

[00:18:05] Some numbers a, b, c, d are taken here...

[00:18:08] n is how many times it needs to be applied.

[00:18:14] "a"...

[00:18:16] We start gradually changing "a"...

[00:18:19] slowly...

[00:18:21] n is the number of steps. Let's increase this number.

[00:18:28] Here...

[00:18:30] Changing "a"...

[00:18:34] This is a diverging spiral.

[00:18:37] When we decrease n, the outer links begin to disappear.

[00:18:43] Now let's increase it again.

[00:18:49] And this is how the inner links disappear.

[00:18:59] "с"...

[00:19:02] Well... a similar effect.

[00:19:17] They all more or less make the same picture.

[00:19:24] But we have already obtained some strange cases here.

[00:19:38] No longer spirals, but such strange ones...

[00:19:45] Alright. Let's see how our viewer is doing.

[00:19:49] Our viewer's hair is standing on end.

[00:19:53] Well... good. That's the expected effect.

[00:19:57] Moving on.

[00:20:00] Let's apply this transformation twice.

[00:20:04] Or better yet:

[00:20:05] once with coefficients a1, b1, c1, d1,

[00:20:08] and once with coefficients a2, b2, c2, d2.

[00:20:11] What do we get?

[00:20:13] We get this expression.

[00:20:15] Using the Collect function, we can gather the coefficients for x and y.

[00:20:19] Here...

[00:20:20] We see that the double application of the NewPoint transformation gives us a transformation of the same type,

[00:20:30] where a = a1a2+b2c1,

[00:20:35] the new b = a2b1+b2d1, and so on.

[00:20:41] So...

[00:20:43] Well, what...

[00:20:44] This is what is called matrix multiplication.

[00:20:46] This set of coefficients for matrix 1,

[00:20:48] this set of coefficients for matrix 2,

[00:20:51] and this new set of coefficients a, b, c, d is the result of multiplying matrices.

[00:21:00] I think it's very clear where this comes from.

[00:21:04] We want to apply these stretches and shears one after the other.

[00:21:10] One transformation has certain coefficients a1, b1, c1, d1, while the other has different ones.

[00:21:18] What will be the coefficients of the transformation obtained by applying sequentially, firstly the first one, then the second?

[00:21:26] Here's the answer.

[00:21:28] And in Mathematica, this answer is already built into the operator for multiplying two matrices.

[00:21:37] The first matrix is a1, b1, c1, d1.

[00:21:40] Here's the second matrix.

[00:21:42] We multiply them and then ask to write this in matrix form.

[00:21:49] It seems to match.

[00:21:55] Here's our matrix.

[00:21:57] Let's multiply it by itself several times.

[00:22:00] We'll find the numbers 34, 21.

[00:22:04] In mathematics, there's a function called MatrixPower, which allows you to compute the product of 8 such matrices.

[00:22:15] Okay.

[00:22:17] And here's our fourth definition of Fibonacci numbers.

[00:22:20] To get MatrixPower (1, 1, 1, 0), we take the first element of the first row.

[00:22:28] This is like the first row, and 34 is the first element in this case.

[00:22:34] Let's check how it works.

[00:22:35] It just works!

[00:22:37] How long does it take to work?

[00:22:39] Very fast.

[00:22:41] But let's compare anyway.

[00:22:43] First, let's try to define the MatrixPower function ourselves.

[00:22:47] Let's call it MatrixPower2.

[00:22:49] How will we define it?

[00:22:51] For n=0, we'll return the matrix that is equal to one.

[00:22:55] As usual for aⁿ. If n = 0, then one must be returned.

[00:23:00] And here we act in the world of matrices, so we need to return the identity matrix.

[00:23:04] The identity transformation matrix.

[00:23:07] If n > 0, then we return m * m^(n-1).

[00:23:14] Let's check if this definition works.

[00:23:18] It seems to work.

[00:23:19] And it's quite fast.

[00:23:21] What about two thousand?

[00:23:23] Not instant anymore.

[00:23:26] It takes 0.038 seconds.

[00:23:31] Let's define mⁿ more efficiently.

[00:23:34] This is a very important code. The classic one.

[00:23:40] Let's analyse it.

[00:23:42] If n = 0, we return the identity matrix as before. The identity transformation matrix.

[00:23:50] And here's the interesting part...

[00:23:52] Here's an old option.

[00:23:54] If "n" modulo 2 (i.e. the remainder of n divided by 2) equals 0,

[00:24:00] then we do this.

[00:24:02] If "n" is odd, then it's this.

[00:24:05] So for odd "n", we do the old way.

[00:24:09] That is, we recursively call mⁿ⁻¹ and multiply it by m.

[00:24:15] And if "n" is even, we multiply "m" by itself and square the matrix m to the power of n/2.

[00:24:26] This is a cool idea if you need 3 * 3 * 3 * 3 * 3 * 3.

[00:24:33] You can do this...

[00:24:36] You can multiply three by itself six times,

[00:24:39] or you can do 3 * 3, and then multiply the result of 3 * 3 three times.

[00:24:47] Multiply three numbers, that is, choose two multiplication operators.

[00:24:52] Of course, with the example of six, it's not that impressive,

[00:24:54] but imagine if you have 3²⁵⁶.

[00:24:58] So then you probably quickly understand that

[00:25:03] (3*3)^128 – is the big leap!  Not forward, but backwards. We are going to zero, not to the infinity.

[00:25:12] When "n" equals zero, we'll know the answer and return it immediately.

[00:25:17] We need to reduce "n" as quickly as possible using recursion.

[00:25:21] And this is a good way to reduce it. We half number n here.

[00:25:26] Okay...

[00:25:28] I know, it is quite vague explanation...

[00:25:29] Read it carefully, meditate on it, and you'll understand.

[00:25:36] It works.

[00:25:38] But how fast does it work?

[00:25:40] Oh! It takes only 0.007 seconds. Do you remember how long it was before?

[00:25:44] It was 0.03-0.04 seconds.

[00:25:54] Yes. The unoptimized version returns around 0.03-0.04.

[00:26:01] And here it is for 10000.

[00:26:05] But the numbers here are very large.

[00:26:08] Let's do a trick.

[00:26:11] Let's take it modulo 1597 in order not too much returns.

[00:26:20] There we go.

[00:26:22] And let's compare it with the built-in function MatrixPower.

[00:26:27] Oops! We've beaten it.

[00:26:29] Again...

[00:26:32] We've beaten it again! We're great.

[00:26:36] We've given such a definition to MatrixPower2o (o – stands for optimized)

[00:26:42] that we've beaten the built-in MatrixPower function.

[00:26:45] Well, that's it for today.

[00:26:49] Of course, I haven't told you everything about matrices yet...

[00:26:55] A very important point, of course, I haven't mentioned.

[00:26:59] In this algorithm for computing matrices...

[00:27:03] Alright, let me delete this.

[00:27:06] ...a very important property is explicitly used.

[00:27:09] Namely...

[00:27:11] Where are these matrices? Let me copy them.

[00:27:13] Here they are.

[00:27:15] ...a very important property of matrices is:

[00:27:19] that I can group them however I want.

[00:27:21] I can group them like this.

[00:27:26] Like so...

[00:27:31] And the result doesn't depend on how I group them.

[00:27:39] This is a challenge.

[00:27:41] Try proving it yourself.

[00:27:43] This property is called the associative property of matrix multiplication.

[00:27:48] Also, I didn't mention that matrices can be not only 2x2, but also 3x3.

[00:27:53] But you can figure that out on your own.

[00:27:54] Instead of x, y and the transformation of x, y to a new x, y,

[00:27:57] we need to take the transformation of x, y, z.

[00:28:02] Task: write down the formula for multiplying 3x3 matrices.

[00:28:08] Ask Mathematica to perform the same operation we did.

[00:28:17] Here it is.

[00:28:20] Apply Collect  on expanded expression.

[00:28:24] You will have x, y, z here.

[00:28:26] And you need to see what the coefficients are in each row for x, y and z.

[00:28:33] Well, in general...

[00:28:35] there are many ideas for independent work,

[00:28:38] for independent mathematical experiments.

[00:28:42] Let's see how our viewer is doing.

[00:28:45] Great! Good bye!
