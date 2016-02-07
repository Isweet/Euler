import System.Environment (getArgs)

import Data.List
import Data.Ord

collatz :: Integral a => a -> a
collatz 1 = 4
collatz n | n > 1 = 
    if n `mod` 2 == 0 then 
        n `quot` 2 
    else 
        3 * n + 1

collatzLength :: Integral a => a -> Integer
collatzLength idx = (+ 1) $ fromIntegral . length $ takeWhile (/= 1) $ iterate collatz idx

main = do
    args <- getArgs
    let candidates = [1..999999]
    print $ fst . maximumBy (comparing snd) $ zip candidates $ map collatzLength candidates
    
    {-
     -(putStrLn . show . maximum . map ((+) 1 . length)) [takeWhile (/= 1) $ iterate collatz x | x <- [1..(read . head $ args)]]
     -}
