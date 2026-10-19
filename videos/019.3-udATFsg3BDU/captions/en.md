# 19. Часть 3. Расширения конечных полей. Число неприводимых многочленов (English subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [udATFsg3BDU](https://www.youtube.com/watch?v=udATFsg3BDU). Получено: 2026-10-08T17:42:08+01:00.

[00:00:00] "Mathematical Experiments" Channel.

[00:00:03] It's time to talk about the quadratic extension of a field.

[00:00:07] Of course, it's helpful here to have an analogy with complex numbers.

[00:00:12] We had real numbers, and then we added √-1.

[00:00:17] Suddenly, we had a plane instead of a line.

[00:00:22] Similarly, we'd like to do something here, but now with residue fields modulo p.

[00:00:29] In Mathematica, √-1 is represented by the symbol i.

[00:00:35] And how it works: it's an unusual symbol, the square of which is -1.

[00:00:42] So, when you have an expression where i^2 should be present,

[00:00:49] in that expression, i^2 disappears because it's replaced with -1.

[00:00:56] In other words, we multiply two expressions like polynomials and then make a substitution in this polynomial.

[00:01:05] In Mathematica, this is directly called a "Replacement Rule".

[00:01:10] And we get exactly the same expression we'd have with i, but with x.

[00:01:17] It's as if we fixed this ratio for x^2

[00:01:23] and turned polynomials in x into complex numbers.

[00:01:29] A miracle!

[00:01:31] Let's try the same for the field F5, for example.

[00:01:36] How is this done?

[00:01:37] We consider numbers of the form a + bi,

[00:01:42] where i is √-1.

[00:01:45] And we treat the coefficients "a" and "b" as residues modulo 5.

[00:01:51] In Mathematica, this is done using the function PolynomialMod.

[00:01:55] And here, we simply get i.

[00:01:59] Why? Because modulo 5, 5 is equal to 0.

[00:02:03] So, this first part "5 +" here disappears.

[00:02:09] The same thing could be achieved if we just wrote

[00:02:15] this sort of thing here.

[00:02:17] PolynomialMod takes a list of expressions as the second argument, which are equal to zero.

[00:02:25] A miracle!

[00:02:27] Here, we could even take a polynomial in x and y.

[00:02:30] And then write some polynomials in x and y here.

[00:02:35] So...

[00:02:37] Okay...

[00:02:39] Let's check if our multiplication works as it should

[00:02:43] in our polynomial arithmetic, where we make the substitution x^2 → -1.

[00:02:50] Let's define all the polynomials of the form a + bi.

[00:02:55] Here they are. There are 25 of them.

[00:03:00] Let's multiply each of these polynomials (25 of them)

[00:03:03] by this specific polynomial.

[00:03:06] It's like looking at one row of the multiplication table.

[00:03:10] Multiplying one element by all the others.

[00:03:17] Uh-oh!

[00:03:18] We had 25 elements,

[00:03:20] but after multiplying by this, we got 5.

[00:03:24] That means in the multiplication table of this element, not all 25 field elements are present.

[00:03:33] So, it's not a field.

[00:03:36] Not all 25 elements are present, meaning what we constructed is not a field,

[00:03:41] but a ring.

[00:03:43] "Ring" is a set of elements with multiplication and addition. A commutative ring has all the same properties as a field, except that not every element has a multiplicative inverse (addition is fine). This, in particular, means that there can be rows in the multiplication table where not all field elements are present and that there can be two elements whose product is zero (these are called zero divisors).

[00:03:51] So, what's the problem here?

[00:03:53] The problem is that the root √-1 is present in arithmetic modulo 5.

[00:04:00] x^2 = -1 has solutions. Specifically: 2 and 3.

[00:04:05] Let me try to show this explicitly...

[00:04:16] 0

[00:04:17] The product of these two numbers from our ring is 0.

[00:04:24] In such cases, it's said that the ring is non-integral. It has zero divisors.

[00:04:33] But for example, modulo 7, everything would work fine for these two elements.

[00:04:41] Let's check for the field F7.

[00:04:44] Generate 49 elements

[00:04:49] and see how many elements we get in the row 1 + 2i.

[00:04:57] 49 of them.

[00:04:58] All is well.

[00:05:01] Now we've come to the point where we can construct the field F7^2 from the field F7.

[00:05:08] For the field F7, the idea of adding √-1 works.

[00:05:14] But what works for the field F5?

[00:05:17] There, we need to take a factorization (it's called factorization) not by the polynomial x^2 + 1,

[00:05:25] like we did here,

[00:05:27] but by the polynomial x^2 + 2.

[00:05:31] Because -2 is no longer a quadratic residue in the field F5.

[00:05:38] I'm trying already to say these smart algebraic words.

[00:05:44] Maybe it's still too early...

[00:05:46] Well, okay... get used to it.

[00:05:49] Here we've constructed all 25 elements of our assumed field F5^2.

[00:05:58] We're checking that this specific row in the multiplication table contains all 25 elements.

[00:06:05] Here we can try various elements and always get 25.

[00:06:13] Let's check this globally

[00:06:16] for p = 5.

[00:06:19] Checking...

[00:06:21] See?

[00:06:22] Here we're checking all possible rows in the multiplication table.

[00:06:27] Including the row where multiplication by 0 happens, and there's a unique result.

[00:06:32] All other rows have 25 unique elements.

[00:06:38] Let's look at the field F7.

[00:06:42] The quadratic extension of the field F7 using the polynomial x^2 + 1.

[00:06:51] And we find that its multiplication table is normal,

[00:06:56] meaning it's actually a field of 49 elements.

[00:07:02] Among these 49 elements, there's also 1.

[00:07:08] This is important.

[00:07:10] Since all 49 elements are present, 1 is also there.

[00:07:14] If it weren't, there would be 48 or fewer.

[00:07:19] This means that, for example, for our element 2 + 3x, there's a some polynomial from here

[00:07:27] that yields 1.

[00:07:29] We can explicitly find it using the "Select" function.

[00:07:34] It's 5 + 3x.

[00:07:36] Indeed. We multiply 2 + 3x by 5 + 3x.

[00:07:40] What do we get?

[00:07:43] This.

[00:07:45] Here, we should make a substitution. Turn x^2 into -1.

[00:07:51] This means that x^2 + 1 equals 0.

[00:07:54] We want to live in a world where x^2 + 1 = 0.

[00:07:58] And here's what we get.

[00:08:00] Then we remember that 7 also equals 0, so 21 here also equals 0.

[00:08:05] Because 21 is 7 + 7 + 7.

[00:08:10] So, we've checked that the multiplication table contains all elements in each row.

[00:08:16] But that's not all the properties of a field. There's also commutativity in multiplication, addition, etc.

[00:08:21] All the other properties of a field...

[00:08:25] these ones

[00:08:27] ...follow from the fact that they hold for polynomials.

[00:08:31] All these properties are present in polynomials.

[00:08:34] So, our polynomials (taken modulo something) also inherit these properties.

[00:08:44] Thus, we've already proven, through numerical verification,

[00:08:51] that polynomials over F5 modulo x^2 + 2

[00:08:58] and polynomials over the field F7 modulo x^2 + 1

[00:09:04] give us fields of size 25 and 49.

[00:09:09] What correct words are spoken here...

[00:09:12] We take the factor of the ring of polynomials F5[x]

[00:09:18] by the ideal generated by the polynomial x^2 + 2.

[00:09:24] An ideal is the set of all polynomials that are divisible by x^2 + 2.

[00:09:30] Let's put it this way... it's not quite exact.

[00:09:35] Moving on to the next point.

[00:09:37] Now we want to get fields of size 5^3, 7^3 and so on.

[00:09:42] How is this done...

[00:09:45] With the polynomial x^2 + 1 in the field F5, we couldn't achieve anything,

[00:09:51] because it factors

[00:09:54] and as a result, we get two elements whose product is zero,

[00:09:59] and we end up with a problematic multiplication table.

[00:10:02] And from here, we immediately sense the idea.

[00:10:06] We need to find a cubic polynomial that doesn't factor.

[00:10:12] x^2 + 1 factors.

[00:10:15] We need a cubic polynomial that doesn't factor.

[00:10:20] Well, I used the Solve function here to find some polynomial that doesn't factor.

[00:10:30] This is not always true. Some polynomials do factor.

[00:10:34] For example, this polynomial factors into 3 terms: (x - 1)(x - 2)(x - 2).

[00:10:41] But this one doesn't factor.

[00:10:45] By the way, Solve doesn't talk about factorization, it talks about the absence of roots.

[00:10:49] These are slightly different things, but that's enough for our purpose here.

[00:10:57] Alright... Let's move on.

[00:11:00] Now let's consider all second-degree polynomials of the form a + bx + cx^2.

[00:11:10] There will be 125 of them.

[00:11:15] And we want to factor them using this polynomial.

[00:11:20] In other words, we want to replace "x^3" with "minus this expression".

[00:11:25] We want to replace x^3 with - (x + 1).

[00:11:30] With this substitution, we can immediately turn x^4

[00:11:35] into this expression.

[00:11:38] Already a second-degree.

[00:11:40] So, for higher degrees (x^3 and above),

[00:11:44] using this substitution, we can reduce the degree down to the second degree.

[00:11:50] That's why I immediately generate only second-degree polynomials.

[00:11:54] It doesn't make sense to go further because we have this substitution.

[00:11:58] Okay.

[00:11:59] Here, I'm checking a specific row of our new arithmetic,

[00:12:04] where we consider this polynomial equal to zero.

[00:12:09] Alright... Lucky shot!

[00:12:12] And this?

[00:12:14] Well...

[00:12:16] Here, I could do the same thing and check all rows of the multiplication table

[00:12:19] (all 125 rows of the multiplication table) and get the same result.

[00:12:25] In all rows of the multiplication table, I get 125 unique elements.

[00:12:30] Including 1.

[00:12:34] If we took not this polynomial,

[00:12:36] but this one, we'd encounter a problem.

[00:12:41] Let's observe this problem.

[00:12:44] Here, I encountered a problem with the polynomial 1 + x^2.

[00:12:49] For the polynomial 2 + x^2, everything is bad.

[00:12:53] By the way, it's just one of the zero divisors in this field.

[00:13:00] And for this one, I also get 25.

[00:13:04] Less than 125.

[00:13:07] In short, we have two zero divisors that we can immediately see,

[00:13:14] as well as other elements

[00:13:17] for which the multiplication table row is disrupted.

[00:13:22] I'm explaining this here.

[00:13:24] (x^2 + 2) when multiplied by 0 gives 0, of course.

[00:13:31] And also (x^2 + 2) when multiplied by (x - 2) gives 0

[00:13:37] simply because we consider this expression as zero in this ring.

[00:13:42] So if we take any polynomial pp,

[00:13:46] as well as the polynomial (x - 2 + pp),

[00:13:49] we get two elements,

[00:13:51] such, that in the multiplication table (x^2 + 2)

[00:13:56] multiplied by this polynomial

[00:13:57] and (x^2 + 2) multiplied by this polynomial

[00:13:59] give the same result.

[00:14:02] This equality comes as the sum of these two equalities.

[00:14:06] In the multiplication table, where we take the modulus of the polynomial

[00:14:11] that's the product of three monomials, there will also be issues.

[00:14:19] Not always, but sometimes.

[00:14:24] So, look at what happened.

[00:14:27] We took polynomials modulo (x^3 + x + 1).

[00:14:32] Meanwhile, we were working in the arithmetic of F5.

[00:14:36] And we found that the multiplication table is good.

[00:14:44] So, from the equation a[x] * b1[x] = a[x] * b2[x],

[00:14:50] it immediately followed that b1 = b2.

[00:14:56] But how do we prove this rigorously?

[00:14:58] Let's try to do that.

[00:15:00] I don't do this often, but sometimes, perhaps, it's useful.

[00:15:04] Let's argue by contradiction.

[00:15:06] Suppose we have some polynomial.

[00:15:08] Irreducible. Which can't be factored into the product of two polynomials of degree greater than 0.

[00:15:18] And let's have this equation, where b1 and b2 are different polynomials.

[00:15:25] I'm immediately in the world of degree 2 polynomials,

[00:15:27] because I understand that we can make this substitution.

[00:15:33] I can derive from this equation

[00:15:36] that equation.

[00:15:38] Simply move to one side

[00:15:41] and take a[x] out of the bracket.

[00:15:44] And we end up with an equation of the next form:

[00:15:48] the product of two polynomials a[x] * (b1[x] - b2[x]) is zero modulo f[x].

[00:15:57] This means that this product is equivalent to some polynomial k[x] multiplied by f[x].

[00:16:08] The polynomial k[x] cannot be a simple number.

[00:16:13] Let k be a number.

[00:16:16] Then, let's bring 1/k inside a[x], for example.

[00:16:21] And then we have: the product of two polynomials equals f[x].

[00:16:28] If these are polynomials of degree greater than 0, we have a contradiction.

[00:16:32] It turns out f[x] is reducible.

[00:16:34] We initially assumed it couldn't be factored, but it has factored.

[00:16:40] And x can't be a number.

[00:16:42] And b1 - b2 can't be a number.

[00:16:45] Because then we have a second-degree polynomial here,

[00:16:49] and a third-degree polynomial here.

[00:16:52] So, both of them are polynomials

[00:16:58] where x or x^2 carries a non-zero coefficient.

[00:17:03] So, if k[x] is a number, we have a contradiction.

[00:17:08] Thus, k[x] is not a number.

[00:17:09] Thus, k[x] is a polynomial.

[00:17:12] Moreover, it's a first-degree polynomial.

[00:17:15] It can't be second degree,

[00:17:16] because then it's a fifth-degree polynomial and we get a contradiction.

[00:17:21] We can't multiply two second-degree polynomials to get a fifth-degree polynomial.

[00:17:26] So, k[x] is definitely a first-degree polynomial.

[00:17:33] Then we have the following thing...

[00:17:40] Let's do the following.

[00:17:42] Write a[x] as the polynomial k[x]

[00:17:47] multiplied by the polynomial ll[x] plus the number jj.

[00:17:53] And let's denote this difference as b12[x]

[00:17:57] and write it in this way.

[00:18:03] We divide these two polynomials by k[x] with remainder.

[00:18:08] Here's what I did.

[00:18:10] I wrote a[x] as something that's divisible by k[x]

[00:18:14] plus something that's not divisible by k[x].

[00:18:17] And this something that's not divisible by k[x] is a number. Just a number.

[00:18:23] An important concept. Look it up online if you don't understand it.

[00:18:27] Division of polynomials by each other with a remainder.

[00:18:32] By writing a[x] this way,

[00:18:35] and this thing,

[00:18:36] I have that this product

[00:18:42] consists of a part that's divisible by k[x]

[00:18:47] and a part that's not divisible by k[x].

[00:18:49] This is just a number.

[00:18:53] And this number must be equal to 0.

[00:19:00] In other words, either a[x] is proportional to k[x],

[00:19:07] or (b1 - b2) is proportional to k[x].

[00:19:12] Alright...

[00:19:16] For example, a[x].

[00:19:20] Then we have that k[x] * ll[x]

[00:19:26] (this expression here)

[00:19:29] multiplied by this thing

[00:19:34] is exactly equal to

[00:19:37] this thing here.

[00:19:39] Yes, I need to explain.

[00:19:41] If this was an equation modulo f,

[00:19:45] then here it's just an equation of polynomials.

[00:19:53] Sorry, I forgot to mention.

[00:19:56] In short, we have an equation of polynomials.

[00:20:00] And so, we can divide by the polynomial k[x] while preserving the equality.

[00:20:08] And once again, we arrive at a contradiction.

[00:20:11] f[x] once again turns out to factor into polynomial products.

[00:20:15] Here I'll reiterate, that irreducible means, that it has no roots, but the reverse isn't true:

[00:20:29] if there are no roots, it doesn't imply the polynomial is irreducible.

[00:20:34] This was true for a cubic polynomial,

[00:20:37] but, let's say, for a sixth-degree polynomial, this is not the case.

[00:20:40] And this is clearly demonstrated.

[00:20:41] We take the product of two irreducible polynomials.

[00:20:45] And we get a polynomial with no roots.

[00:20:51] Now, pay attention...

[00:20:53] We've already proven the following:

[00:20:57] that if we have an irreducible cubic polynomial,

[00:21:01] we get a field when considering polynomials modulo this irreducible polynomial.

[00:21:08] A similar reasoning can be repeated for polynomials of any other degree: 4, 5, etc.

[00:21:17] Thus, we've shown that we can get an extension of the field Fp.

[00:21:22] Creating fields of size p^k, where k is precisely the degree of the irreducible polynomial,

[00:21:30] over which we consider all polynomials with coefficients from the field Fp.

[00:21:35] But how can we prove that for any field Fp, there's always an irreducible polynomial of any degree k?

[00:21:44] A very good question!

[00:21:47] Let's think about cubic polynomials first.

[00:21:51] Here's how they look:

[00:21:53] (x^3 + ax^2 + cx + d)

[00:21:55] We'll consider monic polynomials.

[00:21:58] That is, polynomials where the coefficient of the highest power is one.

[00:22:04] The number of such polynomials is p^3.

[00:22:11] Moving on...

[00:22:13] Let's try to formulate the number of irreducible polynomials of different degrees.

[00:22:22] For example, the number of irreducible polynomials of degree 1 is simply all degree 1 polynomials.

[00:22:32] Polynomials of degree 2. Their count can also be calculated.

[00:22:38] Irreducible polynomials of degree 2 are written like this:

[00:22:42] ((x + b)^2) - a, where "a" must be quadratic non-residues, and all will be well.

[00:22:52] Indeed, such a polynomial won't have roots,

[00:22:55] since equating it to zero gives (x + b)^2 = a.

[00:23:00] And there's no value (x + b) that squares to "a".

[00:23:05] b can be any number. Any of the p numbers.

[00:23:10] So, here the factor p appears.

[00:23:12] And "a" can be any of (p - 1)/2 numbers.

[00:23:16] (p - 1)/2 numbers is the range for "a".

[00:23:21] So, Irreducibles of degree 2 amount to p(p-1)/2.

[00:23:27] Now, can we, knowing the number of all monic cubic polynomials,

[00:23:34] subtract from this set all the reducible ones

[00:23:39] and see if anything remains or not?

[00:23:44] That's the idea.

[00:23:46] Here's how we're going to crack it. Let's write down irreducible polynomials.

[00:23:56] Reducible polynomials, those that can be factored, degree 2 ones, are constructed like this:

[00:24:01] take polynomials with root a1.

[00:24:04] Take, as it were, (x - a1) and multiply it by (x - a2),

[00:24:08] where a1 and a2 are distinct.

[00:24:11] How many such polynomials?

[00:24:13] p(p-1)/2

[00:24:15] That's how many ways we can take two elements from the field Fp.

[00:24:19] So, I've listed the set of all polynomials

[00:24:22] which are got as a result of multiplying degree 1 polynomials

[00:24:25] with roots a1 and a2, where a1 and a2 are different roots.

[00:24:30] There are this many of them.

[00:24:32] Now let's consider polynomials of the form (x - a1)^2.

[00:24:37] That is, when root a1 and a2 are the same.

[00:24:40] There are p of them.

[00:24:42] Alright.

[00:24:44] Moving on.

[00:24:45] Let's consider degree 3 polynomials that factor.

[00:24:52] They factor into either three distinct roots (a1 * a2 * a3),

[00:24:58] or one root is repeated twice

[00:25:02] and another only once.

[00:25:04] Or one root is repeated three times.

[00:25:07] Or we take polynomials with a root "a" of degree 1

[00:25:13] and irreducible polynomials of degree 2.

[00:25:18] Let "b" denote an irreducible polynomial of degree 2.

[00:25:25] Recording the count.

[00:25:27] I have this many of them.

[00:25:30] How many of them do I have?

[00:25:31] For the first root, I choose in "p" ways.

[00:25:35] Leaving "p - 1" numbers and choosing the second root "a2".

[00:25:41] Here I choose the root "a1". I can do this in "p" ways.

[00:25:46] And this.

[00:25:47] To choose a polynomial "a", univariate, there are "p" ways.

[00:25:51] To choose a polynomial "b", bivariate, degree 2,

[00:25:56] that many ways.

[00:25:58] Look.

[00:26:00] Recording this.

[00:26:03] These equalities can be ignored.

[00:26:04] This is me jotting down the essence,

[00:26:06] and then the answer in quantities.

[00:26:10] How many irreducible polynomials of degree 2 will there be?

[00:26:15] Very simple.

[00:26:16] We need to subtract what I've got here from the total number of degree 2 polynomials, which is p^2.

[00:26:22] It all simply equals this identity.

[00:26:25] Now, degree 3 polynomials. Irreducibles.

[00:26:30] From all degree 3 polynomials (monic).

[00:26:40] All polynomials that are reducible, monic, of degree 3.

[00:26:45] Here's what the answer looks like.

[00:26:49] Alright! Moving on. It gets more complicated.

[00:26:54] We're considering reducible polynomials of degree 4.

[00:27:00] Either all 4 distinct roots,

[00:27:02] or one root repeated twice, and two other distinct roots.

[00:27:07] And so on...

[00:27:08] Look.

[00:27:09] I'm writing all of this in detail.

[00:27:11] Either I have two factors of the form (x - a1),

[00:27:16] the second factor (x - a2),

[00:27:18] and some irreducible polynomial of degree 2.

[00:27:24] Or this,

[00:27:26] or the product of two different irreducible polynomials of degree 2,

[00:27:31] or the same polynomial squared,

[00:27:35] or an irreducible polynomial of degree 1 multiplied by an irreducible polynomial of degree 3.

[00:27:41] By the letter "c," I denote all degree 3 polynomials that are irreducible.

[00:27:50] The answer:

[00:27:52] It turns out to be this sum.

[00:27:55] This corresponds to

[00:27:56] this set.

[00:27:58] This corresponds to

[00:27:59] this.

[00:28:00] And so on.

[00:28:03] This corresponds to

[00:28:04] this set.

[00:28:06] And we know how many irreducible polynomials of degree 2 there are in total.

[00:28:10] That many.

[00:28:12] We choose one of them

[00:28:14] in that many ways.

[00:28:16] And if the second one is different,

[00:28:18] it's chosen in that many ways.

[00:28:23] But it doesn't matter to us which one was chosen first.

[00:28:26] So there's a division by 2 here.

[00:28:28] Otherwise, we'd count b1 * b2 twice. First as b1 * b2, then as b2 * b1.

[00:28:37] Towards the end, this value.

[00:28:40] This is exactly

[00:28:41] this.

[00:28:43] Recording...

[00:28:45] and getting the answer.

[00:28:48] Listen... fascinating!

[00:28:49] Two simple terms here. In the denominator, 4.

[00:28:52] Here too.

[00:28:55] And here too.

[00:29:00] Some sort of answer is emerging.

[00:29:03] For five, the answer looks like this.

[00:29:06] But for six, everything breaks down.

[00:29:09] For six...

[00:29:11] I'll show you what happens for six.

[00:29:15] For six, we get 6 here,

[00:29:20] and 2 here.

[00:29:25] And we also get 3.

[00:29:29] And one more term +p/6. That's the answer for six.

[00:29:37] It's not so easy to watch and understand what's hidden here.

[00:29:43] A small note:

[00:29:45] this complex sum that I calculated,

[00:29:49] can actually be calculated in one go.

[00:29:52] Like this.

[00:29:53] All these terms are calculated in one go using this formula.

[00:29:58] This is called the number of combinations with repetitions.

[00:30:04] Indeed, what we want to do is from the set of roots, from all the numbers we have in Fp,

[00:30:13] choose 4 numbers to make them the roots of our polynomial.

[00:30:21] And when we construct the polynomial, we're allowed to take the same roots multiple times.

[00:30:28] This is called multiple roots.

[00:30:30] So here, we have nothing other than the number of selections with repetitions, for which there's a known formula.

[00:30:41] Specifically, here it's written for k = 4.

[00:30:45] In the numerator, we simply have k factors from p to p + k - 1,

[00:30:52] and in the denominator, k!.

[00:30:57] All this combination that I've written here,

[00:31:06] can actually be formally described like this:

[00:31:16] In the form of  multiplication of these four brackets,

[00:31:22] where by "a1" I mean the number of degree 1 polynomials,

[00:31:31] which are irreducible degree 1 polynomials. (Attention! Here a_i, b_i, ... have a new meaning)

[00:31:35] And "a2" is everything that can be constructed from degree 2 polynomials.

[00:31:40] (these ones)

[00:31:44] What degree 2 polynomial can be constructed from these (a1) polynomials.

[00:31:48] And "a3" is how many degree 3 polynomials can be constructed from these (a1) polynomials.

[00:31:53] ...and so on.

[00:31:56] And when it comes to, say, x^3, it comes this thing.

[00:32:02] "a3" is how many degree 3 polynomials can be constructed from degree 1 polynomials.

[00:32:12] Plus, how many polynomials of degree 3 can be constructed from one degree 1 polynomial and one degree 2 polynomial.

[00:32:21] And here, how many irreducible degree 3 polynomials there are.

[00:32:28] And this truly describes the set of all degree 3 polynomials.

[00:32:33] In other words, this expression,

[00:32:35] it's actually equal to p^3.

[00:32:40] And I'm writing down the equality.

[00:32:43] And from this equality, I get the answers.

[00:32:47] It immediately follows that

[00:32:48] this is equal to this, meaning a1 = p.

[00:32:54] Next, I know what a2 is equal to.

[00:32:58] This is the number of selections with repetitions from "a".

[00:33:01] I substitute a2 here and immediately

[00:33:06] from this and this, I get

[00:33:10] that b1 is equal to what it's equal to above,

[00:33:15] namely, to this.

[00:33:17] This is precisely b1.

[00:33:21] And so on.

[00:33:22] So, this equation is a good use to us.

[00:33:26] It's difficult to make a mistake while writing this polynomial.

[00:33:30] Then, you can ask Mathematica to solve it.

[00:33:34] How is this done?

[00:33:36] Essentially, we need to write this equation

[00:33:41] multiple times.

[00:33:43] Substitute "a2" with this here.

[00:33:46] Substitute "a3" with this here.

[00:33:49] What is b2?

[00:33:51] b2 is how many degree 4 polynomials can be constructed from b1 polynomials.

[00:34:05] This many.

[00:34:10] All these substitutions that I've written here,

[00:34:13] can be concisely expressed like this.

[00:34:16] Each letter signifies the number of irreducible polynomials.

[00:34:20] a1 is the number of irreducible degree 1 polynomials,

[00:34:24] and a2, a3, a4, ... are how many 2nd, 3rd, 4th, ... degree polynomials can be constructed from them.

[00:34:31] b1 is the number of irreducible degree 2 polynomials,

[00:34:38] and b2, b3, b4 are how many (reducible) 4th, 6th, 8th, ... degree polynomials can be constructed from them.

[00:34:49] Then I write down this equation for four x's.

[00:34:55] For no reason, as the saying goes.

[00:34:59] I just need to determine what eq0 is.

[00:35:12] I write like this, briefly.

[00:35:14] And here's what I get.

[00:35:18] a equals p.

[00:35:20] b equals this.

[00:35:22] c equals this.

[00:35:24] This is the number of irreducible polynomials of degrees 1, 2, 3, 4.

[00:35:34] We could write an equation, which you could jokingly rewrite,

[00:35:41] shift these subscripts to superscripts by drawing the powers.

[00:35:47] As if we have such equation:

[00:35:53] the sum of a geometric progression,

[00:35:55] the sum of a geometric progression, and so on.

[00:35:59] Equals the sum of a geometric progression.

[00:36:04] But here, you have to understand that a^2 – it's not exactly a^2.

[00:36:08] If a is p, then a^2 is p(p+1)/2.

[00:36:13] A bit tricky, but you can take it and write it as if it's a geometric progression.

[00:36:20] In jest. I haven't gone mad. It's just a fun thing to try,

[00:36:24] to try and write it as a sum of a geometric progression, and then take the reciprocals.

[00:36:31] But it doesn't result in any equality.

[00:36:35] If you write it like this, you'll get an incorrect equation.

[00:36:40] Not equal.

[00:36:44] But if, instead of the sum of a geometric progression on the right,

[00:36:48] you write this thing,

[00:36:50] you get a true statement.

[00:36:52] It's just some unexplainable magic.

[00:36:57] The answer is expressed through the Möbius function (μ).

[00:37:03] Here's what it looks like.

[00:37:07] p

[00:37:08] A familiar expression.

[00:37:12] Here's the broken thing for 6.

[00:37:15] By the way, I forgot to write down one more term, p.

[00:37:21] For 7, it's simple again.

[00:37:24] For 8, we see a 4.

[00:37:31] It's evident that the expression is simple for prime numbers.

[00:37:34] And for composite numbers, the expression is more complex.

[00:37:38] We've already covered the Möbius function together.

[00:37:41] It's either +1, -1, or 0.

[00:37:48] It's 0 for all numbers where a prime squared is present in the factorization.

[00:37:55] It's -1 for prime numbers.

[00:37:59] For the product of two different prime numbers, it's +1.

[00:38:03] For the product of three different prime numbers, it's -1 again.

[00:38:07] It's -1 for all numbers that are the product of an odd number of distinct prime numbers.

[00:38:17] This is how the factors are arranged in this factorization.

[00:38:25] The summation occurs not over all numbers from 1 to 14,

[00:38:30] but over the divisors of the number k.

[00:38:33] In this case, it's 7, 2, and 1.

[00:38:39] By the way...

[00:38:42] You understand, this is the number of objects,

[00:38:46] meaning these are all integers.

[00:38:49] In particular, this expression is an integer.

[00:38:51] And it's an integer for any p.

[00:38:55] A bit of a marvel.

[00:38:57] And of course, it's positive.

[00:38:59] How to prove it's positive?

[00:39:02] Very simply.

[00:39:03] This expression here is certainly greater

[00:39:08] than p^15 minus this thing.

[00:39:11] All powers from 1 to 14.

[00:39:14] Well, this thing is less than p^15 for any p,

[00:39:20] because this sum up to p^14

[00:39:25] is gotten from subtracting one from this number and dividing by something.

[00:39:31] Hence, the number of irreducible polynomials is greater than zero for any k.

[00:39:40] So... let's reconsider this magical equation.

[00:39:47] I tried moving the subscripts to the superscripts above, but it didn't work out.

[00:39:54] It did, but I had to hack the right-hand side.

[00:39:57] So, let's try to understand the meaning of this bracket here.

[00:40:02] When a1 equals a.

[00:40:03] a2 equals a(a+1)/2.

[00:40:07] a3 equals this value.

[00:40:09] What kind of product is this?

[00:40:12] Answer:

[00:40:16] We actually need to do the following.

[00:40:20] We need to take...

[00:40:24] We need to take this thing and raise it to the power of 2.

[00:40:34] Then this expression will be equal to

[00:40:41] this expression with these values of a.

[00:40:49] Now I'm writing the actual correct equation,

[00:40:54] where a is the number of irreducible polynomials of degree 1,

[00:40:59] b is of degree 2,

[00:41:01] c is of degree 3, d is of degree 4, and so on.

[00:41:07] And all of this

[00:41:11] equals the generating function describing the number of all polynomials of degree k.

[00:41:19] We verify this for what we've already calculated

[00:41:25] and confirm the truth of the result.

[00:41:29] Here, in each bracket, we can take the inverse element

[00:41:34] and get this equation.

[00:41:37] Next, we can take the logarithm with respect to x

[00:41:40] and get the following equation.

[00:41:44] Next, I need to replace a, b, c, d with these things.

[00:41:55] And then I write:

[00:41:59] for x^k we have p^k,

[00:42:03] and this p^k should result if we collect the coefficients of x^k from all these expressions.

[00:42:15] And what do we get?

[00:42:19] We have a[d] * d here.

[00:42:23] The sum of a[d] * d is what adds up to p^k.

[00:42:30] But we need to take d as all those d's that divide k.

[00:42:38] The Möbius function is beautiful in that, having the function p^k as a sum,

[00:42:46] we can draw the sum from these values and return to the original values.

[00:42:53] So these terms a[k]

[00:42:57] can be got from these sums.

[00:43:02] This is a universal law that I recommend you read about.

[00:43:06] About the Möbius function and how it can reverse summation.

[00:43:14] From function f, which is a sum of function g, you can again get function g.

[00:43:21] Similar formulas were already covered in one of the previous videos about the Möbius function.

[00:43:28] Next important result.

[00:43:31] We need to prove that there are no fields other than fields of size p^k.

[00:43:36] How is this done?

[00:43:39] Let's introduce the concept of characteristic.

[00:43:41] The characteristic of field F is how many ones you need to add to get 0.

[00:43:47] First of all, why can we get 0 by adding ones?

[00:43:50] The answer is simple.

[00:43:52] Our field F is finite.

[00:43:53] That's our initial assumption.

[00:43:55] Therefore, when adding ones, repetitions will eventually occur.

[00:44:00] For example, the sum of 5 ones will turn out to be the same as the sum of 18 ones.

[00:44:07] Let's subtract 5 ones from these two sums.

[00:44:10] We get: 0 equals the sum of 13 ones.

[00:44:15] You understand?

[00:44:16] So, if there are repetitions, there are repetitions of 0 as well.

[00:44:21] And we can introduce this notation for field F.

[00:44:24] mF is actually m times the repeated one.

[00:44:34] Therefore, when we take m as the characteristic of field F,

[00:44:40] then we get exactly 0.

[00:44:43] Interestingly, this immediately implies that the sum of any (char(F)) numbers will be zero.

[00:44:52] Why?

[00:44:53] Because the law of distributivity holds true.

[00:44:56] This sum is 1*a + 1*a + 1*a, and so on.

[00:45:02] We take "a" outside the bracket,

[00:45:03] leaving here a sum of some number of ones.

[00:45:08] If there are exactly (char(F)) of them, then it's 0.

[00:45:11] Alright.

[00:45:14] As for our fields constructed on polynomials,

[00:45:17] their char is p, because this is just a special case of the field Fp.

[00:45:26] And in general, the characteristic must be prime.

[00:45:30] Because if it's not

[00:45:32] (let char(F) = c and this equals m * n),

[00:45:36] then we can take the product of two sums of ones.

[00:45:40] In the first sum, let's have m ones,

[00:45:44] and in the second sum, exactly n ones.

[00:45:47] Then by the rules of distributivity, all of this will eventually simplify to n times m ones.

[00:45:56] In other words, it will be 0.

[00:45:58] This can mean only one thing.

[00:46:00] One of these brackets must be equal to zero.

[00:46:03] In a field, there should be no zero divisors.

[00:46:06] So our assumption is incorrect.

[00:46:08] If they are equal to zero, then we have a contradiction.

[00:46:11] We took the minimum "c" for which the sum of c ones equals zero.

[00:46:17] And we ended up with the sum of m ones also equaling zero,

[00:46:20] or the sum of n ones equaling zero.

[00:46:22] In general, some smaller number of ones.

[00:46:26] Next. The next observation.

[00:46:28] char(F) is a prime number.

[00:46:31] And it's clear that numbers of this kind generate a field.

[00:46:36] A subset in our field F, which is also a field.

[00:46:40] Let's call this field mF.

[00:46:42] In fact, it's isomorphic to the field Fp.

[00:46:45] Definition: two finite number fields are ISOMORPHIC if the elements of the first field can be ordered and denoted as elements of the second in such a way that the multiplication and addition tables of the two fields coincide.

[00:46:52] You can understand this with a little contemplation.

[00:46:56] We can further notice that what we have here is a linear space over the field Fp.

[00:47:05] Let's take numbers of this kind:

[00:47:08] a * 1, where a is from the field Fp.

[00:47:13] Let's find a number that we can't represent in this way – β1.

[00:47:20] And let's consider numbers that are gotten when we consider these formal sums.

[00:47:26] We won't multiply these formal sums.

[00:47:28] We'll just describe everything that can be got in this way.

[00:47:33] Where a1 ranges over the field mF again.

[00:47:38] Such numbers will be p^2 in total.

[00:47:43] Let's see if there's any number left that we haven't covered with these combinations.

[00:47:50] If there is, let's call it β2.

[00:47:53] And so on.

[00:47:55] Let's continue this process, introducing new numbers β3, β4, and so on.

[00:48:03] In the end, this process will stop, and our whole field F will be described by these expressions.

[00:48:12] Clearly, the number of these expressions is p^k.

[00:48:16] But why are there no repetitions among them?

[00:48:19] Let's suppose otherwise. Let's suppose there are numbers that are actually the same.

[00:48:25] Let's equate them as expressions and subtract one from the other.

[00:48:29] One will have coefficients aᵢ, the other cᵢ.

[00:48:34] When we subtract one from the other, we'll have aᵢ - cᵢ coefficients.

[00:48:40] We'll have an expression with some non-zero coefficients that equals zero.

[00:48:48] Let's look at the highest term in this expression,

[00:48:50] move it to the right, and we'll get the following thing.

[00:48:54] Some β large is expressed as a linear combination of some β small,

[00:49:00] which contradicts the construction.

[00:49:02] We were looking for the new highest β as numbers that cannot be represented by a linear combination of the lower ones.

[00:49:09] This way, it is proven that any field F is actually a linear space over the field Fp.

[00:49:19] And the number of elements in it is p^k.

[00:49:22] So, today we've covered a lot.

[00:49:25] First, we understood how to construct finite fields of size p, where p is prime.

[00:49:31] We built a quadratic extension of the field Fp.

[00:49:34] For this, you need to add a root of some number a, where a is a quadratic non-residue.

[00:49:39] The same can be expressed using the Legendre symbol.

[00:49:45] The field Fp^k is constructed as a field of polynomials modulo some irreducible polynomial of degree k.

[00:49:57] It exists. We've proven it.

[00:50:00] We've proven this for all numbers.

[00:50:04] Furthermore, we understood that these fields of size p^k...

[00:50:11] (any fields, not just those constructed via polynomial rings modulo)

[00:50:15] ...сan actually be interpreted as linear spaces.

[00:50:20] Or, as they say: linear spans spanned by β0, β1, ... βk-1.

[00:50:29] The subfield Fp is simply a field gotten by summing ones.

[00:50:35] It's closed under addition and multiplication.

[00:50:38] When you perform operations with sums of ones, you get a sum of ones again.

[00:50:43] We haven't yet proven a very important fact, that all fields Fp^k are isomorphic to each other.

[00:50:53] But today we've tried machine learning for the first time to crack some number theory stuff.

[00:51:00] Namely, to understand that the product of two Legendre symbols depends on (p-1)/2 and (q-1)/2 by this law.

[00:51:11] You can find the derivation of this law using elementary methods in this video.

[00:51:17] Sorry for the long talk today! Have a great evening, everyone! Goodbye!
