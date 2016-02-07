fact :: Integer -> Integer
fact n = product [1..n]

digits :: Integer -> [Integer]
digits n = map (read . return) $ show n

main = do
    print . sum . digits . fact $ 100
