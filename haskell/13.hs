main = do
    contents <- readFile "../inputs/13.in"
    let nums = map read $ lines contents :: [Integer]
    print . (take 10) . show $ foldl (+) 0 nums
