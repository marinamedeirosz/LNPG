main::IO()
main = do 
    putStrLn "Digite a nota 1: "
    input1 <- getLine
    let n1 = read input1 :: Float
    putStrLn "Digite o peso 1: "
    input2 <- getLine
    let p1 = read input2 :: Float

    putStrLn "Digite a nota 2: "
    input3 <- getLine
    let n2 = read input3 :: Float
    putStrLn "Digite o peso 2: "
    input4 <- getLine
    let p2 = read input4 :: Float

    putStrLn "Digite a nota 3: "
    input5 <- getLine
    let n3 = read input5 :: Float
    putStrLn "Digite o peso 3: "
    input6 <- getLine
    let p3 = read input6 :: Float

    let media = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
    putStrLn ("Media: " ++ show (media))