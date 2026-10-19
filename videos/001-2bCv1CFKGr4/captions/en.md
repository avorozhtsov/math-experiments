# 1. Знакомство с Wolfram Mathematica. "Галопом по Европе" (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [2bCv1CFKGr4](https://www.youtube.com/watch?v=2bCv1CFKGr4). Получено: 2026-10-08T17:44:19+01:00.

[00:00:00] Hello! My name is Artem Vorozhtsov and this is the first episode of the channel "Math Experiments".

[00:00:07] I'm going to tell you about the Wolfram Mathematica program. It’s a review video

[00:00:12] Let’s look at some code examples and see what can be done in it

[00:00:15] My goal is to interest you and show what it is capable of.

[00:00:19] Firstly, in this program, you can add, multiply, and calculate more complex expressions.

[00:00:28] Essentially using it as a calculator.

[00:00:31] Interestingly, that 23 divided by 37 in Wolfram Mathematica it is the fraction twenty-three over thirty-seven.

[00:00:39] This is the number with an infinite precision.

[00:00:42] If you want to obtain a numerical value of an expression, you need to use the N function.

[00:00:48] Btw, the functions in Wolfram Mathematica are called by square brackets.

[00:00:57] You may be wondering, why not use the round brackets?

[00:01:00] The answer is complex, tbh.

[00:01:04] But actually, it is understandable that round brackets are used to group certain parts of an expression.

[00:01:11] And Wolfram Mathematica has a specific language, and if you use round brackets here, there would be some ambiguity.

[00:01:21] The second argument of the N function, which is optional, indicates how many decimal digits you want.

[00:01:31] For example, if we want 100 decimal digits, it will give us our number with a precision of up to 100 decimal digits.

[00:01:41] Of course, it can simplify fractions.

[00:01:47] Actually, this concept of an interactive notebook originated in Wolfram Mathematica a long time ago.

[00:01:55] Although you may know this concept from Jupyter Notebook.

[00:02:00] Where is also a similar division into in/out blocks.

[00:02:05] 3² = 9

[00:02:08] It is possible to enter powers in a beautiful way. You need to press 3, Ctrl + ^2 and such notation appears.

[00:02:18] It can compute such big blocks.

[00:02:22] Here, look, how many signs are here.

[00:02:25] This is a whole number and in so many signs Wolfram Mathematica has calculated it quickly enough.

[00:02:31] When we add a number with finite precision to a number with infinite precision, we get a number with finite precision.

[00:02:41] In Wolfram Mathematica, there is a number Pi that has infinite precision.

[00:02:47] If you want to know 100 digits, you need to use the known function "N".

[00:02:53] That's how numbers work.

[00:02:57] I haven't told you yet about complex numbers that naturally appear in different places.

[00:03:07] For example, (1 + i)² = 2i

[00:03:13] Аnd i²=-1, etc. We'll meet them soon.

[00:03:22] Functions.

[00:03:25] Here is the √4.

[00:03:27] You can take sine.

[00:03:29] The answer can be a number with infinite precision, like in this example.

[00:03:36] Next, you can define your own functions.

[00:03:40] This is done like this.

[00:03:42] Write the function name, square brackets.

[00:03:46] Then in square brackets you need to specify the arguments with their types.

[00:03:50] The types are specified here.

[00:03:53] But if you do not want to specify the type, just write the name of the argument with an underscore symbol at the end.

[00:04:01] This function has one argument and it calculates x²+1.

[00:04:07] For example, f[10]=101.

[00:04:12] You can make more extensive descriptions of the function, not one-line, with the help of the Module construction.

[00:04:22] Here we specify local temporary variables that can be used to calculate the value of the function.

[00:04:30] The value of the function is the last line inside the body of the second argument of the Module.

[00:04:39] Separate parts should be separated by a semicolon.

[00:04:44] f [2] = 5... Interesting... And f[а] = 1+а²

[00:04:57] This is an error. There was the old function F definition.

[00:05:05] Now I have executed the new function F definition and it has replaced the definition which was used before.

[00:05:14] Let's go ahead.

[00:05:16] You can give a recurrent function definition. More precisely, a recursive one.

[00:05:23] Fibonacci numbers are defined as 1, 1, and then each subsequent number is the sum of the two preceding ones.

[00:05:32] For example, 13 is the sum of 5 and 8, 8=5+3, 5=3+2.

[00:05:42] How can we define this sequence as a function so that Fib[10] gives the 10th number in the sequence?

[00:05:51] It's done like this: there is a function "if" that takes a condition as its first argument,

[00:06:00] what to take if this condition is true as the second argument,

[00:06:06] and what expression to take if this condition is false as the third argument.

[00:06:15] Let's define. Here is the 10th Fibonacci number.

[00:06:20] Then, if we want to get the first six Fibonacci numbers, we need to call this construction.

[00:06:27] What needs to be said here?

[00:06:29] The construction here means "a function with one argument".

[00:06:37] We could write it like this: x + 2.

[00:06:42] And then this function adds 2 to the argument x.

[00:06:50] If we call it g, then g[3] = 5.

[00:06:57] Here, this construction means the Fib function.

[00:07:04] Actually, I wrote this unnecessarily; it's equivalent to this expression.

[00:07:11] These two symbols denote an operator that applies the function on the left to each element of the list on the right.

[00:07:26] There we go! We have the first 9 Fibonacci numbers.

[00:07:34] Btw, it's boring to add natural numbers one by one, so we can use the Range function instead.

[00:07:46] For example, Range[20] gives us the first 20 Fibonacci numbers.

[00:07:53] Btw, you may have noticed that it took some time to compute these numbers, because it's already spending some time

[00:08:00] computing these 20 Fibonacci numbers in an extremely inefficient way.

[00:08:06] If we write the number 25 here, we'll probably even feel it more.

[00:08:13] We can use Timing to find out that this expression takes one second and twenty-two thousandths to execute.

[00:08:24] Btw, what do these slashes mean? Another magic trick.

[00:08:30] Generally speaking, 3 // g is equal to g[3].

[00:08:45] So two slashes "//" – it is the operator, which considers the right part as a function and the left part as that, what is needed to put as an argument in this function

[00:09:01] Let's move on.

[00:09:03] Inside the function, instead of a number, you can put a letter,

[00:09:08] then it will explicitly show what it's going to calculate, when a number is placed instead of the "m".

[00:09:22] Here, I've already done something very complicated. Let's start with something simpler.

[00:09:30] Here, we see an interesting thing, which is defining a tower with five floors.

[00:09:39] We see exactly five "x"s. How can we define such a tower?

[00:09:45] Here it is. If n = 0, then we return 1,

[00:09:50] and if n > 0, then we return (1+x) divided by the tower with one less floor.

[00:09:58] This is the recursive definition of the function Fib[x].

[00:10:03] Below, in In(10), you can also see how the function FullSimplify works.

[00:10:08] It will try to simplify the tower expression.

[00:10:11] Specifically: it will try to make the expression with the minimum number of nodes during syntactic parsing.

[00:10:25] I don't know the details, but it's trying to do something like that.

[00:10:30] Moving on. Here's another definition of a complex multi-level expression, which is essentially a continued fraction.

[00:10:41] Where these numbers grow linearly according to the law 2n + a,

[00:10:50] and these numbers in the numerator grow according to the law n²+b.

[00:10:58] Just an example that we'll need later.

[00:11:02] The PCF function is a function of three arguments,

[00:11:08] where the first argument is a pair of numbers a and b, the second argument is not clear what...

[00:11:17] I assume they are integers.

[00:11:23] And n0 means: from which n to start in these expressions, and 6 means when to finish.

[00:11:32] If we call the PCF function now and substitute the number 12 as the first argument,

[00:11:40] it will say: I don't know what it is or how to expand it,

[00:11:43] because I only know the definition where the first argument is a pair of numbers a and b.

[00:11:55] Next, let's talk about graphs.

[00:11:58] Also known as data visualization.

[00:12:01] Let's draw a parabola.

[00:12:04] Our favorite parabola.

[00:12:07] By the way, it's useful to always draw graphs with gridlines.

[00:12:11] Like this grid here.

[00:12:13] This is so that Mathematica remembers to call the Plot function with gridlines.

[00:12:20] You can execute the "SetOptions" operation.

[00:12:25] If you don't do this, then you'll have to write the option "GridLines => Automatic" every time.

[00:12:35] But we set this option for all Plot function calls.

[00:12:40] Here's another graph: a polynomial with four roots.

[00:12:48] You can draw two functions on one graph.

[00:12:51] To do this, you need to put them in curly braces as a pair.

[00:12:55] First, define these functions and then draw them.

[00:12:59] So, the first argument of the plot function is the expression, which is a list or just a function.

[00:13:11] The second argument is a triple of elements:

[00:13:18] x – the name of the variable that needs to be substituted into the expression,

[00:13:23] the starting point where the value of x changes and where it ends.

[00:13:28] So we drew a graph from -3 to 1.

[00:13:34] Only here everything is broken, because I defined the function g above.

[00:13:40] To clear the previous definitions, we use the Clear function.

[00:13:45] So we drew two functions.

[00:13:48] They're a bit complicated, with exponentials. It's not that important.

[00:13:53] Let's draw the function sin[a x]/x.

[00:13:57] Only here we'll enclose this function in Manipulate. We'll put this entire expression inside Manipulate.

[00:14:07] The last argument of the Manipulate function, the second one, is to set the parameter, its initial value of 1 and the range in which it changes.

[00:14:24] Let's try changing the plot. We get such a beautiful picture. Everything changes on the fly.

[00:14:33] Moving on.

[00:14:35] We can immediately plot three functions here: Sin[a x]/x, Sin[a x], and 1/x.

[00:14:44] Let's draw two components, Sin[a x] and 1/x, whose product is the first function.

[00:14:52] Let's see what we get.

[00:14:55] Let's change it.

[00:14:59] We have plotted 1/x. Here is what it looks like.

[00:15:08] Moving on. Here is our familiar PCF function that I plotted.

[00:15:14] For all kinds of Plot functions, I want to set GridLines -> Automatic.

[00:15:23] Done.

[00:15:25] And now, let's plot, for example, a RegionPlot.

[00:15:33] Some function where the arguments for RegionPlot are not expressions, but inequalities involving x and y.

[00:15:44] That variables that you specified as the last arguments of the RegionPlot function.

[00:15:56] The x-axis changes from 0 to 6, and the y-axis changes from 0 to 5.

[00:16:01] You can get such pictures.

[00:16:04] There are two elements in curly brackets here:

[00:16:09] the first element is simple, x + y < 5 and it defines the blue region,

[00:16:15] and the second argument is composite. It says to take x + y - 5 < 2Sin[Pi (x - y)] and wherein x + y > 5.

[00:16:30] You can change the number of points you want to see here.

[00:16:38] The degree of roughness of the plot is controlled by this option.

[00:16:46] If you specify a small number, the result is plotted quickly, but not very accurately.

[00:16:53] We can see angular elements here.

[00:16:55] And if we write a large number here, the lines will be smoother and more accurate.

[00:17:04] Next.

[00:17:06] DensityPlot. You specify an expression, as the first argument.

[00:17:13] And depending on the value of this argument, which should depend on the two elements specified here.

[00:17:22] Here, a and b.

[00:17:24] A plane is drawn in the a,b plane, where the color depends on the value of the expression.

[00:17:32] I decided that I'm interested in this very expression that I drew at the top.

[00:17:39] For some unclear reason. Now it's clear why I did it.

[00:17:42] It's a complicated multi-level expression,

[00:17:45] in which the variables a and b occur.

[00:17:49] Here it is. I subtracted Pi/2 from it and took the absolute value of this number.

[00:17:57] And I also applied the Soft function. It simply takes the logarithm of the value if y is positive.

[00:18:08] Let's run it.

[00:18:09] Well, okay. I won't run it, it has already been computed. Here's what the DensityPlot looks like.

[00:18:17] To avoid these jagged edges, you need to increase the number of PlotPoints.

[00:18:25] Next.

[00:18:27] You can also draw 3D plots.

[00:18:33] By analogy with RegionPlot, there is RegionPlot3D.

[00:18:37] Here, you already need to specify three variables with ranges as the last arguments.

[00:18:44] Each is specified as a triple.

[00:18:48] The first element in the triple is the name, followed by the initial value and the final value.

[00:18:54] Here we have a cube with sides of 30 from -15 to 15.

[00:19:06] And here some expression is drawn. Greater than zero.

[00:19:11] And this shape is called a Swallowtail. It is related to the discriminant of a 4th-degree polynomial.

[00:19:25] So.

[00:19:27] Let's move on.

[00:19:29] In Wolfram Mathematica, you can solve equations. Let's do that.

[00:19:35] Here we have a system of two equations.

[00:19:41] We need to describe not just one =, but two. Because just = means: assign to the left side what's on the right.

[00:19:50] But == means: equality, identity. Is the left side equal to the right.

[00:20:02] We can solve quadratic equations.

[00:20:06] Sometimes, when solving quadratic equations, complex numbers can arise.

[00:20:10] Here they are.

[00:20:14] Interestingly, what happens if we ask to compute the equation Sin[x] == 2.

[00:20:24] Strangely enough, it says that the answer is not empty and there are two of them.

[00:20:30] It writes this thing ArcSin[2].

[00:20:33] Surprise. ArcSin[2] exists and it is equal to ArcSin[2].

[00:20:39] To find out more specifically what ArcSin[2] is equal to, you can call the function ComplexExpand.

[00:20:47] And obtain an expression through logarithms, exponentials, and other simpler analytical functions than trigonometric ones.

[00:20:59] Simpler from the point of view of Wolfram Mathematica.

[00:21:05] We can solve equations of higher degree. And it finds some roots with absolute accuracy.

[00:21:16] Sometimes it does. It's not necessarily going to find some roots absolutely accurately, if they exist.

[00:21:27] And it describes other roots in a very interesting way.

[00:21:37] It writes that this is the root №2 of such-and-such a polynomial. -1+#1+#1²...

[00:21:52] #1 – is the notation for argument #1. Think of it as x.

[00:22:00] We can take equations of one unknown. Of x.

[00:22:05] And it describes the result very simply, that it is the roots of the same equation that you entered.

[00:22:16] But if you want to see a more accurate representation, then you can use the option Quartics -> True.

[00:22:26] And then all the roots will be described absolutely accurately.

[00:22:32] It can solve equations of the fourth degree with absolute accuracy, if the coefficients of the equation are also given with absolute accuracy.

[00:22:43] Using some expression, which has absolute or infinite precision.

[00:22:52] For example, Pi is another example of an expression with absolute precision.

[00:22:58] Besides natural numbers, integers, and fractions, there are also such expressions with absolute precision.

[00:23:06] And then the answer of the Solve function with the Quartic -> True option will also be absolutely accurate.

[00:23:15] And very large, very scary.

[00:23:18] And you can ask to solve the equation numerically. For this, there is the NSolve function.

[00:23:27] Let's go back to our PCF function again, write down what the expression looks like in three dimensions.

[00:23:36] And ask to solve the equation expr = Pi/2.

[00:23:40] Here is the answer found.

[00:23:43] Yes, pay attention.

[00:23:44] Here is an example of when the number of equations may be less than the number of variables and then such a warning is given.

[00:23:56] And the answer is given parametrically. b depends on the parameter a.

[00:24:04] Series. Let's go.

[00:24:06] You can sum 1/n²

[00:24:12] Absolutely accurate answer.

[00:24:15] Here we get the sum of something.

[00:24:18] When the sum is not calculated, it does not calculate it. Function h is unknown, I did not define it, so it says: the sum equals the sum.

[00:24:28] It can accurately calculate sums of the form one divided by a polynomial of n.

[00:24:36] For example: this is 1/4

[00:24:40] Ah, the intrigue is somehow missing. It should have been like this: it is unknown what it equals.

[00:24:50] Pressing shift + enter and now it's known. Pressing shift + enter and now it's known. Pressing shift + enter and now it's known.

[00:24:58] And final series can also be calculated.

[00:25:03] Moving on.

[00:25:05] There is a function called EulerPhi.

[00:25:09] It tells us how many natural numbers are less than n and coprime with n, meaning they don't have any common divisors.

[00:25:20] For example, for the number 12, the coprime numbers are: 1, 3, 5, 7.

[00:25:26] Why is 4 not included? Because 12 is divisible by 4 and 4 is also divisible by 4.

[00:25:32] Why is 6 not included? Because 12 is divisible by 6 and 6 is also divisible by 6.

[00:25:38] Okay, some strange examples we're getting.

[00:25:43] EulerPhi [7]: these are numbers 1, 2, 3, 4, 5, 6. Because they don't have any common divisors with 7.

[00:25:55] Let's look at another example. For instance, 15. What are these numbers 8?

[00:26:03] 1, 2

[00:26:05] 3 is not included because 15 is divisible by 3.

[00:26:08] 4 is included, 5 is not included.

[00:26:12] 6 is not included because both 6 and 15 are divisible by 3.

[00:26:18] 7, 8

[00:26:22] 9 is not included because it's divisible by 3.

[00:26:25] 10 is not included, 11 is included, 13 is included and also 14.

[00:26:33] So, there are 8 numbers that are coprime with 15.

[00:26:40] We can call the Euler function for the first 10 numbers. Here are the resulting numbers.

[00:26:47] Look, I have used the Range function with EulerPhi here, which means the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.

[00:26:57] And it calculated for each of them.

[00:27:00] This is not possible for all functions.

[00:27:03] For the sine function, for example, it is possible, but

[00:27:09] if I define some function f, it won't know how to expand it.

[00:27:26] However, as far as I understand, we can call the Thread function and it will do it.

[00:27:36] But for the EulerPhi function, threading is done automatically. That's a nice feature.

[00:27:48] Automatic threading is not necessary and should not be used for functions that can receive a list as their first argument.

[00:27:58] That's clear.

[00:27:59] Okay. So, we have calculated the first value of the Euler function.

[00:28:05] Now we want to sum these numbers,

[00:28:09] or more precisely, get the sum of the first two, three, four, etc.

[00:28:17] For this, we have the Accumulate function.

[00:28:20] Accumulate[{a, b, c, d}] gives {a, a + b, a + b + c, a + b + c + d}

[00:28:26] And here is Accumulate[EulerPhi[Range[10]]]. For example, the number 4 is the sum of the first three elements.

[00:28:36] Alright. Let's plot the result of accumulation.

[00:28:41] To plot lists, let me show you again what this list is.

[00:28:46] Accumulate is a large list of 100 elements.

[00:28:52] To plot this list, we need to call the ListPlot function.

[00:28:58] For convenience, we'll store this list in variable l1.

[00:29:03] Then we'll ask to plot l1 for us. Here's the graph.

[00:29:09] Mathematicians can see a parabola just by looking at it. Can you see it too?

[00:29:17] Let's verify this. I want to show you another operator, "@@."

[00:29:24] Plus @@ {a, b, c, d} gives the sum of a + b + c + d.

[00:29:29] So, Plus @@ (EulerPhi)[Range[1000]]) will compute the sum of the first thousand values of the Euler function.

[00:29:40] Let's divide by 1000². This is the resulting number.

[00:29:46] I've erased the expression value here, just to create some suspense.

[00:29:53] Let's compute it. The numerical value of this fraction is 0.304192,

[00:29:59] and if we take 10000, it becomes 0.303975.

[00:30:05] Surprise! It turns out to be 3/Pi².

[00:30:12] Moving on. Watch this.

[00:30:16] And so, Accumulate[EulerPhi[Range[n]]] grows approximately like 3/Pi² * n². That's roughly what we can deduce from these computations.

[00:30:31] Let's subtract from Accumulate[EulerPhi[Range[n]]] this quadratic parabola.

[00:30:42] How do we subtract one list from another?

[00:30:44] Like this: When we subtract list a from list b, we obtain a new list.

[00:30:52] But only if the number of elements is the same.

[00:30:56] If the number of elements is different, then something will go wrong.

[00:31:01] So, I'm subtracting from Accumulate[EulerPhi[Range[n]]] a parabola with a coefficient of 3/Pi².

[00:31:09] We calculated this coefficient here, by finding that the sum of the first 10000 Euler numbers divided by 10000²

[00:31:21] equals this, which secretly I told you, is 3/Pi².

[00:31:29] We subtract and draw. Look: instead of this graph, which reached 3000 at point 100,

[00:31:41] we obtained a new graph which reaches some number... 50, maybe less, at point 100.

[00:31:51] Interesting! Let's subtract Range from it too.

[00:32:06] You can already peek into the future.

[00:32:09] Here's where the excess happened, we subtracted too much. Let's subtract 0.5.

[00:32:16] There we go. It's an excess, but not as strong.

[00:32:21] 0.4, 0.3

[00:32:25] Alright, we're getting very close. What if we make it 0.2?

[00:32:28] Now it's leaning towards the other direction. It's an undershoot.

[00:32:32] So, from Accumulate[EulerPhi[Range[n]]], we need to subtract 3/Pi² * Range[n]².

[00:32:40] Oops! I forgot to mention that.

[00:32:44] What is Range[n]², though?

[00:32:47] First of all, Range[10] is the first set of numbers.

[00:32:51] And if we square them, each number is squared,

[00:32:56] because squaring is also a function that automatically applies to lists.

[00:33:03] So, Range[n]² is just the first n of the squares of the natural numbers.

[00:33:12] And this is just the first n of the natural numbers.

[00:33:16] Yes. I'm using some magic here.

[00:33:20] It turns out that the list Range[n], for example, Range[10], can be multiplied by a number, like a or 0.1.

[00:33:35] That's the trick used here and here.

[00:33:41] Anyway, I won't torture you with this.

[00:33:43] So, as you can see, we need to subtract 3/Pi², and then it will be perfectly straight.

[00:33:52] This triangle will be perfectly straight.

[00:33:55] The numbers are arranged chaotically, if we ask to draw a graph by connecting these points with lines, it won't look great.

[00:34:05] Let's take a look.

[00:34:07] True. Here it is. It's not clear how to edit this.

[00:34:13] So the nature of this function is clearer now.

[00:34:17] As you can see, it changes more or less chaotically from -200 to +200.

[00:34:24] More precisely, the range keeps growing. So, let's divide it by n to prevent it from growing.

[00:34:30] How to divide it by n. We need to divide the n-th element of this list by n.

[00:34:35] Here's the magic. It turns out we can take 1/Range[10].

[00:34:42] This is what we get.

[00:34:47] Now let's take Range[10] * 1/Range[10], this list, and let's plot it.

[00:35:00] Here's what it looks like. An incredibly interesting observation about the Euler function.

[00:35:11] The situation does not change as the number n increases.

[00:35:16] There's some sort of strip that apparently lasts to infinity.

[00:35:20] This is our assumption. We're doing experimental mathematics right now.

[00:35:25] By the way, what's the histogram of these numbers?

[00:35:28] How many numbers are in the vicinity of 0? How many numbers are in the vicinity of 0.2?

[00:35:33] The Histogram function gives us the answer to this question.

[00:35:41] We'll talk about interesting experimental facts about the Euler function and Accumulate of the Euler function some other time.

[00:35:53] Let's move on quickly. We need to keep going.

[00:35:59] Here's how you can get a list of squares.

[00:36:02] In addition to the method described above, Range[10]², you can use this syntax.

[00:36:14] It's more universal, because instead of n², you can write anything you want.

[00:36:20] Including a function that isn't precompiled.

[00:36:25] Next.

[00:36:26] Here's a two-dimensional table. A two-dimensional table is a list of lists.

[00:36:32] To create one, you need to specify two ranges for two variables.

[00:36:39] Next.

[00:36:40] You can place this table inside the Grid function.

[00:36:47] If you specify Frame -> All as an option, you get a table like this.

[00:36:52] And if you don't specify it, we will have no grid.

[00:37:00] You can also do it like this.

[00:37:04] So, something is stuck here. Abort evaluation.

[00:37:11] I need to write n = 13. Slap!

[00:37:17] Here I used not a * b, but a * b modulo n. That is, subtract n if a * b is greater than n.

[00:37:27] Subtract as many times as necessary to get a number less than n.

[00:37:34] This table of numbers can be represented as an ArrayPlot.

[00:37:40] Well, it's something similar to DensityPlot, only it's ArrayPlot.

[00:37:46] It takes a two-dimensional array as an argument.

[00:37:53] And here we drew the same 12x12 table from 1 to n-1 as colors.

[00:38:08] Here the numbers change 1 2 3 4 5 6 7 8,

[00:38:13] and here the colors change from light to black.

[00:38:19] And we put all this inside Manipulate again to see how this ArrayPlot will change with increasing n.

[00:38:27] Increasing...

[00:38:31] Such beauty.

[00:38:37] In the middle, it changes. Either intersecting lines appear in the center, or they disappear.

[00:38:46] Here you can expand this control for manipulation.

[00:38:50] And start the animation. Click Play and it will start playing.

[00:38:55] You can click pause, reduce the speed. It's probably not visible, but here I'm reducing the speed.

[00:39:04] And then I run it again and it goes slower, I can make it even slower.

[00:39:09] See, it's going slower and slower.

[00:39:13] Let's start from the beginning:

[00:39:20] This simple beauty can be programmed by anyone. It's very easy.

[00:39:35] Stop.

[00:39:37] Moving on.

[00:39:39] There are many predefined functions in Wolfram Mathematica.

[00:39:47] For example, polynomials.

[00:39:49] There's a function called Zeta, which, by the way, at the point 2 equals the sum of inverse squares that we computed earlier.

[00:40:05] It knows various polynomials.

[00:40:08] And, by the way, you can find the roots of these polynomials.

[00:40:11] For example, let's find all the roots of the 60th-degree Bernoulli polynomial.

[00:40:21] We get 60 numbers. Some of them are integers and we can even assume that some are really 3/4 and others are -1/4.

[00:40:33] And other roots are complex.

[00:40:37] How do we draw them on a plane?

[00:40:40] Let's define a function CPoint, which takes one argument z.

[00:40:44] It is assumed that z is a complex number.

[00:40:47] And it returns a pair of points: the real part of the complex number and the imaginary part.

[00:40:54] Defined.

[00:40:56] Then we use this manipulation... let me explain.

[00:41:04] Without Transpose, we get a list of two lists, because instead of using a single complex number for z, we used a list.

[00:41:19] There was automatic threading.

[00:41:22] Real of a list gives a list of real parts.

[00:41:28] And this is what we got.

[00:41:31] But in order to get the transposed matrix from this matrix, we need to call the Transpose function.

[00:41:40] Then we will have not a list of two lists, but a list of pairs.

[00:41:47] A list of pairs is something that can be sent to the ListPlot function.

[00:41:52] Oops!

[00:41:53] This is what the roots of the Bernoulli polynomial look like.

[00:41:58] AspectRatio -> 1 for greater beauty. Just like that.

[00:42:04] And these are the roots of a 200-degree polynomial.

[00:42:11] It's very interesting to run an animation and see how these roots change as the number n increases.

[00:42:19] Moving on. In Wolfram Mathematica, you can also do modeling.

[00:42:23] Here, for example, I modeled the Covid virus. This is a standard model.

[00:42:30] In general, you can write more complex code, multiline code.

[00:42:33] Not just drawing something or outputting tables, but writing code, algorithms, creating data structures.

[00:42:43] Well, we won't be able to get to that level in this introductory class.

[00:42:49] So, here I built this simple standard model.

[00:42:52] Or rather, I took it and wrote it down.

[00:42:57] The Covid virus has a certain ability to infect, called the transRate.

[00:43:06] And there is a certain value that characterizes the probability that a person will recover in the next quantum of time.

[00:43:15] tS - this is the proportion of the population that is uninfected and has not got sick yet.

[00:43:21] tI - this is the proportion of the population that is currently infected.

[00:43:28] tR - recovered, those who have recovered.

[00:43:34] The proportion of healthy, non-infected people decreases by transRate * tS * tI.

[00:43:43] Sick people tI infect healthy people without immunity.

[00:43:49] And the rate of infection is proportional to the product.

[00:43:54] The proportion of infected people is just increasing. deltaS is precisely what moved from tS.

[00:44:10] In tS, it decreased, and in tI it increased.

[00:44:16] But some number of people who recovered decreased in tI.

[00:44:24] Then deltaR is the fraction of those who recovered.

[00:44:33] This term is moved here with a plus sign.

[00:44:40] Well, it doesn't matter. The model is simple, it's not important what kind of math is hidden here.

[00:44:48] I set some values for these two parameters.

[00:44:56] I set the number of steps to 10 and started the evolution process of this system.

[00:45:03] Initially, there were 99% healthy and 1% sick people.

[00:45:10] Then the infection and recovery process began.

[00:45:16] After 10 steps, we already have 86% healthy people, 12% are currently sick, and almost 1% have recovered.

[00:45:27] Recovered means those who are no longer contagious.

[00:45:34] Now we can again put this inside the Manipulate function and see what can happen in this system.

[00:45:43] This way, we continue the evolution forward for a larger number of steps.

[00:45:48] But that's not so interesting.

[00:45:50] And then we can change the infectivity of the disease.

[00:45:55] If it is highly contagious, the following phenomenon occurs:

[00:45:59] Almost everyone becomes sick in just 100 time steps.

[00:46:05] The blue line represents the number of healthy people. There are practically none left.

[00:46:12] The yellow line is those who are currently sick.

[00:46:15] There are the most sick people somewhere around this step. Let's say at the 80th step.

[00:46:21] And the green line represents those who have recovered and are now healthy.

[00:46:31] We reduce it...

[00:46:34] Yes, it's interesting that at some point, when we greatly reduce the infectivity of the disease, the blue line reaches some limit.

[00:46:43] That is, there are people who have never been sick and will never get sick.

[00:46:48] Even in the very distant future.

[00:46:52] And that's wonderful.

[00:46:55] Well, that's it!

[00:46:57] Goodbye, everyone!

[00:46:58] Write in the comments what you would like to learn about, what topics are interesting to you.

[00:47:05] As for me, I plan to talk more about number theory, modular arithmetic, and similar topics.

[00:47:15] Goodbye for now!
