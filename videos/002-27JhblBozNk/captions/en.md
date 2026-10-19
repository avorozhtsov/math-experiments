# 2: Числа Фибоначчи. Нельзя объять необъятное (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [27JhblBozNk](https://www.youtube.com/watch?v=27JhblBozNk). Получено: 2026-10-08T17:44:15+01:00.

[00:00:01] Hello, everyone! My name is Artem Vorozhtsov.

[00:00:05] And today I'm going to talk about Fibonacci numbers.

[00:00:08] It is impossible to tell the full story about Fibonacci numbers ,  I'll try to cover just tiny portion.

[00:00:12] So...

[00:00:13] Fibonacci numbers are numbers like: 1, 1, 2, 3, 4, 5, 8, 13, ... and so on.

[00:00:20] Each number is the sum of the two preceding ones.

[00:00:24] We've defined this explicitly with the expression F[n_] := F[n-1]+F[n-2];

[00:00:31] Will it work?

[00:00:33] No, it won't...

[00:00:35] Recursion depth exceeded...

[00:00:37] Because it doesn't know what the first two Fibonacci numbers are.

[00:00:42] They are 1, 1. We need to specify them.

[00:00:45] Let's be imperative programmers for a moment

[00:00:47] and define a function F1 that returns 1 if n=0 or n=1 (two vertical lines " || " mean "or").

[00:00:59] Otherwise, it returns F[n-1]+F[n-2].

[00:01:03] In other words, it recursively returns itself with smaller parameters.

[00:01:07] Let's check if this works...

[00:01:09] Yes, it works. 10946.

[00:01:12] Moving on.

[00:01:13] Range [0, 20].

[00:01:16] Apply the function F1 to all these numbers: 0, 1, 2, 3, 4, 5, and so on.

[00:01:25] Interestingly enough, the same result could be obtained from this "not working" definition.

[00:01:31] Just had to add two more lines.

[00:01:34] Like this.

[00:01:37] Let's check...

[00:01:38] Yes!

[00:01:39] It works.

[00:01:41] Programmers (imperative) might wonder: What's the hack? How can these three lines work?

[00:01:48] They are defined independently of each other,

[00:01:52] and for some reason, the first line led to infinite recursion,

[00:01:56] but these two additional lines remove this infinite recursion.

[00:02:02] I'll explain it like this:

[00:02:04] You can think about it as polymorphism. Symbol F represents two different objects.

[00:02:11] On one hand, it is function F (":=" rule),  and on the other hand, it is a dictionary ("=" rule).

[00:02:15] And Mathematica does the following:

[00:02:18] when an expression with F comes in, it first checks if there is already a ready answer in the dictionary  F,

[00:02:26] and if not, then it goes to function F[n_].

[00:02:30] Let's see what, for example, F[n_] will be equal to if we write xxx here.

[00:02:38] The first definition worked.

[00:02:40] Note that it did not move on further...

[00:02:45] Or rather, it did move on further, found the recursion and stopped.

[00:02:50] Good.

[00:02:52] Let's erase this.

[00:02:53] Now...

[00:02:55] The new F works just like F1.

[00:02:58] F[25] is computed in about half a second,

[00:03:08] and F1[25] is computed in just over a second.

[00:03:16] Thus, function F1 computes 25 Fibonacci numbers for over a second,

[00:03:23] while function F does it in half a second – that's a lot.

[00:03:29] To make the calculations more efficient, let's add memorization.

[00:03:35] Memorization is done like this:

[00:03:38] We define the function F2 in a very similar way, but add F2[n]= inside it.

[00:03:49] Here again, a colon equals " := " defines a function (SetDelayed-rule),

[00:03:53] while an equals sign " = " puts the value of n into the dictionary F2 (Set-rule).

[00:04:00] So, the function F2[n] is defined as follows:

[00:04:04] We need to evaluate this expression, get a numerical result, and save it in the dictionary F2.

[00:04:12] Only then we return this value.

[00:04:15] Let's check...

[00:04:18] It's practically instantaneous, we can replace it with 35 and get even more numbers.

[00:04:25] Let me illustrate this idea with an example where one symbol can be both a function and a dictionary.

[00:04:35] Using the symbol g.

[00:04:37] g[n_] is equal to n as a function.

[00:04:40] g[n_, a_] as a function of two variables is equal to n + a.

[00:04:45] And we also defined 3 values of g at three points. We stored them in the dictionary g.

[00:04:51] Let's check...

[00:04:56] The first line worked here.

[00:04:58] The second line worked here.

[00:05:00] g[42]...

[00:05:03] Correct.

[00:05:05] g[b] = 3

[00:05:06] Interestingly, if we write b = 2 and evaluate g[b] again,

[00:05:13] we get a different result.

[00:05:15] The reason is that this line was executed when " b " was an undefined symbol.

[00:05:24] And that's exactly how it was stored in the dictionary g: g of the symbol b is equal to 3.

[00:05:31] Here, in square brackets, it's not the symbol "b", but the number 2.

[00:05:38] g[a] = a, the first line of the definition is executed here.

[00:05:44] By the way, we can view all of these definitions using the Definition function.

[00:05:50] And with the FullDefinition function, we can see more.

[00:05:56] First of all, we see all the definitions,

[00:05:58] and also he writes some additional definitions of symbols

[00:06:04] that appear in the right side of SetDelayed rule (to the right of the ":=").

[00:06:13] Let's check the status of our audience.

[00:06:18] Oh...

[00:06:19] It seems like brains have exploded.

[00:06:22] Well, let's be more careful.

[00:06:24] Moving on to the next point - Continued Fractions.

[00:06:29] A continued fraction is such a multi-story expression where arbitrary numbers can be used instead of ones.

[00:06:37] Instead of these ones.

[00:06:40] Well, instead of these ones too.

[00:06:42] Let's see what we get...

[00:06:45] 1/2

[00:06:48] 2/3

[00:06:52] 3/5

[00:06:55] 5/8

[00:06:58] Moving on...

[00:07:00] Let's define this multilevel fraction.

[00:07:05] How do we do that?

[00:07:07] Let me temporarily put the letter x here

[00:07:15] and write what Fib[4] is equal to.

[00:07:25] Fib[4] is equal to this.

[00:07:29] If we remove x from here,

[00:07:34] it immediately calculates the entire expression as 5/8.

[00:07:38] 5

[00:07:40] 6

[00:07:41] Looks like it works.

[00:07:43] Okay.

[00:07:44] Let's calculate for the first 20 natural numbers.

[00:07:50] It's clear that this is the ratio of neighboring Fibonacci numbers.

[00:07:57] To get the numerator of these numbers, we need to call the Numerator function.

[00:08:03] Let's see how quickly Numerator works.

[00:08:07] Also fast.

[00:08:12] Although this is 10 times slower than the F2 function.

[00:08:19] The next interesting topic.

[00:08:22] Another place where Fibonacci numbers appear is in the partitioning of a rectangle into squares.

[00:08:30] Here. We now have an image on which I can explain what I'm going to do.

[00:08:39] Let's say we have some rectangle.

[00:08:43] We will take the smaller of its sides and draw a square attached to it from the inside.

[00:08:53] We get the remainder. The remainder is also a rectangle.

[00:08:56] We will find the smaller side in it and attach a square to it in the same way.

[00:09:01] Let's assume that at the top.

[00:09:03] We will again get a rectangle.

[00:09:07] We will also find the smaller side in it and draw a square.

[00:09:11] Here, it turned out that square, square, square...

[00:09:14] I cut off one square each time,

[00:09:17] because that's how I already chose.

[00:09:20] But if you take 27/8, such a longer rectangle,

[00:09:29] then at first we will have to cut off three squares.

[00:09:33] Okay, we get such a vertical rectangle.

[00:09:37] So we cut off a square from the top...

[00:09:39] Not enough...

[00:09:40] Let's cut off one more...

[00:09:42] And now we have a lying rectangle.

[00:09:46] From it, we cut off a square on the right and there are still two squares left.

[00:09:51] That's how it goes...

[00:09:55] If we write 8 here, nothing will change.

[00:09:59] 8 is how many steps we need to take.

[00:10:03] 1, 2, 3, 4, 5, 6, 7, 8

[00:10:07] The first one doesn't count, apparently.

[00:10:10] Eight steps are enough, so further increasing this number will not lead to anything.

[00:10:15] Let's go back up.

[00:10:17] So...

[00:10:18] The function SplitToSquares should split the rectangle,

[00:10:25] wich has the bottom left corner at x1, y1, the top right corner at x2, y2,

[00:10:33] into n parts.

[00:10:35] Well, into n minus one square and what's left.

[00:10:40] So...

[00:10:42] We use Module and temporary variables a, b.

[00:10:46] If you want to write a complex function with local variables, use Module.

[00:10:54] If n = 0, that is, there are 0 steps left,

[00:10:58] then we take and return this rectangle as is.

[00:11:02] Yes, I know. Too many curly braces...

[00:11:04] Well, yes, because I want to return a list with one figure.

[00:11:10] The fact that it is a list is indicated by the curly braces.

[00:11:15] One figure is a list of pairs.

[00:11:18] These are the second set of curly braces and the third ones.

[00:11:23] Now if we have more steps left, I want to return a list of more than one figure.

[00:11:31] I calculate side a, side b, and finding out which side is smaller.

[00:11:37] a is the length of x2 - x1.

[00:11:41] b is the height.

[00:11:42] If a<b, meaning our rectangle is in portrait orientation, then we need to cut off one square from the top.

[00:11:54] How do we cut off one square from the top?

[00:11:56] This square.

[00:11:58] Indeed, the height of this square is a, because it's y2 minus this expression.

[00:12:06] And the width of this square is also a, because it's x2 - x1.

[00:12:11] This is the square that we cut off.

[00:12:14] And we're left with a rectangle with these coordinates.

[00:12:18] Check it.

[00:12:19] We need to cut it into n-1 pieces.

[00:12:23] Checking...

[00:12:25] Cutting...

[00:12:29] I asked to cut the rectangle 13/8 and make 2 cuts, which resulted in 3 figures.

[00:12:37] And if you ask for more cuts to be made, this is what we get.

[00:12:44] Okay.

[00:12:45] The Graphics function takes a list of directives as its argument.

[00:12:50] The first directive is Hue, to select a color with these parameters.

[00:12:55] The second directive is Rectangle. Draw a Rectangle.

[00:13:00] I'll show you how to work with Hue.

[00:13:04] When you type Hue, it suggests you to select the color you need in the selector.

[00:13:11] Okay, click and the necessary parameters are substituted.

[00:13:15] Then you execute it and see the rectangle you need.

[00:13:22] Color scheme number 10, we'll use it.

[00:13:26] This is what I already showed you.

[00:13:30] Let's explicitly write that the coordinates are equal to Fibonacci numbers.

[00:13:36] That is, we want to take a rectangle whose sides are neighboring Fibonacci numbers,

[00:13:44] and divide it into squares. n - 1 squares.

[00:13:50] Let's check how it all works...

[00:13:55] I take it and get a list of squares.

[00:14:02] Next.

[00:14:04] I take Range[Length[sqs]] (from one to the number of squares).

[00:14:10] And this becomes my variable i.

[00:14:15] i = #

[00:14:16] These parentheses here are the expression.

[00:14:21] It is denoted as a function of the hash.

[00:14:24] But inside this expression, we immediately send the hash value to the i variable.

[00:14:29] And then we write not " # ", but " i ".

[00:14:34] It's more visual than using the hash everywhere.

[00:14:38] i is an index. Index of the square in the sqs array.

[00:14:44] We take a Rectangle with vertices equal to this square.

[00:14:51] Like this.

[00:14:52] And we take its color from the colors array, which I calculated above.

[00:15:01] As a result, we get a list of pairs. A list of directives.

[00:15:06] Set this color.

[00:15:08] Draw a Rectangle.

[00:15:10] We turn this list of pairs into just a list.

[00:15:13] Flatten means to turn a list of lists into a list.

[00:15:18] It removes the inner brackets.

[00:15:22] We draw and get what we see on the screen.

[00:15:26] Good!

[00:15:28] By the way, here we have a proof of a very interesting theorem.

[00:15:34] The sum of the squares of Fibonacci numbers that are involved here equals the area of the entire rectangle.

[00:15:41] And the area of the rectangle is the product of adjacent Fibonacci numbers.

[00:15:46] So, we take the product of adjacent Fibonacci numbers,

[00:15:49] and it should be equal to the sum of the squares of all previous Fibonacci numbers.

[00:15:56] Let's check...

[00:15:57] Here's the sum of the squares,

[00:16:00] and here's the product.

[00:16:02] The sum of squares from zero to the fourth,

[00:16:06] and the product of the fourth and fifth.

[00:16:09] They match!

[00:16:11] We can verify this...

[00:16:12] Here are the Fibonacci numbers.

[00:16:14] Here are their squares.

[00:16:16] The square is a magical function. It is Listable. It threads through the list.

[00:16:20] It threads through the list. That is, when called on a list, we get a list in which this function is applied to each element.

[00:16:29] I remind you what Accumulate is.

[00:16:32] Accumulate of a list is a list consisting of the sum of various prefixes.

[00:16:40] Prefix is the beginning of a list.

[00:16:43] The beginning of the list "a", The beginning of the list "a + b", The beginning of the list "a + b + c".

[00:16:47] All possible prefixes are aggregated by summation.

[00:16:53] Let's sum up all the prefixes of the squares of Fibonacci numbers.

[00:16:59] This is what we will get.

[00:17:02] And now let's take the Fibonacci numbers...

[00:17:04] and take the Fibonacci numbers shifted by one and multiply these two lists.

[00:17:10] See? These Fibonacci numbers start at 1, 1, 2, and these start at 1, 2, 3.

[00:17:18] Multiplying:

[00:17:20] 1 * 1 = 1

[00:17:22] 1 * 2 = 2

[00:17:24] 2 * 3 = 6

[00:17:27] This is how you multiply two lists. Simply place a multiplication sign between them.

[00:17:33] 3 * 2 = 6

[00:17:37] 3 * 5 = 15, everything matches

[00:17:42] 5 * 8 = 40

[00:17:46] So, what do you think? Let's see your status...

[00:17:54] Okay... what is this?

[00:17:58] Alright. I'll be more careful.

[00:18:00] Now we're going to move on to a simpler topic.

[00:18:03] Oh, no. It's not going to be simpler, it's just going to be more interesting.

[00:18:08] Let's immediately make sure that all of our graphs have GridLines.

[00:18:13] I'll write that F = F2 and now, hopefully, everything will be faster.

[00:18:19] Slap!

[00:18:21] There they are!

[00:18:23] A thousand Fibonacci numbers.

[00:18:29] A lot of digits...

[00:18:32] Oh, it didn't fit.

[00:18:34] Well, okay...

[00:18:35] We have to hide this somehow.

[00:18:36] There, it's hidden.

[00:18:38] Let's erase it and put a semicolon here so that it doesn't output everything.

[00:18:43] Let it store the result in an array called fibs.

[00:18:46] And let's have it draw the logarithm of these numbers.

[00:18:50] I took the logarithm right away because without it, things get really sad.

[00:18:55] If we remove the logarithm and take the first 10 numbers, we get this image:

[00:19:01] But if we take the first 100 numbers, it looks like this.

[00:19:04] In general, it's meaningless to observe it.

[00:19:09] Everything is at the bottom, and then it goes up.

[00:19:12] Because Fibonacci numbers grow very quickly.

[00:19:16] And this can be seen in this plot.

[00:19:18] What is a logarithm? Perhaps not everyone knows.

[00:19:22] Essentially, it is the number of digits.

[00:19:24] We saw that the number of digits...

[00:19:27] Ha! What do you think of that definition? A logarithm is the number of digits.

[00:19:33] The Take function takes a certain number of elements from an array,

[00:19:39] and it can be seen that the number of digits grows with each step by a certain amount.

[00:19:51] Well, not with each step...

[00:19:53] Here we have a sequence of two-digit numbers, then a sequence of three-digit numbers, then a sequence of four-digit numbers...

[00:20:01] The point is that the number of numbers with the same number of decimal digits is roughly the same.

[00:20:10] Look again: 1, 2, 3, 4, 5,

[00:20:18] and there were 4.

[00:20:19] How many six-digit numbers will there be? 1, 2, 3, 4, 5

[00:20:25] How many seven-digit numbers will there be? 1, 2, 3, 4, 5

[00:20:33] This is logarithmic growth,

[00:20:37] when roughly the same number of steps are taken to add the next digit in some representation, such as decimal.

[00:20:48] A logarithm is...

[00:20:51] Let me give you some definition.

[00:20:54] Log[2, 8] = 3

[00:21:00] How many times do we need to multiply 2 by itself to get 8?

[00:21:06] Log[2, 16] = 4

[00:21:09] If we don't write 2 here, then we take some other number as the base, which is called "e".

[00:21:18] And we can numerically find out what Log[16] equals.

[00:21:26] Okay.

[00:21:27] The logarithm grows approximately linearly.

[00:21:31] Linearly means that you can put a ruller on your plot

[00:21:36] and see that they are approximately on a line.

[00:21:40] Let's find this linear function.

[00:21:45] For this we use the function Fit - the simplest function for regression.

[00:21:53] To find some approximate functions for your number series.

[00:21:59] 0.48x

[00:22:04] We see that the Fibonacci numbers are approximately a geometric progression.

[00:22:12] When the logarithm of the numbers grows linearly, it means that we are dealing with approximately a geometric progression.

[00:22:22] Let's find the power of this geometric progression.

[00:22:28] Approximately.

[00:22:29] For this, we need to divide adjacent 2 Fibonacci numbers.

[00:22:32] Well, we no longer have F2, we made it so that F = F2

[00:22:39] Here's the number...

[00:22:41] Oops...

[00:22:43] If there were some Gauss or Euler with us...

[00:22:47] he would say: Ah, I know this number!

[00:22:51] More precisely, he would say it in German...

[00:22:55] But in general, of course, any mathematician recognizes this number, as well as ancient Greek architects...

[00:23:06] This is the number φ "phi" - the Golden Ratio.

[00:23:10] Let's write more digits.

[00:23:14] 1.618033988...

[00:23:20] Remember it.

[00:23:22] And let's draw 2 graphs now.

[00:23:25] Our original graph...

[00:23:27] and here is the result of fitting.

[00:23:30] Fitting is the same as adjustment.

[00:23:33] We can draw it like this in different colors.

[00:23:38] Let's draw the dots in blue and the line in red.

[00:23:43] Now let's do something that's typical for researchers.

[00:23:48] Let's try to study these deviations. Microscopic deviations from the red line.

[00:23:55] At first, they're big and then they get smaller and smaller.

[00:23:59] To do this, we need to subtract the approximate value of the logarithm of the Fibonacci numbers from the list of true values of the logarithm of the Fibonacci numbers.

[00:24:14] The approximate values look like this, I remind you.

[00:24:19] Where x is n.

[00:24:23] And instead of x, we substitute Range[100], which is the first 100 natural numbers.

[00:24:29] And we get...

[00:24:33] We've fitted. It's clear that the difference in logarithms is small.

[00:24:37] At first, it jumps around, then it goes here.

[00:24:43] Honestly, it's not very good. Because then it will go away.

[00:24:52] Yes, it's not very good further.

[00:24:57] That is, it fitted it, but only in the vicinity of [0, 100].

[00:25:02] But in general, this fitting works poorly at infinity, it goes down.

[00:25:08] It's visible. And further, most likely, it takes arbitrarily small values.

[00:25:17] Okay, but now we'll take not the result of the fitting, but directly the logarithm of φ.

[00:25:25] Slap!

[00:25:26] Oh! That's different!

[00:25:29] A smooth curve.

[00:25:31] He knows φ with absolute accuracy.

[00:25:35] And here we used such a trick: that if you subtract one list from another, you get the difference of the lists.

[00:25:47] A list of differences.

[00:25:50] Now let's add the constant 0.3235 that we have obtained.

[00:25:58] More precisely, we need to do the following:

[00:26:01] Add 0.32 -> undershoot, cause we have negative numbers.

[00:26:05] Okay, let's write 0.325 here ->positive numbers,  it is overshoot.

[00:26:11] Okay, so we write 0.324 -> still overshoot...

[00:26:19] 0.323 -> undershoot.

[00:26:21] So between three and four...

[00:26:24] I write 0.3235.

[00:26:28] 0.3235 - this is an undershoot.

[00:26:31] 0.3237 - overshoot.

[00:26:35] 0.3236, 0.3235.

[00:26:42] Between 5 and 6, so I write 55.

[00:26:47] Next, 55 -> overshoot.

[00:26:52] I write 4...

[00:26:55] I write 3...

[00:26:59] I write 2...

[00:27:01] I write 1...

[00:27:05] Still the same. I write 0...

[00:27:10] There. Okay.

[00:27:12] I write 5 here -> undershoot.

[00:27:16] I write 7 here -> undershoot.

[00:27:19] I write 8 here -> overshoot.

[00:27:24] So between 7 and 8.

[00:27:26] Writing 75 -> overshoot.

[00:27:33] Writing 73... 71

[00:27:40] 71 - undershoot. So the next number is 5.

[00:27:45] Gradually, we are learning the truth about this constant.

[00:27:53] Even better than what fitting gave us earlier.

[00:27:58] Now Mathematica is starting to fail.

[00:28:02] So let's pause. Here is the constant.

[00:28:11] So we have calculated that Fibonacci numbers are approximately a geometric progression with a base of φ.

[00:28:20] The golden ratio is approximately 1.62.

[00:28:26] But there's a small correction:

[00:28:27] This number, which we put under an exponent with a minus sign,

[00:28:31] because the truth minus this thing,

[00:28:37] plus this constant, means that actually this constant is not with plus, but with minus.

[00:28:43] Alright.

[00:28:44] Here is the approximate value of Fibonacci numbers.

[00:28:48] Here are the first ten approximate Fibonacci numbers.

[00:28:52] Approximately 1, approximately 2, approximately 3, approximately 5,

[00:28:55] approximately 8, approximately 13, approximately 21, approximately 34.

[00:29:00] That's what we need!

[00:29:01] Round - a function that rounds to the nearest integer. Gives the truth.

[00:29:10] Oh, by the way, let's mark that all our F functions are Listable,

[00:29:14] so that we can create the same miracles with them as we do with logarithms, rounds, and so on.

[00:29:22] Round of a list equals: a list in which each element is rounded.

[00:29:28] Same with logarithms...

[00:29:32] And we want our function F to work the same way.

[00:29:35] To do this, we set the Listable attribute for the function F.

[00:29:39] And now we can write F[Range[20]] and get the answer for the whole range.

[00:29:44] Good!

[00:29:46] Now let's look at the errors that occur between our approximation and the true function F.

[00:29:57] They are small and seem to be approaching zero in absolute value.

[00:30:04] Excellent!

[00:30:07] By the way, now that we understand that the Fibonacci numbers are approximately a geometric progression,

[00:30:13] let's look for geometric progressions that exactly satisfy this relationship.

[00:30:19] We write "=", and get this equation.

[00:30:25] We can see that this can be reduced by m. We reduce it.

[00:30:31] And this is what we get.

[00:30:34] This can be simplified to obtain an equation.

[00:30:37] This is actually a quadratic equation.

[00:30:40] If you mentally multiply by λ, you'll see why it's quadratic.

[00:30:44] Let's solve this quadratic equation.

[00:30:46] Oh, we'll find out. This is what φ is.

[00:30:50] And what is this?

[00:30:52] I'll tell you a secret, the second number is "-1/φ".

[00:31:00] This is exactly equal to this second λ.

[00:31:12] Yes. True.

[00:31:16] The numerical solution to the equation looks like this: λ = -0.618034 and 1.618034

[00:31:32] Let's check...

[00:31:36] We need to simplify. FullSimplify will help us.

[00:31:39] True.

[00:31:40] We're beginning to see elements of paranoid programming.

[00:31:43] True.

[00:31:45] Is that right?

[00:31:46] True.

[00:31:49] Moving on.

[00:31:51] We've found two geometric progressions, two different λs,

[00:31:57] that fit the geometric progression pattern,

[00:32:02] so that the relation c[n] = c[n-1] + c[n-2] holds.

[00:32:12] By the way, the sum of two geometric progressions will also satisfy this recurrence relation.

[00:32:21] Proof: These three lines.

[00:32:25] If the first line is true and the second line is true, then the third line is also true,

[00:32:29] because the third line is the sum of the first two equalities.

[00:32:35] Let's try to find such a and b that...

[00:32:42] the zeroth element of this sum of geometric progressions

[00:32:45] and the first element are both equal to 1.

[00:32:50] That is, like the first two Fibonacci numbers.

[00:32:53] The answer is here.

[00:32:55] Let's write it as...

[00:32:58] " a " times the first geometric progression

[00:33:00] plus " b " times the second geometric progression.

[00:33:04] This is another explicit formula for the Fibonacci numbers.

[00:33:11] Let's check what it gives...

[00:33:14] Wow...

[00:33:16] And numerically...

[00:33:18] Numerically, it seems to be true.

[00:33:22] Now FullSimplify.

[00:33:23] FullSimplify is able to collapse this expression to completely accurate integers.

[00:33:32] And the F3 execution time is also microscopic.

[00:33:38] All right.

[00:33:40] Moving on.

[00:33:41] It's a complex topic, though.

[00:33:44] Let's draw the generating function for Fibonacci numbers.

[00:33:49] So, here are our Fibonacci numbers.

[00:33:51] And now, let's take powers of 1, x, x², and so on.

[00:33:56] And let's multiply them element-wise.

[00:33:59] This is done like this, as described here.

[00:34:03] We need to multiply and then add.

[00:34:06] " Plus @@ ", and to the right of " @@ " should be a list.

[00:34:13] In this list, commas are replaced by the operator Plus, which is to the left of " @@ ".

[00:34:21] So, we get...

[00:34:24] We element-wise multiplied the top and bottom lists up to 10.

[00:34:32] And we got the following polynomial of degree 10.

[00:34:37] This is the generating function for Fibonacci numbers.

[00:34:41] Well, if we continue to infinity, then this will be the generating function,

[00:34:47] but we took the first 10 elements.

[00:34:50] Let's pay attention to the next point.

[00:34:54] If we add the generating function with x multiplied by itself,

[00:34:59] we'll get this thing.

[00:35:02] And what will happen?

[00:35:04] What will happen with x⁵, for instance?

[00:35:06] For x⁵, we'll have 8x⁵ plus...

[00:35:13] and from the second bracket comes out a five.

[00:35:17] 5x⁴ multiplied by x, which will be 5x⁵,

[00:35:21] and 8 will be added to 5 to get 13.

[00:35:27] It will be 13. To do this, we need to execute the Expand function...

[00:35:36] Again, we get the generating function for Fibonacci numbers.

[00:35:42] Only it's shifted.

[00:35:47] Here we have 13x⁵, and before it was 13x⁶.

[00:35:58] So it turns out that we've divided by x.

[00:36:02] Let's write this down...

[00:36:06] We subtract 1 from g10 and divide by x.

[00:36:10] And we get this equation.

[00:36:14] Let's forget about the ten and imagine that it's an infinite series,

[00:36:19] and then the following identity will be true.

[00:36:20] Let's call the Solve function.

[00:36:23] Although it's not that hard to solve this mentally.

[00:36:26] We've obtained some function g[x], which is exactly this infinite series.

[00:36:36] Let's ask Mathematicia to compute this infinite series.

[00:36:44] There we go. We didn't make a mistake.

[00:36:48] By the way, note that from school math we know that

[00:36:55] 1/(1-q)=1+q²+q³, etc.

[00:37:02] The sum of a geometric series, if it goes to infinity, is equal to this expression.

[00:37:11] But here we have x + x² as q.

[00:37:14] Look, here we have something like one minus q, and q is x + x²,

[00:37:18] so we can write it like this.

[00:37:21] Interesting!

[00:37:24] Let's remember what (a+b)², (a+b)³, (a+b)⁴, etc. are equal to.

[00:37:30] Let's draw Pascal's triangle.

[00:37:35] And let's think about what is in this expression on the right side when x⁶ is present.

[00:37:44] In this Pascal's triangle, we have y = x², and x = x.

[00:37:52] So from this bracket (x + x²)⁶, we get x⁶,

[00:38:01] and all the other terms are not interesting to us.

[00:38:06] Right now, we are interested in the coefficient of x⁶.

[00:38:11] In this bracket, there will be a term x⁶.

[00:38:25] Oh, it's in this bracket here.

[00:38:31] This term 5x⁴y will be in this bracket. y = x². This gives us 5x⁶.

[00:38:40] Here we will find x⁶...

[00:38:46] at this point.

[00:38:48] x²y², y = x² This gives us x²x⁴,

[00:38:54] and here we also get six...

[00:38:57] And in the previous line, x⁶ is found here - y³.

[00:39:03] So, to get x⁶, we need to take:

[00:39:08] this term,

[00:39:10] this term,

[00:39:14] this term,

[00:39:16] and this term.

[00:39:20] The entire Pascal's triangle, all the terms shown here, are present on the right side.

[00:39:27] Because on the right side, we see the sum of all the rows of Pascal's triangle.

[00:39:36] And we've just shown that for x⁶, it will be 1 + 5 + 6 + 1

[00:39:45] Here, I've written it down.

[00:39:50] That is, the sum of the binomial coefficients (which are the coefficients in this triangle),

[00:39:57] that go diagonally like this, skipping every other one,

[00:40:04] the sum of these coefficients is equal to the Fibonacci number.

[00:40:11] You can check this, for example, for the previous x⁵.

[00:40:15] 1 + 4 + 3

[00:40:22] Here there is no

[00:40:23] 1 + 4 + 3 = 8 Indeed, the previous Fibonacci number is 8.

[00:40:33] Moving on...

[00:40:39] Let's note that if we replace the minus sign with a plus sign, we will get the same series, but alternating in sign.

[00:40:48] Interesting!

[00:40:49] What if we now multiply these two expressions?

[00:40:54] Here's what we get.

[00:40:59] We can notice the following:

[00:41:01] that the first expression is (1-x²)-x, and the second expression is (1-x²)+x.

[00:41:12] We get that this is the square of the first minus the square of the second.

[00:41:16] And then a little trick: subtract one and add one.

[00:41:24] This is very similar to what happened if we take 1-x² as "y"

[00:41:35] Let's see what the expansion of this product is...

[00:41:42] and in this expansion, we will recognize the Fibonacci numbers.

[00:41:47] What does this imply?

[00:41:49] We've just had an interesting observation.

[00:41:53] To understand what this implies, we need to learn how to multiply two generating functions.

[00:41:58] Let's say we have two generating functions with some coefficients.

[00:42:02] One with coefficients "a", and the other with coefficients "b".

[00:42:07] Let's think about what will happen at x⁶ when we multiply the first one by the second one.

[00:42:14] Firstly, x⁶ will be obtained when we multiply a[0] by x⁶b[6].

[00:42:22] Secondly, we can multiply xa[1] by x⁵b[5].

[00:42:29] Thirdly, we can multiply x³a[3] by x³b[3].

[00:42:37] Fourthly, x⁴a[4] can be multiplied by x²b[2].

[00:42:42] And so we get...

[00:42:46] that at x⁶, we get this expression.

[00:42:49] This expression is called the convolution of the first 6 elements of the series "a", and the first 6 elements of the series "b".

[00:43:00] We are multiplying two generating functions here,

[00:43:07] the first of which has coefficients "a" - these are Fibonacci numbers,

[00:43:11] and the second of which has coefficients that are Fibonacci numbers with alternating plus and minus signs.

[00:43:21] So, we write it like this...

[00:43:24] At x⁶ we will have F[0] * F[6] - F[1] * F[5] + F[2] * F[4] - F[3] * F[3] and so on.

[00:43:36] Let's calculate...

[00:43:37] 21 is a Fibonacci number, I recognize it.

[00:43:40] And if we take the same convolution for the first five, we get 0.

[00:43:45] So...

[00:43:46] We can write all of this in the form of a table F[n-k] * F[k].

[00:43:52] And here comes the alternating sign.

[00:44:00] Let's calculate the convolution function of Fibonacci numbers

[00:44:07] with the alternating sign sequence of Fibonacci numbers.

[00:44:11] We get a remarkable result.

[00:44:15] We see Fibonacci numbers, in which some are missing, replaced by zeros.

[00:44:23] In essence, we have proved a certain identity.

[00:44:27] The convolution of Fibonacci numbers with itself and alternating signs is equal to Fibonacci numbers again.

[00:44:38] So...

[00:44:40] Next it's more difficult...

[00:44:44] Derivatives are being checked...

[00:44:48] Let's take the derivative of our generating function

[00:44:53] By the way...

[00:44:55] How are our viewers doing?

[00:44:59] Smoking...

[00:45:00] Smoking nervously...

[00:45:03] Okey, not nervous. The look is quite positive.

[00:45:08] Great!

[00:45:10] This is wonderful!

[00:45:12] The derivative of our generating function is this,

[00:45:18] and the square is this.

[00:45:21] They are similar in some way. The denominator of both is a square.

[00:45:26] Let's take the first one...

[00:45:28] Ah! Note that the first one has -2x.

[00:45:32] Or rather, +2x, because there's a minus sign in front.

[00:45:35] Let's subtract 2x from G' to get rid of this 2x.

[00:45:40] What will we get?

[00:45:42] Oh!

[00:45:43] We'll get something very simple.

[00:45:44] This is just the square of G, let's write it down.

[00:45:47] G'[x] - 2xG[x]² == G[x]²

[00:45:54] This is a differential equation that the generating function G satisfies.

[00:46:05] Checking...

[00:46:06] G[x]²

[00:46:09] G[x]² yields: 1, 2, 5, 10, 20, 38...

[00:46:15] And if we take 1+2x,

[00:46:17] 1, 4, 9, 20, 40...

[00:46:20] Here's G',

[00:46:24] Here's G prime, 1, 4, 9, 20, 40

[00:46:25] It matches!

[00:46:27] So it is indeed true that (1+2x)G[x]² = G'[x]

[00:46:33] But what does this imply?

[00:46:37] It implies the following:

[00:46:38] G[x]² yields the Fibonacci convolution coefficients with itself, without alternating signs.

[00:46:49] For example, one term will be 38.

[00:46:53] And another term will be 71.

[00:46:57] And it says that if we add these two series,

[00:47:03] we will get something interesting.

[00:47:05] Let's check.

[00:47:06] So first let's define the Fibonacci convolution without alternating signs.

[00:47:14] Let's write it as Listable, so we can perform ConF on a list.

[00:47:21] (38, 71) That's what we need. That's what we got above.

[00:47:26] Now let's multiply the numbers N by the Fibonacci numbers.

[00:47:32] So the first Fibonacci number times 1.

[00:47:33] The second Fibonacci number times 2,

[00:47:37] The third Fibonacci number times 3,

[00:47:40] The fourth Fibonacci number times 4, and so on.

[00:47:45] Now let's add our сonvolutions of convolutional coefficients

[00:47:51] plus the doubled list of convolution coefficients, but shifted.

[00:47:59] Or is it better vice versa...

[00:48:02] Twice the unshifted plus one shifted.

[00:48:07] We get 4, 9, 20, 40, 78...

[00:48:12] It matches!

[00:48:14] We have found that N times F of N equals this convolution expression.

[00:48:25] By the way, another interesting observation about the generating function...

[00:48:29] Let's do this.

[00:48:32] What is the series equal to at x equals 1? Not x equals 0, but x equals 1?

[00:48:40] Here we see Fibonacci numbers again.

[00:48:43] Only every other one is missing...

[00:48:47] Every other Fibonacci number is missing and the signs alternate.

[00:48:52] And at x equals -1,

[00:48:56] 1, -1, 2, -3, 5, -8...

[00:49:00] Here they are not missing, but the signs alternate.

[00:49:05] What do you think follows from this?

[00:49:09] And finally...

[00:49:12] Let's draw the function 1 over G of x,

[00:49:16] and also draw the value of this function G of x on the complex plane.

[00:49:27] Here we have two poles at the points...

[00:49:35] As far as I know, 1/φ and -φ (phi).

[00:49:40] This is negative phi on the real axis,

[00:49:45] and this is 1/φ.

[00:49:53] That's all for today. Stay tuned for bonus tracks!

[00:49:57] Goodbye, everyone!
