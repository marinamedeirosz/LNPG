import Text.Printf

cbrt :: Double -> Double
cbrt x = x ** (1/3)

serieCalc :: Int -> Double -> Bool -> Int -> Double
serieCalc terms sum operator count
    | terms <= 0    = sum
    | otherwise = serieCalc (terms-1) sum2 operator2 count2
    where
        term = if operator then 1/fromIntegral(count^3) else -(1/fromIntegral(count^3))
        sum2 = sum + term
        count2 = count + 2
        operator2 = not operator

piFormula :: Double -> Double
piFormula sum = cbrt (sum*32)


main::IO()
main = do 
    putStrLn "Digite a quantidade de termos: "
    input1 <- getLine
    let terms = read input1 :: Int
    let totalSum = serieCalc terms 0 True 1
    let pi = piFormula totalSum
    printf "Valor de pi: %.5f" pi