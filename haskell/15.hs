fact :: Integer -> Integer
fact n = product [1..n]

main = do
    let gridsize = 20
    let num = (fact (2 * gridsize))
    let den = (fact gridsize) ^ 2
    print $ num `div` den
