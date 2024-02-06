module Main where

whileLoop :: (a -> Bool) -> (a -> a) -> a -> a
whileLoop condition action value =
    if condition value
        then whileLoop condition action (action value)
        else value

isPrime :: Integer -> Bool
isPrime x = 
  let count = 1
  in whileLoop (> 1) (\y -> y - 1) (x - 1)
  where
    whileLoop condition action value =
            if condition value
                then let count = value in
                    if x `mod` count == 0 then False else whileLoop condition action (action value)
                else True

main :: IO ()
main = do 
  putStrLn "Digite um numero:"
  input <- getLine
  let number = read input :: Integer
  putStrLn $ if isPrime number then "Primo!" else "Nao primo!"