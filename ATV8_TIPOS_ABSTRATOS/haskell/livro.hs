newtype Livro = Livro (String, String, Int, Int)

inicializar :: String -> String -> Int -> Int -> Livro
inicializar titulo autor ano copias = Livro (titulo autor ano copias)

emprestaCopia :: Livro -> Livro
emprestaCopia (Livro titulo autor ano copias) = Livro (titulo autor ano (copias - 1))

devolveCopia :: Livro -> Livro
devolveCopia (Livro (titulo autor ano copias)) = (Livro titulo autor ano (copias + 1))

verificaCopia :: Livro -> Int
devolveCopia (Livro (_, _, _, copias)) = copias

getLivro :: Livro -> String
getLivro (Livro (titulo, autor, ano, _)) = "Título: " ++ titulo ++ ", Autor: " ++ autor ++ ", Ano: " ++ show ano
