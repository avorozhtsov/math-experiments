# 23. Geometric Algebra.  Уравнения Максвелла в одну строчку (English Subtitles)

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [Nl3nYVMnn44](https://www.youtube.com/watch?v=Nl3nYVMnn44). Получено: 2026-10-08T17:41:52+01:00.

[00:00:01] Hello everyone! This is the "Mathematical Experiments" channel.

[00:00:05] Today, I'm going to talk about geometric algebra.

[00:00:09] There is algebraic geometry - one of the most advanced fields in mathematics.

[00:00:14] And, there is also geometric algebra, which is something completely different,  although also a trendy thing with applications in physics.

[00:00:21] You can find many videos online about the geometric algebra.

[00:00:27] Title on the video "Swift Introduction"  has somewhat like definition of geometric product, but it is incorrect.

[00:00:30] But still, the video is good, I recommend it.

[00:00:33] These videos has pictures, animations, and beautiful examples.

[00:00:37] In particular, many of the videos provide this impressing example of how to write Maxwell's equations in one line using the geometric product.

[00:00:48] I will also try to get to this example in todays's video

[00:00:51] And I want to pursue my way of telling about geometric algebra via Wolfram Mathematica (WM).

[00:00:54] As you might guess, I will show how to implement Clifford algebra in Wolfram Mathematica (WM).

[00:01:00] I won't mislead you, this is not school material at all.

[00:01:05] And the complexity is primarily in the question: "Why?"  or "What are all these constructs for?"

[00:01:10] Or ... maybe not. if you've heard about matrix determinants, vector products,

[00:01:18] if you know the concept of factorization, for example, what is a factor group.

[00:01:24] Or, if you know how to integrate over a surface,

[00:01:28] and familiar with differential forms.

[00:01:31] THEN, you might see the reasoning behind these constructs.

[00:01:40] And, it may also be interesting for programmers,

[00:01:43] who will learn how to define new operators or redefine existing ones in the Wolfram language.

[00:01:51] That's also an interesting topic.

[00:01:54] And the way you define operators in WM is completely different from how it's done in traditional programming languages, like  C++, Java, or Python.

[00:02:00] That's because Wolfram Mathematica is not an imperative programming language.

[00:02:07] It is a term rewriting system.

[00:02:11] It is based on rules on transformations of expressions.

[00:02:14] Literally, calculations in WM are not the execution of step-by-step instructions,

[00:02:19] but a step-by-step application of expression simplification rules.

[00:02:23] For example, this expression is simplified to the following.

[00:02:29] It is reduced to some expression that can not be reduced any further.

[00:02:31] So, b multiplied by 5 is reduced to  5 b.

[00:02:34] And this collapses to 32.

[00:02:37] Let's go.

[00:02:38] The first important concept is the concept of a multivector.

[00:02:42] Suppose we have some vector space.

[00:02:46] For example, three-dimensional.

[00:02:48] And it has basis vectors e₁, e₂, e₃.

[00:02:52] So we will write down these formal expressions:

[00:02:56] e₁ ^ e₂

[00:03:01] The " ^ " is the Wedge operator. We will define some rules for this operator.

[00:03:05] In English, it is called Wedge. And it stands for special product, called exterior- or outer- product.

[00:03:07] When it is applied in a unary way, it remains the word Wedge.

[00:03:13] And when it is applied to two operands or more,

[00:03:18] then it is displayed  as  ^.

[00:03:22] Nothing is clear yet, and it shouldn't be. Just follow me.

[00:03:26] In short, besides the vectors e₁, e₂, e₃,

[00:03:31] we will also consider  bivectors  e₁ ^ e₂ , e₂ ^ e₃ , etc

[00:03:38] And trivectors like e₁ ^ e₂ ^ e₃ .

[00:03:40] And we will also consider scalars - numbers, like 1, 2, -0.5, etc.

[00:03:48] In order to remove word Wedge when Wedge is applied in a unary way, we will add such a rule...

[00:03:58] Ok, here I probably need to draw some more examples...

[00:04:07] In general, one can write any combination of basic vectors connected by the wedge symbol " ^ "  and treat it as new basic vector.

[00:04:13] These are our new basic vectors. Now we have an extended vector basis.

[00:04:19] In addition to the vectors e₁, e₂, e₃, we also have bivectors, trivectors, and so on.

[00:04:26] This is an basic vector multiplied by a given number.

[00:04:33] And this is a linear combination of basic vectors multiplied by numbers.

[00:04:38] Here we have formal sum of a scalar, a vector, and a trivector.

[00:04:44] A regular vector is written in this way. Its a vector with coordinates x, y, z.

[00:04:50] Well, we also have bivectors and function B3 for generating them.

[00:04:54] tAnd we have this thing P3. in three-dimensional space it is called pseudoscalar.

[00:05:00] In general, the space of ALL multivectors is the space of linear combinations of these four expressions

[00:05:10] So, now we want to endow " ^ " operator with some properties.

[00:05:15] First, we want it to be like multiplication.

[00:05:18] Namely, we want to be able to expand these braces according to rule we learned in school – distributive low.

[00:05:22] Each element from one expression must be "multiplied" via " ^ " by each element from the second expression.

[00:05:29] To apply this distributive law, WM has a Distribute function.

[00:05:35] It interprets the expression given inside as multiplication.

[00:05:41] That is, any function f, it will treat as multiplication.

[00:05:47] And expand it, as if it were the multiplication of two expressions.

[00:05:53] Let's check that this works not only for f but also for " ^ ".

[00:05:57] Here, it works.

[00:06:00] We want this distributivity to be applied automatically.

[00:06:04] And we also want these numbers: 3, 13, to be pulled to the left and multiplied.

[00:06:12] So, from " ^ " we demand: associativity, so that it doesn't matter how we arrange the braces.

[00:06:20] The distributivity with respect to addition, as if " ^ " was multiplication.

[00:06:25] Numbers should be brought to the left, as a common factor.

[00:06:30] And also, " ^ " should be such that when multiplied by a number, that number is also brought to the left.

[00:06:38] And finally, the most important part about " ^ " is that it is anticommutative.

[00:06:44] So, when we have defined all that we have just defined, we have essentially defined the exterior Grassmann algebra.

[00:06:54] These are the laws.

[00:06:56] When we defined anticommutativity, what automatically appeared?

[00:07:02] What automatically appeared was that eᵢ ^ eᵢ == 0

[00:07:05] Why?

[00:07:07] Because... well, let's take i instead of j, move everything to one side, and we get 2 eᵢ ^ eᵢ == 0.

[00:07:14] This means that eᵢ ^ eᵢ == 0.

[00:07:18] It follows from the commutativity, we can't have two identical eᵢ in the product through " ^ ".

[00:07:25] We can, but the expression will be equal to zero.

[00:07:29] Therefore, the effective number of the basis vectors in the exterior Grassmann algebra over R³ is 8.

[00:07:39] We have scalars.

[00:07:41] We have three basis vectors from the usual vector space.

[00:07:46] Three bivectors and one trivector.

[00:07:50] Why is there only one? Why isn't there e₂ ^ e₁ ^ e₃?

[00:07:54] There is, but we can permute the elements

[00:07:59] and therefore, all combinations of permutations of the indices 1, 2, 3, ultimately reduce to this vector.

[00:08:06] By using permutation and bringing out the -1.

[00:08:14] Let's consider the simplest implementation of the exterior algebra in WM in 3-dimensional space.

[00:08:22] This implementation literally fits on one screen. With comments.

[00:08:28] Forget everything we knew about the Wedge operator and say that it is flat.

[00:08:35] This is how associativity is denoted in WM.

[00:08:40] Distributivity is done like this:

[00:08:43] We say that if we have Wedge of " a " multiplied by something and this " a " is an expression with a head plus, that is an expression where something plus something,

[00:08:57] then we must apply the Distribute function.

[00:09:01] Let's temporarily denote Wedge as tmpV, as such... some temporary symbol.

[00:09:09] We ask WM to interpret this symbol as multiplication and perform distribution with respect to addition.

[00:09:18] This is interpreted as multiplication.

[00:09:20] There are also two additional arguments in the Distribute function, which specify what to replace plus with (with plus)

[00:09:28] and what to replace what we perceive as a multiplication with.

[00:09:32] The answer is Wedge.

[00:09:34] Next.

[00:09:35] If there is some prefix inside Wedge - some number of arguments...

[00:09:44] Three underscores mean some number of arguments: 0, 1 or more.

[00:09:49] That is a sequence of arguments.

[00:09:51] Then there is an argument that represents multiplying a number by something,

[00:09:58] and then another sequence of the arguments.

[00:10:01] ...so ultimately we have to simplify this expression to this,

[00:10:06] that is, to factor out the x multiplier from the expression.

[00:10:09] Next.

[00:10:11] If we encounter just a number, it should also be factored out of the expression.

[00:10:17] And then the rule of anticommutativity goes:

[00:10:21] We say that eᵢ ^ eᵢ == 0...

[00:10:25] Here, Wolfram understands such patterns.

[00:10:27] It understands that this index is any number, but it should be the same number in both places.

[00:10:35] Next, we say that e₂ ^ e₁ should be turned into e₁ ^ e₂,

[00:10:41] e₃ ^ e₁ should be turned into e₁ ^ e₃,

[00:10:45] and e₃ ^ e₂ should be turned into e₂ ^ e₃.

[00:10:47] So essentially what we're saying here is that when we search for neighbors inside Wedge arguments with indices in the wrong order,

[00:10:57] we need to arrange those indices in the correct order.

[00:11:00] And the "-1" comes from anti-commutativity.

[00:11:04] Wedge[a_] is just equal to "a";

[00:11:06] We're saying here that the unary Wedge[a] is the argument "a" itself.

[00:11:13] And Wedge of nothing is equal to one: Wedge[] := 1;

[00:11:17] In the end... everything works.

[00:11:21] And at this point, after a one-page definition, we get something useful and applicable.

[00:11:28] We get that with the help of the wedge product, we can write determinant of a matrix formed by three vectors.

[00:11:36] The wedge product of three vectors gives us a pseudoscalar with length equal to the determinant of the matrix.

[00:11:49] Let's learn more about attributes.

[00:11:56] For example, here's the built-in operator "+".

[00:11:59] It has the name "Plus", And "a + b" is just the neat way to write Plus[a, b].

[00:12:06] So, the Plus operator has the following attributes.

[00:12:12] The first: it is Flat - which means that (a + b) + c, where the braces are placed like this,

[00:12:18] becomes Plus of three arguments.

[00:12:23] In general, any hierarchy of Plus-es becomes Plus with n arguments.

[00:12:29] That's what Flat means.

[00:12:31] And yes, it's not the associativity property. It is not the definition of associativity property.

[00:12:34] It's about making the hierarchy one level deep.

[00:12:40] If we allow such flattening, then the operator should be associative.

[00:12:46] Next. Listable is a convenient attribute that allows to apply this function or operator directly to a list.

[00:12:54] A list plus a number is a list where each element has this number added to it.

[00:12:59] NumericFunction == number in then numbers out.

[00:13:02] OneIdentity means that the unary Plus operator applied to x gives x.

[00:13:10] Orderless is an indication of commutativity.

[00:13:16] It means that Plus with any number of arguments automatically becomes Plus with the sorted arguments.

[00:13:27] And yes, again, it's not commutativity itself.

[00:13:29] It's the transformation rule.

[00:13:33] And if the operator is commutative, then we allow such transformation.

[00:13:39] Protected means that we cannot redefine this operator.

[00:13:44] Regarding the last one, it's simple.

[00:13:46] Imagine we want 1 + 2 to be equal to 4.

[00:13:49] Wolfram says No.

[00:13:50] But if we do Unprotect Plus, then we can redefine the Plus operation for some cases.

[00:13:58] Let's step-by-step see how all this works.

[00:14:02] Let's consider some operator CirclePlus "⊕", for example.

[00:14:09] Currently, it doesn't know what to do with this expression and no calculations are performed.

[00:14:14] It doesn't have any rules about the CirclePlus operator.

[00:14:18] But as soon as we assign the Flat attribute,

[00:14:22] it starts performing some transformations.

[00:14:24] And the hierarchy of depth two is transformed into a single-level expression of the three arguments.

[00:14:33] Like this.

[00:14:35] If we set Orderless, then Wolfram automatically sorts arguments.

[00:14:39] See?

[00:14:40] It was 3 ⊕ 2 ⊕ 1, and now it's 1 ⊕ 2 ⊕ 3.

[00:14:42] And this allows it to know that these expressions are equal, without performing any calculations.

[00:14:55] So CirclePlus[3]. It doesn't know what to do with this yet,

[00:14:59] but we can say that OneIdentity is fulfilled.

[00:15:03] Which means that the unary CirclePlus operator doesn't change its argument.

[00:15:08] But, truthfully, I found out that it doesn't quite understand this.

[00:15:12] If you want to explicitly make the transformation of CirclePlus from " a " to " a ",

[00:15:17] then you need to write this rule.

[00:15:21] For complex reasons, you have to write Verbatim here, I won't explain why.

[00:15:26] Here!

[00:15:29] Thus, if you want to define some properties of any operator, partially it can be done via setting attributes.

[00:15:39] And part of it can be done with rules,

[00:15:43] like these.

[00:15:48] Next.

[00:15:49] I want to tell you a little bit about mathematics.

[00:15:52] About what tensor algebra, free algebra is.

[00:15:55] And what factorization is.

[00:15:59] Tensor algebra is a very simple thing.

[00:16:04] And the main misunderstanding can arise with the question of why all of this is being done, this strange thing.

[00:16:12] So here it is. Why is all of this being done?

[00:16:16] Tensor algebra is a raw blank thing, from which you can later make whatever algebra you want.

[00:16:25] How it is constructed.

[00:16:27] Let's you have a number field K and some vector space over this field.

[00:16:34] And of course, there are operators for adding vectors.

[00:16:38] And multiplying vectors by numbers.

[00:16:41] What you do.

[00:16:43] You add an operator of tensor multiplication,

[00:16:48] which is associative, distributive, and linear with respect to multiplication by numbers.

[00:16:54] What does this mean?

[00:16:55] This means that it is not so important how the parentheses are arranged here.

[00:17:00] What needs to be done is to expand such expressions as if it were multiplication.

[00:17:06] I didn't write it here...

[00:17:10] And that numbers can be taken out and multiplied with each other.

[00:17:18] Tensor algebra consists of expressions of this type.

[00:17:23] Sum. A formal sum of a scalar,

[00:17:26] some numbers multiplied by eᵢ.

[00:17:29] Some numbers multiplied by eᵢ ⊗ eⱼ, and so on.

[00:17:34] How to multiply two such formal sums?

[00:17:38] In very intuitive way. Each element from the first expression is multiplied by each element from the second expression.

[00:17:45] Then 3e₃⊗3e₁e₃ turns into 9 times e₃⊗e₁⊗e₃.

[00:17:57] Just like that.

[00:17:59] Two numbers 3 were factored out, multiplied, and became a multiplier for this expression.

[00:18:06] This is recorded as follows:

[00:18:08] Tensor algebra over V denoted as T(V) is the direct infinite sum of spaces.

[00:18:15] The first is the number field K itself. The second is the original vector space V.

[00:18:19] then V² and V³ go and so on.

[00:18:28] For this sample formal sum we have

[00:18:32] 2 belongs to the component K.

[00:18:35] This subexpression belongs to the component V.

[00:18:38] This bivector belongs to the component V², and so on.

[00:18:43] This is called grades.

[00:18:45] And all this stuff is just a formal sum,

[00:18:49] constructed over eᵢ as if they were variables,

[00:18:53] and instead of multiplication we use sign "⊗". Which is not commutative in general.

[00:18:57] Just a formal sum.

[00:19:02] Sometimes it's hard to explain the concept of formal sums.

[00:19:05] People just starve for answer:

[00:19:09] What is the result of this tensor multiplication?

[00:19:12] It's difficult.

[00:19:15] We don't expand this multiplication because there is no answer to this question.

[00:19:20] Let's say...

[00:19:22] There is a joke like this:

[00:19:25] There are ten types of people: those who understand binary arithmetic and those who don't.

[00:19:32] I think we can come up with a similar joke about formal sums:

[00:19:36] There are people who understand formal sums and those who don't understand them,

[00:19:42] Or better like this:

[00:19:43] There are different types of people:

[00:19:46] those who don't care about formal sums,

[00:19:49] those who don't understand them,

[00:19:52] those who understand them,

[00:19:53] those who don't understand them twice,

[00:19:57] those who don't understand, but later understand,

[00:19:59] understand, and then don't understand,

[00:20:00] understand twice.

[00:20:04] And so people are divided into these total number of types.

[00:20:09] In summary: Tensor algebra is an algebra of formal expressions constructed on vectors e₁, e₂, e₃, eₙ,

[00:20:18] where the multiplication sign looks like this. It is associative, distributive, and numbers are factored to the left.

[00:20:28] Now...

[00:20:30] When we

[00:20:32] postulate the anti-commutativity of this multiplication,

[00:20:37] we immediately obtain the Grassmann algebra.

[00:20:42] And the moment we postulate this, we need to change tensor product symbol to this wedge symbol

[00:20:46] And that's it!

[00:20:48] On a mathematical language, it is written as follows:

[00:20:53] The exterior product of a vector space with itself is the tensor product V ⊗ V,

[00:21:01] factored by expressions of the form v ⊗ v.

[00:21:06] In other words, we are saying that two elements inside the tensor algebra V ⊗ V are considered the same,

[00:21:14] if they do differ by v ⊗ v.

[00:21:20] Or an equivalent definition of the exterior algebra.

[00:21:24] Once again.

[00:21:26] The exterior algebra over the vector space V is the tensor algebra T(V). So it ingerits from  T(V) all its properties.

[00:21:34] Then we replace the tensor multiplication symbol with Wedge.

[00:21:40] This replacement is the most important thing, apparently.

[00:21:42] We also postulated anti-commutativity when we take the exterior multiplication of two vectors from V.

[00:21:51] Or two basis vectors from V.

[00:21:56] So...

[00:21:58] The formal sum looks the same as before.

[00:22:01] But there are some new aspects in the multiplication of expressions.

[00:22:05] Let's take a look at this.

[00:22:08] And what will be in the end?

[00:22:10] In the end, it will be...

[00:22:14] Well, it seems like I have some errors here ...

[00:22:20] Here we have 1 and 3

[00:22:25] So, in the end, we have 1 multiplied by each element in this expression, resulting in this.

[00:22:32] -2e₂ multiplied by each element in this expression results in this.

[00:22:38] And 3e₃ does the same.

[00:22:42] What do we do next?

[00:22:44] Next, we see that this equals zero because e₂ ^ e₂ = 0.

[00:22:50] Next, here we order the indices and swap e₂ and e₁.

[00:22:56] We mentally draw brackets around them, swap them, a minus sign appears, which cancels out the previous minus sign.

[00:23:04] Resulting in 6.

[00:23:08] And here this term disappears because e₃ ^ e₃ appears in it.

[00:23:16] How can we prove that this expression equals zero?

[00:23:20] First, we draw brackets around it, swap them, the minus sign appears,

[00:23:25] and now e₃ is here.

[00:23:27] Then we draw brackets around e₃ ^ e₃ and it equals zero,

[00:23:34] the zero flies out as a common factor, so this term is also eliminated.

[00:23:40] That's how it is.

[00:23:43] A small addition about anticommutativity and from the general blank, tensor algebra, we obtained the exterior algebra of Grassmann.

[00:23:51] And here we have this interesting result that the exterior product of three vectors

[00:23:58] gives us a pseudovector with a determinant in front of it.

[00:24:01] Clifford algebra is constructed similarly to factorization over T(V).

[00:24:10] There is a wrong approach to defining Clifford algebra.

[00:24:13] Like this.

[00:24:15] Let's define the operator " ∘ " (geometric product) using " ^ " and " · ".

[00:24:21] And a dot " · " represents a scalar product.

[00:24:24] But no. This is the wrong approach. This expression cannot be the definition.

[00:24:29] This expression is true in specific cases.

[00:24:32] It's like a consequence for some specific cases.

[00:24:34] And the definition of Clifford algebra is as follows:

[00:24:39] We take the tensor algebra T(V) again,

[00:24:42] and postulate that for any vector " a " in V,

[00:24:49] " a ∘ a " gives us a number, a scalar, equal to the quadratic form of the vector " a ".

[00:24:58] Usually, the ordinary form is taken as the quadratic form,

[00:25:02] which returns the number 1 for all unit vectors in space V.

[00:25:11] Or in other words:

[00:25:12] Clifford algebra is the factorization of the algebra T(V) over the set of such expressions.

[00:25:19] The words may be unclear, but what to do in practice is very understandable.

[00:25:24] I'll show you now.

[00:25:26] So, let our quadratic form Q be equal to 1 for our unit vectors.

[00:25:31] Then eᵢ ∘ eᵢ - Q(eᵢ) should be equal to zero.

[00:25:36] What does this mean? This means that eᵢ ∘ eᵢ = 1.

[00:25:41] Okay.

[00:25:43] Next, let's write this expression, which should be equal to zero, for eᵢ + eⱼ.

[00:25:50] This is what we will get.

[00:25:53] Moving Q to the other side.

[00:25:55] Understanding that the square of the length of this vector is 2.

[00:26:01] This is the square of the hypotenuse in a right triangle with legs of length 1, 1.

[00:26:07] As a result, we get...

[00:26:09] We expand these brackets according to the distributive law.

[00:26:13] We get this expression.

[00:26:16] We set it equal to 2 and obtain the anticommutativity of our basic vectors.

[00:26:22] You see: we postulated this,

[00:26:25] and as a consequence, we obtained anticommutativity.

[00:26:28] Just like in exterior algebra.

[00:26:30] But in exterior algebra, eᵢ ^ eᵢ = 0.

[00:26:34] While for us, eᵢ ∘ eᵢ = 1.

[00:26:39] That is, anticommutativity holds for different unit vectors,

[00:26:42] and unity holds for the square of one specific vector.

[00:26:51] In the end, we have the following thing:

[00:26:55] let's say we have such a long expression,

[00:26:58] where through the circle are multiplied some unit vectors from the original space V.

[00:27:05] Then with the help of such permutations of adjacent elements,

[00:27:11] we can move any of these vectors in any direction.

[00:27:18] And in particular, if we have two identical factors, eᵢ and eᵢ here too,

[00:27:23] then we can move eᵢ closer in some number of steps.

[00:27:29] When we connect them and draw them side by side, we can draw brackets around them

[00:27:36] and perform this multiplication according to this rule.

[00:27:41] As a result, we can collapse identical eᵢ in this product.

[00:27:49] In the end, our effective basis consists only of products of different eᵢ.

[00:27:58] Just like in exterior algebra, we end up with 8 basic vectors in this tensor algebra.

[00:28:13] Let's move on.

[00:28:14] Here I just showed that it's possible to redefine multiplication,

[00:28:18] the star operator " * ",

[00:28:20] for example, like this:

[00:28:22] by introducing the special letter tau " τ " to represent unit vectors...

[00:28:28] I didn't use " e " here to avoid spoiling " e ".

[00:28:32] ...and saying that the multiplication of two vectors equals 1 if i=j, and 0 otherwise.

[00:28:40] So this thing allows us to immediately get the scalar (inner) product of vectors.

[00:28:49] Okay. A lot of time has passed and I haven't told you anything interesting yet.

[00:28:56] Here I carefully define the exterior algebra and define the Wedge operator for the exterior product

[00:29:05] and the CenterDot operator for the scalar (inner) product.

[00:29:10] A lot of things are repeated here.

[00:29:13] In fact, I repeat all the same things that we had.

[00:29:18] I make convenient functions to generate:

[00:29:22] bivectors or just vectors, or pseudovectors of the general type.

[00:29:29] Here's the definition you've already seen.

[00:29:32] I just repeat it here.

[00:29:34] CenterDot, the scalar (inner) product, is defined in a similar way.

[00:29:40] Everything is the same. Distributivity. The ability to pull numbers out of brackets.

[00:29:47] But a little different here.

[00:29:51] Scalar (inner) product with a number always gives 0.

[00:29:55] The unary operator CentorDot gives 0.

[00:29:58] The operator applied to an empty set also gives zero.

[00:30:03] And it is also postulated that it is orthogonal.

[00:30:09] Here you might wonder: why does e₁ • e₁ equal 1 when this rule exists?

[00:30:16] The answer is complicated.

[00:30:18] This rule takes precedence because it is simpler.

[00:30:22] I won't go into detail.

[00:30:26] The scalar (inner) product is understood as being constructed in grade 1, within the space V.

[00:30:34] But how do we define it in V² or V³?

[00:30:39] The answer is: however you like, but it is usually accepted to define the scalar (inner) product in this way.

[00:30:48] The scalar product of a bivector with itself is -1.

[00:30:56] The scalar product of a unit bivector with itself is -1.

[00:31:01] The scalar product of a trivector with itself is also -1.

[00:31:05] The scalar product of a four-vector with itself is 1.

[00:31:07] There such rule is used...

[00:31:11] You need to understand it in your mind like this:

[00:31:15] Let's move this eₖ to the left twice.

[00:31:19] Moved.

[00:31:20] And we have eₖ here and eₖ here

[00:31:24] and we mentally draw brackets here and get 1.

[00:31:27] And our eₖ annihilates itself.

[00:31:31] Then we move eⱼ to the left.

[00:31:34] And again eⱼ • eⱼ annihilates each other.

[00:31:40] In short, practice permutation in your mind here

[00:31:44] and when two vectors are close to each other through a dot, they annihilate each other if it is the same unit vector eᵢ.

[00:31:54] Next.

[00:31:55] The scalar product of a vector from V and a vector from V² works like this.

[00:32:03] eᵢ appears to collapse with eᵢ, resulting in 1. Only eₖ remains.

[00:32:09] And here, in order to collapse eᵢ with this eᵢ, we need to first rearrange the elements inside the bracket, and the -1 will come out of the bracket.

[00:32:16] In short, this is probably all complicated,

[00:32:19] but this is how we need to correctly define the scalar product.

[00:32:28] In principle, instead of a set of rules, we could write one rule in a general form.

[00:32:34] Multiplying eⱼ, eₖ, and eᵢ

[00:32:37] and writing that j is equal to k and what if is not equal, etc.

[00:32:43] We check that all this works...

[00:32:50] So, something didn't work here, we'll fix it now...

[00:32:56] I just didn't execute this block. We continue checking...

[00:33:02] We execute: this is 0,

[00:33:04] this is -1,

[00:33:06] this is -e₃.

[00:33:08] e₁ ^ e₂ collapsed with e₁ ^ e₂ and gave -1

[00:33:14] Because this is -1.

[00:33:18] And this gives e₃.

[00:33:21] Because first we move e₃ twice to the end,

[00:33:24] then e₂ annihilates and e₁ annihilates.

[00:33:28] These definitions could be given through the signature of the permutation.

[00:33:36] For example, let's look here.

[00:33:38] We could do the following:

[00:33:40] The outer product eᵢ ^ eⱼ ^ eₖ is equal to...

[00:33:46] If all of these indices are different, that is, i, j, k are 1, 2, 3 in some order.

[00:33:52] This product should be equal to e₁ ^ e₂ ^ e₃ multiplied by 1 or -1,

[00:33:59] depending on how many permutations of adjacent elements are needed to obtain 1, 2, 3.

[00:34:05] This is called the signature of a permutation.

[00:34:07] But here we encounter an unpleasant surprise:

[00:34:10] When we write down this rule, we get e₁ ^ e₂ ^ e₃ on the right, and this rule is applied to that expression again.

[00:34:19] This results in infinite recursion.

[00:34:22] To avoid this, we need to write something on the right-hand side that doesn't fit this pattern.

[00:34:28] In some packages, this is done as follows:

[00:34:34] This product is written as " e " with a set of indices, where the set of indices is already ordered.

[00:34:43] This is one possible approach, but I didn't go down this path.

[00:34:49] So, let's check that everything is working...

[00:34:52] The numbers are outside the brackets.

[00:34:54] But there's a problem with x. It doesn't know that x is a number. It could be a vector too.

[00:35:00] We would like it to eventually realize that x is a number and take it outside the brackets.

[00:35:09] We'll do that now.

[00:35:11] Here's how it's done.

[00:35:13] So you see, it calculates the determinant of the matrix, but if we add abstract symbolic coordinates x1, y1, z1, etc.,

[00:35:23] we won't get the determinant formula, but we want to.

[00:35:28] To do this, instead of defining it like this,

[00:35:35] where we require x to be a number and then take x outside the brackets, we will require x to be a non-vector.

[00:35:45] And we will take the non-vector outside the brackets.

[00:35:48] Here's how it's done...

[00:35:52] We say that a vector is an expression that begins with CenterDot or an expression that begins with Wedge or the basic vector e.

[00:36:05] And everything else, Except[VectorT], is not a vector.

[00:36:10] Yes, and we also say that an expression that begins with Plus is also not a vector.

[00:36:16] We want Plus to be handled through the distributive law

[00:36:21] and therefore do not consider sums as non-vectors.

[00:36:29] We check what matches what

[00:36:33] and see that e₃ is a vector and NOT a non-vector.

[00:36:42] But this expression is kind of meaningless.

[00:36:45] It is neither an expression of type VectorT nor of type NVectorT.

[00:36:53] Next.

[00:36:55] I define CenterDot,

[00:37:00] now using NVectorT instead of Q-number.

[00:37:06] Well, as I already said.

[00:37:08] We check: " 123 " is taken out of the bracket and " abc " is also taken out of the bracket.

[00:37:15] We check...

[00:37:19] It considers this a non-vector, and when a vector is scalar multiplied by a non-vector, it always equals zero.

[00:37:26] So we postulated here. There is no secret.

[00:37:34] Next.

[00:37:35] We want it to collect identical terms while doing symbolic computations.

[00:37:43] Like here, for example, where 1+a is collected when x is used.

[00:37:46] We want the same thing to happen in this expression,

[00:37:57] so that these two terms are combined into one term.

[00:38:02] To do this, we define the function tE, which performs a Collect operation on the expression.

[00:38:10] And the second argument of Collect is the patterns that should be treated as variables.

[00:38:17] We are saying something like: we need to collect all expressions with these variables.

[00:38:25] Let's check...

[00:38:27] Here is an important milestone: using Grassmann algebra, we obtained a symbolic expression for the determinant of a 3x3 matrix.

[00:38:43] Let's check that everything works as expected.

[00:38:48] Here, the product of this and this gives us this.

[00:38:53] Because the product of this and this is zero,

[00:38:59] and only this part remains.

[00:39:02] Good. Everything is correct.

[00:39:04] Another way to obtain a symbolic expression for the determinant is to perform a mixed product of three vectors.

[00:39:10] Here it is transformed into an outer product of two vectors multiplied by a bivector.

[00:39:21] What else I wanted to tell you here.

[00:39:23] I wanted to tell you how you can leave some things until the end.

[00:39:29] That is, some laws, transformations, you write them using " := ",

[00:39:36] and some can be postponed until the very end, at the time of executing the tE function.

[00:39:43] In this function, there is a hidden Collect operation and also, for example, some rules for simplification.

[00:39:50] Here I use this arrow, not that one, because I want the right-hand side computations

[00:40:00] to be performed each time,

[00:40:03] and not that we first memorize these rules, compute the right-hand side and then substitute the computed value.

[00:40:11] No. We will calculate the right-hand side in the rules every time.

[00:40:14] The difference between these two arrows is well visible in these two examples.

[00:40:21] I have to say that I don't really need this, it all works without it.

[00:40:26] I just didn't get it to work at first and I thought it would be useful.

[00:40:31] In short, some final transformation rules can be left until the last stage.

[00:40:38] Now let's define the Clifford algebra.

[00:40:42] Using the SmallCircle symbol "∘".

[00:40:47] I'll say it again,

[00:40:49] there is a temptation to define SmallCircle using the dot symbol "•" and the exterior product "^",

[00:40:57] but it doesn't work.

[00:41:00] It works, but only for small grades.

[00:41:03] Therefore, for SmallCircle, for geometric product, we need to start from scratch.

[00:41:09] Now we will use SmallCircle to create multivectors.

[00:41:16] We write that SmallCircle[v_] := v;

[00:41:20] Yes, and here I tried not to make the attribute Flat, but to define the concept of Flat myself.

[00:41:26] The concept of Flat can be defined manually like this.

[00:41:31] Any hierarchy of SmallCircle turns into a flat thing.

[00:41:34] SmallCircle of many arguments.

[00:41:37] Here, it is written that if one of the arguments inside SmallCircle is again SmallCircle, then SmallCircle must be applied to all these arguments.

[00:41:46] Three underscores represent some sequence of arguments of length 0, 1, or more.

[00:41:53] And one underscore represents one argument.

[00:41:57] Here, in the sequence, they are expanded as sequences, not as a list.

[00:42:04] So, if s1 has three arguments,

[00:42:07] then here we have SmallCircle of: one, two, three...

[00:42:11] the fourth argument,

[00:42:12] some number of arguments here

[00:42:14] and some number of arguments here.

[00:42:17] Moving on.

[00:42:18] Because I didn't specify that SmallCircle is Flat,

[00:42:21] I manually defined it,

[00:42:23] and now I have to struggle with it.

[00:42:25] I have to state that:

[00:42:27] any pair eᵢ, eⱼ inside SmallCircle should be represented in such a way that the indices are in increasing order.

[00:42:41] Numbers are taken outside the brackets. Number " a " is taken outside the brackets.

[00:42:46] If number " a " is in the second position, the operator is also taken outside the brackets.

[00:42:55] If it's just a number, it's taken outside the brackets.

[00:43:00] And if we encounter a Plus, we need to apply Distribute.

[00:43:07] Now I want it to work for both exterior and geometric products.

[00:43:14] I consider all these things as basic variables, which we need to build expressions from.

[00:43:25] I'm checking that everything works...

[00:43:30] I forgot to execute this...

[00:43:36] Checking again...

[00:43:38] Alright, now everything works.

[00:43:42] And we get the correct expression.

[00:43:48] The product of any formal sums becomes a formal sum,

[00:43:53] where the elements are such products of eᵢ with different indices,

[00:43:59] and they are multiplied by some numbers that are no longer vectors.

[00:44:06] And tE does here an important operation called Collect.

[00:44:11] And when we have the same basis multivectors, we accumulate expressions.

[00:44:20] Here, I multiplied two general multivectors,

[00:44:24] and got a very long expression.

[00:44:30] Well...

[00:44:31] Here, I want to clarify again.

[00:44:34] Where does this expression come from?

[00:44:38] It comes from the fact that it's true.

[00:44:41] Indeed, eᵢ • eᵢ = 1.

[00:44:45] And the left side equals the right.

[00:44:48] And when i and j are different, then this is true.

[00:44:55] Since this expression is true for basic vectors, it's true for any vector in V due to the bilinearity of this, this, and this.

[00:45:07] Moving on.

[00:45:09] We, in a way, postulate that this multiplication, the "∘" circle,

[00:45:15] in the case when it's multiplied by a number, is equal to ordinary multiplication by a number.

[00:45:20] That is, if there is 10 ∘ eᵢ here, then a vector of length 10 in the direction of the basic vector eᵢ is obtained.

[00:45:31] From this statement, it immediately follows that

[00:45:36] the scalar product of 1 • eᵢ must be zero, because this expression already equals eᵢ,

[00:45:44] so this remainder must be zero.

[00:45:47] This is precisely why the intuition arose that the scalar product of a number with a vector is zero.

[00:45:54] Well, here I am just explaining various intuitions that were used

[00:46:01] to understand how to correctly define the scalar product on multivectors.

[00:46:06] About application.

[00:46:08] It's been a while, it's time to talk about the application.

[00:46:12] Most likely, what I've said so far doesn't make sense and is not clear.

[00:46:18] But my goal is to spark an interest.

[00:46:21] You need to carefully read this notebook to truly understand how everything is done, how everything is implemented.

[00:46:30] There are many examples. I will talk about the most basic ones.

[00:46:33] Firstly, using the concept of geometric product, you can implement complex numbers.

[00:46:41] To do this, you need to take the Clifford algebra, where the quadratic form gives -1, and the initial vector space is one-dimensional.

[00:46:51] Simply put, it's just one real number.

[00:46:54] So, we say that the quadratic form is equal to -1 on the only basic vector in the space V.

[00:47:05] And then, of course, we get that this multiplication corresponds to the multiplication of complex numbers,

[00:47:12] and the basic vector e₁ corresponds to the imaginary unit " i ".

[00:47:18] We could take the Clifford algebra in a two-dimensional space R²

[00:47:25] with the ordinary Euclidean scalar product, where eᵢ ∘ eᵢ = 1, not -1.

[00:47:34] But in this algebra, we would only need to take bivectors.

[00:47:39] Well, more precisely, there is only one e₁ ∘ e₂.

[00:47:43] e₂ ∘ e₁ also exists, but it is equal to - e₁ ∘ e₂.

[00:47:50] That is, in the Clifford algebra Cl₂,₀(R), we could consider a space consisting of a linear combination of a scalar and a bivector.

[00:48:02] We only consider bivectors and scalars, and then in this space, we get complex numbers.

[00:48:10] Let's check...

[00:48:12] The same multiplication formula.

[00:48:14] Both e₁ and e₂ should be seen as imaginary units.

[00:48:19] We took the tensor algebra. Only its even part, where we take K, V², V⁴, etc.

[00:48:30] We don't take V and V³.

[00:48:33] The next application:

[00:48:35] Quaternions.

[00:48:38] Quaternions can be realized in this way:

[00:48:41] Take the Clifford algebra,

[00:48:44] where the squares of all vectors are equal to -1.

[00:48:50] And also postulate these three equations.

[00:48:54] And we get a quaternion.

[00:48:57] That is, make an additional factorization of the Clifford algebra according to these three relationships.

[00:49:03] And then we'll have a quaternion.

[00:49:05] But there is another option: again, we can consider the even subalgebra in the Clifford algebra 3,0.

[00:49:13] It was 0,3 because we took -1 three times.

[00:49:19] e₁² yields -1, e₂² yields -1, and e₃² yields -1.

[00:49:25] And here we took vectors whose squares are equal to one,

[00:49:30] but again, we only considered linear combinations of scalars and bivectors.

[00:49:37] We only looked at these expressions.

[00:49:42] The product of these things again yields a vector consisting of scalars and bivectors.

[00:49:52] That's a scalar...

[00:49:58] Here's a scalar,

[00:50:00] and here are the three components of a bivector.

[00:50:04] And this is the correct multiplication of quaternions.

[00:50:08] Let me illustrate this with the well-known rotation formula.

[00:50:15] To rotate a vector v:

[00:50:17] you need to multiply it on the left by this,

[00:50:18] and on the right by this.

[00:50:20] Then, the result will be a rotation by angle " α " around vector " u ".

[00:50:26] Vector " u " needs to be represented as a bivector.

[00:50:31] Okay...

[00:50:33] In short,

[00:50:35] Clifford algebra is the general case.

[00:50:39] And as a special case, you can implement complex numbers.

[00:50:42] For example, either like this, or even subalgebra in Clifford algebra R².

[00:50:48] Quaternions can be implemented as the even subalgebra in Clifford algebra 3,0.

[00:50:54] Or as the Clifford algebra 0,3 with additional relations.

[00:51:01] Oh, and let me explain again:

[00:51:02] the notation Cl p,q means that we take a quadratic form Q,

[00:51:07] where the first p vectors have norm 1,

[00:51:12] and the next q vectors have norm -1.

[00:51:18] Here are two implementations of the quaternions.

[00:51:22] Moving on. Maxwell's equation.

[00:51:24] Can be written in one line...

[00:51:27] Here, actually, multiplication through a circle " ∘ " is used.

[00:51:32] Like this.

[00:51:33] ...where F is an electromagnetic field,

[00:51:37] composed of vector E

[00:51:40] and bivector B.

[00:51:43] This symbol "∇" means the differentiation operator.

[00:51:50] Here is the differentiation operator, which is perceived as a number, and basic vectors are simply multiplied on the left by the differentiation operator.

[00:51:59] And J is a multivector consisting of the scalar density of charge and the vector of current j.

[00:52:09] And you can verify that when you expand this expression, you will have precisely the Maxwell's equations.

[00:52:17] Well, and the determinant...

[00:52:18] Let me tell you about Maxwell's equations right now.

[00:52:22] Here's what I just said.

[00:52:25] The electromagnetic field F,

[00:52:27] the differentiation operator d,

[00:52:29] and the multivector J,

[00:52:33] consisting of the charge density

[00:52:34] and the current vector.

[00:52:37] Let's check...

[00:52:39] And we get...

[00:52:43] This expression equals zero.

[00:52:46] It equals zero when the scalar is zero.

[00:52:50] Here's the scalar.

[00:52:52] When the bivector is zero.

[00:52:56] These three components are equal to zero.

[00:53:01] And when the vector part, this one here, equals zero.

[00:53:04] That is, when e₁, e₂, e₃.

[00:53:06] And when the pseudoscalar is also equal to zero.

[00:53:10] Then the divergence of the magnetic field, this one here, equals zero.

[00:53:15] The divergence of the E field equals the charge density ρ.

[00:53:19] Everything is written correctly.

[00:53:22] Next, the rotor of E gives H.

[00:53:28] And the rotor of H gives the derivative of E (with respect to time t) and j.

[00:53:38] In one equation, we are able to write two scalar equations about the divergence of E and H,

[00:53:47] and three vector equations about the rotor of E and H.

[00:53:52] Here we were able to implement the Maxwell equation in Clifford algebra 3,0 over R.

[00:53:59] But it is more correct to implement it in the four-dimensional space R⁴, where the quadratic form has a signature of 1,3.

[00:54:08] I won't do this.

[00:54:11] Explicitly, it is necessary to determine that e₁² equals 1, and e₂², e₃², e₄² equals -1.

[00:54:19] I have ready-made implementations of the Clifford algebra in this file, ready to go.

[00:54:24] Although, nothing works, because I already messed up the symbol " e ".

[00:54:29] But nevertheless, let's try.

[00:54:31] Maybe it will still work.

[00:54:34] There is a ready-made implementation of the Clifford algebra in the most general form for various quadratic forms Q.

[00:54:44] I recommend using it.

[00:54:47] With this package.

[00:54:51] Let's check...

[00:54:53] Here is the signature of our quadratic form.

[00:54:59] This is an ordinary vector.

[00:55:03] Here we have the recording of the electromagnetic field F,

[00:55:08] the differentiation operator,

[00:55:11] and the current multivector J.

[00:55:14] The four-vector J.

[00:55:17] And we get the same result again.

[00:55:20] It is correct to express Maxwell's equations in the Clifford algebra 1,3.

[00:55:26] That's all for today.

[00:55:28] It was a very difficult topic.

[00:55:32] Requiring independent study.

[00:55:35] Yes, don't expect that just by watching a YouTube video, something will remain in your head.

[00:55:42] Something will remain only if you take a pen and paper or the WM language and do something with your own hands.

[00:55:48] Wolfram Mathematica is an unusual programming language. It is a term reduction system.

[00:55:54] And it is probably suitable for implementing various factor algebras of the free algebras.

[00:56:01] T(V) is a free tensor algebra,

[00:56:04] and the Clifford algebra is a factor algebra by this relationship.

[00:56:10] And this notation Clp,q means that the quadratic form Q we have chosen has signature p,q.

[00:56:19] The Clifford algebra is actively used by physicists and this is one of the most vivid examples - the Maxwell equations.

[00:56:26] Simpler examples are quaternions and complex numbers, which can be implemented through the Clifford algebra.

[00:56:33] Perhaps all of these arguments seem extremely complicated and unnatural,

[00:56:40] and this is not accidental, because the Clifford algebra has a long history of thought, spanning centuries.

[00:56:47] And naturalness arises when you know all this backstory.

[00:56:53] Then this calculus in the Clifford algebra looks understandable.

[00:56:59] It is clear that it really generalizes many things that have been encountered before.

[00:57:04] External vector product, external differential form product, etc.

[00:57:10] That's all for today. I hope it was interesting. At least I've got you interested.

[00:57:16] I do not hope that something was understandable.

[00:57:19] To make it clear, please read the notebook whose link I left in the description below.

[00:57:25] Good luck to everyone! Bye!
