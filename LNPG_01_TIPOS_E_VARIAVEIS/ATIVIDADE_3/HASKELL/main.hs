module Main where


cToF :: Float -> Float
cToF c = c * 1.8 + 32

main = do 
  putStrLn "Digite a temperatura em celsius: "
  input <- getLine
  let temp = read input :: Float
  putStrLn ("A temperatura em farenheit e " ++ show (cToF temp))