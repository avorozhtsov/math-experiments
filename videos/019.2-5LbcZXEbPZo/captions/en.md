# 19. Часть 2. ML в теории чисел? Открываем квадратичный закон взаимности.

Язык: en. Опубликованная дорожка субтитров YouTube; без нового перевода или редакторских исправлений.

Источник: [5LbcZXEbPZo](https://www.youtube.com/watch?v=5LbcZXEbPZo). Получено: 2026-10-08T17:42:15+01:00.

[00:00:00] So, we've reached the quadratic reciprocity law and machine learning.

[00:00:07] Let's define the Jacobi table,

[00:00:13] which will consist of Legendre symbols.

[00:00:18] Let's draw it.

[00:00:22] Here, yellow represents 1, and blue represents -1.

[00:00:32] X and Y are the numbers of the prime numbers.

[00:00:38] I took a hundred prime numbers,

[00:00:40] placed them here on the X-axis,

[00:00:43] and placed the hundred prime numbers here too.

[00:00:47] And in each little pixel, I drew yellow or blue based on

[00:00:56] whether Q (let's call this axis Q) is a quadratic residue modulo p.

[00:01:02] This is the X-axis.

[00:01:05] Rooster here is excited, wants to add something :D

[00:01:10] We look and don't see any regularity.

[00:01:14] Interesting maze generator appears here (or QR codes).

[00:01:18] Alright. Let's generate a train set for machine learning.

[00:01:25] We record a random p,

[00:01:29] a random q

[00:01:31] and the value of the function we want to learn to predict from p and q.

[00:01:38] This is my dataset.

[00:01:42] Next, I start generating features.

[00:01:45] Some factors.

[00:01:48] I understand that the Jacobi function is a function of p and q.

[00:01:53] I need to generate factors – properties of objects p and q.

[00:02:00] What properties do I know?

[00:02:01] For example, I know residues modulo 3, 5...

[00:02:06] Also, I can take (p-1)/2, because earlier I saw that something can depend on this number.

[00:02:14] And also, whether this number is divisible by 3 or not.

[00:02:19] I ended up with 4 here and another 4 – 8 factors.

[00:02:24] And t – this is what I want to predict. I took t from the data.

[00:02:29] The expression is complex, but read it like this:

[00:02:33] we run through the elements of the data list.

[00:02:36] Each one is a triple.

[00:02:38] And as we know, each element is a triplet.

[00:02:42] We save this triplet in the variables p, q, and t.

[00:02:47] t is precisely our target function.

[00:02:54] Let's see what the mean squared deviation from the target is.

[00:03:01] 0.999...

[00:03:05] This means that the mean is zero,

[00:03:08] and further, -1 or 1 appear in the dataset with a probability of about 50%.

[00:03:16] We need to learn to predict something close to t,

[00:03:20] so that the standard deviation for the forecast deviation and target,

[00:03:28] is less than 1.

[00:03:30] That's our goal.

[00:03:33] Lets run it...

[00:03:35] In Mathematica there's a Predict function,

[00:03:40] to which you need to pass an array of factors or FeatureSet.

[00:03:47] Then draw an arrow and then the target list.

[00:03:52] The first set of features from this list

[00:03:54] corresponds to the first element from the this list.

[00:03:59] It calculated what the StandartDeviation is.

[00:04:05] You can see from this graph that it couldn't reduce it.

[00:04:10] The standard deviation remained 1.

[00:04:16] So, failure.

[00:04:18] We couldn't use machine learning to guess any dependency

[00:04:25] and I immediately draw a conclusion:

[00:04:28] most likely, information about what the Legendre symbol is not encoded in these factors.

[00:04:37] Alright, failure is also a result.

[00:04:41] Next, we do a very natural action from my point of view.

[00:04:46] We got an asymmetrical picture,

[00:04:49] but let's take this picture,

[00:04:53] reflect it about the yellow line,

[00:04:55] and multiply it by itself.

[00:04:58] Make the picture symmetrical.

[00:05:04] Defining...

[00:05:06] Drawing...

[00:05:07] Now, in cell (i, j), I have the product of two Legendre symbols.

[00:05:17] I don't know why I wrote it so complicated here...

[00:05:21] We could make it simpler.

[00:05:24] And now I see regularity.

[00:05:27] This is not what was expected from a symmetrical picture.

[00:05:30] Symmetrical pictures can be more complex.

[00:05:32] Here it's much simpler.

[00:05:34] It's evident that if a prime number is yellow,

[00:05:39] then all the answers for it are yellow.

[00:05:44] Yellow color seems to win.

[00:05:46] As if yellow is 0, and blue is 1.

[00:05:51] And in the cell is drawn the product

[00:05:54] of the color of this prime number

[00:05:56] and the color of that prime number.

[00:05:59] Yellow color prevails.

[00:06:01] Curious, can we...

[00:06:04] Alright... here's a bigger picture.

[00:06:07] Curious, can we this time achieve something less than 1 through machine learning?

[00:06:18] Or rather, not 1.

[00:06:20] This time, the standard deviation will already be < 1 even without any prediction.

[00:06:27] The standard deviation of the target – that's its mean deviation from the mean,

[00:06:33] and the mean is no longer 0, we have more yellow color.

[00:06:40] So, our goal is to get a value during machine learning that's less than 0.75

[00:06:46] Let's check...

[00:06:56] Took a while to think...

[00:06:57] Yes!

[00:06:58] A miracle happened. 0.0339

[00:07:04] We managed to make the standard deviation smaller than the original standard deviation.

[00:07:11] That means we were able to extract some useful information from those factors.

[00:07:17] Sometimes machine learning cannot predict the target exactly.

[00:07:22] Like here, the standard deviation is not 0.

[00:07:25] But the signals are important,

[00:07:28] that among these numbers there are some numbers, maybe all of them,

[00:07:32] from which the product of two Legendre symbols pq and qp depends.

[00:07:40] Moving on...

[00:07:42] Next, I would like to show that we could work not with DecisionTree,

[00:07:47] as it was automatically selected here,

[00:07:50] but with neural networks.

[00:07:52] For that, there's the NetTrain function.

[00:07:54] Here, the architecture of the neural network is described.

[00:07:58] First layer of size 5.

[00:08:00] Then this activation function.

[00:08:03] Ramp – it's the well-known Rectified Linear Unit (ReLU) function.

[00:08:09] Here it's called Ramp.

[00:08:12] Then a layer of size 4,

[00:08:14] then activation again.

[00:08:17] And finally, a neuron.

[00:08:21] In the end, we have one  neuron where the answer should be.

[00:08:28] Let's see how the training looks.

[00:08:31] In the NetTrain function, you can explicitly specify the LossFunction and also ValidationSet.

[00:08:37] Above, I divided the DataSet into two parts.

[00:08:43] The first 80 thousand is the TrainSet,

[00:08:46] and the next 20 thousand is the ValidationSet.

[00:08:52] And accordingly, fs and target for them.

[00:09:00] Here we have the loss on the Validation Set, already 10^-4.

[00:09:07] This is the mean squared deviation.

[00:09:12] So, the Standard Deviation, the square root of this number, is about 10^-2.

[00:09:16] Here he writes that he used the default here.

[00:09:21] So, success!

[00:09:24] Among the factors we made up,

[00:09:27] there are some factors that affect the target.

[00:09:31] Through trial and error, I find out that there are two factors.

[00:09:35] These ones.

[00:09:37] Well, and then it starts to be a bit of guessing and trying.

[00:09:45] And it turns out that this thing is always equal to 1.

[00:09:54] The product of two Legendre symbols multiplied by (-1)^((p-1)/2)((q-1)/2) always equals 1.

[00:10:05] And here's where you can grasp the concept of the yellow color.

[00:10:08] If you have a prime p such that (p - 1)/2 is divisible by 2,

[00:10:14] then inevitably, this multiplier becomes 1.

[00:10:24] You won't get -1 here, regardless of q.

[00:10:30] This explains the dominance of the yellow color.

[00:10:35] This theorem, that this product always equals 1,

[00:10:41] meaning always yellow.

[00:10:44] Carl Friedrich Gauss proved it in eight different ways.

[00:10:48] He considered it a very important theorem.

[00:10:50] And it truly is a very important theorem.

[00:10:52] It has many fascinating generalizations.

[00:10:55] Below, I'll leave a link to a video by Alexey Savvateev about quadratic reciprocity laws.

[00:11:05] That's how it's described on Wikipedia.

[00:11:07] We define the Legendre symbol as follows.

[00:11:11] Is there a solution to n^2 = q or not?

[00:11:15] And the law of quadratic reciprocity.

[00:11:20] Alright.

[00:11:23] The Jacobi symbol, it can be extended as follows.

[00:11:28] When you have the second argument here as the product of two numbers,

[00:11:34] it's then expanded into the product of two Jacobi symbols.

[00:11:38] And when the first place is the product of two numbers,

[00:11:40] it's also expanded into the product of two Jacobi symbols.

[00:11:44] So, the Jacobi symbol is a multiplicative function of two arguments.

[00:11:50] To find out the value of the Jacobi symbol, you need to expand it over all products,

[00:11:58] based on the factorization of the first argument and the factorization of the second argument.

[00:12:04] Then you get exclusively prime numbers as arguments for the Jacobi function

[00:12:10] and then you expand them as Legendre symbols.

[00:12:19] To be continued...
