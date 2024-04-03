newtype Peca = Peca (String String String)

inicializar :: String -> String -> String -> Peca
inicializar tipo cor posicao = Peca (tipo cor posicao)

moverPeca :: Peca -> String -> Peca
moverPeca (Peca (tipo cor posicao)) pos = Peca (tipo cor pos)

capturarPeca :: Peca -> Peca
capturarPeca (Peca (tipo cor posicao)) = Peca (tipo cor "0x0")

verificaPosicao :: String -> Boolean
verificaPosicao pos = length pos == 3

getPeca :: Peca -> String 
getPeca (Peca (tipo, cor, posicao)) = "Tipo: " ++ tipo ++ ", Cor: " ++ cor ++ ", Posição: " ++ posicao