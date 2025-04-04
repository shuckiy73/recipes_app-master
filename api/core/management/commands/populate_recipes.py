from django.core.management.base import BaseCommand
from core.models import Recipe


class Command(BaseCommand):
    help = 'Populates the database with sample recipes'

    def handle(self, *args, **kwargs):
        recipes = [
            {
                "title": "Паста с томатным соусом",
                "ingredients": "Паста, томаты, чеснок, оливковое масло, базилик",
                "instructions": "Сварите пасту. Обжарьте чеснок, добавьте томаты и базилик. Смешайте с пастой.",
                "description": "Простое и вкусное блюдо.",
                "category": "Основное блюдо"
            },
            {
                "title": "Омлет",
                "ingredients": "Яйца, молоко, соль, перец, зелень",
                "instructions": "Взбейте яйца с молоком, посолите и поперчите. Обжарьте на сковороде.",
                "description": "Легкий завтрак.",
                "category": "Завтрак"
            },
            {
                "title": "Салат Цезарь",
                "ingredients": "Салат, курица, пармезан, гренки, соус Цезарь",
                "instructions": "Смешайте все ингредиенты и подавайте.",
                "description": "Классический салат.",
                "category": "Салат"
            },
            {
                "title": "Шоколадный торт",
                "ingredients": "Мука, сахар, яйца, какао, разрыхлитель",
                "instructions": "Смешайте все ингредиенты, выпекайте в духовке.",
                "description": "Вкусный десерт.",
                "category": "Десерт"
            },
            {
                "title": "Борщ",
                "ingredients": "Свекла, капуста, картофель, морковь, лук, мясо, специи",
                "instructions": "Отварите мясо, добавьте овощи и специи, варите до готовности.",
                "description": "Традиционный украинский суп.",
                "category": "Суп"
            },
            {
                "title": "Панкейки",
                "ingredients": "Мука, молоко, яйца, сахар, разрыхлитель",
                "instructions": "Смешайте все ингредиенты, жарьте на сковороде до золотистой корочки.",
                "description": "Вкусные и легкие блины.",
                "category": "Завтрак"
            },
            {
                "title": "Курица с лимоном",
                "ingredients": "Курица, лимон, чеснок, оливковое масло, специи",
                "instructions": "Замаринуйте курицу с лимоном и специями, запекайте в духовке.",
                "description": "Ароматное и сочное блюдо.",
                "category": "Основное блюдо"
            },
            {
                "title": "Ризотто с грибами",
                "ingredients": "Рис, грибы, лук, бульон, пармезан",
                "instructions": "Обжарьте лук и грибы, добавьте рис, постепенно вливайте бульон.",
                "description": "Кремовое итальянское блюдо.",
                "category": "Основное блюдо"
            },
            {
                "title": "Тушеная говядина",
                "ingredients": "Говядина, морковь, лук, специи, бульон",
                "instructions": "Обжарьте мясо, добавьте овощи и бульон, тушите до готовности.",
                "description": "Сытное и вкусное блюдо.",
                "category": "Основное блюдо"
            },
            {
                "title": "Капрезе",
                "ingredients": "Моцарелла, помидоры, базилик, оливковое масло",
                "instructions": "Сложите ингредиенты слоями, полейте оливковым маслом.",
                "description": "Свежий итальянский салат.",
                "category": "Салат"
            },
            {
                "title": "Фахитас",
                "ingredients": "Курица, перец, лук, специи, тортильи",
                "instructions": "Обжарьте курицу с овощами, подавайте с тортильями.",
                "description": "Мексиканское блюдо.",
                "category": "Основное блюдо"
            },
            {
                "title": "Суп-пюре из тыквы",
                "ingredients": "Тыква, лук, бульон, сливки, специи",
                "instructions": "Отварите тыкву и лук, затем пюрируйте и добавьте сливки.",
                "description": "Нежный и ароматный суп.",
                "category": "Суп"
            },
            {
                "title": "Котлеты по-киевски",
                "ingredients": "Куриное филе, масло, панировочные сухари, специи",
                "instructions": "Заверните масло в куриное филе, обваляйте в сухарях и обжарьте.",
                "description": "Классическое украинское блюдо.",
                "category": "Основное блюдо"
            },
            {
                "title": "Пирог с яблоками",
                "ingredients": "Яблоки, тесто, сахар, корица",
                "instructions": "Уложите яблоки в тесто, посыпьте сахаром и корицей, выпекайте.",
                "description": "Вкусный десерт.",
                "category": "Десерт"
            },
            {
                "title": "Лазанья",
                "ingredients": "Листы лазаньи, мясной фарш, томатный соус, сыр",
                "instructions": "Сложите слои лазаньи, фарша и соуса, запекайте в духовке.",
                "description": "Итальянское блюдо с мясом.",
                "category": "Основное блюдо"
            },
            {
                "title": "Салат Оливье",
                "ingredients": "Картофель, морковь, яйца, колбаса, горошек, майонез",
                "instructions": "Отварите все ингредиенты, нарежьте и смешайте с майонезом.",
                "description": "Традиционный русский салат.",
                "category": "Салат"
            },
            {
                "title": "Крем-брюле",
                "ingredients": "Сливки, сахар, яйца, ваниль",
                "instructions": "Смешайте ингредиенты, запекайте и карамелизируйте сахар.",
                "description": "Французский десерт.",
                "category": "Десерт"
            },
            {
                "title": "Пицца Маргарита",
                "ingredients": "Тесто, томатный соус, моцарелла, базилик",
                "instructions": "Соберите пиццу и выпекайте в духовке.",
                "description": "Классическая итальянская пицца.",
                "category": "Основное блюдо"
            },
            {
                "title": "Блины",
                "ingredients": "Мука, молоко, яйца, сахар, соль",
                "instructions": "Смешайте ингредиенты, жарьте на сковороде.",
                "description": "Традиционные русские блины.",
                "category": "Завтрак"
            },
            {
                "title": "Куриный суп",
                "ingredients": "Курица, морковь, картофель, лук, специи",
                "instructions": "Отварите курицу с овощами до готовности.",
                "description": "Сытный и ароматный суп.",
                "category": "Суп"
            },
            {
                "title": "Творожная запеканка",
                "ingredients": "Творог, яйца, сахар, манка, изюм",
                "instructions": "Смешайте все ингредиенты, запекайте в духовке.",
                "description": "Вкусный десерт.",
                "category": "Десерт"
            },
            {
                "title": "Гречка с грибами",
                "ingredients": "Гречка, грибы, лук, специи",
                "instructions": "Обжарьте грибы и лук, добавьте гречку и воду, варите до готовности.",
                "description": "Полезное и сытное блюдо.",
                "category": "Основное блюдо"
            },
            {
                "title": "Кабачковые оладьи",
                "ingredients": "Кабачки, яйца, мука, специи",
                "instructions": "Натрите кабачки, смешайте с остальными ингредиентами и жарьте.",
                "description": "Легкие и вкусные оладьи.",
                "category": "Закуска"
            },
            {
                "title": "Чизкейк",
                "ingredients": "Творог, сахар, яйца, печенье, масло",
                "instructions": "Смешайте все ингредиенты, запекайте в форме.",
                "description": "Нежный десерт.",
                "category": "Десерт"
            },

        ]

        for recipe_data in recipes:
            Recipe.objects.create(
                title=recipe_data["title"],
                ingredients=recipe_data["ingredients"],
                instructions=recipe_data["instructions"],
                description=recipe_data["description"],
                category=recipe_data["category"]
            )

            self.stdout.write(self.style.SUCCESS('Successfully populated recipes'))
