class BasePokemon:
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __str__(self):
        return f'{self.name}/{self.category}'


class EmojiMixin:
    ICON = {
        'grass': '🌿',
        'electric': '⚡',
        'water': '🌊',
        'fire': '🔥'
    }

    def __str__(self):
        for cat, emoji in self.ICON.items():
            replased = self.category.replace(cat, emoji)
            if replased != self.category:
                return f'{self.name}/{replased}'
        return f'{self.name}/{self.category}'


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Pikachu', category='electric')
    print(bulbasaur)





# Миксины
#решают проблемы вынесения в отдельный класс какой-либо логики, которая работает только в паре с другими классами,
# т.е. объект этого класса не создаются отдельно, и он указывается первым при наследовании
#просто класс, самостоятельно не используется, название заканчивается на Mixin, частично изменяет поведение класса
# самый левый при наследовании, чтобы сначала вызвался он со своей логикой

# магические методы испльзуются питоном под капотом, двойное подчеркивание-метод-подчеркивание
# __repr__-представление для разработчиков, __str__-для пользователей, обычно так
# есть магические методы для сравнения

