"""Сценарий тестирования для проверки функциональности allure.id."""

import vedro
import allure
from vedro_allure_reporter import allure_labels

# Пример 1: Корректный сценарий с декоратором @allure.id()
@allure.id("TEST-123")
@allure_labels(feature="Test Feature", story="Test Story")
class CorrectScenario(vedro.Scenario):
    subject = 'Пример корректного сценария с декоратором @allure.id()'
    
    def given_something(self):
        pass
        
    def when_something_happens(self):
        pass
        
    def then_check_result(self):
        pass


# Пример 2: Исправленный сценарий с декоратором @allure.id()
@allure.id("TEST-456")
@allure_labels(feature="Test Feature", story="Test Story")
class IncorrectScenario(vedro.Scenario):
    subject = 'Теперь этот сценарий правильный с декоратором @allure.id()'
    
    def given_something(self):
        pass
        
    def when_something_happens(self):
        pass
        
    def then_check_result(self):
        pass


class Scenario:
    """Базовый класс сценария."""
    
    def __init__(self, *args, **kwargs):
        pass


@allure.feature("Test Feature")
@allure.description("Test description for scenario")
@allure.id(12345)
class TestScenario(Scenario):
    """Тестовый сценарий."""
    
    def when_some_action(self):
        """Выполнение действия."""
        return True
    
    def then_check_results(self):
        """Проверка результатов действия."""
        assert self.when_some_action() is True, "Действие должно вернуть True"
    
    def and_additional_check(self):
        """Дополнительная проверка."""
        assert 1 + 1 == 2 