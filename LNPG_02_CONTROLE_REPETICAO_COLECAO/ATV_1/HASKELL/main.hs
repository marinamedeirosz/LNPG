checkRG :: String -> Bool
checkRG rg = rg == "RG"

checkTicket :: String -> Bool
checkTicket ticket = ticket == "Passagem"

checkBirthDate :: String -> String -> Bool
checkBirthDate rgDate ticketDate = rgDate == ticketDate

getPassengersData :: IO ([String])
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
	return [rg, rgDate, ticket, ticketDate, seat]

-- for with recursion
passengersDecrement :: Int -> IO ()
passengersDecrement p
	| p <= 0    = putStrLn ""
	| otherwise = do
		userData <- getPassengersData
		if not (checkRG (userData!!0))
		then putStrLn "A saida e nessa direcao"
		else if not (checkTicket (userData!!2))
		then putStrLn "A recepcao e nessa direcao"
		else if not (checkBirthDate (userData!!1) (userData!!3))
		then putStrLn "190"
		else putStrLn ("Seu assento e " ++ show(userData!!4))
		passengersDecrement (p - 1)


main::IO()
main = do 
	putStrLn "Quantidade de passageiros: "
	input1 <- getLine
	let passengers = read input1 :: Int
	passengersDecrement passengers