# Poison

Label all bottles from 0 to 999, and all strips from 1 to 10. Note that since
$2^{10}=1024$, the binary expansion of 999 has only 10 digits, and that
therefore we can put samples on the $i$-th strip from all bottles that have a
$1$ in the $i$-th position of their binary expansion, and have a strip for all
such $1$'s. This allows us to run all tests at once. Once we have the results,
we can easily recover the label of the bottle: its binary expansion has a $1$
in every position corresponding to a positive test strip, and a zero otherwise.
