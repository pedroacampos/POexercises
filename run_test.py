import pathlib
import unittest

import run

example_path = pathlib.Path().absolute().joinpath("example")


class RunTestCase(unittest.TestCase):

    def test_something(self):
        po = run.PO(example_path)
        cpf = "11122233344"
        name, data = po.by_cpf(cpf)
        self.assertEqual(name, "123 de Oliveira 4")

        max_profit = po.max_profit(cpf)
        self.assertEqual(max_profit, 90.73)


if __name__ == '__main__':
    unittest.main()
