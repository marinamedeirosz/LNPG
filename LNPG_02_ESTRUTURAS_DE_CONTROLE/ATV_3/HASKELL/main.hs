main::IO()
main = do 
    putStrLn "Digite a quantidade de jogos vendidos: "
    input <- getLine
    let games = read input :: Double

    let gameValue = 19.9
    let totalProfit = gameValue*games
    let partSalary = totalProfit/2
    let totalSalary = fromIntegral (floor (games / 15)) * (totalProfit * 0.08) + partSalary
    putStrLn ("Total arrecadado: " ++ show (totalProfit))
    putStrLn ("Salario sem bonus: " ++ show (partSalary))
    putStrLn ("Com bonus: " ++ show (totalSalary))