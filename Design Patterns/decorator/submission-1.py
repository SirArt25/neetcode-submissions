class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return self.decoratedCoffee.getCost()

class MilkDecorator(CoffeeDecorator):
    def __init__(self, decoratedCoffee):
        super().__init__(decoratedCoffee)
    
    def getCost(self):
        return super().getCost() + 0.5

    # Implement the Milk decorator

class SugarDecorator(CoffeeDecorator):
    def __init__(self, decoratedCoffee):
        super().__init__(decoratedCoffee)
    
    def getCost(self):
        return super().getCost() + 0.2

class CreamDecorator(CoffeeDecorator):
    def __init__(self, decoratedCoffee):
        super().__init__(decoratedCoffee)
    
    def getCost(self):
        return super().getCost() + 0.7

