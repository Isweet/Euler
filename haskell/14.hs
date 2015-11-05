import System.Environment (getArgs)

collatz :: Integral a => a -> a
collatz 1 = 4
collatz n | n > 1 = 
    if n `mod` 2 == 0 then 
        n `quot` 2 
    else 
        3 * n + 1

main = do
    args <- getArgs
    (putStrLn . show . maximum . map ((+) 1 . length)) [takeWhile (/= 1) $ iterate collatz x | x <- [1..(read . head $ args)]]
