from typing import Union, NoReturn


class Component:
    """Класс Деталь"""

    def __init__(self, id: int, name: str, price: Union[int, float], fabric_id: int):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__fabric_id = fabric_id

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> Union[int, float]:
        return self.__price

    @property
    def fabric_id(self) -> int:
        return self.__fabric_id


class Fabric:
    """Класс Производитель"""

    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name


class FabricComponent:
    """Класс детали производителя"""

    def __init__(self, fabric_id: int, component_id: int):
        self.__fabric_id = fabric_id
        self.__component_id = component_id

    @property
    def fabric_id(self) -> int:
        return self.__fabric_id

    @property
    def component_id(self) -> int:
        return self.__component_id


def request1(components: list[Component], fabrics: list[Fabric]) -> list[tuple[str, str]]:
    response = [
        (c, f)
        for c in components
        for f in fabrics
        if c.fabric_id == f.id and c.name.startswith("Тормоз")
    ]
    return [(c.name, f.name) for c, f in response]


def request2(components: list[Component], fabrics: list[Fabric]) -> list[tuple[str, int]]:
    response = {}
    for fabric in fabrics:
        minimal_price = min([c.price for c in components if c.fabric_id == fabric.id])
        response[fabric.name] = minimal_price

    response_items = list(response.items())
    response_items.sort(key=lambda item: item[1])

    return response_items


def request3(components: list[Component], fabrics: list[Fabric], fabric_components: list[FabricComponent]) -> list[tuple[str, str]]:
    response = [
        (f, c)
        for fc in fabric_components
        for f in fabrics
        for c in components
        if fc.fabric_id == f.id and fc.component_id == c.id
    ]

    response.sort(key=lambda item: (item[0].name, item[1].price))
    return [(fabric.name, component.name) for fabric, component in response]


def components_data_test() -> list[Component]:
    return [
        Component(1, "Тормозные колодки", 12000, 1),
        Component(2, "Фары", 5000, 1),
        Component(3, "Заднее крыло", 10000, 2),
        Component(4, "Генератор", 15000, 3),
        Component(5, "Аккумулятор", 8000, 3),
        Component(6, "Тормозные диски", 9000, 4),
        Component(7, "Дворники", 3000, 4)
    ]


def fabrics_data_test() -> list[Fabric]:
    return [
        Fabric(1, "АВТОВАЗ"),
        Fabric(2, "УАЗ"),
        Fabric(3, "КАМАЗ"),
        Fabric(4, "УВЗ"),
    ]


def fabrics_components_data_test() -> list[FabricComponent]:
    return [
        FabricComponent(1, 1),
        FabricComponent(1, 2),
        FabricComponent(2, 3),
        FabricComponent(3, 4),
        FabricComponent(3, 5),
        FabricComponent(4, 6),
        FabricComponent(4, 7)
    ]


def main() -> NoReturn:
    components = components_data_test()
    fabrics = fabrics_data_test()
    fabrics_components = fabrics_components_data_test()

    response1 = request1(components, fabrics)
    response2 = request2(components, fabrics)
    response3 = request3(components, fabrics, fabrics_components)

    print('Запрос №1. Список деталей, которые начинаются с "Тормоз", и их производителей.')
    for (component_name, fabric_name) in response1:
        print(f"    Деталь: {component_name} | Производитель: {fabric_name}")
    print()

    print("Запрос №2. Список производителей с минимальной стоимостью деталей.")
    for (fabric_name, minimal_price) in response2:
        print(f"    Производитель: {fabric_name} | Минимальная стоимость детали: {minimal_price}")
    print()

    print(
        "Запрос №3. Список всех связанных деталей и производителей, отсортированный по производителям. Сортировка деталей по цене."
    )
    for (fabric_name, component_name) in response3:
        print(f"    Производитель: {fabric_name} | Деталь: {component_name}")
    print()


if __name__ == "__main__":
    main()
