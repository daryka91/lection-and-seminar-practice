class BasePokemon:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def to_str(self):
        return f'{self.name}/{self.category}'


# class Pokemon(BasePokemon):
#     def __init__(self, name, category, weaknesses: list):
#         super().__init__(name, category)
#         self.weaknesses = weaknesses


ICON = {
    'grass' : '🌿',
    # fire => 🔥
    # water => 🌊
    'electric': '⚡'
}
class EmojiMixin:
    ICON = {
        'grass': '🌿',
        # fire => 🔥
        # water => 🌊
        'electric': '⚡'
    }

    def __str__(self):
        text: str = super().__str__()
        for cat, emoji in self.ICON.items():
            replaced = text.replace(cat, emoji)
            if replaced != text:
                return replaced
        return text

class Pokemon(EmojiMixin, BasePokemon):
    pass

# Pokemon(name='Bulbasaur', poketype='grass')
# print(bulbasaur)
# Out: 'Bulbasaur/grass'
# charmander = Pokemon(name='Charmander', category='Lizard')
# charmander.to_str()
if __name__ == '__main__':
    # charmander = Pokemon(
    #     name='Charmander',
    #     category='Lizard',
    #     weaknesses=['water', 'ground', 'rock']
    # )
    # print(charmander.__dict__)
    # print(charmander.to_str())
        bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
        print(bulbasaur)





# Миксины
#решают проблемы вынесения в отдельный класс какой-либо логики, которая работает только в паре с другими классами,
# т.е. объект этого класса не создаются отдельно, и он указывается первым при наследовании
#просто класс, самостоятельно не используется, название заканчивается на Mixin, частично изменяет поведение класса
# самый левый при наследовании, чтобы сначала вызвался он со своей логикой

# магические методы испльзуются питоном под капотом, двойное подчеркивание-метод-подчеркивание
# __repr__-представление для разработчиков, __str__-для пользователей, обычно так
# есть магические методы для сравнения

pikachu = Pokemon(name='Pikachu', category='electric')
print(pikachu)
Out: 'Pikachu/⚡'
grass => 🌿
fire => 🔥
water => 🌊
electric => ⚡
