# 9. Формула суммы корней √ 1 + √ 2 + √ 3 + ... Дзета функция в дробных точках (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [Mc1wxCzegdg](https://www.youtube.com/watch?v=Mc1wxCzegdg). Получено: 2026-10-08T17:43:14+01:00.

[00:00:01] Hello, everyone!

[00:00:03] Welcome to the channel "Mathematical Experiments."

[00:00:05] Today, we have another dose of experimental mathematics without proofs.

[00:00:10] There's proven medicine, proven mathematics,

[00:00:13] and then there's our unproven mathematics.

[00:00:16] By the way, our unproven mathematics is very close to proven medicine.

[00:00:21] We conduct experiments.

[00:00:24] We get results and observe them.

[00:00:26] And we consider that to be the most important proof.

[00:00:30] Of course, it's not the most significant proof. It would be great to have a real proof.

[00:00:35] But you should seek it on your own.

[00:00:40] Here, we don't consider the fact that we lack a genuine proof as an obstacle.

[00:00:47] We simply discover interesting facts.

[00:00:49] Last time, we discovered an interesting fact

[00:00:51] that the sum of the k-th powers of the first "n" natural numbers can be expressed as a polynomial.

[00:00:57] In Mathematica, there is an answer to the question of how to calculate the sum of the k-th powers of the first "n" natural numbers.

[00:01:03] It's called the HarmonicNumber function.

[00:01:06] In Mathematica, there are also Bernoulli polynomials

[00:01:08] that allow us to get the same result using a different method.

[00:01:13] If you want to sum the k-th powers from 1 to 10, you need to take the value of the Bernoulli polynomial at point 11,

[00:01:21] subtract the value of the Bernoulli polynomial at point 0,

[00:01:24] divide by k + 1,

[00:01:27] and the first argument is also equal to k + 1.

[00:01:29] That's what you need to do to get the sum of squares of the first ten natural numbers.

[00:01:36] A concise expression in the Mathematica language to explicitly define it.

[00:01:43] HarmonicNumber. This function is defined in Mathematica as follows.

[00:01:49] To calculate the sum of the first ten natural numbers raised to the power of 3,

[00:01:55] you can perform these calculations.

[00:01:57] They all yield the same result.

[00:01:59] Okay.

[00:02:00] But we won't rely on the achievements of humanity in the form of a pre-defined HarmonicNumber function.

[00:02:06] We will define this HarmonicNumber ourselves like this.

[00:02:13] "Nk" is a function that returns a list of k-th powers.

[00:02:17] Here, we got the squares of the first ten numbers.

[00:02:20] "AccNk" is very straightforward.

[00:02:23] Each number is the sum of powers.

[00:02:27] For example, 5 is the sum of 1 + 4.

[00:02:30] 14 is the sum of 1 + 4 + 9, and so on.

[00:02:35] So, the array returned by AccNk

[00:02:40] is the HarmonicNumber for different values of the first argument "m".

[00:02:48] Okay.

[00:02:50] AccNk is translated as "Accumulate list N to the power of k."

[00:02:56] You could get AccNk like this.

[00:02:59] And perhaps it would calculate faster...

[00:03:01] but we won't. We'll do everything in a simple way

[00:03:05] so that what we're doing right now can be replicated in C++, Python, and so on.

[00:03:13] Let's plot our list.

[00:03:16] For example, this is what we get when we sum the cubes.

[00:03:23] It's a strongly growing function.

[00:03:26] Today, I'd like to show you

[00:03:27] how you can get the same Bernoulli polynomials with their tricky coefficients

[00:03:34] without using a system of linear equations.

[00:03:39] Without using what's called matrix inversion,

[00:03:43] but instead using programming skills

[00:03:46] so that a programmer can quickly get all these tricky coefficients of the Bernoulli polynomials.

[00:03:55] How will we do it?

[00:03:57] The programmer sees a growing function.

[00:04:00] He has a desire to know how it grows.

[00:04:05] And here we can experiment.

[00:04:07] Let's divide, for example, by the square - it still grows.

[00:04:13] Divide by cubes - it still grows.

[00:04:16] Divide by four - oops... it doesn't grow anymore.

[00:04:20] It's evident that it tends. And it tends not to zero, but to some number.

[00:04:27] What number does it tend to?

[00:04:30] Let's try to repeat this experiment for k = 4. The sum of fourth powers.

[00:04:39] We also find that the function grows

[00:04:43] and when we divide by the k-th power of "n", we get this converging thing.

[00:04:53] Those who know calculus already guess the answer here. What does this line tend to?

[00:05:00] Here it tends to 1/5, which is 0.2.

[00:05:03] And above, it tends to 0.25.

[00:05:08] Why does this happen?

[00:05:11] Let's understand it with the square.

[00:05:12] Here's our parabola.

[00:05:15] When we sum the squares, it means

[00:05:19] that we sum these columns.

[00:05:22] We want to calculate the area of this tan color.

[00:05:28] Each column has an area equal to n^2.

[00:05:34] And so, when we add up the area of all the columns,

[00:05:36] we precisely get the sum of squares of the first "n" natural numbers.

[00:05:42] But look, there's a cool thing here.

[00:05:47] Those who know calculus,

[00:05:51] they know what this blue area is equal to.

[00:05:55] It's easier to compute than the tan one, strangely enough.

[00:06:05] The process of calculating the area under the graph is called integration.

[00:06:10] And the integral, for example, for a parabola is equal to (m^3)/3 when we sum up to "m".

[00:06:20] It's evident that the blue area...

[00:06:22] The entire blue area. Not just the upper triangles, but the entire blue area.

[00:06:26] ...and the tan area, they are close.

[00:06:29] And that's why most likely this tan area grows with the same strength as the blue one.

[00:06:38] So...

[00:06:41] Therefore, when we sum the squares, we need to divide by the cube, by three.

[00:06:50] Here, I want to divide "m^3" by 3.

[00:06:55] Just that the three ended up here when I started dividing.

[00:07:00] This expression in parentheses is (m^3)/3.

[00:07:06] We just need to remove it here.

[00:07:09] And if we sum the cubes,

[00:07:12] we need to write a 4 here.

[00:07:16] And the tendency will also be towards one. And so on.

[00:07:25] The fact that the blue and tan areas coincide asymptotically can be seen from the image.

[00:07:38] Slap! See?

[00:07:40] You can't see this little difference in blue.

[00:07:45] This means that it is negligible compared to the entire brown area.

[00:07:50] The difference between the total blue and total tan areas is negligible compared to their sizes.

[00:08:01] Okay.

[00:08:02] Moving on.

[00:08:05] Next, we want to calculate more.

[00:08:10] Let's move the 4 here after all.

[00:08:15] Let's work with the 3 for now.

[00:08:19] There you go. Let's start with the 3.

[00:08:22] We get 1.

[00:08:23] Subtract this 1.

[00:08:25] We get 1 at infinity on the right.

[00:08:31] We get a graph that keeps getting smaller and smaller...

[00:08:36] Let's enclose this in parentheses and multiply it by, let's say, "m".

[00:08:44] This expression here represents "m" for me.

[00:08:48] Slap.

[00:08:50] Degree 1 is "m," and when I write 4 here, it will be n^4.

[00:08:55] For now, I just want to multiply by "m".

[00:09:04] Got the answer.

[00:09:08] Something approaching 2.

[00:09:10] Well, okay...

[00:09:11] Subtracting 2.

[00:09:13] Enclose everything in parentheses again and multiply by a linearly increasing thing.

[00:09:23] Oh!

[00:09:23] I get 1.

[00:09:25] Subtracting 1.

[00:09:29] So what did I get?

[00:09:31] I got the following expression,

[00:09:36] which equals 0.

[00:09:39] Let's denote this as HarmonicNumber[3].

[00:09:49] I'll call this m^4.

[00:09:56] I'll simply call this "m".

[00:09:58] This is also "m".

[00:10:00] One parenthesis got lost... There we go.

[00:10:05] And I want to solve this equation with respect to this thing here.

[00:10:15] Here's what I got.

[00:10:20] So... Expand...

[00:10:25] It matches.

[00:10:27] What has just been demonstrated is a way to get HarmonicNumber for k = 3,

[00:10:34] well, or -3 if we're talking about the argument of this function.

[00:10:38] Similarly, we can get other HarmonicNumbers,

[00:10:44] which are slightly transformed Bernoulli polynomials.

[00:10:51] Let's move on.

[00:10:53] Let's calculate for k = 4...

[00:10:57] Alright.

[00:10:57] I'll handle this differently here...

[00:11:02] Divide by Nk to the power of 5.

[00:11:10] Well, and I'll write 5 explicitly here too.

[00:11:15] Okay...

[00:11:15] Everything tends to 1, as we expected.

[00:11:18] Subtract 1,

[00:11:21] enclose in parentheses,

[00:11:23] and multiply by what we call "m."

[00:11:29] Slap!

[00:11:32] Very close to 2,5.

[00:11:33] Subtract 5/2.

[00:11:36] Enclose everything in parentheses,

[00:11:40] and multiply by "m."

[00:11:48] So...

[00:11:49] 1,66666...

[00:11:53] Subtract 1,6666...

[00:11:57] Well, by the way, what is 1.6666...? It's 5/3.

[00:12:18] Multiply by "m"...

[00:12:27] Apparently, we didn't multiply enough.

[00:12:29] There we go! That's much better!

[00:12:32] See? Sometimes you have to multiply not by "m," but by "m^2" right away.

[00:12:39] Nk[n, 2] is m^2.

[00:12:42] Here's a certain number...

[00:12:50] 0,15.

[00:12:54] Not strong enough, we need to add more.

[00:12:56] Adding 0,015 gives us 0,165.

[00:13:01] And we need to add more. Now it's 0,0015.

[00:13:07] This is what we get.

[00:13:10] Well, you can already guess what to add next.

[00:13:13] And 0.16666... is precisely 1/6.

[00:13:19] That's it. We have the answer.

[00:13:21] Here's the answer.

[00:13:24] This thing equals zero.

[00:13:31] And here, I want to show you how Mathematica works. Let me demonstrate.

[00:13:38] We can add some letters here,

[00:13:41] enclose everything in parentheses, and transform it using rules.

[00:13:48] We can say that all of this equals HN[k].

[00:13:58] And this...

[00:14:03] place "l_" here and turn all of this into m^l.

[00:14:25] There we go...

[00:14:26] Well, write "Solve" with respect to...

[00:14:35] And based on our previous experience, we need to write "Expand," in case it factors it again.

[00:14:42] Let's check...

[00:14:51] We got it.

[00:14:53] This way, you can find polynomials that correspond to HarmonicNumbers

[00:14:59] and then get Bernoulli polynomials as well.

[00:15:03] Here, this was done.

[00:15:04] Slightly differently, I subtracted here at the beginning.

[00:15:07] Instead of dividing right away, I subtracted right away because I knew the answer.

[00:15:11] The same thing was done for five as well.

[00:15:15] And here, it's convenient to define a function called difNK,

[00:15:20] which subtracts the k+1 degree from the sum of the kth powers multiplied by k+1.

[00:15:28] From the tan area multiplied by k+1 subtracts the blue area multiplied by k+1.

[00:15:42] To deal with these triangles,

[00:15:45] which are located between these two areas.

[00:15:50] Here, all of this was done for six.

[00:15:59] And when we do this for six, what do we notice?

[00:16:01] We notice that these numbers appear, 7/2.

[00:16:05] In fact, we should have divided everything by 7, and here I divided by 7.

[00:16:12] I realized that I made a mistake. I shouldn't have written it like this,

[00:16:16] but rather like this.

[00:16:21] Like this... More directly. In explicit form.

[00:16:24] Subtract the blue area from the brown area.

[00:16:27] So, this example is erroneous. Let's erase it.

[00:16:31] It's more convenient to work in this format.

[00:16:33] Here, I won't divide by 7 anymore.

[00:16:36] We've determined...

[00:16:42] And these coefficients, -1/42, 1/6, -1/2, -1/2,

[00:16:49] they're already familiar to you from the previous video.

[00:16:52] In the previous video, we performed this operation.

[00:16:55] We constructed a triangular matrix from binomial coefficients,

[00:17:00] removed its right slope,

[00:17:03] took the inverse matrix, and got this answer.

[00:17:08] And...

[00:17:13] And in this answer, we need to look at this row and see here:

[00:17:20] 1/42, -1/42

[00:17:23] -1/6, +1/6

[00:17:27] 1/2, -1/2

[00:17:33] -1/2, also -1/2

[00:17:38] See? The signs are strictly opposite, except for this last -1/2.

[00:17:45] This is something I always overlook and forget to tell you about.

[00:17:51] When we sum the first "n" k-th powers,

[00:17:59] we get Bernoulli polynomials of m+1, not m.

[00:18:05] What's the difference between the Bernoulli polynomial for m and the Bernoulli polynomial for m+1 (both divided by k)?

[00:18:11] It differs only in one place. Right here.

[00:18:14] And why is that?

[00:18:16] Because the Bernoulli polynomial for n+1 differs from the previous one by exactly m^k.

[00:18:24] Here, k = 6, and we need to substitute k+1.

[00:18:29] And when we add m^6,

[00:18:31] -(m^6)/2 turns into (m^6)/2.

[00:18:37] In the previous video, I consistently ignored this difference and made mistakes...

[00:18:44] I looked. The coefficients match, but I often missed this subtle difference in signs.

[00:18:49] For 7...

[00:19:08] So, in the matrix we drew last time, it contains the answer to the question:

[00:19:15] how should we arrange the numbers in this expression to eventually get 0?

[00:19:24] Good.

[00:19:26] Now let's move on.

[00:19:28] Last time we got a matrix, and it contains the answer for summing k-th powers, where "k" is an integer.

[00:19:34] But what if k = 1/2?

[00:19:38] To study this case, we'll have to complicate the definition of NK and AccNK a bit.

[00:19:46] Specifically, we need to add precision everywhere.

[00:19:53] Defined it a bit strangely here...

[00:19:55] And I'll have to sum a lot more numbers.

[00:19:57] I'll be summing up to a million.

[00:20:00] But plotting a graph with a million points is difficult, so I want to plot only a fraction of these points.

[00:20:04] To take every hundredth number from an array, you can add this thing to the end of the array.

[00:20:15] And specify 100 or any number you want as the "step".

[00:20:21] Example.

[00:20:22] This one if you want to take every second element from the list.

[00:20:29] You can specify from which to which.

[00:20:32] If you don't specify, it takes the first and the last, respectively.

[00:20:41] Enk differs from Nk in that the numbers, which are got there, have high precision.

[00:20:47] I specified a large precision, and it will perform all operations with high precision.

[00:20:55] Good.

[00:20:56] So, our "n" has increased.

[00:21:01] Oops. Well, that's too much.

[00:21:04] Let's do what is written here.

[00:21:08] I forgot to remove the answer...

[00:21:18] Below, we have the answer to the question, but let's try not to peek at it.

[00:21:24] For now, let's choose these values and draw a plot.

[00:21:30] It will be computed for a while.

[00:21:32] I added caching to all these expressions.

[00:21:35] It looks quite strange, probably for C or Python programmers.

[00:21:42] The function is defined as "Function ="

[00:21:46] What's happening here?

[00:21:48] This should be read as follows:

[00:21:51] evaluate the expression...

[00:21:54] So, the function is defined like this. This is its body.

[00:21:57] We need to evaluate this expression,

[00:22:00] store it in the dictionary ENk with the key [n, k],

[00:22:08] and return it as the result as well.

[00:22:12] When calling "ENk," Mathematica first checks if there is a dictionary with that name and the given argument values.

[00:22:20] If there is an answer in the "k -> value" table, it returns it.

[00:22:23] If not, it proceeds to this definition, which computes and stores the final answer in the dictionary.

[00:22:31] This is called "memoization." This is how it is implemented in Mathematica.

[00:22:39] Simply append the expression without an underscore at the end.

[00:22:44] And use the ordinary "=" sign instead of ":=".

[00:22:46] The ordinary "=" sign means "store in the dictionary."

[00:22:50] Let's call it that way. As if we simply stored it in the dictionary.

[00:22:54] During this time, it calculated the growing graph.

[00:22:58] And I suspect it approaches the point 1/2.

[00:23:04] Great. We had 1/2 there, and here it also becomes 1/2,

[00:23:08] even though we are summing not integer powers but roots.

[00:23:11] We are currently calculating the sum of roots of the first "n" natural numbers.

[00:23:17] We subtracted.

[00:23:20] We got a number that now approaches zero.

[00:23:23] What should we multiply it by?

[00:23:28] Well, let's multiply it by this...

[00:23:33] Of course, we could multiply by one out of habit,

[00:23:36] but here we see that the graph grows sharply modulo.

[00:23:45] That is, when summing roots, we should multiply here not by "m" but by "√m".

[00:23:53] Next.

[00:23:55] This number... it's unclear what it is.

[00:24:00] Let's add it.

[00:24:01] +0.20784

[00:24:08] I wrote down exactly what I see here.

[00:24:13] So...

[00:24:15] Here, we probably need to add a two...

[00:24:23] More than a two.

[00:24:25] Probably an eight.

[00:24:28] Well, never mind...

[00:24:29] That means we won't be able to determine many digits of this number.

[00:24:33] We need to multiply by ENk again.

[00:24:39] Down it goes.

[00:24:41] I'll write a 5 here.

[00:24:45] So...

[00:24:50] And if it's 7...

[00:24:52] Oh! It is an overshoot.

[00:24:54] And if it's 6...

[00:24:56] It is an undershoot.

[00:24:57] Alright.

[00:24:58] 5.

[00:24:59] 5 is an overshoot.

[00:25:02] 3.

[00:25:03] 2.

[00:25:14] Here, we need to subtract 0.04 for convenience.

[00:25:26] There!

[00:25:27] Oh, by the way, it's even clear that we should continue here.

[00:25:30] We have 0.04, and it suggests we should write another 1 and many sixes.

[00:25:38] Oh! Then it goes straight from zero.

[00:25:41] And now, it will probably be easier here.

[00:25:44] 4. Undershoot.

[00:25:47] 5. Overshoot.

[00:25:49] So, 4 and 5...

[00:25:53] 7...

[00:26:06] Something interesting is starting. Can you see it?

[00:26:10] 5...

[00:26:12] 6...

[00:26:14] 55...

[00:26:16] Wow...

[00:26:26] So, we've reached something. Something very fascinating.

[00:26:30] What is 0.04166666? It's some fractional number.

[00:26:38] Clearly defined.

[00:26:39] To understand what this number is, we can call ContinuedFraction and take a look.

[00:26:47] It's 1/24.

[00:26:52] We can write it like this...

[00:26:55] FromContinuedFraction.

[00:26:59] 1/24.

[00:27:00] Here we first converted it into ContinuedFraction and then derived it back.

[00:27:06] How does it work?

[00:27:09] It works approximately like this.

[00:27:12] Suppose you have some number, some unusual number...

[00:27:16] You get the ContinuedFraction.

[00:27:19] But you can see that this number is very large.

[00:27:26] So, it makes sense to truncate the ContinuedFraction series here

[00:27:33] and write FromContinuedFraction for this set.

[00:27:39] And understand that the nearest fractional number to this is 1/24.

[00:27:44] Of course, you can take everything and get a completely precise description of this number,

[00:27:48] but if you want to get an approximate fractional approximation, do the following:

[00:27:55] Take the ContinuedFraction expansion, truncate it somewhere, and perform the reverse transformation.

[00:28:04] You can find more information about ContinuedFraction online.

[00:28:10] Here's the exact answer, 1/24, if there are an infinite number of sixes.

[00:28:18] So, this is what we have.

[00:28:21] Let me draw it again.

[00:28:24] Here, it's already evident that Mathematica is reaching its own precision limit in calculations.

[00:28:30] The number we got here is the value of the zeta function at -1/2.

[00:28:36] I'm giving it to you as a mere designation.

[00:28:40] Let's say we denote the number that emerged here as zeta of -0,5.

[00:28:46] We currently have no proof that this is precisely the zeta function at this point.

[00:28:53] For now, we're simply discovering unusual numbers and assigning names to them,

[00:28:59] and Mathematica already provides the ready answer, which I occasionally guide them to.

[00:29:05] This unusual number we discovered here is indeed the value of the zeta function at -1/2.

[00:29:14] Here, we summed the roots, but we can also sum the reciprocals of the roots.

[00:29:23] Oops. Well, here's the answer to the question again.

[00:29:26] You can trust me that in a completely analogous manner, you can get the signs of this number.

[00:29:35] Now, the computation and caching of the value of EDNk at k = -1/2 are taking place.

[00:29:53] And we immediately encounter an unusual number that cannot be simply represented as a fraction.

[00:30:18] Here you need to act as follows:

[00:30:21] Take and multiply by this

[00:30:28] and then start adjusting.

[00:30:33] 5. Undershoot.

[00:30:36] 6. Undershoot.

[00:30:38] 7. Overshot.

[00:30:40] Then it is 6...

[00:30:44] With these manipulations, you draw all these signs.

[00:30:49] And, by the way, it's immediately evident here that you need to subtract 1/2 because the plot starts there.

[00:30:55] It's clear, from 1/2.

[00:30:56] That's how this 1/2 appears.

[00:30:59] Then you can multiply again, and here we discover that we need to multiply not by the root, but directly by "m."

[00:31:08] And then we find that we need to add 1/24.

[00:31:12] And, in secret, I'll tell you that this number we encountered here,

[00:31:17] is the value of the zeta function at 1/2.

[00:31:20] What we got here, Mathematica knows, of course.

[00:31:23] And to ask it the answer to the question,

[00:31:26] you have to ask it to output the series for HarmonicNumber at k = 1/2 around "m" equal to infinity.

[00:31:40] Those who studied first-year calculus can guess and understand what is written here, what Mathematica outputted.

[00:31:46] Mathematica provided the expansion of this function in powers of 1/m.

[00:31:54] It still has this term "m."

[00:32:02] Initially, it was "m," but I don't want to see all these divisions by 2,

[00:32:10] so I at once indicate the square here, and the expression becomes simpler.

[00:32:15] Not as large and more concise.

[00:32:17] And, by the way, here, when we take any number,

[00:32:22] for example, this,

[00:32:24] and we call FactorInteger,

[00:32:27] we see that it contains 18 twos, so it's (2^18) * (3^1).

[00:32:33] A lot of twos.

[00:32:35] To eliminate these twos, we can choose to divide by 4 here,

[00:32:43] so that it expands into a series for this variable, and then the powers of two stop accumulating in the denominator.

[00:33:00] Mathematica knows perfectly well that in the expansion of HarmonicNumber around infinity,

[00:33:08] the zeta function is present as a constant term.

[00:33:14] Now, this is definitely an interesting phenomenon.

[00:33:21] If you're curious about what happens when you sum the cube roots,

[00:33:31] here's the answer to that question.

[00:33:40] Similarly, you can get the value of the zeta function at 3/2 and -3/2.

[00:33:48] I'd like to draw your attention to the fact

[00:33:53] that these coefficients in these expansions resemble each other.

[00:34:01] Let's, for example, divide 1/18 by 1/168,

[00:34:07] and divide 1/20 by 3/80.

[00:34:12] Let's see what happens when we divide 1/18 by 1/168.

[00:34:16] And what happens when we divide this coefficient

[00:34:19] by this coefficient.

[00:34:22] The ratio of these two coefficients with large numbers in the numerator and denominator gives a simple expression.

[00:34:29] Let's try it out.

[00:34:31] Discover another connection between the expansion of HarmonicNumber at -3/2 and at -1/2.

[00:34:43] So...

[00:34:44] These are the coefficients at 1/2,

[00:34:49] these are the coefficients at -1/2,

[00:34:53] and these are the coefficients at -3/2.

[00:34:55] This is our 1/18,

[00:34:57] and here's 1/168.

[00:34:59] And now let's directly divide a1 by a2.

[00:35:03] For example, a1/a2.

[00:35:07] It's complaining a lot here. To avoid that, we need to disable these warnings.

[00:35:12] And for aesthetics, we need to replace Indeterminate with 0.

[00:35:18] And here's what we get:

[00:35:26] 76/3

[00:35:27] -20, which is actually -60/3.

[00:35:31] -44/3

[00:35:33] -28/3

[00:35:34] Well, of course, we need to multiply by 3.

[00:35:37] All the numbers we see here are divisible by 4, so it makes sense to divide by 4.

[00:35:42] There you go.

[00:35:44] From this, we can see that the coefficients in the expansion

[00:35:49] this one and this one are connected in a clear way.

[00:35:55] We have discovered this, but we haven't proven it.

[00:36:05] At -1/2, the expansion is connected to the expansion at 1/2.

[00:36:12] Here, we also get ratios with a visible dependence.

[00:36:18] -1, -5, -4, -13, -17... Each number differs from the previous one by 4.

[00:36:24] And all of this can be written out in the form of formulas.

[00:36:28] There's another interesting case when we sum the harmonic series.

[00:36:32] When we sum the reciprocal of natural numbers.

[00:36:35] This corresponds to our K = -1.

[00:36:42] And here, if you try to figure out what needs to be subtracted from this sum,

[00:36:54] after some time, you will realize that it needs to be subtracted by the logarithm.

[00:36:59] But when you subtract the logarithm,

[00:37:03] you will see that it all tends to a certain constant that can be gradually written out.

[00:37:27] And so on.

[00:37:28] Here, an interesting constant is written out, which in Mathematica is called EulerGamma.

[00:37:39] This is what it equals.

[00:37:42] If we write it here

[00:37:46] with a large number of digits, this is what we'll see.

[00:37:48] And it can be seen here that we need to subtract 1/2.

[00:37:51] Again, 1/2. The story of subtraction always starts with 1/2.

[00:37:57] Enclose it in parentheses again.

[00:38:02] Multiply by it.

[00:38:06] Here, perhaps, we need to continue...

[00:38:12] Let me write "EulerGamma" right here.

[00:38:18] Like this...

[00:38:20] + 0,08

[00:38:31] We also need to add 0.003.

[00:38:38] Alright... I've figured it out.

[00:38:48] It's 1/12.

[00:38:54] These calculations can be continued to get the expansion for the sum of the harmonic series up to the term "m".

[00:39:06] Let's take a look at the answer.

[00:39:09] Here's the representation of this expansion.

[00:39:12] If we continue searching.

[00:39:15] Again, we enclose it in parentheses and multiply again...

[00:39:27] Here, perhaps, we need to square it.

[00:39:31] Here's another number.

[00:39:33] Here we can guess the next elements...

[00:39:38] Well, the complete answer, if we keep going, looks like this.

[00:39:43] It's clear that these terms will be difficult to find,

[00:39:47] but the thing is that these coefficients are well-known to us.

[00:39:54] Let's get them explicitly using the CoefficientList function.

[00:40:02] But before calling the CoefficientList function, here I used rules

[00:40:08] to get rid of this part and turned 1/m into m.

[00:40:12] The coefficients in this expansion coincide with those very numbers that we got

[00:40:18] in the first column of the inverse matrix of Pascal's triangle,

[00:40:25] and after dividing by the binomial coefficients.

[00:40:33] Their ratio is always equal to one, except for one place where it is -1.

[00:40:37] Again, 1/2 changes its sign.

[00:40:43] So, what did we get?

[00:40:47] We got the following expansion:

[00:40:52] That the sum of the reciprocals of natural numbers up to "m" is equal to the logarithm plus the Euler constant (EulerGamma),

[00:41:05] and then follows the sum of the values of the zeta function at negative points, divided by "m" to the power of some "k".

[00:41:16] Here, I adjusted...

[00:41:22] It's more accurate to write +1. Here.

[00:41:27] This is what we got.

[00:41:32] By definition, EulerGamma is a constant equal to the limit of the sum of the harmonic series minus the logarithm of "m".

[00:41:44] As "m" approaches infinity, so it's natural to see it here.

[00:41:52] This component is interesting.

[00:41:58] Let's see what we get here.

[00:42:07] Well, here it is. I just made sure that I got what I needed.

[00:42:14] Alright...

[00:42:17] Here, I calculated the sum of the harmonic series up to term "m" with decimal places,

[00:42:24] and on the other side, I calculated this sum.

[00:42:27] You can see that the numbers coincide. Good.

[00:42:30] We can put a minus sign between them instead of a comma.

[00:42:35] Here, I chose m = 200,

[00:42:37] and here, I chose the sum up to 10.

[00:42:41] Like this...

[00:42:46] And if we put 1000 here, I'm afraid it won't be pleasant.

[00:42:49] Yes, an unpleasant thing happened...

[00:42:52] Alright, just a moment...

[00:42:55] This is all very interesting, of course.

[00:43:00] On the one hand, you can see that there is some convergence,

[00:43:05] but it is not recommended to increase the sum here to a thousand.

[00:43:12] Well... That's a separate topic. A very complex topic.

[00:43:15] Alright.

[00:43:17] I just want to explain the meaning of a quite complex and interesting equation.

[00:43:29] The meaning is... Let me draw it from the top here.

[00:43:34] Here, the function 1/x is drawn, it's the red line.

[00:43:40] It's drawn here twice. First at the beginning, then at the end.

[00:43:42] In order for this area to be colored in red.

[00:43:48] Then there is this step function up to the 10th element.

[00:43:56] And then it continues with a different color.

[00:44:02] Overall, this preparation is done.

[00:44:08] The area under the smooth curve is the logarithm.

[00:44:13] When we stop at 10 and calculate the area under this smooth curve,

[00:44:16] it is exactly the natural logarithm of 10.

[00:44:22] The sum of these triangles...

[00:44:24] all of them, an infinite number of triangles. They are not perfect triangles, one side is smooth.

[00:44:31] So, the sum of them equals EulerGamma, an unusual number that we calculated earlier.

[00:44:41] It's approximately 0.5, but a bit larger, 0.57.

[00:44:45] By the way, if these triangles were perfect and there was a straight line segment here,

[00:44:53] then the sum of these triangles would exactly be 0.5.

[00:44:59] Why is that?

[00:44:59] Because the triangles can be aligned to the left edge

[00:45:04] and it can be determined that they exactly occupy half of this column,

[00:45:08] if they have this segment as a straight line.

[00:45:12] But they don't have this segment as a straight line, so it's slightly larger than half.

[00:45:19] So, the sum of all the triangles is EulerGamma,

[00:45:23] this number right here.

[00:45:29] It turns out that this sum should be negative

[00:45:35] and correspond to subtracting all these little triangles

[00:45:38] that we don't want to calculate,

[00:45:39] because we only want to calculate the sum of the harmonic series up to the 10th term.

[00:45:47] That's the meaning of it.

[00:45:50] This sum is negative

[00:45:56] and equals the sum of triangles starting from the m-th triangle.

[00:46:07] These triangles can be separately drawn using the RegionPlot function.

[00:46:14] Like this.

[00:46:17] And here below are four triangles aligned to the left edge, as I mentioned.

[00:46:29] It takes a long time because I asked RegionPlot to draw it all neatly,

[00:46:36] using a large number of calculations.

[00:46:44] So, we got all these triangles separately from everything.

[00:46:49] It says: "y" is greater than 1/x, and at the same time "y" is less than 1 divided by the integer part of "x".

[00:46:58] And "x" is greater than 1 so that it doesn't draw anything from 0 to 1.

[00:47:05] To align them to the left...

[00:47:09] It's not that easy to do,

[00:47:10] but, for example, like this.

[00:47:12] We draw four different regions,

[00:47:16] Mathematica assigns them four different colors.

[00:47:18] If desired, the number of "regions" can be increased.

[00:47:21] Here, I simply shifted each piece to the left.

[00:47:26] First by 1, then by 2, then by 3, then by 4.

[00:47:34] So, what have we done?

[00:47:37] We recalled the previous video where we got this matrix

[00:47:43] by inverting this matrix.

[00:47:47] We also remembered that we found a pattern in this matrix

[00:47:51] and divided the elements of the inverted matrix by the elements of the original matrix, but slightly shifted,

[00:48:00] in other words, we divided them by the binomial coefficients, but slightly shifted.

[00:48:04] And we got diagonals consisting of the same numbers, as shown in the previous video.

[00:48:11] So we saw that there are certain numbers hidden in the idea of Pascal's Triangle inversion,

[00:48:18] a sequence of numbers.

[00:48:21] And the entire inverse matrix can be got from these numbers.

[00:48:26] We called these numbers zeta minus 1, zeta minus 2, zeta minus 3, and so on.

[00:48:30] And it turned out that these numbers, which are in the first column, play an important role.

[00:48:38] They appear everywhere.

[00:48:41] And, in particular, they appear when calculating the partial sum of the harmonic series.

[00:48:48] We got a beautiful, complex formula.

[00:48:56] We sort of discovered that it's true.

[00:48:59] We also discovered that it behaves strangely.

[00:49:02] Actually, writing infinity here is probably not possible. We have to write some small numbers.

[00:49:07] And it provides a fairly good approximation.

[00:49:16] And this is already quite serious mathematics.

[00:49:19] That's all for today!

[00:49:21] Good luck, everyone! Bye!
