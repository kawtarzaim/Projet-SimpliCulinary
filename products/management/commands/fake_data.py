from django.core.management.base import BaseCommand
from products.models import Category, Product
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Genere les donnees fictives pour les produits'

    def handle(self, *args, **options):
        faker=Faker('fr_FR')

        # Create categories
        categories = []
        for _ in range(5):
            name=faker.word().capitalize()
            slug=faker.slug(name)
            categorie=Category.objects.create(name=name, slug=slug)
            categories.append(categorie)
            self.stdout.write(f'categorie cree avec succes:{name}')

        # Create products
        for i in range(8):
            Product.objects.create(name=faker.sentence(nb_words=4).replace('.',''),
                                   description=faker.text(max_nb_chars=450),
                                   price=faker.random_number(digits=4),
                                   stock=faker.random_int(0, 100),
                                   category=random.choice(categories)
                                   )

        self.stdout.write(f'Produit {i+1} cree avec succes')