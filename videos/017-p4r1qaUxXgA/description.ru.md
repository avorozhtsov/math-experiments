00:00 Введение
00:14 Простые числа
00:54 Let’s crack primes counting Pi function
01:25 Описание функции PrimePi 
01:58 Изучение функции PrimePi: 
02:08 Изучаем, как меняется доля простых чисел среди всех чисел ≤ x
03:49 Рисуем разницу PrimePi[x] - x/(Log[x] - а)
06:10 Закон невязки между функцией PrimePi и апроксимацией
07:27 Шум
07:51 Выписываем приблизительный закон невязки
08:49 Метод фиттинга для выписки более точного закона
09:16 Выражение шума
09:44 Функция QRange
10:10 Нахождение коэффициентов путем минимизации среднего значения квадрата шума
10:34 Функция NMinimize использует метод отжига
10:53 Определение функции PrimePiMy
11:04 Рисуем разнице между функциями PrimePiMy 
 и истинной функцией PrimePi 
13:51 Нахождение коэффициентов путем минимизации шума, попытка 2
14:54 Рисуем значение шума: PrimePiMy[#] - PrimePi[#]
16.01 Нахождение коэффициентов путем минимизации шума, попытка 3
17:25 Функция LogIntegral
19:29 Факториал в коэффициентах
20:36 Сравнение коэффициентов
21:19 Подытоживаем
22:15 Графики 3-x приближений
23:25 Формула Римана 
24:29 Функция MoebiusMu
24:56 Приближение Римана
26:04 Графики 4-x приближений
28:32 Выводы

Начнём с функции pi(x) – количества простых чисел меньше  либо равно x.
Довольно быстро мы приходим к загадочному шуму, скрытому внутри pi(x). Размер этого шума растёт как sqrt(x)/log(x), а ограниченность его модуля сверху  С * sqrt(x) * log(x) эквивалентна гипотезе Римана о нулях дзета-функции.

https://en.wikipedia.org/wiki/Prime-counting_function
https://en.wikipedia.org/wiki/Logarithmic_integral_function
https://en.wikipedia.org/wiki/Cauchy_principal_value
https://en.wikipedia.org/wiki/Riemann_hypothesis

Mathematica notebook: 
https://www.wolframcloud.com/obj/artem.voroztsov/Published/017-prime_pi.nb
https://disk.yandex.ru/d/pHW8P_Q_gcc4wg

Материалы, код и файлы Mathematica: https://github.com/avorozhtsov/math-experiments/tree/main/videos/017-p4r1qaUxXgA
