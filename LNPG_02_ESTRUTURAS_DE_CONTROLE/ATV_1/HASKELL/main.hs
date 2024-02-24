first :: (a, b, c, d, e) -> a
first (f, _, _, _, _) = f

second :: (a, b, c, d, e) -> b
second (_, s, _, _, _) = s

third :: (a, b, c, d, e) -> c
third (_, _, t, _, _) = t

fourth :: (a, b, c, d, e) -> d
fourth (_, _, _, f, _) = f

fifth :: (a, b, c, d, e) -> e
fifth (_, _, _, _, f) = f

checkRG :: String -> Bool
checkRG rg = rg == "RG"

checkTicket :: String -> Bool
checkTicket ticket = ticket == "Passagem"

checkBirthDate :: String -> String -> Bool
checkBirthDate rgDate ticketDate = rgDate == ticketDate

getPassengersData :: IO (String, String, String, String, String)
getPassengersData = do
  putStrLn "RG? (Se sim, RG; Se não, Nao possui): "
  rg <- getLine
  putStrLn "Data de nascimento no RG (DD/MM/AAAA): "
  rgDate <- getLine
  putStrLn "Passagem? (Se sim, Passagem; Se não, Nao possui): "
  ticket <- getLine
  putStrLn "Data de nascimento na passagem (DD/MM/AAAA): "
  ticketDate <- getLine
  putStrLn "Assento (A12): "
  seat <- getLine
  return (rg, rgDate, ticket, ticketDate, seat)

passengersDecrement :: Int -> IO ()
passengersDecrement p
  | p <= 0    = putStrLn ""
  | otherwise = do
      userData <- getPassengersData
      if not (checkRG (first userData))
        then putStrLn "A saida e nessa direcao"
      else if not (checkTicket (third userData))
        then putStrLn "A recepcao e nessa direcao"
      else if not (checkBirthDate (second userData) (fourth userData))
        then putStrLn "190"
      else putStrLn ("Seu assento e " ++ show(fifth userData))
      passengersDecrement (p - 1)


main::IO()
main = do 
  putStrLn "Quantidade de passageiros: "
  input1 <- getLine
  let passengers = read input1 :: Int
  passengersDecrement passengers