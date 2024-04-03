data Empregado = Empregado String Int String Double Departamento

inicializarEmpregado :: String -> Int -> String -> Double -> Departamento -> Empregado
inicializarEmpregado nome id cargo salario departamento = Empregado nome id cargo salario departamento

atualizarNome :: Empregado -> String -> Empregado
atualizarNome (Empregado nome id cargo salario departamento) novoNome = Empregado novoNome id cargo salario departamento

atualizarId :: Empregado -> Int -> Empregado
atualizarId (Empregado nome id cargo salario departamento) novoId = Empregado nome novoId cargo salario departamento

atualizarSalario :: Empregado -> Double -> Empregado
atualizarSalario (Empregado nome id cargo salario departamento) novoSalario = Empregado nome id cargo novoSalario departamento

atualizarCargo :: Empregado -> String -> Empregado
atualizarCargo (Empregado nome id cargo salario departamento) novoCargo = Empregado nome id novoCargo salario departamento

atualizarDepartamento :: Empregado -> Departamento -> Empregado
atualizarDepartamento (Empregado nome id cargo salario _) novoDepartamento = Empregado nome id cargo salario novoDepartamento

transferirEmpregado :: Empregado -> Departamento -> Empregado
-- Define the transfer function based on your requirements

data Departamento = Departamento String Int String [Empregado]

inicializarDepartamento :: String -> Int -> String -> [Empregado] -> Departamento
inicializarDepartamento nome id localizacao empregados = Departamento nome id localizacao empregados

addEmpregado :: Empregado -> Departamento -> Departamento
addEmpregado empregado (Departamento nome id localizacao empregados) = Departamento nome id localizacao (empregado : empregados)

removeEmpregado :: Empregado -> Departamento -> Departamento
removeEmpregado empregado (Departamento nome id localizacao empregados) = Departamento nome id localizacao (filter (/= empregado) empregados)

getEmpregados :: Departamento -> [Empregado]
getEmpregados (Departamento _ _ _ empregados) = empregados

