parOuImpar :: Integer -> Bool
parOuImpar = even

main::IO()
main = do 
  putStrLn "Digite um numero: "
  input1 <- getLine
  let n1 = read input1 :: Integer
  if parOuImpar n1 then putStrLn "Par"
  else putStrLn "Impar"