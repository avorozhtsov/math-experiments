# 3:  Картинки про умножение. Умножение "по модулю" (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [HSlG4S5G3r8](https://www.youtube.com/watch?v=HSlG4S5G3r8). Получено: 2026-10-08T17:44:04+01:00.

[00:00:01] Hello!

[00:00:02] This is the "Mathematical Experiments" podcast.

[00:00:04] Today we will experiment with multiplication.

[00:00:06] We'll draw these beautiful pictures.

[00:00:08] This picture is the multiplication table of 141 x 141.

[00:00:12] This is multiplication by 2.

[00:00:13] This is multiplication by 3.

[00:00:15] By 6.

[00:00:16] This is some other number.

[00:00:18] And this seems to be multiplication by -2.

[00:00:21] Let me explain how we got this picture.

[00:00:25] Take n points on a circle.

[00:00:28] Here, I took 41 points.

[00:00:30] Let's number them 0, 1, 2, 3, 4, and so on.

[00:00:35] Let's do a simple action:

[00:00:37] connect 1 with 3,

[00:00:39] 2 with 6.

[00:00:41] And let's connect point "x" with point "3x".

[00:00:45] 3 connects with 9,

[00:00:47] 4 with 12,

[00:00:49] 5 with 15, and so on.

[00:00:52] 12 connects with the number 36,

[00:00:54] 13 with the number 39,

[00:00:57] and we need to connect 14 with the number 42,

[00:01:01] but there is no number 42 here.

[00:01:04] You probably guessed it. We need to take the number 1 because 42 locates in the number 1.

[00:01:09] We are kind of numbering further

[00:01:11] 40,

[00:01:12] 41, 42, 43, 44, 45, 46, and so on around the circle.

[00:01:19] Think that all natural numbers locate on this circle.

[00:01:23] This picture is different from the one on the right because it has 141 instead of 41.

[00:01:32] Now things get interesting.

[00:01:34] If you've seen the pictures above somewhere before,

[00:01:38] you're likely seeing these pictures for the first time.

[00:01:41] Okay... Let me try to explain in detail how to get these pictures.

[00:01:46] Let's draw them and take a look.

[00:01:50] Here's a big mouse.

[00:01:52] Here's a weirdo.

[00:01:54] Here's a star.

[00:01:55] And here's an eared one.

[00:01:57] It's some kind of coat of arms pattern.

[00:02:00] They are obtained in a similar way,

[00:02:01] only we connect not "x" and "3x", but two points x and y such that their product is 1.

[00:02:09] Let's do it. 3 * 14 = 42, and 42 locates in unity.

[00:02:15] 2 * 21 also gives 42 and so on.

[00:02:20] Here all the segments are connected with pairs of x and y such that their product is 1.

[00:02:28] And here the same thing is done for the number 70,

[00:02:31] when we put 70 points on a circle and connect pairs whose product locates in the point 1.

[00:02:41] Here we have some unusual "whiskers"... let me explain.

[00:02:45] Some pairs of x and y consist of the same number x, that is x, x.

[00:02:48] For example, 1. 1*1 equals 1.

[00:02:52] Here, 40 * 40 also equals 1, because it's like -1 * -1.

[00:03:03] Moving on.

[00:03:04] So we got these segments that connect inverse elements.

[00:03:08] What do we do next?

[00:03:10] Next, we simply move along the circle and take these segments as they appear.

[00:03:18] First, we take the segment that connects 2 and 21.

[00:03:21] This segment is here.

[00:03:23] Then we take the segment that connects 3 and 14.

[00:03:26] This segment is here.

[00:03:27] It's like very reduced here.

[00:03:29] Here it's big, and here it's small.

[00:03:34] Then we come to the number 4.

[00:03:37] From 4, the segment goes to 31.

[00:03:40] This segment here.

[00:03:41] And so on.

[00:03:42] So we move along the circle,

[00:03:44] encounter the end of the segment and draw it,

[00:03:47] starting from the point where we are at the moment.

[00:03:50] As a result, we get this closed curve.

[00:03:55] A closed broken line.

[00:03:57] Why is it closed?

[00:03:59] It's very simple here.

[00:04:00] We take each segment twice, first in one direction, then in the other.

[00:04:04] And that's why in the end we will end up in the same point where we started.

[00:04:09] Well, here... look.

[00:04:11] First comes this segment.

[00:04:14] Here it is.

[00:04:15] Then this segment.

[00:04:18] Here it is.

[00:04:20] The next segment from 11 to some number (not visible here).

[00:04:25] Here it is.

[00:04:26] And so on.

[00:04:32] And here is the image for the number 213.

[00:04:36] Next, I want to show the code that can generate all of this.

[00:04:39] You can quickly look through it without stopping,

[00:04:42] and then, if desired, go back and meditate on individual pieces of code.

[00:04:48] This is how you can draw a circle.

[00:04:50] If desired, you can specify the center and radius of the circle.

[00:04:54] By default, it has the value [{0, 0}, 1].

[00:04:58] I draw the points using the ListPlot function,

[00:05:01] and the coordinate pairs using the Table function.

[00:05:03] And a pair of coordinates on the circle is the cosine and sine.

[00:05:07] In fact, this is the definition of the cosine and sine functions.

[00:05:10] These are the coordinates of a point on the circle,

[00:05:13] where φ is the length of the rope that we tied to the point on the far right.

[00:05:19] We stretched this rope along the circle.

[00:05:21] We stopped when the rope ran out, and looked at the coordinates of the points - these are the coordinates of cos(φ) and sin(φ).

[00:05:29] Here below is a visualization of this idea using ParametricPlot.

[00:05:36] The length of the rope is controlled by a slider here.

[00:05:41] For clarity, the radius is constantly slightly increasing.

[00:05:47] And we see individual coils.

[00:05:49] But in reality, imagine that the rope is infinitely thin and is wound directly on the circle.

[00:05:55] The next point...

[00:05:58] Well, this is also a visualization of how points gradually appear as we move the slider.

[00:06:03] If desired, you can put labels on each point.

[00:06:08] This is done using the Labeled function.

[00:06:12] So we're gradually moving forward...

[00:06:19] Here's a trick, like this.

[00:06:22] If you remove it, you get the following picture...

[00:06:28] We'll keep moving, moving...

[00:06:33] And on the second loop, new labels won't appear, but old ones will disappear.

[00:06:38] The thing is, points are drawn on top of each other and it doesn't know which label to draw.

[00:06:44] To prevent this, we slightly change the coordinates of the points that belong to the second loop.

[00:06:51] And it turns out well.

[00:06:58] It somehow chooses the location of these labels in a less than ideal way.

[00:07:02] The Mod function is responsible for calculating the remainder of division in Mathematica.

[00:07:06] Mod[m, n] gives the remainder of dividing m by n.

[00:07:10] Let's take a look at these remainders.

[00:07:18] The remainder of dividing 17 by 5.

[00:07:21] It's like finding the nearest number that is divisible by 5 (which is 15) and seeing how much needs to be added to 15 to get 17.

[00:07:28] 2. Answer: 2.

[00:07:31] When you want to see what the remainder of dividing the product of two numbers is,

[00:07:36] you can do this trick,

[00:07:37] instead of the original (larger) numbers, take the remainders of division and multiply the remainders themselves.

[00:07:44] They are usually smaller and therefore require less computation.

[00:07:49] The same answer will be obtained.

[00:07:50] So instead of the actual numbers, we could take their remainders when divided by 5.

[00:07:58] This is especially clear when you act in modular arithmetic modulo 1000 or 100.

[00:08:06] The thing is, the remainder of division by 100 is the last two digits of the decimal representation.

[00:08:12] 1000 is the last three digits.

[00:08:15] And most people know that to find the last three digits of a product,

[00:08:20] you just need to take the last three digits of each number and multiply them.

[00:08:25] Here are two large numbers.

[00:08:27] We multiplied them and took the remainder of division by 1000.

[00:08:31] Then we multiplied the remainders of division by 1000.

[00:08:35] And took the remainder of division of the product of remainders.

[00:08:38] All four expressions end in 236.

[00:08:43] Let's write this out in words.

[00:08:46] Big numbers a and b, small numbers as, bs.

[00:08:51] The remainder of division of the product of big numbers is equal to the remainder of the product of small numbers.

[00:08:56] This is how you can write it.

[00:08:59] Well... clear.

[00:09:00] Here it took specific values of a, b, and p.

[00:09:03] So what it wrote as True is not that interesting.

[00:09:07] This is true for specific three numbers.

[00:09:08] But is it true in general?

[00:09:10] You can also ask such questions in Mathematica.

[00:09:13] To do this, you need to use the Reduce function.

[00:09:17] Reduce takes an expression as its first argument,

[00:09:21] then you need to specify the variables,

[00:09:23] for which you want to simplify this expression,

[00:09:28] and specify the range of numbers in which you act.

[00:09:32] I wrote Integers here, which means a and b are integers.

[00:09:36] And it gave me this answer:

[00:09:39] both a and b belong to integers.

[00:09:42] This letter "Z" means integers.

[00:09:45] This symbol is read as "belongs to".

[00:09:47] The vertical bar is an alternative.

[00:09:50] It can be read as:

[00:09:52] each of the numbers a and b belongs to the integers.

[00:09:56] This is all that is required for this identity to hold.

[00:10:01] That is, it is true for any numbers a and b.

[00:10:04] Here's an alternative way to show why it's enough to take remainders when you're computing a product's remainder.

[00:10:11] Let's say there are two numbers:

[00:10:13] one has a remainder k1, that is, this number is expressed as k1 plus something that is divisible by 5,

[00:10:20] and the other number has a remainder k2, and it is expressed as k2 plus something that is divisible by 5.

[00:10:26] Then, after we expand the brackets, it's evident that the result contains k1 * k2 plus something that is divisible by 5.

[00:10:36] And we're not interested in that. We're only interested in k1 * k2.

[00:10:39] When we want to calculate the remainder of dividing all of this expression by 5.

[00:10:45] Let's check if Reduce can help us here.

[00:10:48] Yes, Mathematica can also simplify such expressions.

[00:10:53] Finally, let's move on to the multiplication table.

[00:10:56] Let's start with the addition table.

[00:10:59] Here's the addition table modulo 5.

[00:11:03] You can put 19 here and the table will be bigger.

[00:11:07] The addition table looks very simple.

[00:11:10] The same numbers are on the diagonals.

[00:11:14] There are no numbers greater than 18 in this table.

[00:11:18] That's understandable.

[00:11:20] Now, the multiplication table.

[00:11:29] Multiplying by 0 gives 0.

[00:11:31] Multiplying by 1 leaves all numbers as they are.

[00:11:35] It can be seen that the table is symmetric with respect to the diagonal.

[00:11:42] Let me try to define a numerical field using these two tables.

[00:11:47] The addition table and the multiplication table.

[00:11:50] Let's say we have a finite set of elements.

[00:11:53] I will define a finite numerical field for them.

[00:11:56] Let's say we have some finite set of elements.

[00:12:00] And someone has provided addition and multiplication tables for them.

[00:12:04] By hand.

[00:12:05] And I say, if these tables are good enough, then this set of elements can be called a numerical field.

[00:12:13] What does that mean? What does "good enough" mean?

[00:12:19] First of all, both tables must be symmetric with respect to the diagonal.

[00:12:24] If we reflect with respect to this diagonal, we get the same table.

[00:12:31] The second point is:

[00:12:33] two elements must be selected: 0 and 1

[00:12:36] We will call 1 "zero",

[00:12:38] the other element we will call "one".

[00:12:40] Zero is an element that, when added to x, gives x.

[00:12:45] Let it be the first element.

[00:12:47] This means that the first row in the addition table should repeat the elements themselves,

[00:12:52] which we implicitly arranged at the top and left.

[00:12:58] The second highlighted element is one.

[00:13:01] Multiplying by one should repeat everything.

[00:13:03] Let it be the second element, which means that in the second row all the elements should be repeated,

[00:13:08] which are implicitly arranged up here.

[00:13:12] Since both tables are symmetric with respect to the diagonal,

[00:13:15] this means that the second column repeats all the elements that are here on the left.

[00:13:22] The next important property:

[00:13:24] is that multiplying by 0 gives 0.

[00:13:26] This means that the first row and column of the multiplication table are entirely zeros.

[00:13:33] Such an unusual definition for tables.

[00:13:36] Tables must be symmetric with respect to the diagonal.

[00:13:39] The multiplication table should consist of the first row of zeros,

[00:13:43] the second row repeating all elements.

[00:13:46] And the addition table should have a repetition of all elements in the first row.

[00:13:53] And that's not all.

[00:13:55] It is also necessary for each row to contain all the elements.

[00:13:59] In both the addition and multiplication tables, each row and column must contain all field's elements.

[00:14:08] There is one more important property that cannot be expressed/described using tables.

[00:14:13] This is the distributivity property.

[00:14:15] Here it is written at the bottom. (here is a mistake, right will be: a(b + c) = ab + ac)

[00:14:18] If addition and multiplication are such that this identity holds, (here is a mistake, right will be: a(b + c) = ab + ac)

[00:14:24] then, together with the previous properties, we obtain a numerical field.

[00:14:31] Let's write the addition table in color.

[00:14:37] To do this, we will use the ArrayPlot function.

[00:14:41] As we increase the value of P, we get this image.

[00:14:50] Let's recall what our addition table looked like.

[00:14:52] There was a gradual increase as we approached this diagonal,

[00:14:56] then a switch to zero and growth again.

[00:15:03] Here, our zero corresponds to white,

[00:15:06] and 18, if we live modulo 19, to black.

[00:15:12] Here are zeros, ones, twos, threes, and so on.

[00:15:18] We can do the following trick.

[00:15:21] These numbers are arranged on a circle.

[00:15:25] And the numbers 18 and 0 are very close.

[00:15:28] I would like their colors to be close as well.

[00:15:31] To do this, I use ColorFunction and define it as follows.

[00:15:37] Hold on a sec... Let me first show you the result.

[00:15:40] There. I made it so that 18 and 0 have similar colors - green.

[00:15:46] This was done as follows:

[00:15:48] I wrote that ColorFunction is RGBColor,

[00:15:51] which takes the amount of red, green, and blue components.

[00:15:57] As a hash, a number from zero to one is substituted, it seems.

[00:16:01] Zero corresponds to the minimum value, and one to the maximum.

[00:16:05] So I made that the color red is Sin[Pi#]^2,

[00:16:09] and green is Cos[2Pi#]^2.

[00:16:13] I got such a color profile.

[00:16:17] Let's fix this function and use it to get an image of multiplication.

[00:16:24] A multiplication table in color.

[00:16:27] This number is 104...

[00:16:29] 105...

[00:16:30] Let's move step by step.

[00:16:35] For even numbers, we have a green cross in the center.

[00:16:42] For odd numbers, it's purple.

[00:16:46] As the number P increases, the picture becomes thinner and thinner.

[00:16:55] Okay!

[00:16:56] In addition to the addition and multiplication tables, there is one more very interesting table - the power table.

[00:17:03] Let's draw it.

[00:17:06] Here it is.

[00:17:08] It is structured as follows:

[00:17:11] at the top are numbers that correspond to points on the circle.

[00:17:15] Here we placed 13 points on the circle.

[00:17:19] And then we do the following operation:

[00:17:22] for example, the column for two.

[00:17:25] We multiply each subsequent element by 2.

[00:17:30] 2 * 2 = 4, 4 * 2 = 8, 8 * 2 = 16

[00:17:34] 16 on the circle, where 13 points is 3.

[00:17:38] 3.

[00:17:39] Then we multiply by 2 again - 6.

[00:17:42] And so on...

[00:17:44] Here for three, it's like powers of three.

[00:17:48] Here are powers of four.

[00:17:51] What do we see?

[00:17:54] We see a pattern.

[00:17:55] In the last row, which is -1, there are all ones.

[00:18:01] And, by the way, if we continue the powers,

[00:18:04] (This j is our variable. Let's say we write +5 lines.)

[00:18:10] then we will see that it continues repeating 1, 2, 3, 4, 5, 6, 7, 8, 9, etc... The first row repeats.

[00:18:18] That's why I stopped at P - 1.

[00:18:22] There's no point in drawing further.

[00:18:24] Let's draw a power table in color.

[00:18:27] Just add a little manipulation:

[00:18:30] We multiply I^j by a and add b.

[00:18:34] When a = 1 and b = 0, it's just i^j.

[00:18:44] Here's what we see.

[00:18:47] Modulo 67, we see a picture with some structure.

[00:18:54] Here, we can see a bright green solid stripe.

[00:18:59] If we start increasing P, we get all sorts of patterns.

[00:19:12] When P is prime, the pattern is not so regular.

[00:19:16] The only thing we see for prime P is a horizontal line somewhere in the middle.

[00:19:22] But if we change "a", then sometimes we can see some additional structure.

[00:19:30] Like here.

[00:19:31] Separating horizontal lines and two vertical ones.

[00:19:37] That's to say, the multiplication by "a" somehow changes the palette and allows us to see the structure.

[00:19:47] Changing "b" is a simpler thing.

[00:19:51] It just cycles through the palette.

[00:19:56] "a" acts more complexly.

[00:20:03] It is the "a" that allows us to see the hidden structure.

[00:20:10] Let's look at our table of powers again in numbers.

[00:20:15] What is that line in the middle for prime numbers?

[00:20:20] Here it is. Here we have the numbers 1 and 18.

[00:20:26] Alright.

[00:20:27] Let's define the function Mod2, which will return -1 instead of 18.

[00:20:35] Because 18 just corresponds to moving in another direction by one segment.

[00:20:44] Let's calculate the Mod2 remainders.

[00:20:47] These are again remainders of division by 19, only instead of large remainders we see remainders with a minus sign.

[00:20:55] Mod2 chooses the remainder with the minimum absolute value.

[00:20:59] With a plus or minus sign.

[00:21:02] Let's draw a table of powers using Mod2.

[00:21:06] And here we see ones and minus ones,

[00:21:09] and here ones.

[00:21:12] Thus, we have discovered two facts:

[00:21:15] The P - 1 row in the table of powers consists of ones - this is called Fermat's Little Theorem.

[00:21:22] And the P - 1/2 row in the table of powers consists of ones and minus ones.

[00:21:28] We will come back to these statements and perhaps even prove them.

[00:21:34] The use of the Mod2 function allows us to see a simple, obvious, and in principle, regularity.

[00:21:40] If we ignore the minus signs in this table, we will see that the lower part of the table repeats the upper part.

[00:21:49] And indeed. Here are 3, 9, 8, 5.

[00:21:53] Here are -3, -9, -8, -5.

[00:21:58] These are opposite to the numbers that give -1 in the middle.

[00:22:03] And those that in the middle give one away...

[00:22:05] already, there was a repetition without discarding -1.

[00:22:10] The sequence 4, -3, 7, 9 is repeated by the sequence that follows the line P - 1/2.

[00:22:19] 4, -3, 7, 9

[00:22:23] We will come back to the study of power tables later.

[00:22:26] But now let's move on to another visualization of multiplication.

[00:22:32] There is a video on YouTube: Times Tables, Mandelbrot and the Heart of Mathematics.

[00:22:37] I recommend everyone to watch it.

[00:22:40] That's where this visualization is actually shown.

[00:22:44] Let's repeat it.

[00:22:46] Let's start by visualizing the addition of three.

[00:22:50] Let's say we have a number n.

[00:22:53] It is represented by this point.

[00:22:56] Let m be equal to n + k.

[00:22:59] It is represented by this point.

[00:23:01] By the way, we didn't need to write Mod here because Cos and Sin themselves perform the mod operation.

[00:23:08] Implicitly.

[00:23:10] Next, we output the segment (p1, p2). p1 is a point. p2 is a point.

[00:23:16] And we perform this operation (calculating the segment (p1, p2)) for the most different values of n.

[00:23:23] This is what we get.

[00:23:26] Here's the point n. We added 3 to it and got the point m.

[00:23:33] Let's repeat this operation, but manipulate the variable k.

[00:23:42] Increase k...

[00:23:45] we get these images.

[00:23:48] We can also increase p.

[00:23:54] And this is what we get.

[00:23:58] Moving on.

[00:24:01] Next up, multiplication.

[00:24:04] We replace addition with multiplication...

[00:24:07] And draw.

[00:24:08] Here's multiplication by 3 modulo 17.

[00:24:15] We put it inside the Manipulate function.

[00:24:18] Here we allow k to be a decimal and step by 0.1 instead of 1.

[00:24:25] Let's see what we get.

[00:24:29] We increase...

[00:24:31] Gradually increase k...

[00:24:34] We see the birth of a cardioid...

[00:24:38] We got a cardioid.

[00:24:40] Move on...

[00:24:51] We went through the nephroid...

[00:24:57] Here's the curve with three petals.

[00:25:06] We can run Animate and get an animation of this process.

[00:25:14] Although it happens too fast.

[00:25:17] You can play with these pictures yourself.

[00:25:20] Check out the links in the description.

[00:25:28] Let's choose a triplet.

[00:25:32] And gradually increase p, starting with the number 10.

[00:25:52] A nephroid gradually appears.

[00:26:02] And here's the same thing but with labels.

[00:26:12] There's a video on YouTube showing an animation of gradually increasing the number k.

[00:26:17] It's very beautiful! I recommend it to everyone.

[00:26:20] The link is in the description.

[00:26:22] That's all for today.

[00:26:23] In the next video, we'll learn how to draw these pictures.

[00:26:27] We'll also learn what the inverse element is

[00:26:29] and prove that if p is prime, then there is an inverse element for any number n.

[00:26:34] We'll also get to know the Legendre symbol and learn how to compute it.

[00:26:39] Goodbye!
