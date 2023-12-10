import unittest
from RK2.main import *


class TestComponent(unittest.TestCase):
    def test_component_init(self):
        component = Component(1, "shock absorber", 5871, 1)
        self.assertEqual(component.id, 1)
        self.assertEqual(component.name, "shock absorber")
        self.assertEqual(component.price, 5871)
        self.assertEqual(component.fabric_id, 1)


class TestFabric(unittest.TestCase):
    def test_fabric_init(self):
        fabric = Fabric(1, "АВТОВАЗ")
        self.assertEqual(fabric.id, 1)
        self.assertEqual(fabric.name, "АВТОВАЗ")


class TestFabricComponent(unittest.TestCase):
    def test_fabric_component_init(self):
        fc = FabricComponent(1, 2)
        self.assertEqual(fc.fabric_id, 1)
        self.assertEqual(fc.component_id, 2)


class TestRequest(unittest.TestCase):
    def setUp(self) -> None:
        self._components = components_data_test()
        self._fabrics = fabrics_data_test()
        self._fabrics_components = fabrics_components_data_test()

    def test_request1(self):
        expected_result = [
            ("Тормозные колодки", "АВТОВАЗ"),
            ("Тормозные диски", "УВЗ")
        ]
        actual_result = request1(self._components, self._fabrics)
        self.assertEqual(actual_result, expected_result)

    def test_request2(self):
        expected_result = [
            ("УВЗ", 3000),
            ("АВТОВАЗ", 5000),
            ("КАМАЗ", 8000),
            ("УАЗ", 10000)
        ]
        actual_result = request2(self._components, self._fabrics)
        self.assertEqual(actual_result, expected_result)

    def test_request3(self):
        expected_result = [
            ("АВТОВАЗ", "Фары"),
            ("АВТОВАЗ", "Тормозные колодки"),
            ("КАМАЗ", "Аккумулятор"),
            ("КАМАЗ", "Генератор"),
            ("УАЗ", "Заднее крыло"),
            ("УВЗ", "Дворники"),
            ("УВЗ", "Тормозные диски"),
        ]
        actual_result = request3(self._components, self._fabrics, self._fabrics_components)
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
