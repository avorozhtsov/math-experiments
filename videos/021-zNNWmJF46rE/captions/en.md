# 21. Числа Каталана. Тестируем страсть к программированию (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [zNNWmJF46rE](https://www.youtube.com/watch?v=zNNWmJF46rE). Получено: 2026-10-08T17:42:01+01:00.

[00:00:01] Hello, everyone! Welcome to "Mathematical Experiments".

[00:00:04] Today, we're diving into combinatorics, specifically Catalan numbers.

[00:00:09] It's not a very complicated topic.

[00:00:11] But with some effort, we can explore more advanced concepts, like prime number distribution,

[00:00:18] which is what I'm doing.

[00:00:20] This problem really inspired me a lot back when I was in school.

[00:00:25] I was amazed that there were such fascinating programming challenges.

[00:00:33] So, let's dive into this challenge:

[00:00:35] You're given a string of parentheses.

[00:00:39] Your task is to determine whether it's a valid parenthetical expression or not.

[00:00:43] Here, you can see some valid parenthetical expressions.

[00:00:47] Here parentheses are balanced.

[00:00:49] And here are some examples of invalid parenthetical expressions.

[00:00:54] In valid parenthetical expressions, it's not just about having an equal number of opening and closing parentheses.

[00:01:01] For example, here, the counts are equal, but it's still incorrect.

[00:01:05] Similarly, in this case, the counts match, but there are two closing parentheses while only one is open.

[00:01:15] So, this closing parenthesis makes the entire expression invalid.

[00:01:22] There are three problems related to this topic.

[00:01:25] In each combinatorial problem, there are three programming tasks.

[00:01:29] First, check if the object belongs to the set you're studying.

[00:01:34] Second, count the objects of a specific size.

[00:01:38] And third, learn how to generate objects of a given size.

[00:01:43] These three tasks serve as a test, whether you enjoy programming or not.

[00:01:50] There's 1 valid parenthetical expression of length 2 (one pair of parentheses).

[00:01:57] There are 2 valid expressions with two pairs of parentheses.

[00:02:01] For three pairs of parentheses, there are 5 valid expressions.

[00:02:05] And so on, reaching 14.

[00:02:06] Try listing all 14 valid parenthetical expressions of length 6 on your own.

[00:02:11] As I mentioned, the initial part will be straightforward, but later, we'll delve into more complex concepts.

[00:02:16] We'll explore how Catalan numbers can help us estimate prime number distribution.

[00:02:22] I'll also introduce you to fractal functions, as I like to call them.

[00:02:28] The idea is to associate each parenthetical expression with a path of arrows.

[00:02:34] An opening parenthesis corresponds to an upward arrow (↑).

[00:02:36] A closing parenthesis corresponds to a downward arrow (↓).

[00:02:41] Now, let me show you the grid we'll use for this.

[00:02:45] Here's the grid, and we'll navigate it using these arrows.

[00:02:49] However, I'll draw it without arrows to keep the illustration clean.

[00:02:56] It'll become clear in a moment.

[00:03:01] This function generates a path on the grid from a parenthetical expression.

[00:03:08] You can only move right, either up or down, but always to the right.

[00:03:15] Here we go. A parenthetical expression like this.

[00:03:20] transforms into a bold path on this grid.

[00:03:24] An opening parenthesis leads to an upward step.

[00:03:27] Another opening parenthesis, another upward step.

[00:03:30] Then, two closing parentheses lead to two downward steps.

[00:03:33] Opening, closing.

[00:03:36] Well... you got the idea.

[00:03:39] Let's see how paths look for different parenthetical expressions.

[00:03:45] And this correspondence between paths in the graph and valid objects...

[00:03:51] I was genuinely thrilled when I discovered this in school.

[00:03:56] Here's an example of a bad string of parentheses.

[00:04:01] Here, we go below ground level.

[00:04:05] See? Three closing parentheses come after two opening ones.

[00:04:11] And we end up below ground level.

[00:04:16] A parenthetical expression is correct when it never dips below ground level.

[00:04:24] Here's another example of a bad parenthetical expression.

[00:04:28] So, the IsCorrect function, which checks for valid parenthetical expressions, is quite simple.

[00:04:34] We move along this grid, ensuring we never go below ground level.

[00:04:40] In the end, we must be at ground level.

[00:04:44] The Split function breaks the string into individual characters.

[00:04:48] We count how many characters there are.

[00:04:51] Then, we check that we're above ground level (on the Y-axis),

[00:04:58] and that we haven't reached the end.

[00:05:00] X is our horizontal axis, and Y is our vertical axis.

[00:05:05] We take the next symbol "c".

[00:05:08] If it opens, we step up.

[00:05:12] If it closes, we step down.

[00:05:16] And x always increases by 1 with each symbol.

[00:05:20] In the end, we check if y equals 0 or not.

[00:05:24] If we find ourselves below zero during the process,

[00:05:30] we exit the loop based on this condition.

[00:05:32] And here's False.

[00:05:35] But if we reach the end, we must ensure that y = 0.

[00:05:45] Seems to be working...

[00:05:47] Next up is some complex code.

[00:05:49] When you have two types of brackets.

[00:05:54] This is where the concept of "Stack" comes in.

[00:05:57] Maybe I should show an illustration first...

[00:06:00] The idea is simple: we color the path with two colors.

[00:06:06] Square brackets are blue.

[00:06:08] Round brackets are orange.

[00:06:11] And we ensure that the closing bracket has the correct color.

[00:06:17] So, on the same horizontal level, the arrows are the same color.

[00:06:24] Here, we open round brackets three times, moving with orange arrows.

[00:06:30] Then blue - we open square brackets. And we close with blue as well.

[00:06:37] Then we close three times with orange.

[00:06:41] We introduce the concept of a "Stack". We remember unclosed brackets.

[00:06:46] In this illustration, if we reach this point, our stack should consist of three objects:

[00:06:52] an orange bracket, a blue bracket, and another orange one.

[00:07:00] When we step down, we must take the top item from the stack and check if the color matches.

[00:07:08] Let's look at the code.

[00:07:11] Again, we split the string into individual characters.

[00:07:15] And as long as we haven't reached the end and everything is okay,

[00:07:19] we take the next character "c".

[00:07:22] If it's an opening bracket, we put it in the stack to remember that we need to close it.

[00:07:30] The stack is just a list, and we add it to the end of the list.

[00:07:34] If a closing bracket arrives,

[00:07:38] we check if something is in the stack that needs to be closed.

[00:07:42] If it's empty, it's an error.

[00:07:43] We're trying to close a bracket, but there's nothing to close.

[00:07:48] If it's empty, we immediately raise an error.

[00:07:53] Otherwise, if it's not empty, we take the last bracket from the stack,

[00:07:59] remove it from there,

[00:08:01] and check if it's of the same type.

[00:08:03] We take "cs" from the stack and check if its type matches the incoming bracket.

[00:08:12] If it doesn't match, we raise an error.

[00:08:15] Finally, at the end of each iteration, we step to the right. x increases by 1.

[00:08:20] At the end, we just check that everything is okay. And that's the result.

[00:08:25] That's how it works.

[00:08:30] You can accordingly write a program that calculates the number of bracket expressions.

[00:08:37] I'll do it for just one type of bracket.

[00:08:41] Here's how it's done.

[00:08:43] Instead of solving one specific problem (calculating the number of correct bracket expressions of length 2n),

[00:08:51] I'll embed my problem in a set of parameterized problems x, y.

[00:08:58] And I'll solve a larger set of problems.

[00:09:01] Namely, I'll count the number of paths to any point [x, y] on this grid.

[00:09:08] The number of paths to point [x, y] is a sum of two numbers.

[00:09:15] We can reach this point in two ways.

[00:09:17] Either reach this point somehow and then take a step,

[00:09:20] or somehow reach this point and then step up.

[00:09:25] So, knowing the number of paths to this point

[00:09:27] and to this one,

[00:09:28] we know the number of paths to this point.

[00:09:30] Just by adding these two numbers.

[00:09:34] It's a simple idea.

[00:09:36] You can fill in these numbers on a piece of paper yourself.

[00:09:42] Opposite each intersection write down how many ways to get to it.

[00:09:49] Here, there will be 1s.

[00:09:51] Here too, 1.

[00:09:53] I haven't done that; please do it yourself.

[00:09:56] In the end, the code becomes simple.

[00:10:02] The number of paths to [x, y] is the sum of the number of paths to [x - 1, y - 1] and [x - 1, y + 1].

[00:10:12] But we need to check that we haven't gone below the ground.

[00:10:16] Here, for example, this vertex lacks one term.

[00:10:20] This one.

[00:10:23] And this vertex lacks an upper term.

[00:10:27] That's why I have two "if" statements here.

[00:10:31] Besides, I'm using memoization here.

[00:10:35] Once I've computed something for [x, y],

[00:10:37] I store it in the symbol CountPaths as a mapping [x, y] to the final answer.

[00:10:48] This technique is called memoization.

[00:10:51] In the end, what I'm doing here is called dynamic programming.

[00:10:55] The idea of immersing my problem in a parameterized set of problems

[00:10:59] and then sequentially calculating all the problems.

[00:11:04] It turns out that we have dynamic programming from the top. A recurrence formula with memoization.

[00:11:13] Checking...

[00:11:14] Indeed, 5 bracket expressions of length 3 pairs.

[00:11:20] Here we see the first 10 Catalan numbers for the first time.

[00:11:24] These are called Catalan numbers.

[00:11:29] For Catalan numbers, there is a recurrence formula that allows you to calculate them faster

[00:11:34] than using this algorithm.

[00:11:39] Look at this idea.

[00:11:41] We can divide all paths from point A to point B into groups like this.

[00:11:50] A group where the first touch happens at this point.

[00:11:56] And in general, we can choose any point for the first touch.

[00:12:00] And consider a group of paths where the first touch happens at a specific given point.

[00:12:06] The first touch to the ground.

[00:12:08] Let's say, for example, the first touch to the ground happens here.

[00:12:11] Then the set of paths of this type is made up of the set of paths

[00:12:17] where anything can happen in the orange triangle,

[00:12:20] and anything can happen in the blue triangle.

[00:12:25] Here we step up.

[00:12:27] Here we step down.

[00:12:28] And in the orange triangle, we have a valid bracket expression

[00:12:32] that doesn't drop below the orange line.

[00:12:36] So, specifically, this group of paths is made up of the product of paths of length 3 pairs

[00:12:45] and paths of length 6 pairs.

[00:12:50] Accordingly, if we had moved this touch point here, it would have been C2 * C7.

[00:12:58] Why multiplication? Because any path here

[00:13:03] can be combined with any path here.

[00:13:06] The recursive formula looks like this.

[00:13:12] Writing...

[00:13:14] Again, we use memoization.

[00:13:16] We call the function "c".

[00:13:18] We fix some value.

[00:13:21] Checking...

[00:13:23] It works!

[00:13:24] 5, 14, 42, 132, ...

[00:13:28] Perfect!

[00:13:30] We look at the logarithm of the Catalan numbers and see that the logarithm grows approximately linearly.

[00:13:36] Good...

[00:13:37] Interesting observation.

[00:13:41] We look closely at the numbers...

[00:13:48] Notice:

[00:13:50] here is a series of numbers that are divisible by 5.

[00:13:58] Many consecutive numbers that are divisible by 5,

[00:14:01] but then it breaks.

[00:14:03] Let's look at the remainder when dividing the first 70 Catalan numbers by 5.

[00:14:09] Yes, such subsequences of zeros appear right here.

[00:14:14] Interesting. Is this the same for 7?

[00:14:17] Yes!

[00:14:18] For seven, it's the same.

[00:14:20] Long sequences of consecutive Catalan numbers that are divisible by 7 appear.

[00:14:28] Furthermore, you can study where the numbers that have a nonzero remainder appear.

[00:14:37] And here's one observation of mine.

[00:14:40] For powers of 3 (when we take n as a power of 3),

[00:14:45] c[n] turns out to be not divisible by three.

[00:14:48] Moreover, it has a fixed remainder of 2.

[00:14:53] The same is true for 5 and 7.

[00:14:57] An interesting hypothesis.

[00:14:58] We'll have to try to prove it someday.

[00:15:02] Let's move on to the explicit formula.

[00:15:07] It exists.

[00:15:10] And it's expressed in terms of factorials.

[00:15:14] How can we arrive at this formula?

[00:15:18] Actually, I don't know how to derive this formula directly.

[00:15:22] I know how to get to it through generating functions.

[00:15:25] Generating functions are a powerful tool for analyzing asymptotics

[00:15:31] and geting explicit formulas for various sequences.

[00:15:36] For example, for the Fibonacci sequence, you can write a generating function

[00:15:41] like this.

[00:15:42] It's the sum of an infinite series where the coefficients are Catalan numbers.

[00:15:52] And now, we're going to study this function.

[00:15:56] We'll derive a formula for it and deduce an explicit formula for Catalan numbers.

[00:16:04] We'll do this using our recurrence formula.

[00:16:08] These identities were derived together.

[00:16:12] And it's interesting how this works.

[00:16:15] In this sum,

[00:16:18] the sum of indices is 3.

[00:16:20] 1 + 2 = 3, 2 + 1 = 3, 3 + 0 = 3.

[00:16:27] And this suggests taking this product.

[00:16:31] We take the product...

[00:16:35] And look...

[00:16:37] With x^3, we get this thing,

[00:16:40] which is precisely this quantity.

[00:16:42] So here, we have C4.

[00:16:46] The same here.

[00:16:48] This expression...

[00:16:49] is this thing.

[00:16:53] And so on...

[00:16:56] Let's write it with numbers.

[00:16:58] We took an infinite series with Catalan numbers as coefficients.

[00:17:05] Squared it, and we get another series with Catalan numbers as coefficients.

[00:17:10] Only, previously, there was a 14 with x^4,

[00:17:13] now it's with x^3.

[00:17:18] So, we'll multiply the result of squaring by x.

[00:17:24] We get x + 2x^2.

[00:17:27] Add 1, and we get what we had before. It's f[x] again.

[00:17:33] Next is another identity. It's like a functional identity for the generating function of Catalan numbers.

[00:17:40] We calculate it...

[00:17:41] And see that the answer we get indeed fits.

[00:17:47] The coefficients in the Taylor series expansion are Catalan numbers.

[00:17:54] You can take a closer look at this component.

[00:17:59] Here, we almost have the answer, just the minus signs and 1/2 is extra.

[00:18:03] And here, we're removing this 1/2.

[00:18:08] This function has an explicit formula for the coefficients in the Taylor series.

[00:18:18] And those who've studied analysis know this formula.

[00:18:22] You can watch a video about it on my channel.

[00:18:25] This video here.

[00:18:27] Links to all interesting and useful things will be in the description.

[00:18:32] We'll deal with the analysis of this formula later.

[00:18:36] Now, let's quickly write a function to generate all valid bracket structures of a given length.

[00:18:44] Here we go...

[00:18:46] A function that returns all bracket expressions of a given length.

[00:18:50] 4 represents 4 pairs of brackets.

[00:18:54] The generation function is based on the recurrence formula.

[00:18:59] So, we iterate through "i" in a loop.

[00:19:03] Generate a bracket expression of length "i".

[00:19:06] And generate a bracket expression of length n - i - 1.

[00:19:11] Then, we take the direct product of these two sets.

[00:19:14] The direct product in Mathematica is denoted by Tuples.

[00:19:17] We create a set of pairs, where the first element is from here,

[00:19:22] and the second element is from here.

[00:19:25] p is the prefix, and s is the suffix.

[00:19:28] We surround the prefix with brackets like this.

[00:19:32] This operation in Mathematica denotes string concatenation.

[00:19:40] And we get a new bracket expression from the prefix and suffix.

[00:19:45] This idea is illustrated by this picture.

[00:19:52] The prefix is some orange path in this orange triangle,

[00:19:57] and the suffix is some blue path.

[00:20:00] So, we start with an opening parenthesis,

[00:20:03] then a prefix path,

[00:20:05] then the closing parenthesis,

[00:20:07] and then the suffix path.

[00:20:12] Okay...

[00:20:19] Now, what else do we have here of interest...

[00:20:23] Catalan numbers can give us another formula for calculating Pi.

[00:20:30] We've already realized that the logarithms of Catalan numbers grow approximately linearly.

[00:20:37] Let's try to understand this linear relationship.

[00:20:41] First: it turns out that the coefficient when we approximate the logarithm of Catalan numbers,

[00:20:50] it equals the logarithm of four.

[00:20:52] So, Catalan numbers are approximately equal to 4^n.

[00:20:58] Let's divide the logarithm of Catalan numbers by n and by the logarithm of 4.

[00:21:04] We get something that tends to 1.

[00:21:09] Alright...

[00:21:10] Next, I'm here doing my classic thing.

[00:21:15] Trying to extract components in terms of the logarithm of Catalan numbers.

[00:21:21] And I get this answer.

[00:21:23] That the logarithm of Catalan numbers is, firstly, Log[4] times n,

[00:21:31] then minus 3/2Log[n]

[00:21:36] and some constant.

[00:21:38] I adjusted this constant here to make the graph asymptotically approach zero.

[00:21:45] You can take larger n.

[00:21:47] The formula allows for 100 million and a billion.

[00:21:50] Well... I won't bother with that here.

[00:21:53] In general, this residue is related to the number Pi.

[00:21:57] It equals 1/√Pi.

[00:22:01] Mathematica knows this limit perfectly.

[00:22:04] So, there's this approximate formula for Catalan numbers,

[00:22:09] where √Pi is involved.

[00:22:13] The first main component is 4^n.

[00:22:16] Then you need to divide by n^(3/2).

[00:22:19] And also divide by √Pi.

[00:22:22] This formula arises from the explicit formula

[00:22:26] and Stirling's formula.

[00:22:29] Try it out for yourself.

[00:22:33] Now, the formula for approximating Pi.

[00:22:38] This converges very slowly.

[00:22:42] Just for fun, so to speak.

[00:22:45] To get 12 correct digits,

[00:22:53] you need to take something exponentially dependent on the number 12.

[00:22:59] The number of correct digits of Pi in this formula logarithmically depends on n.

[00:23:06] Moreover, to get the n-th Catalan number, for example, using the recurrence formula,

[00:23:12] you need to compute all the previous n Catalan numbers.

[00:23:16] For the n-th Catalan number, n operations are required.

[00:23:19] There, you end up with a cubic formula,

[00:23:23] But the numbers themselves are long; they have n digits.

[00:23:27] So, you get a cubic formula overall if you implement Catalan number calculations using the recurrence formula and arbitrary-precision arithmetic.

[00:23:39] But you can do it faster by using the explicit formula involving factorials.

[00:23:46] In any case, you could calculate Pi directly from Stirling's formula.

[00:23:51] I tried it here. And there's also a logarithmic dependence

[00:23:56] on the accuracy of the gotten value of Pi.

[00:24:01] Alright...

[00:24:01] So,

[00:24:03] we've got several formulas for calculating Catalan numbers.

[00:24:08] Three of them.

[00:24:09] Through the number of paths, through the recurrence formula, and through the explicit formula.

[00:24:15] We've seen the asymptotics, that it's approximately 4^n.

[00:24:19] And I've told you about a more precise formula based on Stirling's approximation.

[00:24:27] We got the explicit formula involving factorials using generating functions.

[00:24:32] Generating functions are a very cool tool.

[00:24:36] In general, when you start doing something with a generating function, you don't want to do it any other way.

[00:24:44] We've also discovered an interesting behavior for the residues of division by p.

[00:24:49] There are large ranges of numbers divisible by the prime number p.

[00:24:55] For any prime number.

[00:24:57] We'll study this in the bonus part. Right here.

[00:25:02] And we'll get different estimates for the distribution of prime numbers.

[00:25:11] Lastly, I'd like to say that these three combinatorial problems:

[00:25:16] calculating the number of objects,

[00:25:18] checking the correctness of an object,

[00:25:19] and generating all correct objects,

[00:25:22] are wonderful problems to introduce someone to programming in general.

[00:25:27] And if your child's eyes light up when they encounter these three problems

[00:25:34] using parenthetical expressions as an example,

[00:25:36] that's a sign that child have some inclination toward programming.

[00:25:42] And it's not so important whether child will solve them or not.

[00:25:45] What's important is whether child finds them interesting.

[00:25:47] Whether child is willing to spend an hour or more thinking about these problems?

[00:25:52] It is all for today.

[00:25:54] Watch the bonus video.

[00:25:57] In the description, I usually provide various interesting and useful links for studying.

[00:26:02] Leave comments. What's interesting, what's not. What topics interest you.

[00:26:07] Goodbye!
