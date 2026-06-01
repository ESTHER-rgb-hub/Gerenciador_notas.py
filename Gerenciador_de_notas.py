# Estrutura base para armazenar estudantes.
# Cada estudante será representado por um dicionário.
estudantes = [
        {"nome": "Ana", "notas": [8.0, 7.5, 8.0]},
        {"nome": "Bruno", "notas": [6.0, 5.5, 7.0]},
        {"nome": "Gabriela", "notas": [9.0, 8.5, 8.0]}
  ]

def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.
    Args:
            notas (list[float]): Lista contendo valores numéricos (int ou float)
                                         representando as notas de um estudante.
    Returns:
            float: Valor da média aritmética das notas fornecidas.
    Raises:
            ValueError: Se a lista de notas estiver vazia.
            TypeError: Se algum elemento da lista não for numérico.
    """
    if not notas:
        raise ValueError("A lista de notas não pode ser vazia")
    if not all(isinstance(n, (int, float)) for n in notas):
        raise TypeError("Todas as notas devem ser números")
    return sum(notas) / len(notas)

def verificar_aprovacao(media, media_minima=6.0):
    """
    Verifica se a média atinge o limite mínimo de aprovação.

    Args:
            media (float): Média calculada das notas do estudante.
            media_minima (float, opcional): Valor mínimo exigido para aprovação.
                                                                O padrão é 6.0.

    Returns:
            str: "Aprovado" se a média for maior ou igual ao limite,
                   "Reprovado" caso contrário.

    Raises:
            TypeError: Se os valores de média ou média_minima não forem numéricos.
    """
    if not isinstance(media, (int, float)):
        raise TypeError("A média deve ser um número")
    if not isinstance(media_minima, (int, float)):
        raise TypeError("A média minima deve ser um número")
    return "Aprovado" if media >= media_minima else "Reprovado"

def gerar_relatorio(alunos):
    """Gera relatório com nome, média e situação de aprovação."""
    print("=== Relatório de Desempenho ===")
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        status = verificar_aprovacao(media)
        print(f"Estudante: {aluno['nome']} | Média: {media:.2f} | Status: {status}")
        
# Executando o relatório
gerar_relatorio(estudantes)
                      
