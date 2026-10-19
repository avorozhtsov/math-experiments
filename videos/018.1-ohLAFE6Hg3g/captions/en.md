# 18. Первый ноль ζ – функции. Суммы по степеням простых чисел

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [ohLAFE6Hg3g](https://www.youtube.com/watch?v=ohLAFE6Hg3g). Получено: 2026-10-08T17:42:25+01:00.

[00:00:01] Hello everyone! Welcome back to the "Mathematical Experiments" channel.

[00:00:04] Last time, we studied the Pi function – The number of prime numbers ≤ x.

[00:00:11] And we got a quite complex formula for approximating this Pi function,

[00:00:15] which imperfectly approximates the Pi function.

[00:00:19] When we subtract this approximation from Pi,

[00:00:21] we get this noise in the result,

[00:00:24] which oscillates from -0.5 to +0.5 approximately,

[00:00:29] but sometimes goes beyond this range.

[00:00:33] Today, we will continue studying this noise and try to decompose it into components,

[00:00:38] but this time, we will deal not with the Pi function,

[00:00:41] but with various sums over prime numbers and powers of prime numbers.

[00:00:48] Why is this necessary?

[00:00:50] Where does this idea of taking sums over prime numbers and powers of prime numbers come from?

[00:01:00] I tried to find a simple explanation for where this desire might come from,

[00:01:06] and I found nothing simpler than an explanation through the zeta function.

[00:01:11] We naturally came to the zeta function with you

[00:01:14] when we studied partial sums of natural number powers.

[00:01:18] And when we came to the Euler-Maclaurin formula, an approximate calculation of partial sums,

[00:01:26] there we also encountered the zeta function,

[00:01:29] which is defined in this way for s > 1,

[00:01:34] and for other s, it is defined as the analytic continuation of this function.

[00:01:40] So... the zeta function of s can be written as a product of these brackets.

[00:01:48] The product is taken over prime numbers.

[00:01:52] Look how interesting it is.

[00:01:54] Initially, the sum is taken over natural numbers,

[00:01:57] but this sum can be represented as a product over prime numbers p.

[00:02:02] Each of these brackets (next step) can be written as 1/(1 - 1/(p^s)).

[00:02:13] What kind of formula is this? It is the formula of an infinite geometric progression.

[00:02:20] Thus,

[00:02:22] the zeta function can be represented as 1 divided by the product.

[00:02:29] And here is the next clever trick.

[00:02:32] Let's take the logarithm of the zeta function and then take the derivative of that.

[00:02:39] What's the idea behind taking the logarithm and then the derivative?

[00:02:43] The thing is, it's a very fruitful idea that allows you to crack any function f.

[00:02:50] Why?

[00:02:51] Because cracking a function f means understanding its zeros and poles.

[00:02:57] I also have a video on the channel about that.

[00:03:01] So, what happens?

[00:03:02] If the function f has a zero or pole at point s0,

[00:03:09] then when we take the logarithm of f,

[00:03:12] this pole or zero separates from the rest.

[00:03:17] And when we take the derivative, this pole or zero becomes a pole.

[00:03:27] So... when you take the logarithmic derivative of the function f,

[00:03:31] all its zeros and poles turn into ordinary poles of degree 1,

[00:03:38] whose numerator is equal to the degree of that pole or zero of the original function f.

[00:03:45] Therefore, this idea of taking the logarithmic derivative is very fruitful for cracking functions.

[00:03:52] And what will happen if we take the logarithmic derivative of this thing?

[00:03:57] We take the logarithm of this ratio...

[00:04:01] Well... it's the same as taking the logarithm of this product with a minus sign.

[00:04:04] The logarithm of a product becomes the sum of logarithms.

[00:04:07] And we take the derivative with respect to s.

[00:04:09] What do we get?

[00:04:11] Here I wrote this down.

[00:04:13] We get that each bracket gives

[00:04:20] this term.

[00:04:22] The derivative of the logarithm of some function is equal to 1 divided by that function, multiplied by the derivative.

[00:04:28] Here I wrote it.

[00:04:30] Implicitly, there is a 1 here, divided by the zeta function.

[00:04:35] And here I drew the derivative of this function.

[00:04:40] Thus, the logarithmic derivative of the zeta function equals...

[00:04:47] Well... without the minus sign, because here I have 1 divided by the zeta function.

[00:04:52] So, we get a sum over powers of prime numbers

[00:05:00] and each power of a prime number is weighted by the logarithm of "p".

[00:05:08] Notice that here, inside the logarithm, there's no "s" and no "k".

[00:05:16] And essentially, I'm going to work with this sum now.

[00:05:22] Let me demonstrate on a simple small example the sums that I'm going to calculate today.

[00:05:29] So, here, we get 2 lists:

[00:05:31] the first list consists of prime numbers and their powers.

[00:05:36] That is, not only 2, but also 4, 8, 16, etc.

[00:05:41] Not only 3, but also 9, 27, etc.

[00:05:46] The second list contains the prime numbers themselves.

[00:05:49] And what do I want to calculate today?

[00:05:52] I want to calculate, for example, this sum.

[00:05:56] Prime number or power of a prime number multiplied by the logarithm of that prime number.

[00:06:03] Let me calculate these two arrays up to 1000

[00:06:09] and add up, for example, this.

[00:06:12] This is the sum of the logarithm of "p" multiplyed by "pp".

[00:06:16] "pp" - I denote the power of the prime number, and "p" - the prime number itself.

[00:06:21] This is how this sum looks.

[00:06:24] Looks like a quadratic dependence.

[00:06:27] Let's divide it by "pp".

[00:06:31] Indeed, it's quadratic, because after dividing by "pp," we're left with something linear.

[00:06:35] And I even tried to approximate it here.

[00:06:38] But let me divide it by the square instead.

[00:06:45] What do I see here?

[00:06:47] It really converges to some constant.

[00:06:49] This constant looks very much like 0.5.

[00:06:54] Next...

[00:06:55] Well... I'm an experienced guy. Let me multiply it all by the square root of "pp".

[00:07:01] "pp" is sort of our x in this video.

[00:07:06] Here's what we get.

[00:07:08] And I see a changing noise.

[00:07:11] More or less, it lies in the range (-0.5, 0.5)

[00:07:16] Okay.

[00:07:18] Another example:

[00:07:19] we can take the sum of Log[p] divided by "pp".

[00:07:24] And here we can see that the dependence is more logarithmic.

[00:07:28] When we subtract the logarithm, here's what we see.

[00:07:31] A noise that converges to some number, maybe -0.57.

[00:07:36] Add this 0.57

[00:07:39] and again, we see noise that lies more or less in the range (-0.5, 0.5), etc.

[00:07:49] In short, I've already precalculated the powers of prime numbers less than or equal to 50 million.

[00:07:58] I've also calculated the prime numbers themselves, 3 million of them.

[00:08:03] And I've calculated various sums.

[00:08:05] Today we will be interested in these sums.

[00:08:07] But in the process, I also calculated sums over prime numbers.

[00:08:12] Here we have two arrays of the same size, "pp" and "p".

[00:08:18] We consider our sum function as a function of "pp".

[00:08:24] Based on what is written in the "pp" array.

[00:08:27] But during summation, we can use both the power of the prime number "pp",

[00:08:31] and the prime number "p" itself, the power of which we take.

[00:08:35] Today, I'm interested in sums with logarithms.

[00:08:37] Simply the sum of logarithms of "p" over all powers of prime numbers.

[00:08:42] Summ "pp" multiplyed by logarithm "p" is denoted as "sumPPp1Log".

[00:08:51] I use the letter "r" to denote negative powers, when I take 1/p or 1/(p^2).

[00:09:03] Now, let's try to crack these sums.

[00:09:09] Let's move to this place.

[00:09:13] First.

[00:09:16] We take the sum...

[00:09:19] I remind you of this notation.

[00:09:21] This is sort of the sum of "1/p", multiplied by the logarithm of "p".

[00:09:30] Or you can write it like this:

[00:09:32] this sum is in this list.

[00:09:38] The function ListQPart takes a part of this list.

[00:09:41] The list itself is quite large.

[00:09:43] How many elements do I have there... I don't even remember.

[00:09:48] 3 million elements.

[00:09:51] And I don't want to plot a graph of 3 million points because Mathematica will lag.

[00:09:59] I'm taking only 10 thousand points from this quantity.

[00:10:05] I take points that are approximately in a geometric progression.

[00:10:09] Their indices form an approximate geometric progression from 1 to 3000000.

[00:10:16] Lets draw it...

[00:10:21] Here I have the answer right away,

[00:10:24] but it wasn't difficult to get it.

[00:10:27] How is it done?

[00:10:30] First, I simply plot the function y[x],

[00:10:37] or rather, y of the logarithm of x.

[00:10:41] #[1] is our x,

[00:10:43] #[2] is our y,

[00:10:45] that is, the sum up to x.

[00:10:50] Here we can see that y is approximately equal to x,

[00:10:54] but, in fact, it's not x, but the logarithm of x.

[00:10:56] So, it's very natural to subtract this logarithm.

[00:11:04] We immediately get noise.

[00:11:06] Remember how long we struggled before extracting the noise from Pi?

[00:11:14] Here, all of this happened in one step from the first try.

[00:11:18] That's why I chose this sum over powers of prime numbers.

[00:11:21] The results are much easier to get here.

[00:11:24] Similar results are gotten when summing over prime numbers,

[00:11:28] but there you need to perform two actions,

[00:11:32] while here it's just one.

[00:11:34] Let's multiply this noise by √x.

[00:11:41] So...

[00:11:42] But before multiplying it,

[00:11:44] first we need to see that it's shifted,

[00:11:47] and I remove this shift.

[00:11:51] I add 0.577

[00:11:56] Here wo go... shifted it to the center, to one, but here I also need to...

[00:12:04] To do like this...

[00:12:10] The thing is, an experienced mathematician recognizes this constant as EulerGamma,

[00:12:16] and I recognized it immediately and wrote it down as well.

[00:12:24] And as a result, I got this noise.

[00:12:29] Sum of Log[p] divided by pp.

[00:12:35] This is just the logarithm of pp

[00:12:39] minus EulerGamma.

[00:12:42] Okay... moving on.

[00:12:46] Now, the sum of just logarithms of p.

[00:12:51] That is, pp is present with a power of 0, so it's written as 0 here.

[00:12:57] What do we do here?

[00:13:00] The same procedure.

[00:13:02] First, we draw the plot of y of the logarithm of x,

[00:13:08] see a growing graph,

[00:13:12] Though...

[00:13:16] it's not enough to divide by the logarithm of x.

[00:13:19] We divide by x itself.

[00:13:21] We see that it tends to one.

[00:13:26] All these constants are very easy to guess, they turn out to be round numbers here.

[00:13:32] Then we multiply by √x,

[00:13:35] and I did that right here.

[00:13:38] And we get a nice, pretty noise,

[00:13:44] familiar to us already.

[00:13:45] They all look very similar.

[00:13:47] Here we had the same noise as well.

[00:13:49] See this cluster at the very end at the bottom?

[00:13:54] There's a similar cluster here.

[00:13:57] Let's move on...

[00:13:59] This sum is pp multiplied by the logarithm of p.

[00:14:03] Here we divide by x^2

[00:14:06] and find that we need to subtract 0.5,

[00:14:11] to get an unbiased noise.

[00:14:15] Next, we see that we need to subtract 0.3333,

[00:14:19] assume it's 1/3.

[00:14:23] Moving on.

[00:14:27] Here the answers are easy to guess.

[00:14:33] This last thing.

[00:14:35] We sum (pp^4) multiplied by the logarithm of p.

[00:14:42] We need to divide by x^5 and subtract 1/5.

[00:14:51] What we've ultimately got.

[00:14:53] We got five noises,

[00:15:00] six, actually, if we consider that first noise where I took 1/pp,

[00:15:06] and they all look very similar to each other.

[00:15:09] Wonderful!

[00:15:11] Now let's...

[00:15:13] What is naturally to do here...

[00:15:15] We need to subtract one noise from another.

[00:15:18] I'll subtract the noise for power 1 from the noise for power 0.

[00:15:25] The noise for power 2 from the noise for power 1, and so on.

[00:15:29] So, I'll take neighboring noises and subtract one from the other.

[00:15:36] What is CatXYs?

[00:15:39] It is assumed that we combine two lists of XY pairs,

[00:15:43] and their x-values are the same, so we can take any of the x's (x1, x2 and x3).

[00:15:56] Here...

[00:15:58] Lets draw it...

[00:16:01] What a wonderful picture.

[00:16:04] This is the key picture in this video.

[00:16:08] The first noise (blue, original),

[00:16:12] it goes beyond the bounds of our rectangle on the xy plane.

[00:16:19] See? Here, the Y-axis is taken in the range (-0.04, 0.03).

[00:16:29] The first noise, it has a large amplitude of about 0.5.

[00:16:37] These 4 noises

[00:16:40] make up this plot, for example.

[00:16:44] Also, the purple plot.

[00:16:47] Also, the red and blue plots.

[00:16:48] The red and blue plots, they are hidden behind the purple one.

[00:16:55] Further, there are three more things drawn here.

[00:16:59] What are these things?

[00:17:02] Here, I took, essentially,

[00:17:08] the second noise

[00:17:10] and the first one.

[00:17:11] And I subtracted this noise from that noise.

[00:17:14] From this noise,

[00:17:15] this noise.

[00:17:16] Something like that.

[00:17:20] Look at how it happens.

[00:17:23] This can be explained as follows.

[00:17:27] I numbered these three noises (there are three of them)

[00:17:30] as noise #[2],

[00:17:35] #[3].

[00:17:38] Let's also call this #[3].

[00:17:41] And let this be #[4].

[00:17:43] And now when I subtract from this difference

[00:17:45] this difference,

[00:17:47] I get exactly this expression.

[00:17:53] That's the explanation.

[00:17:55] So now I have three levels of noise.

[00:18:00] The original noises we had before.

[00:18:04] Noises of the form "difference of original noises".

[00:18:10] And noises of the form "difference of these previous-level noises".

[00:18:15] And of course, we can keep going further.

[00:18:18] This little yellow sine wave here is precisely one of these three plots.

[00:18:25] The second one is red,

[00:18:27] and the third one is blue. It is hidden behind the yellow one. It's not visible here.

[00:18:33] At the very beginning, it slightly shows, and then disappears.

[00:18:40] Here, I tried to draw the yellow noise in a large scale.

[00:18:51] Here it just turned blue.

[00:18:54] Let's move on.

[00:18:56] Now we can take the noises of this third level and subtract one from the other.

[00:19:02] Subtracting.

[00:19:04] Here, we essentially concatenate four y's,

[00:19:09] and refer to these y's as #[2], #[3], #[4] and #[5].

[00:19:16] Here we get a formula, which is nothing but (a - b)^3.

[00:19:21] These are binomial coefficients.

[00:19:24] And finally...

[00:19:27] So... some unnecessary actions were performed here.

[00:19:30] Let me erase them.

[00:19:36] Look...

[00:19:37] We take the noise of the fourth level

[00:19:41] and it no longer looks like noise.

[00:19:42] It's some smooth curve that tends to zero.

[00:19:46] Let's try to guess the relationship for this smooth curve.

[00:19:52] What are we doing here...

[00:19:54] We repeat the entire expression, only here we write

[00:19:58] some function of x.

[00:20:02] So... forgot the minus sign.

[00:20:06] Here we go...

[00:20:08] Here you could try

[00:20:10] just #[1],

[00:20:12] exponential of #[1],

[00:20:14] or exponential of 0.5#[1].

[00:20:16] And it turns out that this option is successful.

[00:20:20] It corresponds to the yellow plot.

[00:20:23] Only you can see that it needs to be multiplied by something.

[00:20:28] Multiplying a bit more...

[00:20:29] and a bit more... -1.83 or -1.84

[00:20:37] Here we go ... somewhere -1.83, -1.84.

[00:20:40] Alright...

[00:20:43] Subtracting this expression with a minus sign. We get a plus.

[00:20:51] So...

[00:20:53] Now we don't need this yellow approximation anymore.

[00:20:55] I'm removing the 0.5 here.

[00:20:58] Removing the plus sign.

[00:21:01] I see that it goes too far.

[00:21:04] 0.5 – still goes too far.

[00:21:13] Perhaps this is the best option.

[00:21:16] So, I took the noise of the 4th level and started seeing analytical components in it.

[00:21:23] And I extract and subtract these components.

[00:21:26] This is our standard procedure.

[00:21:30] Here, I just drew zero.

[00:21:33] Well, let's try 1 divided by 1.5.

[00:21:38] Well, probably it is right.

[00:21:43] Alright... and then we subtract.

[00:21:46] Subtracting...

[00:21:50] And here I write zero.

[00:21:54] Alright... enough of subtracting these analytical components.

[00:22:00] We can already see a sine wave here.

[00:22:03] Writing...

[00:22:05] Cosine of #1.

[00:22:15] The amplitude here is very small.

[00:22:17] How much...

[00:22:19] So much?

[00:22:23] More frequency...

[00:22:27] This is too much...

[00:22:34] Well, probably, with a minus sign.

[00:22:37] Yes.

[00:22:39] But I didn't guess the amplitude.

[00:22:41] Something like that.

[00:22:43] Subtracting this sine wave.

[00:22:50] Here I already have the answer drawn.

[00:22:58] I adjusted the frequency of the sine wave here

[00:23:04] and also the offset.

[00:23:13] So that this remaining blue noise is as small as possible.

[00:23:23] Thus, we have reached the number 14.1.

[00:23:32] This is the first nontrivial zero of the zeta function.

[00:23:38] In fact, in this video, I wanted to reach the zeros of the zeta function by the shortest path.

[00:23:45] Using elementary methods, simply analyzing these sums over powers of prime numbers,

[00:23:51] we managed to reach a sine wave

[00:23:57] with a frequency equal to the value of the imaginary component of the first zero of the zeta function on the vertical line 0.5

[00:24:14] I have a video where I tried to reach the values of the zeta function at points 2, 4, etc.,

[00:24:22] as well as at fractional values like 0.5 or -0.5.

[00:24:26] And here, for the first time, I reached the zeros of the zeta function.

[00:24:31] Such an interesting observation.

[00:24:34] Such a hierarchy of noises.

[00:24:39] And at the fourth step of removing the fourth component, we saw a sine wave

[00:24:47] that corresponds to the first nontrivial zero of the zeta function.

[00:24:54] The rest is up to you.

[00:24:57] You probably guess that this remainder can be further expanded into a sum of sine waves.

[00:25:05] Try doing it yourself.

[00:25:07] Leave comments, otherwise, it's boring for me.

[00:25:10] Good luck to everyone! Bye!
