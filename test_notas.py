import unittest
from cadastro_de_estudantes import calcular_media, verificar_aprovacao

class TestNotas(unittest.TestCase):

    def test_aprovacao_normal(self):
        """Testa aprovação e reprovação em condições normais."""
        notas_aprovado = [8.0, 7.5, 9.0]
        notas_reprovado = [5.0, 6.0, 5.5]

        media_aprovado = calcular_media(notas_aprovado)
        media_reprovado = calcular_media(notas_reprovado)

        self.assertEqual(verificar_aprovacao(media_aprovado), "Aprovado")
        self.assertEqual(verificar_aprovacao(media_reprovado), "Reprovado")

    def test_lista_vazia(self):
        """Testa comportamento com lista de notas vazia (edge case)."""
        with self.assertRaises(ValueError):
            calcular_media([])

    def test_media_minima_zero(self):
        """Testa estabilidade quando média mínima é zero."""
        notas = [0.0, 0.0, 0.0]
        media = calcular_media(notas)

        # Qualquer média >= 0 deve ser considerado aprovado
        self.assertEqual(verificar_aprovacao(media, media_minima=0), "Aprovado")

if __name__ == "__main__":
    unittest.main()
