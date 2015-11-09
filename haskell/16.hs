digits :: Integral a => a -> [a]
digits 0 = []
digits x = let (q, r) = divMod x 10 in r : (digits q)

main :: IO ()
main = putStrLn $ show $ sum $ digits $ 2^1000
