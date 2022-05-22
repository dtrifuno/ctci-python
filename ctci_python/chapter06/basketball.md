# Basketball

Let $p$ be the probability of making a shot. The probability of making at least
two shots is then

$$
p^3 + 3p^2(1-p) = 3p^2 - 2p^3 = p^2(3 - 2p),
$$

since we either make all three shots or there are three possibilities for which
shot we miss.

Thus, for Game 2 to be better, $p$ must satisfy

$$
\begin{align*}
  p^2(3-2p) &> p \\
  3p - 2p^2 - 1 &> 0 \\
  2p^2 - 3p + 1 &< 0 \\
  (2p-1)(p-1) &< 0,
\end{align*}
$$

i.e. $ p > \frac{1}{2}$. Thus Game 1 is best for
$p\in \left(0, \frac{1}{2}\right)$, Game 2 is best for
$p \in \left(\frac{1}{2}, 1\right)$, and the choice of game is irrelevant for
$p=0$, $p=\frac{1}{2}$ and $p=1$.
