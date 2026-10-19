# 12. От sin(x) до значений дзета функции ζ(-1), ζ(-2), ... (часть 1)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [O5yT6DGvcZI](https://www.youtube.com/watch?v=O5yT6DGvcZI). Получено: 2026-10-08T17:43:04+01:00.

[00:00:01] Hello!

[00:00:03] Math Experiments Channel.

[00:00:05] Today, we will continue exploring approximations of the function Sin[x].

[00:00:10] More precisely, I will do the exploration and you will watch.

[00:00:12] But I hope you're also explore something on your own.

[00:00:17] I have this problem: once I start an exploration, I can't stop.

[00:00:20] I keep explore and explore further...

[00:00:23] Research directions begin to branch out and deepen,

[00:00:29] and it's just impossible to stop.

[00:00:32] But that's not a problem. In fact, I recommend never stopping.

[00:00:37] When you take those final steps, you find the most interesting moments.

[00:00:42] So, patience to take those final steps is a crucial thing.

[00:00:49] Today, I hope to reach the zeta function.

[00:00:52] That means we'll start approximating Sin[x] and reach the zeta function.

[00:01:01] The distance from the sine function to the zeta function is not that great.

[00:01:06] Let's see how it will go.

[00:01:09] Today's material is challenging.

[00:01:12] With two stars.

[00:01:15] Although it's hard to explain what exactly makes this material challenging.

[00:01:20] I'm not doing any integrals here.

[00:01:22] I'm not doing any complex mathematical calculations.

[00:01:26] But the code itself probably looks complex.

[00:01:32] And also, of course, there's this intuition,

[00:01:36] when you need to see a component in the approximation that can be subtracted.

[00:01:41] You need to visually see sixth-degree polynomials or power functions,

[00:01:46] or see that you have (x^2) * Sin[x] in front of you.

[00:01:52] So, some experience with functions is necessary.

[00:01:58] But experience comes with practice.

[00:02:00] Let's see how it goes.

[00:02:04] The idea was as follows:

[00:02:05] Take the function 1/Sin[x].

[00:02:09] And it looks like this.

[00:02:10] These pieces resemble hyperbolas.

[00:02:15] If we change the scale a bit,

[00:02:18] it rises up

[00:02:19] and here returns from minus infinity. Then again...

[00:02:23] The idea is simple: let's try to express the sum of hyperbolas living in these points.

[00:02:32] Maybe something will work out.

[00:02:34] And indeed, it does.

[00:02:36] Hyperbolas are called poles.

[00:02:38] Places where we have asymptotes going up and down.

[00:02:43] These numerators of the poles are called residues.

[00:02:46] Essentially, we found the residues of the function 1/Sin[x]

[00:02:52] and tried to sum a certain number of residues in the vicinity of zero

[00:02:56] and compare the results.

[00:02:58] Here, I'm comparing Sin[x] with 1 divided by the sum of residues.

[00:03:04] And we see that the functions almost coincide in the vicinity of small "x".

[00:03:08] Well, then, of course, there are significant divergences.

[00:03:14] The blue plot goes up and down,

[00:03:17] while Sin[x] calmly oscillates around zero.

[00:03:24] A very natural idea is to look at the difference of the function to which we approximate our function Sin[x].

[00:03:35] Here we have something similar to xSin[x].

[00:03:38] Not exactly xSin[x], of course.

[00:03:41] xSin[x] looks different.

[00:03:48] Firstly, it becomes very large here. We need to multiply it by something.

[00:04:00] There is some difference.

[00:04:01] It is visible that our xSin[x] is oscillating around zero,

[00:04:05] while here, you see, it is a skewed xSin[x].

[00:04:08] And the oscillations of the blue plot are twice as frequent.

[00:04:10] In short, what we did here:

[00:04:12] we divided this plot, the blue one, by "x", after which it started to resemble a regular oscillatory plot.

[00:04:26] But we need to understand the scale here.

[00:04:31] And we need to understand that the oscillations occur twice as often.

[00:04:35] Well, we figured that out.

[00:04:38] To restore the scale to normal,

[00:04:40] from 5 * 10^-6 to normal numbers in the range from 0 to 1,

[00:04:46] we had to multiply it by 20m^2.

[00:04:52] And if we try different values of m here,

[00:04:58] we will get small numbers.

[00:05:00] Here we have taken the next step.

[00:05:02] Here, after this event, we found Cos[2x],

[00:05:08] subtracted it, and this is the result of the subtraction.

[00:05:12] And here we went down the wrong path,

[00:05:16] when we started studying this thing.

[00:05:20] We should have studied another thing.

[00:05:24] We should have simply multiplied this expression by g[x, m].

[00:05:30] Well, what can we do...

[00:05:32] We took Sin[x],

[00:05:34] took the approximation,

[00:05:35] subtracted one from the other,

[00:05:36] didn't think for long...

[00:05:38] But then we realized that it would have been better to act this way.

[00:05:42] But I want to deliberately go down the wrong path for now,

[00:05:47] to hit my head against something and understand... see the wrongness of this path.

[00:05:54] And for now, we have this

[00:06:00] and we wonder what this 20 is.

[00:06:02] It could be 2Pi^2, or it could be a solid 20.

[00:06:06] If we assume that we prefer the yellow plot over the blue one, then we should go with 2Pi^2.

[00:06:15] Here it's unclear, although the picture is undoubtedly beautiful.

[00:06:19] If we need to go with 2Pi^2, here's what we have.

[00:06:25] Such an approximation.

[00:06:27] Or if we replace it with Cos[2x-1]/2 multiplied by Sin[x]^2, then this is what we have.

[00:06:34] Alright. Let's move on.

[00:06:37] Here...

[00:06:39] I won't repeat.

[00:06:40] Also, in the previous video, we took a few steps

[00:06:42] and figured out to replace m^2 with m(m+1).

[00:06:46] It's quite a difficult guess,

[00:06:50] which certainly makes the subsequent steps much easier.

[00:06:54] But in reality, it also leads to a dead end.

[00:06:58] So at some point, we have to abandon m(m+1) and go back to m^2.

[00:07:07] It makes you want to bang your head against the wall again.

[00:07:10] This is what we have here.

[00:07:13] At this stage, I see an oscillatory function here.

[00:07:18] Although around zero, everything is somehow messed up

[00:07:21] and it doesn't get fixed by increasing m.

[00:07:23] But I want to repeat these oscillations as much as possible

[00:07:27] And here comes the idea: what if it's Sin[x]^2 again?

[00:07:31] And yes! It looks like it.

[00:07:33] Although... how can I say.

[00:07:36] Now I'm not absolutely certain if it's exactly 1.

[00:07:42] Maybe it's 0.95 here, who knows.

[00:07:46] We found the yellow plot that matches the blue one in some places,

[00:07:49] and then we subtract the yellow plot from the blue one.

[00:07:53] Well, I'll use these words...

[00:07:57] Of course, functions are subtract.

[00:08:00] All of this goes off to infinity

[00:08:02] and, of course, we want to multiply this difference by x.

[00:08:12] Maybe even multiply it by x again.

[00:08:19] Alright... Good.

[00:08:25] Here, it's already something unclear...

[00:08:29] Next, we try to draw these things.

[00:08:32] Well... good.

[00:08:33] Here's our approximation.

[00:08:35] Here's the function we're approximating.

[00:08:37] And then various ideas for remainders come into play.

[00:08:41] The remainders already have m in the denominator.

[00:08:47] So, as m increases

[00:08:49] it tends towards this,

[00:08:51] but we're interested in the remainders.

[00:08:56] The colors in Mathematica go as follows: blue, yellow, green, red, violet.

[00:09:01] It's impossible to understand, you just need to memorize.

[00:09:05] And what I'm trying here.

[00:09:08] The blue plot - I simply take m^2.

[00:09:10] And here's this guess that m^2 should be replaced with some second-degree polynomial.

[00:09:14] And by trial and error, it was found to be m(m+1).

[00:09:21] Maybe take a different interval after all.

[00:09:23] For example, like this.

[00:09:26] Or even larger,

[00:09:28] to see the difference between all these ol.

[00:09:34] The blue plot is hidden behind the green one.

[00:09:38] I know that and I'm telling you.

[00:09:41] The yellow plot (see?) is much better than the blue-green one.

[00:09:46] And the red and violet ones don't provide any significant improvements compared to the yellow plot.

[00:09:52] So there is the yellow plot

[00:09:54] and here are attempts to guess the value of the second term.

[00:09:57] This is the first term, an approximation of the difference.

[00:10:01] This is the second term.

[00:10:03] But all of them are unsuccessful.

[00:10:08] So you don't have to look at them carefully.

[00:10:12] But this is a process that is important to show, how it all happens.

[00:10:16] One must admit.

[00:10:18] Yes. The yellow plot was an improvement over the blue-green one,

[00:10:23] but the violet and red, although we saw something there,

[00:10:29] it didn't help much.

[00:10:32] We saw this sine wave far from x = 0.

[00:10:40] In the range of large x values, the violet plot may be good.

[00:10:45] Yes, it's good. See?

[00:10:46] The violet plot is closer to the x-axis compared to the red one,

[00:10:52] but not "dramatically," as the English say.

[00:10:58] Attempts to add one more term by analogy also don't yield anything.

[00:11:02] There is green plot...

[00:11:05] Here it is slightly better than the yellow one,

[00:11:08] and here the opposite.

[00:11:11] And all of this is just the beginning.

[00:11:13] The beginning of this game of subtraction and division.

[00:11:20] Let's engage in it more carefully.

[00:11:24] As Zhvanetsky said: "You need to be more thorough, more thorough."

[00:11:27] Now we will try to do all this "more thoroughly."

[00:11:32] And here I have come to such a tangle.

[00:11:41] Which...

[00:11:44] Depending on the scale, we see different pictures.

[00:11:46] It's a power function.

[00:11:49] If we slightly decrease the scale, we see a sine wave above of the power function.

[00:11:55] The power function is not just any parabola like x^2,

[00:11:58] but x^6 or something like that.

[00:12:06] Well, in the vicinity of zero...

[00:12:11] It's more like a parabola...

[00:12:15] Beyond that, something incomprehensible...

[00:12:17] And this incomprehensible thing remains stable when m changes.

[00:12:22] So, this part needs to be approximated with components to which we don't have to add a multiplier m1.

[00:12:32] I denote m1 like this.

[00:12:38] And at larger scales, the dependence on m is felt.

[00:12:44] You move m, and the numbers on the "y" axis change.

[00:12:51] And here, you can still move.

[00:12:53] Here, you can find something further...

[00:12:55] Some steps have been taken here. It doesn't matter which ones.

[00:13:00] Let's put a comma and write, for example, xp^6.

[00:13:09] There it is.

[00:13:16] What do we need to do here... Let's try dividing by m1.

[00:13:23] That's not fair. I guessed.

[00:13:25] I just guessed. It happens sometimes.

[00:13:30] And that's the complexity of this whole story.

[00:13:36] You need to have experience and quickly guess, otherwise the endeavor turns into tedious hours of trial and error.

[00:13:46] Guessed it! (x^6)/m1

[00:13:50] And now, when I subtract, it will be easier for me to deal with these oscillations.

[00:13:57] This component was found in a similar way.

[00:14:00] You understand, right?

[00:14:01] I remove the comma, write a minus sign.

[00:14:04] Slap!

[00:14:06] Again, I go to a larger scale,

[00:14:09] I see these oscillations.

[00:14:10] Great.

[00:14:12] I currently like xm to be around 70.

[00:14:15] I want to act here.

[00:14:17] And I'm quite content with m = 80.

[00:14:21] I want to live on this x scale and with this m.

[00:14:25] I write a comma. xp to some power...

[00:14:28] xp = x/Pi.

[00:14:32] Sinp = Sin[x]/Pi.

[00:14:36] Simply during all these games, it was discovered that

[00:14:40] if you take x, then the next step will require dividing by 3. Something similar to 3.

[00:14:49] If you take x^2, then later you'll want to divide by Pi^2.

[00:14:54] So, x always goes with Pi.

[00:14:55] The same was noticed about Sin[x].

[00:14:57] If you subtract it, the multiplier to it contains 1/Pi.

[00:15:05] I missed this step. Sorry.

[00:15:07] Otherwise, the video would be too long.

[00:15:11] And not everyone will watch this video until the end.

[00:15:14] I think I will lose a significant portion of the audience here.

[00:15:20] But guys, don't get lost. This is very important!

[00:15:25] We will reach the zeta function.

[00:15:28] We started with a simple idea of approximating the sine with hyperbolas.

[00:15:31] And we will get to the zeta function in a matter of hours...

[00:15:43] So... what I want...

[00:15:44] I want to create oscillations with increasing amplitude.

[00:15:52] Let's assume the amplitude grows like x^4.

[00:15:58] Let's check...

[00:16:04] Hmm, some kind of incorrect artifact appears here.

[00:16:10] Mistaken one.

[00:16:12] Clearly a mistaken artifact.

[00:16:16] Alright...

[00:16:23] It feels ike the amplitude increases with a greater degree.

[00:16:34] Here I'm in phase,

[00:16:37] and here in antiphase.

[00:16:39] So I guessed the parity wrong.

[00:16:41] Let's try the 5th power.

[00:16:44] Maybe it's actually the 3rd power.

[00:16:47] Yes!

[00:16:49] That's closer to the truth.

[00:16:52] Although I'm not certain.

[00:16:58] Not sure...

[00:17:00] Sines are better to look for in the region of small x values.

[00:17:08] Well, how can we understand it here...

[00:17:10] The power function that is hidden here interferes with the fitting.

[00:17:19] Let me try writing 2 here.

[00:17:25] Listen... maybe it's actually 2.

[00:17:29] Let's subtract 2.

[00:17:31] We can write "a" here...

[00:17:34] By the way, I added "a" here.

[00:17:36] ...and try different values of "a".

[00:17:38] So, "a" is likely to be equal to one.

[00:17:43] And we'll leave the fitting of "a" for later.

[00:17:45] For now, let's subtract,

[00:17:48] to see this thing here.

[00:17:51] This is a parabola,

[00:17:57] which doesn't change its scale when m changes,

[00:18:02] but it changes over time...

[00:18:11] Let's give it a go...

[00:18:13] xp^2

[00:18:19] With a minus sign.

[00:18:23] And it's not enough...

[00:18:24] Let's add a two.

[00:18:27] Still not enough...

[00:18:30] We're short on twos.

[00:18:32] Let's try a three.

[00:18:35] Oh!

[00:18:36] That looks like the truth.

[00:18:38] Very, very close to the truth.

[00:18:43] Yes! See?

[00:18:44] We have a parabola, and there's a sine wave oscillating around it.

[00:18:49] Excellent!

[00:18:55] Remove the comma.

[00:18:57] Change minus to plus.

[00:18:59] And so on...

[00:19:01] All of this can be unraveled in reverse.

[00:19:04] So we have some approximation here.

[00:19:07] We highlight, we copy,

[00:19:09] and we set it equal to zero.

[00:19:12] I replaced this interior part (this one here) with y to make it easier.

[00:19:17] And we solve this equation for y.

[00:19:20] We get an answer. Here's what the approximation looks like.

[00:19:23] And this is already the next level of quality approximation.

[00:19:29] Let's compare. This is what we had.

[00:19:33] This is what it became.

[00:19:34] Well, I'll say it again, this is all the wrong way.

[00:19:37] We continue down the wrong path, even though we enjoy it and get some results.

[00:19:44] It's clear that the old version (blue) is much worse than the new one (yellow).

[00:19:50] If the new yellow one at this point, in the vicinity of the number 2,

[00:19:56] gives an approximation of 4 * 10^-9 for m = 20,

[00:20:03] then the blue plot at the same point has an approximation of 1 * 10^-6.

[00:20:14] A few orders of magnitude. We earned a couple of orders here.

[00:20:18] But, in truth, we had to add all of this.

[00:20:23] Good.

[00:20:27] Now, by the way, we can look at the plan.

[00:20:29] We have an extensive plan.

[00:20:33] Now we'll look at a more comprehensive version.

[00:20:36] That is, what other terms can we find.

[00:20:42] Also, we will finally choose the right path.

[00:20:45] Realize that the chosen path is wrong and try simply changing the numerator and denominator.

[00:20:53] Then, for the sake of interest, we'll derive another formula for Pi from this approximation.

[00:20:59] And we'll summarize a bit.

[00:21:02] Then we will learn the truth about what is really at stake here.

[00:21:10] What infinite series of m is involved.

[00:21:18] And we will start thinking about this truth.

[00:21:21] This truth will be got through the Taylor series expansion by some function.

[00:21:27] But the coefficients in this expansion will be unknown to us in the form of a formula.

[00:21:35] We will know them numerically for some initial terms.

[00:21:40] And here we will start guessing what these numbers are.

[00:21:47] Here we continue to guess...

[00:21:50] And only here we will get the final answer through the zeta function.

[00:21:55] Further, various bonus tracks,

[00:21:57] but no one will be here anymore...

[00:22:02] Well, listen... maybe you should take breaks? Then you'll make it to the end.

[00:22:09] I just don't feel like dividing this video into parts.

[00:22:13] I'll make one big video.

[00:22:16] And you can pause and have tea at the right places.

[00:22:21] Okay.

[00:22:23] If you approach the problem I solved earlier with enthusiasm, you can uncover this.

[00:22:32] Here we introduce another notation, xsinp.

[00:22:35] It's just a thing: xSin[x]/Pi^2.

[00:22:41] Let's play it.

[00:22:44] I won't repeat how all of this was found.

[00:22:48] Although, I must say, the process is very, very interesting.

[00:22:52] Here I stopped.

[00:22:53] There seems to be some power visible, but it's already difficult. Really difficult.

[00:23:00] Moreover, as you approach small values of x,

[00:23:05] here you can see that we have reached a point where the floating-point precision is not enough.

[00:23:19] 10^-16. We have already reached this limit.

[00:23:23] Here we are already living at the level of approximation of 10^-16.

[00:23:28] When you see such pictures with noise, it is a clear sign that it's time to stop.

[00:23:37] You can stop acting like a dumb programmer-engineer.

[00:23:40] You can start thinking.

[00:23:44] Moreover, this picture around zero,

[00:23:47] it looks like this.

[00:23:50] And here some sharp angle is observed,

[00:23:53] This is the moment when the story with m1, which is equal to m(m+1), ends,

[00:24:05] and it starts...

[00:24:07] Nothing starts. There is a deadlock. It becomes very difficult to move forward.

[00:24:12] If we ask Mathematica to give us an answer: what do we get if we set our approximation to zero?

[00:24:20] As if we found an absolutely accurate approximation.

[00:24:22] If the error were not equal to this nonsense, but if it were equal to zero, what would the coveted "y" be?

[00:24:33] This is what it would be.

[00:24:35] And if we group the terms into these pieces,

[00:24:41] then we get the following approximation formula.

[00:24:47] We approximate Sin[x] with these poles.

[00:24:52] Here we go...

[00:24:53] And of course, after an hour of contemplation, anyone can guess that...

[00:25:02] I won't say the word "obviously."

[00:25:04] ...that actually we should have divided the sine by this expression.

[00:25:11] Because these popping up sines here...

[00:25:14] First of all, it's silly. We are looking for an approximation of the sine, and somehow in this approximation, we have a sine.

[00:25:19] We don't solve the sine approximation problem like this.

[00:25:22] We want to get rid of them.

[00:25:23] Where did these sines come from?

[00:25:25] They appeared here because of this division.

[00:25:30] Here's what we have here.

[00:25:31] If we simplify the picture, here's what we have here.

[00:25:35] And the thought arises: what if we had to act differently?

[00:25:40] Take our approximating function "a" and the original sine function

[00:25:48] and consider this expression.

[00:25:52] Because if this expression equals something simple,

[00:25:56] where there is no such power series of sines,

[00:26:03] then, if this statement is true, then 1/asin...

[00:26:10] we move -1 to the other side.

[00:26:12] We get that 1/asin will be equal to this.

[00:26:19] And we take this and consider it as "p".

[00:26:25] and we find that 1/(1-p) is the formula of an infinite geometric progression.

[00:26:34] And these sine powers pop up.

[00:26:40] Intuition, of course, is complex here.

[00:26:44] But it exists.

[00:26:50] And a person who doesn't know the correct answer could actually turn around here

[00:26:56] and choose this other path.

[00:26:59] We were dealing with this,

[00:27:00] now we'll be dealing with this.

[00:27:03] We go through the same process.

[00:27:07] We play the same game.

[00:27:09] And here we manage to achieve a greater number of m1

[00:27:18] and reach this pattern.

[00:27:22] Of course, I would very much like to show you all these steps, but no. There's not enough time.

[00:27:32] Some interesting moments

[00:27:34] Here I dare to divide by (x^2 - p).

[00:27:38] Yes, it's an interesting moment.

[00:27:40] Maybe it's worth showing.

[00:27:42] (No, it's not)

[00:27:45] As a result, we get this approximation.

[00:27:52] A long polynomial in which there is no Sin[x] and Sin[x] powers.

[00:27:58] Let's remember this as a certain answer.

[00:28:02] Alright.

[00:28:03] Here, a different approach is chosen, where I didn't divide by (x^2 - Pi^2),

[00:28:10] but raised this parabola by one,

[00:28:12] then subtracted this parabola.

[00:28:15] An essentially equivalent option.

[00:28:18] And here's what we end up with when we bring this to the end.

[00:28:25] The last term is quite debatable.

[00:28:29] You can take a look at this option, for example.

[00:28:35] I just wrote it quite roughly.

[00:28:40] 10 and 45.

[00:28:44] Maybe it's not 45.

[00:28:45] Maybe it's 44.

[00:28:46] You can't see it just by looking.

[00:28:52] But you won't believe it, 45 is actually the correct answer, as it turns out later.

[00:28:58] So I saw the component x in some large power,

[00:29:04] picked four and a multiplier of 45,

[00:29:08] and then subtracted.

[00:29:13] And here it's already difficult to proceed because as "m" increases...

[00:29:19] And I want to increase "m".

[00:29:22] As "m" increases, we already have some noise.

[00:29:27] And we've reached a point where machine precision no longer allows us to move further.

[00:29:36] We calculate the answer in this variant.

[00:29:39] Let's remember it.

[00:29:41] We ask Mathematica how much these two variants I found differ,

[00:29:46] with division by x^2 - Pi^2 and without division.

[00:29:49] They don't differ that much.

[00:29:51] In the second one, I managed to reach 45.

[00:29:54] You can see that the difference...

[00:29:57] Don't count the one, maybe I wrote it unnecessarily.

[00:30:07] Here we have a fourth power in the denominator of m1 everywhere.

[00:30:10] So it's actually an eighth power of m.

[00:30:15] And here things are not so straightforward.

[00:30:17] Yes, in the initial approximation, I used the letter "b".

[00:30:20] And, by the way, if b equals 9, then this pair vanishes.

[00:30:25] And if b equals 45, then this pair vanishes.

[00:30:29] That's why in that approximation, I couldn't decide on b.

[00:30:34] One component vanishes with one b, and the other with another.

[00:30:40] Therefore, the variant with division by (xp^2) - 1 is not quite correct.

[00:30:45] Division seems to be bad in general.

[00:30:48] So we need subtraction.

[00:30:50] As this specific problem shows,

[00:30:52] we need to do subtraction, not division.

[00:30:56] Okay.

[00:31:01] I wrote a rule here to eliminate all higher powers of m. Higher than 4.

[00:31:11] And precisely at this level, these two approximations coincide.

[00:31:19] But in the approximation up to the next fourth power.

[00:31:23] Here we see 45, 10

[00:31:27] 6, 3, 13

[00:31:29] Here we already have interesting numbers different from one.

[00:31:32] By the way, it turned out that they all have only a numerator.

[00:31:37] Integers, integer coefficients.

[00:31:40] Why?

[00:31:43] Well...

[00:31:47] Let's go back to the number m.

[00:31:50] Here I replaced our gotten answer.

[00:31:55] In this answer, I replaced m1 with m(m+1)

[00:31:59] and asked to expand this expression in terms of powers of m.

[00:32:05] And here, too, we got integer values for all coefficients.

[00:32:12] As I said, everything seems reliable up to m^8.

[00:32:18] Essentially, we got such an approximation.

[00:32:20] 1 minus Sin multiplied by the sum

[00:32:23] equals xSin/(Pi^2) multiplied by this polynomial,

[00:32:28] which you see in front of you.

[00:32:30] The polynomial starts with the fourth power of m.

[00:32:35] Well, previously it was just 1/(m1^2)

[00:32:43] And if we express the sine from this, here's what we get

[00:32:49] Let's see what happens if we return to the old idea.

[00:32:54] If we really divide 1/gg by sine. ("gg" is the summ)

[00:32:58] What will happen then?

[00:33:00] Then we get this expression.

[00:33:04] Here I divided by Pi^2 mentally

[00:33:08] and xsin also mentally contains division by Pi^2.

[00:33:14] xsin - it's Sin[x]/Pi^2 and also multiplied by x.

[00:33:22] So, this is what we get.

[00:33:26] That is, this is what we could have got in the first incorrect variant, if we had continued.

[00:33:32] But here we have m's, and we need to get m1.

[00:33:35] Well...

[00:33:37] Let's go back to m1 like this.

[00:33:40] Expressing m through m1 using the following formula.

[00:33:43] And then we ask to expand in terms of powers of m1 up to the fourth power.

[00:33:48] And we get something.

[00:33:50] Here we see exactly these components: 1, 2, 8, 13.

[00:33:57] Let's remember the result we had.

[00:34:00] Where is our beloved result.

[00:34:05] Here it is.

[00:34:06] I didn't execute this.

[00:34:08] The result we got by moving in the wrong path.

[00:34:12] And let's compare what we get from this formula

[00:34:15] and from this one.

[00:34:18] That is, we followed the right path.

[00:34:20] Got a certain formula for the expansion of the inverted fraction.

[00:34:25] But here we tried to go back to the old variant and see,

[00:34:29] what would happen if we continued in the old option.

[00:34:33] This is what would happen.

[00:34:34] And there are coincidences.

[00:34:35] 1/m,

[00:34:37] 1/(m^2)

[00:34:40] So these coefficients are correctly found.

[00:34:45] m1 is additionally hidden here.

[00:34:47] So don't pay attention to the fact that there is a square here, and here it's just m.

[00:34:51] 13, 13

[00:34:53] 3, 3

[00:34:54] 1, 1

[00:34:55] 6, 6

[00:34:56] Everything matches. Perfect.

[00:35:00] With Sin[x]^2 there is a variable "a".

[00:35:11] This two matches.

[00:35:14] But with x^2 it's not so straightforward.

[00:35:24] Alright.

[00:35:25] Now let's look at the quality of the approximation.

[00:35:30] Just sin minus one divided by the sum.

[00:35:33] And here are these new approximation variants that we got.

[00:35:39] And these polynomials no longer contain sines.

[00:35:43] Everything is already calculated here.

[00:35:48] Let's try.

[00:35:50] The blue plot - the first approximation.

[00:35:56] The yellow plot - we took m1^2.

[00:36:01] Essentially, we took the component with m1^2 in the denominator.

[00:36:07] And here we took the component with m1^3 in the denominator.

[00:36:12] This is m1.

[00:36:14] Here is m1^2.

[00:36:16] And we got the blue plot.

[00:36:20] The difference is a small number, 0.0005, but we can do better.

[00:36:28] Where is our yellow plot?

[00:36:29] Here it is, finally born.

[00:36:32] 2 * 10^-9.

[00:36:36] And the green plot is 2 * 10^-11.

[00:36:42] These are the different levels of approximation.

[00:36:47] So, what do we have?

[00:36:48] By summing up 20 terms,

[00:36:51] or more precisely, 20 on the left, 20 on the right,

[00:36:54] we get 10^-11 as an approximation in the vicinity of zero, from -5 to 5.

[00:37:04] By the way, it can be not 20 + 20 terms, but exactly 20 terms,

[00:37:07] if we combine these symmetric terms.

[00:37:14] And here it is shown that this

[00:37:18] can be replaced with this.

[00:37:21] And here I tried to take even more terms.

[00:37:29] Let's have a look.

[00:37:33] So, the blue plot

[00:37:37] is this variant.

[00:37:40] This is not that blue plot. This is the first approximation, where we take m1.

[00:37:45] Then the yellow plot appears.

[00:37:50] We took m1^3.

[00:37:55] The old approach.

[00:38:00] This is the new approach. Also m1^3.

[00:38:06] Here it is in green. The new approach,

[00:38:09] where we flipped the fractions.

[00:38:11] It works better.

[00:38:13] And the next approach: we take m1^3 here, and here we also have m1,

[00:38:17] m^4 approximation.

[00:38:21] This is the red plot.

[00:38:23] But there is also the violet one.

[00:38:25] The violet one is simply the approximation of the Taylor series taking m terms.

[00:38:34] Actually, I chose two m terms here because half of the terms in the sine expansion are zeros.

[00:38:44] So, it turns out that the Taylor series approximation works best here.

[00:38:48] That is, we didn't find any new, more efficient way to calculate sine.

[00:38:55] Although our method has its advantages. I'll show you what they are now.

[00:39:01] The Taylor series in the form of this plot goes to infinity abruptly,

[00:39:10] while our approximations work over a large range of x values.

[00:39:18] See, right?

[00:39:22] Here is our red plot.

[00:39:25] It also has a tendency, of course. It works particularly well in the vicinity of small x values.

[00:39:31] But it works quite well around x = 20, unlike the Taylor expansion.

[00:39:41] Moving on...

[00:39:43] Further, we can find the formula for the number Pi.

[00:39:48] Here's what we have.

[00:39:51] Here we got our approximation, subtract it from the sine.

[00:39:54] Set it equal to zero and replace x with (Pi^2)/6.

[00:40:01] Then replace Pi with pix.

[00:40:05] This expression here (/.), and then the rule in curly braces,

[00:40:10] they effectively replace what appears to the left of the rule with what appears to the right of the rule.

[00:40:19] And we get that Pi is expressed from this formula because,

[00:40:29] when we substitute x = (Pi^2)/6, because x is always paired with division by Pi,

[00:40:36] we simply get 1/6 raised to some power.

[00:40:39] Here it is (1/6)^4,

[00:40:41] and here (1/6)^2.

[00:40:44] So...

[00:40:45] Anyway, check for yourself.

[00:40:50] It turns out to be a simple linear equation for Pi.

[00:40:54] Well, Pi can be considered as x.

[00:40:56] And here's what we get.

[00:40:59] Wonderful!

[00:41:00] Let's fix this approximation as the function PiX and draw it.

[00:41:11] Calculate PiX here for different values of m.

[00:41:21] And we get such fractions.

[00:41:27] They are all close to Pi. Very close.

[00:41:30] Let's look at the difference between this and Pi.

[00:41:34] Simply -Pi.

[00:41:38] And you can see that they go to 10^-14, 10^-15.

[00:41:42] Let's draw the plot of errors.

[00:41:44] But it's better to draw not the errors themselves, but the logarithms of them.

[00:41:47] Here I take the absolute values of these errors,

[00:41:51] decimal logarithm, to understand how many correct digits of Pi we know.

[00:42:00] For m equal to ten, we know...

[00:42:03] Well.. some amount. 13 decimal places.

[00:42:06] I sum up 15 terms

[00:42:10] right here.

[00:42:12] And then I compute this formula.

[00:42:15] We have 15 digits of accuracy for the number Pi.

[00:42:18] And with 20 terms, we have -16. The logarithm of the error.

[00:42:29] So, we got a formula for approximating the sine function.

[00:42:39] What is its accuracy?

[00:42:42] We don't have a clear answer.

[00:42:43] We know the experimental error is 10^-13 for m = 10.

[00:42:48] That's not for Pi, but for the sine function.

[00:42:53] Somehow, m(m+1) appeared here. What is it?

[00:43:01] It's unclear for now.

[00:43:05] Why are the coefficients in this expansion integers?

[00:43:08] I'll ask this question again. It's an important question.

[00:43:11] When you see integer coefficients,

[00:43:17] it's likely some combinatorial object.

[00:43:20] That is, the quantity of some things.

[00:43:24] By the way, some Fibonacci numbers. 1, 2, 3, 8

[00:43:29] 6 is not a Fibonacci number, but still.

[00:43:33] Is there any way to guess? To find some patterns in these numbers and guess what's next.

[00:43:39] Well.. I'll say right away: it's unlikely.

[00:43:43] It's difficult to guess.

[00:43:45] Mathematica knows the truth, what this sum equals.

[00:43:49] No, actually, it doesn't know.

[00:43:50] It makes an error here...

[00:43:53] You input this sum and it says:

[00:43:55] I have these nice smooth analytical functions somehow programmed inside.

[00:44:02] And these functions...

[00:44:07] You can check the help...

[00:44:12] It says it's just a sum of (k+a)^s, where k varies from 0 to infinity.

[00:44:19] Well, it turns out that if we take, for example, a = -10,

[00:44:24] and then take a = 10,

[00:44:26] and then subtract this function Φ, where a = -10 and a = 10,

[00:44:33] we get a finite sum.

[00:44:34] Well, indeed.

[00:44:36] But what does "s" equal?

[00:44:38] One.

[00:44:40] Well, yes, that's what he writes.

[00:44:41] "s" equals one,

[00:44:43] and "a" is some complex expression, in short, it wrote.

[00:44:48] We could trust Mathematica,

[00:44:50] but no. Here there is actually some error.

[00:44:56] Slap!

[00:44:59] If we subtract this

[00:45:01] from this. That is, add 0.811, we get 2.

[00:45:07] This is the true value of the sum. I just plugged in a specific value here.

[00:45:12] And here, it used it's great intellect to turn this sum into a specific expression of an analytical function,

[00:45:23] and then he plugged it in and got a different answer.

[00:45:28] This is because this function has poles along the path from -20 to 20,

[00:45:37] and you need to be very careful about how you bypass these poles, from which side.

[00:45:43] We went too far, in short.

[00:45:46] And miracle of miracles! Mathematica knows the series expansion of these functions.

[00:45:52] And you can simply ask it for the answer.

[00:45:56] This function G, which we previously called gg of m.

[00:46:02] And I ask, what is the expansion in terms of x?

[00:46:06] It knows the expansion in terms of x.

[00:46:09] Oh my God! Pi squared is here.

[00:46:11] It knows everything. Everything has already been calculated before us.

[00:46:15] All these formulas were found a long time ago.

[00:46:22] But we need to expand the function G

[00:46:28] (or rather, this expression here)

[00:46:30] in terms of powers of x and powers of 1/m.

[00:46:35] How do we do that?

[00:46:37] Well, from here on, it's just about looking and enjoying.

[00:46:41] Here...

[00:46:44] it showed his intestines. That he knows all about it.

[00:46:49] Here, I allow the computation to be done correctly.

[00:46:55] Please expand it as a series around zero up to x^8.

[00:47:01] And in the vicinity of n, which is infinity,

[00:47:03] but this means that I want to expand it as a series in 1/m.

[00:47:07] I also want to get the expansion up to 1/m^8.

[00:47:13] He starts writing zeta functions here.

[00:47:17] Here we have finally reached them.

[00:47:20] And I tell him that

[00:47:24] it can be simplified by removing the option he added.

[00:47:31] Then I have to ask him to replace m with 1/u and divide it by 2 moreover.

[00:47:39] Why?

[00:47:40] I remind you that the expansion depended on the parity of m,

[00:47:43] so here I wrote 2m,

[00:47:46] and m belongs to Integers.

[00:47:47] You can write it like this. That's how smart it is.

[00:47:51] When you have an expression that depends on whether

[00:47:55] m is an integer or not, what parity m has,

[00:47:58] you surround that expression with Assuming and write a list of your assumptions.

[00:48:05] Your knowledge of the variables involved in the expression here.

[00:48:13] That's how you can manipulate it to get the answer.

[00:48:18] And this answer is quite complex.

[00:48:23] It's a complicated one.

[00:48:25] But let me rather show you this.

[00:48:32] It turns out to be a quite complicated answer.

[00:48:36] And this answer involves u.

[00:48:40] And we need to ask Mathematica for this series in terms of x (powers of x)

[00:48:48] to apply another expansion series in terms of u.

[00:48:57] This was done, and we got this answer.

[00:49:08] There is a long pause here because...

[00:49:14] Of course, it's unclear how we can reach all of this.

[00:49:19] Up to this code.

[00:49:23] It's unclear how all this knowledge was built into Mathematica.

[00:49:31] Well... what can be done here...

[00:49:34] There are gaps in my videos...

[00:49:45] It's inevitable, we have to accept it.

[00:49:51] By the way, the support team replied to me, confirming that there is indeed an error in the "summ" function,

[00:50:00] and it's quite amusing,

[00:50:04] that

[00:50:06] this sum

[00:50:09] is not automatically expanded into the correct analytical form.

[00:50:19] Let's compare the truth we got here with what we previously calculated

[00:50:23] when we were dealing with component selection.

[00:50:26] Here's what we had there.

[00:50:28] Well... actually, we had this, I remind you.

[00:50:31] 1, 2, 8, 13, 3, 45... and our 10, these last two terms.

[00:50:37] And then we simply substituted m1 with m(m+1),

[00:50:42] expanded it in terms of 1/m

[00:50:45] and got this thing.

[00:50:47] With integer coefficients!

[00:50:50] The alarm goes off immediately!

[00:50:54] And what do we see?

[00:50:56] 1, 1, 3, 17, 56...

[00:50:59] Hmm... something's wrong.

[00:51:04] 1, 1, 1, 3, 17, 155...

[00:51:06] Well, that's already an incorrect term.

[00:51:09] It is clear.

[00:51:10] For x^2: 1, 2, 5, 28

[00:51:13] 1, 2, 5, 28...

[00:51:15] 92 for m^10.

[00:51:18] Well, in the 10th power, it's definitely wrong.

[00:51:20] The 8th is still correct.

[00:51:23] x^4

[00:51:25] as well.

[00:51:27] Great.

[00:51:29] So, using experimental methods, we correctly found everything up to the 8th power of 1/m.

[00:51:37] This was confirmed by Mathematica,

[00:51:40] which we trust,

[00:51:43] if we disregard these small errors.

[00:51:48] Alright.

[00:51:50] Let's start thinking!

[00:51:52] To be continued...
