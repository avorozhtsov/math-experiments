# 19. Конечные поля. Часть 1 – основные свойства, малая теорема Ферма, символ Лежандра (eng. subs)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [XZZqAepfsbI](https://www.youtube.com/watch?v=XZZqAepfsbI). Получено: 2026-10-08T17:42:18+01:00.

[00:00:01] Hey there! Welcome to "Mathematical Experiments".

[00:00:05] Today, I want to tell you about finite fields.

[00:00:08] It's one of the coolest and most intriguing topics in mathematics.

[00:00:14] And I have quite an ambitious goal:

[00:00:17] to prove the existence of fields of size p^k,

[00:00:21] and also show how we can use Machine Learning to discover and guess the quadratic reciprocity law.

[00:00:33] Of course, there are many interesting videos on this topic on YouTube.

[00:00:37] And here's my list of recommendations.

[00:00:40] The Mathologer channel. Specifically, this video about finite fields and the quadratic reciprocity law.

[00:00:45] It's in English, but you might find a translation.

[00:00:48] You can also use the Yandex Browser translator.

[00:00:53] Alexey Savvateev

[00:00:55] Also, two lecture series.

[00:00:58] I recommend watching it.

[00:01:00] He's always very enthusiastic, with a lot of inspiration, talking about numbers, Cardano's formulas and more.

[00:01:10] And one last recommendation.

[00:01:13] With only 11 thousand views...

[00:01:15] It should have more, because it's a really great algebra course.

[00:01:19] It's not only about number fields, but also about simpler algebraic structures,

[00:01:24] which are usually the starting point for algebra courses.

[00:01:26] Semigroups, groups, modules and number fields too.

[00:01:31] So... I'm going to tell you in my way.

[00:01:36] What are "numbers"?

[00:01:39] Let me list some facts that you might already know.

[00:01:42] We have rational numbers,

[00:01:45] real numbers,

[00:01:47] complex numbers.

[00:01:49] Objects in these three sets can be multiplied, added, divided, and subtracted.

[00:01:54] Here's the next example. This is the ratio of two polynomials, where Q is not equal to zero.

[00:02:01] And, of course, we need to fix the field of coefficients for this polynomial.

[00:02:07] Here's how these three fields are denoted.

[00:02:11] We can write such relationships between these three fields.

[00:02:17] Alright.

[00:02:19] Apart from fields, where we can add, multiply, subtract and divide,

[00:02:24] there are sets like natural numbers.

[00:02:28] There's a serious issue with subtraction there.

[00:02:30] When you do 2 - 10, you end up outside the realm of natural numbers.

[00:02:35] Z doesn't have a problem with subtraction, but it has an issue with division.

[00:02:41] You can further define polynomials with coefficients from Z.

[00:02:47] These can also be multiplied and added, creating objects within the same set, but you can't divide.

[00:02:54] Interesting fact from the future, so to speak:

[00:02:58] сomplex numbers can be constructed as a certain equivalence class

[00:03:05] in the ring of polynomials over real numbers.

[00:03:09] But that's probably a bit complex words. Let's skip them.

[00:03:13] Today, I want to tell you about something where you can perform addition and multiplication on a finite set of objects,

[00:03:21] creating a structure we're familiar with. The structure of numbers.

[00:03:27] These finite number fields are denoted as F2, F3, F4, F5, and so on.

[00:03:33] But there's no F6, for example.

[00:03:35] And no F10.

[00:03:37] There are fields of size p (where p is prime) and size p^k.

[00:03:44] And these finite fields can't be embedded in this sequence,

[00:03:48] but they can be constructed either from Z or from polynomials with coefficients from Z.

[00:03:59] The details are complex.

[00:04:01] But it's a topic accessible to school students.

[00:04:05] And you don't need to know all these fancy words.

[00:04:08] To define multiplication and addition, you need to define addition and multiplication tables.

[00:04:15] Here, I have an example where I took numbers from 0 to 12 and defined addition for them.

[00:04:22] For example, 3 + 1. Look at the intersection, we see 4. That's the answer.

[00:04:28] 3 + 1 = 4

[00:04:30] Surprise!

[00:04:31] But here's something more interesting.

[00:04:32] For example, 7 + 6 = 0

[00:04:37] We don't need to go beyond these 13 objects, so the number 13 is simply not here.

[00:04:46] Or rather, it's not really a number; it's just a symbol for an object.

[00:04:50] 12 -> 11

[00:04:53] This table is really simple.

[00:04:55] We add the two initial numbers, treating them not just as symbols, but as numbers,

[00:05:01] but we record the result modulo 13.

[00:05:04] "By modulo" means - we take the remainder after dividing by 13.

[00:05:09] You probably already know all this.

[00:05:12] Here's the multiplication table, built using the same principle.

[00:05:16] This creates such edges, consisting of zeros, because 0 times any number is zero.

[00:05:20] And in the middle, we get this interesting table.

[00:05:25] The multiplication table of non-zero numbers modulo 13.

[00:05:29] I'm saying that this is quite a good, successful definition of addition and multiplication,

[00:05:36] because they satisfy laws.

[00:05:42] This law is called the "Associativity Law of Addition".

[00:05:46] That, when you add 3 objects, you can rearrange the parentheses.

[00:05:49] The commutative law. a + b = b + a

[00:05:52] The fact that we have a zero.

[00:05:55] And that for any number, you can find a number "b", where the sum with it is zero.

[00:06:02] And very similar laws for multiplication,

[00:06:06] which I denote with an asterisk.

[00:06:08] And there's also an interesting law that applies to both these laws. Both addition and multiplication.

[00:06:16] And for multiplication, it's written here that just like for addition, there's an inverse.

[00:06:24] But here we get 1, not 0.

[00:06:28] And also a ≠ 0. Inverse elements exist only for numbers not equal to zero.

[00:06:34] These are the laws. And when your addition and multiplication

[00:06:41] have these properties, you can say that you've got a number field.

[00:06:48] All of this might seem a bit dry...

[00:06:52] but you need to overcome this only once, and then it will get interesting.

[00:06:57] We've defined addition and multiplication, but we haven't defined subtraction.

[00:07:02] How do we do that?

[00:07:03] Very simply.

[00:07:04] Because here it's written that for any number "a", there's a "b" such that a + b = 0,

[00:07:10] let's say that b = -a.

[00:07:13] And subtraction "a - c" actually means that we're adding the additive inverse of c to a.

[00:07:23] And division?

[00:07:24] You've probably already guessed.

[00:07:26] a/c = a * c^-1

[00:07:31] -1 power means we're taking the multiplicative inverse.

[00:07:36] Alright.

[00:07:38] Next, for mental exercise, you can try to prove that -(-a) == a.

[00:07:46] Or that getting the additive inverse is very simple: you just need to multiply by -1.

[00:07:54] And -1 is the multiplicative inverse of 1.

[00:08:00] Similarly, you can prove this carefully.

[00:08:03] That when you take the additive inverse element of a product,

[00:08:07] you can take the additive inverse of one of these two factors.

[00:08:13] And many other familiar things can also be proven.

[00:08:16] For example, if you have an equality a*b1 == a*b2,

[00:08:20] you can cancel out "a" and get b1 = b2.

[00:08:25] Look how many steps you need to take here to prove it.

[00:08:30] With numbers, we're already used to these things,

[00:08:34] but here, when we're abstractly forming the concept of a number field, we need to prove it.

[00:08:42] Pause, look at the individual steps.

[00:08:46] What I want to emphasize here.

[00:08:48] Some simple things, which might be more intuitive and understandable.

[00:08:54] Look.

[00:08:55] We have a law that for every number "a", there's a multiplicative inverse "b".

[00:09:00] Let's take this multiplicative inverse and write this equation.

[00:09:04] Now let's multiply both sides by c.

[00:09:07] Next, we can move the parentheses here

[00:09:10] and get that for any element "c", there's a "d" such that "a * d == c".

[00:09:18] Alright...

[00:09:20] But how else can we interpret this?

[00:09:23] This can be interpreted as follows.

[00:09:26] In each row and column of the addition and multiplication tables, all numbers of our number field must appear.

[00:09:35] All the elements.

[00:09:37] So, let me try to formulate the property of a number field using the example of these addition and multiplication tables.

[00:09:44] First: these tables should be symmetric with respect to the diagonal.

[00:09:51] This is the commutativity law of addition and multiplication.

[00:09:56] Second: in each row and column of the addition and multiplication tables, all numbers must be present.

[00:10:07] This is essentially a consequence of the fact that there's an additive inverse for any number.

[00:10:13] And that for any "c" and any "a" not equal to zero, there exists a "d" such that a * d = c.

[00:10:21] This is what we just showed.

[00:10:23] The distributive law (this one here)

[00:10:27] is already challenging to demonstrate and explain using only these two tables.

[00:10:37] The fact that all numbers are present in each row of the multiplication table means,

[00:10:43] that there are no non-zero numbers "a" and "b" such that a * b = 0.

[00:10:49] Otherwise, there would be a zero somewhere in the multiplication table,

[00:10:53] and it would be impossible to place all possible values of the number field in this row.

[00:11:03] Okay. After going through all these pedantic discussions, we move on to interesting things.

[00:11:11] What interesting things?

[00:11:13] Interesting things are equations. You won't believe it! =)

[00:11:16] So, first: how to solve a linear equation?

[00:11:20] The answer is this: if you have a linear equation ax + b = 0,

[00:11:24] you need to take the additive inverse of "a", multiply it by "b",

[00:11:29] and then take the additive inverse of that number.

[00:11:35] Next, x^2 = a. Or taking the square root.

[00:11:39] Here we immediately encounter something very interesting.

[00:11:44] Let's live in these fields for now, fields which involve modular arithmetic.

[00:11:49] Modular arithmetic with respect to "p", where "p" is prime.

[00:11:53] Let's generate a thousand prime numbers and another ten thousand prime numbers,

[00:12:00] and see what squares modulo "p" can be.

[00:12:06] And we see that when we take all possible numbers from 0 to 12, square them,

[00:12:13] we don't get all possible numbers.

[00:12:15] And that's not surprising.

[00:12:17] If we take 2 and -2, the additive inverse of 2 exists,

[00:12:22] square them, we get 4.

[00:12:27] Thus, in these squares, each number is gotten  twice.

[00:12:32] And here, only half of the numbers from 1 to p - 1 are present.

[00:12:39] Here's 3. This means that x^2 = 3 has a solution.

[00:12:44] But there's no number 11. This means that x^2 = 11 has no solution.

[00:12:50] So you can't extract the square root of 11.

[00:12:54] Alright.

[00:12:56] Here we have the function DeleteDuplicates, and we see the unique elements, of which there are (p - 1)/2.

[00:13:03] Only half of the numbers from 1 to p are squares.

[00:13:11] And these numbers are called quadratic residues.

[00:13:15] And all others, except zero, are called quadratic non-residues.

[00:13:19] Let's calculate for each prime number p,

[00:13:25] whether -1, which is the same as p - 1, is a quadratic residue.

[00:13:34] So, 1 – when the prime number p, shown on the X-axis, has -1 as a quadratic residue,

[00:13:45] and -1 – if -1 is a quadratic non-residue.

[00:13:51] Some prime numbers yield 1, some yield -1.

[00:13:55] For example, modulo 5, -1 is a quadratic residue,

[00:14:01] while modulo 7, -1 is a quadratic non-residue.

[00:14:06] Modulo 11 – again a non-residue.

[00:14:08] Modulo 13 – a residue.

[00:14:11] Let's define the function HasSqrt as follows:

[00:14:19] q is a quadratic residue modulo p.

[00:14:25] This function, HasSqrt, is actually called the Legendre symbol,

[00:14:32] but in Mathematica, this function is called the JacobiSymbol.

[00:14:37] And it works not only for prime p. I'll explain that later.

[00:14:42] By the way, first, we can again use my favorite Accumulate...

[00:14:50] and see how prime numbers balance between those for which -1 is a quadratic residue

[00:14:58] and those for which it's not.

[00:15:02] Balancing in some way...

[00:15:04] Here we took a certain number of prime numbers up to 8000.

[00:15:10] And the balance here reached -15, but now it's back to -5.

[00:15:16] We can take more...

[00:15:20] Though calculating this will take quite a while.

[00:15:22] Here it's more appropriate to use, of course, the JacobiSymbol function.

[00:15:27] Let me do that.

[00:15:30] JacobiSymbol[-1, p]

[00:15:36] This is computed instantly.

[00:15:39] And here you can calculate it for very large numbers.

[00:15:43] I'll make a separate video about this balance between two kinds of prime numbers.

[00:15:51] Now, let's think about something else.

[00:15:54] What about cubes?

[00:15:55] I took cubes of all numbers from 1 to 12 and got only 4 numbers.

[00:16:02] So, all other numbers are not cubes.

[00:16:06] And if we write the equation x^3 == 11 modulo 13,

[00:16:14] we have an empty set of solutions.

[00:16:17] And if we write 8, how many solutions will there be?

[00:16:26] Here it gives solutions from real numbers or complex numbers.

[00:16:34] And in this way, it provides a solution from the number field F13.

[00:16:42] Alright... Let's take 17.

[00:16:44] Here we have all the numbers.

[00:16:47] Meaning, by cubing all numbers modulo 17, we get all the numbers again.

[00:16:54] And modulo 19?

[00:16:56] And modulo 23?

[00:16:59] Here we notice a pattern that the number of numbers,

[00:17:05] either all or (p - 1)/3,

[00:17:11] all of this depends on whether p - 1 is divisible by 3 or not.

[00:17:14] If p - 1 is divisible by 3, then you need to divide it by 3 and get the answer.

[00:17:19] That's how many cubes there will be.

[00:17:22] And if it's not divisible, then the cubes cover all numbers.

[00:17:27] Interesting observation.

[00:17:29] Moving on.

[00:17:31] Let's build a table of powers modulo p.

[00:17:36] Each row here represents a power.

[00:17:39] Here's 1^1, 1^2, 1^3, 1^4, and so on.

[00:17:44] And these are powers of two. 1, 2, 4, 8... At first, everything goes as expected.

[00:17:49] Then it should be 16, but 16 modulo 13 is 3. And so on.

[00:17:55] An immediate discovery:

[00:17:58] Row #12 contains all ones.

[00:18:02] Is this a coincidence or not?

[00:18:04] Let's take 19.

[00:18:06] No, it seems, this is not a coincidence.

[00:18:09] This is called Fermat's Little Theorem.

[00:18:11] Any number to the power of p - 1 modulo p equals 1. Except 0.

[00:18:19] Here I added a column with the number k for convenience.

[00:18:24] Meaning...

[00:18:26] in this row are the numbers "a",

[00:18:30] in this row are the numbers "k",

[00:18:33] and in the middle is the number "a^k".

[00:18:38] What do we see for 13?

[00:18:40] Here, in the third row (these are the cubes), we have only the numbers 1, 8, 12, and 5.

[00:18:48] And each number appears 3 times.

[00:18:50] And indeed, when we ask for Solve modulo 13, we get three answers.

[00:18:58] And modulo 19?

[00:19:03] And modulo 17 – one.

[00:19:08] Alright... Moving on.

[00:19:11] Here's the mentioned Fermat's Little Theorem.

[00:19:14] That the row p - 1 contains all ones.

[00:19:18] And the row numbered "p" will again contain 1, 2, 3, 4, 5, and so on up to 12.

[00:19:25] Meaning x^p will be equal to "x".

[00:19:29] And this equality is true for all numbers. Not just for 1, 2, 3, 4... 12, but also for 0.

[00:19:35] In a sense, it's a special equation,

[00:19:39] whose roots are all the elements of the number field.

[00:19:45] Alright.

[00:19:46] Next, we notice the following.

[00:19:48] Here we observe either 1 or -1. 12 is -1.

[00:19:54] And, furthermore, even clear for whom this expression is equal to 1.

[00:20:01] If the number "a" itself, which is here, is a square of some other number "b",

[00:20:07] for example, 4 is 2^2,

[00:20:12] then we will have (b^2)^6 drawn here,

[00:20:16] meaning b^12 is drawn here.

[00:20:19] And any number raised to the 12th power gives 1, so there's a 1 here.

[00:20:24] So, for numbers that are squares (quadratic residues), there will definitely be ones here.

[00:20:32] This is just our observation. An interesting observation.

[00:20:36] So, here... LegendreSymbol, which is denoted like this.

[00:20:44] It can actually be explicitly written as n^((p-1)/2).

[00:20:51] But we should use not 1 and 12, but 1 and -1.

[00:20:55] Alright.

[00:20:58] The next interesting observation.

[00:21:01] The Legendre Symbol is a multiplicative function.

[00:21:06] This immediately follows from this expression.

[00:21:09] Look.

[00:21:11] m^((p-1)/2)

[00:21:13] And this expression is n^((p-1)/2).

[00:21:17] So their product is (m*n)^((p-1)/2).

[00:21:23] Yes... just in case... I should explicitly mention this.

[00:21:27] We haven't proven this formula.

[00:21:30] We discovered it for some "p", but nothing more.

[00:21:34] We also haven't proven Fermat's Little Theorem.

[00:21:37] That these are all ones here.

[00:21:40] But there's nothing wrong with that.

[00:21:43] Let it be homework – to prove these two statements.

[00:21:48] But what I want to say...

[00:21:50] I sometimes start treating experimentally discovered facts for some number of "n" as truth.

[00:21:59] I postpone it for later.

[00:22:00] Maybe, at some point, I'll manage to prove or disprove these discovered facts,

[00:22:04] but there's nothing wrong with considering discovered facts as truth for a while.

[00:22:12] Legendre Symbol, for example. There was a very interesting story behind it.

[00:22:17] Pafnuty Chebyshev, whose polynomials I recently talked about, long ago discovered

[00:22:24] that if we consider the Legendre Symbol for -1,

[00:22:29] that is, consider prime numbers for which √ -1 is extracted,

[00:22:33] and prime numbers for which √ -1 is not extracted,

[00:22:38] then we'll find a certain imbalance between the two classes of prime numbers.

[00:22:43] Prime numbers for which √ -1 is not extracted are slightly more,

[00:22:49] if we take prime numbers < n.

[00:22:52] For small n, and even for fairly large n.

[00:22:56] Let me explain.

[00:22:59] Let's consider the Legendre Symbol for -1.

[00:23:08] So...

[00:23:09] Let's call the team1 prime numbers < n,

[00:23:14] for which this equation holds,

[00:23:16] and team2 prime numbers,

[00:23:19] for which this equation holds.

[00:23:21] Even then, in Chebyshev's time, this theorem was already known,

[00:23:27] called the "Prime Number Theorem of Arithmetic Progressions".

[00:23:38] But Chebyshev noticed that very often, for most n, team2 dominates.

[00:23:47] And then, in 1962, these two mathematicians, Knappowski and Turán, conjectured

[00:23:56] that this inequality is almost always true.

[00:24:00] This means that when you have X and you take any n <= X,

[00:24:09] then the ratio of the fraction of n where team2 wins over team1,

[00:24:18] tends to 100% as X approaches infinity.

[00:24:27] A complex statement, as it involves using two large numbers, X and n,

[00:24:37] and considering the proportion of choices where n < X.

[00:24:43] But then Littlewood came and relatively recently, in 1995 or 1994, proved,

[00:24:51] proved that no...

[00:24:55] This fraction of cases where team2 wins

[00:25:00] actually doesn't have a limit as it approaches infinity,

[00:25:06] but he was able to prove that there's a certain cunning measure,

[00:25:10] namely, 1/n,

[00:25:13] that, in this measure, the size of this team2 is still larger,

[00:25:17] and it's around 0.996... something like that.

[00:25:20] A very complex statement.

[00:25:22] Anyway, despite these two gentlemen making an incorrect assumption,

[00:25:28] their reputation remained unaffected.

[00:25:31] Their karma wasn't diminished at all.

[00:25:34] On the contrary, it's interesting to make assumptions and then either prove or disprove them.

[00:25:41] And a bit more about x^m.

[00:25:49] Let p - 1 be divisible by m,

[00:25:52] then we can show that x^m cannot cover all numbers.

[00:25:58] And this would mean that "x^m = a" will have no solutions for some values of "a".

[00:26:07] See how this is proved.

[00:26:10] It's proven by contradiction.

[00:26:12] Let x^m cover all numbers from 1 to p - 1.

[00:26:17] Then we can raise "x^m" to the power of "n" and get that

[00:26:26] the entire expression should be equal to 1.

[00:26:30] If x^m covers all numbers from 1 to p - 1,

[00:26:35] then the equation y^n = 1 must have p - 1 roots.

[00:26:45] Indeed, we substitute "y" with "x^m",

[00:26:50] "x" ranges from 1 to p - 1,

[00:26:52] and we get here, as we assumed, the same numbers: 1, 2, 3, ..., p - 1.

[00:26:59] They are just rearranged amongst each other when raised to the power of m.

[00:27:05] But the polynomial y^n - 1 cannot have more than "n" distinct roots.

[00:27:13] This is true for real numbers, for complex numbers.

[00:27:17] This is true for any field of numbers.

[00:27:20] Including finite fields.

[00:27:22] Think about why. Try to convince yourself of that.

[00:27:26] And there's another true statement in the opposite direction.

[00:27:30] Let p - 1 not be divisible by "m".

[00:27:33] Moreover, let p - 1 be coprime with the number "m".

[00:27:39] From this, it immediately follows that x^m covers all numbers from 1 to p - 1.

[00:27:45] How is this proved?

[00:27:47] Look.

[00:27:49] If "m" and p - 1 are coprime,

[00:27:54] then we can find such an "n"

[00:27:57] that n * n has a remainder of 1 when divided by p - 1.

[00:28:03] Next, we consider this power.

[00:28:06] Then we recall that m * n has a remainder of 1.

[00:28:10] What does that mean?

[00:28:12] This means that m * n can be represented in this form.

[00:28:18] But x^(p-1),

[00:28:21] if we take only this part of the power,

[00:28:25] gives us 1,

[00:28:27] so we can drop this part from the power

[00:28:31] and we get x^1.

[00:28:33] So x^(m*n) = x^1 modulo p.

[00:28:42] x^m cannot cover not all numbers.

[00:28:49] If not all numbers are encountered in this bracket,

[00:28:52] then we sort of lose information about x,

[00:28:56] and we can't recover it when raised to the power of n.

[00:29:00] Here, it turns out that (x^m)^n is exactly equal to x, thus retaining all information about x.

[00:29:12] So, the promised homework.

[00:29:15] Let's better write the homework in Russian.

[00:29:21] Find a proof for Fermat's Little Theorem.

[00:29:25] That x^(p-1) is congruent to 1 modulo p.

[00:29:31] One of the proofs is based on the following:

[00:29:34] take the a-th row of the multiplication table

[00:29:38] and multiply all the numbers present there.

[00:29:41] On one hand, this product is all the numbers from 1 to p - 1,

[00:29:46] on the other hand, it's equal to this product.

[00:29:52] And then you can work with this expression to prove Fermat's Little Theorem.

[00:29:59] And the next thing about the Legendre symbol.

[00:30:05] Prove that from these three statements,

[00:30:08] this decomposition of the polynomial x^(p-1) - 1,

[00:30:13] from Fermat's Little Theorem

[00:30:15] and the fact that a polynomial with k distinct roots can have degree k or greater,

[00:30:22] the formula for the Legendre symbol follows (from these three statements).

[00:30:28] That's all for today! Good luck to everyone! Goodbye!
