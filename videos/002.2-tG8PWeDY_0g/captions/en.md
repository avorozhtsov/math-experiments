# 2. Бонус 2. Комплексные числа и преобразования плоскости. Красота – страшная сила (English subs)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [tG8PWeDY_0g](https://www.youtube.com/watch?v=tG8PWeDY_0g). Получено: 2026-10-08T17:44:08+01:00.

[00:00:01] Welcome back, Artem Vorozhtsov is in touch and this is a bonus track #2 on Fibonacci numbers.

[00:00:07] While working with Fibonacci numbers, we obtained the following image:

[00:00:09] A rectangle from which we cut a square on the right,

[00:00:13] then a square on top,

[00:00:14] then another square on the right,

[00:00:16] then another square on top, and so on.

[00:00:19] We obtained a rather beautiful image,

[00:00:22] but I want to obtain this image:

[00:00:25] It is directly related to this one.

[00:00:30] Well, not really, but we'll see...

[00:00:33] First, let's clear all the variables we used before. Todays goal is to understand what complex numbers are.

[00:00:41] Complex numbers.

[00:00:45] They emerge when we introduce the number "i", equal to √-1.

[00:00:49] Look, i^2 = -1

[00:00:53] Amazing! Can you believe it?

[00:00:56] Let's introduce such an "i". If no contradictions arise, then It's legit!

[00:01:04] Our numbers will have this form:

[00:01:08] a1 + i * b1.

[00:01:12] Then their product will be equal to this expression.

[00:01:17] a and b are ordinary numbers, real. Integer, fractional... it doesn't matter.

[00:01:23] Product...

[00:01:25] Mathematica didn't tell us anything new here.

[00:01:29] To make it do some work, we need to call the Expand function.

[00:01:32] And then we can see.

[00:01:34] It expanded.

[00:01:36] And take note:

[00:01:38] Instead of b1b2*i^2, we see -b1b2 here.

[00:01:44] And everything else is the expected result.

[00:01:49] ComplexExpand.

[00:01:51] So, what ComplexExpand did was to separate the terms without "i" from the terms with "i".

[00:02:00] And what is 1/i equal to?

[00:02:03] -i.

[00:02:04] Indeed, "i" times "-i" equals 1.

[00:02:14] Because this equals -i^2,

[00:02:19] and i^2 equals -1. Two negatives make an affirmative.

[00:02:24] So, this means that the inverse of "i" is "-i",

[00:02:28] and the inverse of "-i" is 1.

[00:02:33] Well, you can test it by yourself...

[00:02:35] For example, let's take (i+1)^2 - it turns out to be equal to 2i.

[00:02:43] You can check this yourself.

[00:02:45] Let's subtract 2(i+1) from (i+1)^2 to remove that 2.

[00:02:52] The result is -2.

[00:02:53] Now let's add 2.

[00:02:55] The result is 0.

[00:02:57] Look, if we designate the expression in parentheses as x, we get x^2-2x+2=0.

[00:03:06] If you calculate the discriminant of this quadratic equation, you get a negative number.

[00:03:11] You're taught that there are no numbers that satisfy this equation.

[00:03:17] But in complex numbers, there are answers.

[00:03:20] One of the answers is "1+i", and the other answer is "1-i".

[00:03:25] You can check this.

[00:03:27] Now, what is the inverse of 1/(1+i)?

[00:03:31] Indeed!

[00:03:32] Let's check it.

[00:03:33] We multiply "1+i" by this value and get the answer.

[00:03:39] This is not difficult to do mentally.

[00:03:41] We factor out 1/2 from the first multiplier.

[00:03:46] We get 1-i.

[00:03:49] So we've got this bracket sorted out.

[00:03:51] And we need to multiply by 1+i.

[00:03:56] We multiply this using the difference of squares formula.

[00:04:00] We get: 1/2(1^2 - i^2).

[00:04:09] But this is equal to...

[00:04:11] You've probably already guessed it, it's equal to 1/2 * 2

[00:04:15] Because i^2 = -1. Two negatives make an affirmative.

[00:04:22] So!

[00:04:24] These complex numbers are going to come in handy.

[00:04:27] We want to interpret points on the plane as complex numbers.

[00:04:34] We'll interpret a point (x, y) as the number x + iy.

[00:04:43] That's the main idea.

[00:04:45] And the squares we've broken the rectangle into are kind of like a set of points on the complex plane.

[00:04:52] The vertices of these squares, and all points in general, are complex numbers.

[00:04:56] Here's the definition of the function SplitToSquares.

[00:05:02] Let's repeat the calculations we had in the original form.

[00:05:06] Only this time, we'll add a function called ToPolygon.

[00:05:09] Instead of squares, we'll draw polygons.

[00:05:13] Polygons are basically rectangles.

[00:05:15] Previously we drew a rectangle by specifying the bottom left corner and the top right corner.

[00:05:23] But a polygon, that is, a closed broken line, consists of points.

[00:05:31] It is assumed that the last point is connected to the first.

[00:05:35] We call the SplitToSquares function

[00:05:38] and then use the ToPolygon function to transform each square from this representation

[00:05:44] to this.

[00:05:47] So far, we haven't gotten anything new,

[00:05:50] but soon we will.

[00:05:51] Let's define a function that takes a point (a, b pair) and makes it a complex number.

[00:05:57] And vice versa,

[00:05:59] the FromZ function that takes a complex number Z and makes it a point on the plane.

[00:06:04] The X coordinate is obtained using Re.

[00:06:08] The part "a" is called "Re" - the real part of the complex number.

[00:06:12] And "b" is obtained using the "Im" function - the imaginary part of the complex number Z.

[00:06:19] Let's check how this all works...

[00:06:22] It works like this.

[00:06:25] Good.

[00:06:26] PointT is a point transformation function using the function F.

[00:06:35] We use the ToZ function to turn the point P into a complex number.

[00:06:43] We apply the F function to the complex number, and then obtain a point from the result.

[00:06:50] For example, let F be the square function.

[00:06:55] The squared hash (#^2) and ampersand symbol mean the function of the hash, which raises the number (the hash) to the second power.

[00:07:05] Then we get something like the square of the number (aa + ibb)^2,

[00:07:12] from which we take the real and imaginary parts.

[00:07:15] Good.

[00:07:17] We also need a Range, which has a third argument - the step with which we move from the first point to the last.

[00:07:25] The next function is PointsBetween,

[00:07:28] which creates intermediate points between points x1, y1, and x2, y2.

[00:07:38] I won't go into this definition, explaining what's happening here.

[00:07:43] I hope you'll understand the essence through examples.

[00:07:49] Here's a case where we have point x1, y1, point x2, y2,

[00:07:53] and we place another point exactly in the middle of the segment connecting point x1, y1 and point x2, y2.

[00:08:02] What I want to do?

[00:08:03] I want simply draw a polygon with a hundred points on each side instead of this square of four points,

[00:08:13] and then transform each point.

[00:08:17] Of course, I could take the four points of the square and only transform them,

[00:08:21] but the thing is that it's incorrect to say that the transformation of a segment will again be a segment.

[00:08:29] Therefore, to see where the entire side will be mapped to, I place many, many points on this side and transform each point.

[00:08:41] So, here I want to explain how Mathematica works, it can do things like this.

[00:08:46] When you add pairs, it simply adds them element-wise.

[00:08:50] When you multiply a pair by a number, it simply multiplies each element of the pair by that number.

[00:08:56] And it's thanks to this trick that the definition given here works.

[00:09:03] So.

[00:09:04] In the metafunction ToPolygon, I want to write a function ToDetailedPolygon,

[00:09:08] where each side of the polygon is elaborated in detail.

[00:09:12] There are 100 points on each side.

[00:09:16] From the perspective of drawing the polygon, this is meaningless as long as it remains a rectangle.

[00:09:20] But when we start to transform it, it immediately becomes meaningful.

[00:09:24] As the function F[z_], I took simply z.

[00:09:28] F[z_] = z, a function that does nothing, so the squares remained squares.

[00:09:33] But let me square it now.

[00:09:36] There! Something interesting already.

[00:09:39] By the way, in Mathematica, as far as I know, you can take this result,

[00:09:45] click right on it...

[00:09:47] Slap!

[00:09:49] Yes. And even start moving it around.

[00:09:51] See? The red square turned into something that is not a square at all.

[00:09:57] But into some sort of shape.

[00:09:59] The boundary looks like a parabola.

[00:10:02] This boundary remained. Just as it was a segment, so it remained.

[00:10:05] It changed, but it remained a segment.

[00:10:09] This also looks like a parabola.

[00:10:11] This is also a piece of a parabola.

[00:10:12] And this is a piece of a parabola.

[00:10:13] Interesting!

[00:10:16] Moving on.

[00:10:18] Now instead of z^2, I want to take the function 1/z.

[00:10:22] But 1/z is a dangerous function. You can't divide by zero.

[00:10:27] And I write: if z == 0, then ComplexInfinity.

[00:10:32] Look...

[00:10:33] Here it is.

[00:10:34] Here is the first picture of the ones we wanted to get.

[00:10:37] Instead of squares, we get pieces of circles.

[00:10:43] There were squares, and after 1/z they became little circles.

[00:10:48] He's swearing here, saying: You can't divide by zero.

[00:10:53] So it becomes Indeterminate.

[00:10:56] Oh well.

[00:10:56] In order to remove this warning, we will learn to find that there is a point 0,0 in our polygon.

[00:11:04] This very point will turn into the complex number 0, which cannot be divided by.

[00:11:11] Using the Intersection and Length functions, we will check for intersections.

[00:11:26] Oops, something went wrong. Looks like I took the wrong example.

[00:11:30] There we go.

[00:11:31] We'll turn the seventh element from the squares we obtained into a polygon,

[00:11:35] and check if there is a point (0, 0) inside the polygon.

[00:11:39] Answer: 0 intersections. So there is no point (0, 0) inside.

[00:11:43] The length of the intersection list is equal to zero.

[00:11:50] We write: dangerous point pC = (0, 0).

[00:11:57] We obtain the polygon poly from the i-th square.

[00:12:02] We check if the length of the intersection between the polygon and the dangerous point pC is greater than zero.

[00:12:07] If so, we return an empty polygon.

[00:12:10] Otherwise, we just transform each point using F.

[00:12:14] The transformation F is a complex point on the plane.

[00:12:20] Let's draw...

[00:12:21] There we go. Now there are no warnings.

[00:12:25] Here we can also have some fun and edit the result.

[00:12:31] It has a fractal nature, as you might have guessed.

[00:12:41] Alright.

[00:12:44] How can we see what's inside?

[00:12:46] We can zoom in like this.

[00:12:50] But they become invisible.

[00:12:53] I zoomed in on the pieces that were there.

[00:12:57] However, they have been slightly deformed.

[00:12:59] Now, another idea. Let's divide the rectangle differently.

[00:13:05] Not by approaching the point (0, 0), but by using a spiral. Look.

[00:13:11] Let's increase the number of dots here to twelve.

[00:13:16] There we go, in a spiral.

[00:13:21] By the way, here's an interesting puzzle: what is the point to which this spiral converges?

[00:13:26] We need to express this point as a point with coordinates x, y, where x and y are in fractions of the length and width.

[00:13:36] I got 0.27, 0.17, but that's just an approximation.

[00:13:42] And it's not the numbers after the decimal point that matter,

[00:13:45] but the analytical formula for this point towards which the spiral converges.

[00:13:52] Here we are learning an important skill.

[00:13:56] It's very easy to take the last element of a list. You just need to specify -1 as the index.

[00:14:01] This is true in the Python language, the Ruby language, and many other languages.

[00:14:06] Here, I don't want to divide 1/z,

[00:14:11] but take the function F[z_] = 1/(z-zC),

[00:14:14] where zC is the point of the last square. One of the vertices of the last square, so to speak.

[00:14:21] And I'm taking it right here.

[00:14:23] -1 - take the last square and take its first vertice.

[00:14:28] Here we go.

[00:14:31] Slap!

[00:14:32] We get our picture number 2.

[00:14:35] Beauty - a terrible force!

[00:14:40] Let's see what you think about this...

[00:14:46] Hmmm... looks like you like it. Great!

[00:14:49] Moving on.

[00:14:52] And what's next?

[00:14:54] This is the end!

[00:15:01] We can look at the pictures we get for different values of n.

[00:15:05] Here's 17, a beautiful picture. And 12 was a beautiful picture without the clipped circles.

[00:15:10] No, not 12.

[00:15:11] 13.

[00:15:13] There's 13, 17...

[00:15:19] Obviously, we need to add 4.

[00:15:23] 21... and so on.

[00:15:30] That's all for today!

[00:15:32] Leave your comments.

[00:15:34] Write about what you would be interested in learning in the next podcast.

[00:15:40] Goodbye for now!
