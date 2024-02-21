soma :: Float -> Float -> Float
soma x y = x + y
sub :: Float -> Float -> Float
sub x y = x - y
mult :: Float -> Float -> Float
mult x y = x * y
divi :: Float -> Float -> Float
divi x y = x / y

main::IO()
main = do 
  putStrLn "Digite o primeiro numero: "
  input1 <- getLine
  let n1 = read input1 :: Float
  putStrLn "Digite o segundo numero: "
  input2 <- getLine
  let n2 = read input2 :: Float
  putStrLn ("A soma dos numeros e " ++ show (soma n1 n2))
  putStrLn ("A subtracao dos numeros e " ++ show (sub n1 n2))
  putStrLn ("A multiplicacao dos numeros e " ++ show (mult n1 n2))
  putStrLn ("A divisao dos numeros e " ++ show (divi n1 n2))