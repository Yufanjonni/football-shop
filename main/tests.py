from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/random_ahh_ page/')
        self.assertEqual(response.status_code, 404)

    def test_product_creation(self):
        product = Product.objects.create(
            name = "Rumput sintetis",
            price = 36000,
            description = "Hijau, Kuat, dan Tahan lama",
            category = "aksesoris",
            is_featured = True,
            stock = 666,
            rating = 4.1,
            brand = "PT Cinta sejaya"
        )
        self.assertEqual(product.rating, 4.1)
        self.assertEqual(product.category, "aksesoris")
        self.assertTrue(product.is_featured)
    def test_product_default_values(self):
        product = Product.objects.create(
            name = "Test Product",
            description = "test description",
            brand = "test brand"

        )
        self.assertEqual(product.category, "aksesoris")
        self.assertEqual(product.stock, 0)
        self.assertEqual(product.price, 0)
        self.assertEqual(product.rating, 0.0)
        self.assertFalse(product.is_featured)

    def test_add_sticker(self):
        product = Product.objects.create(
            name = "Test Product",
            description = "test description",
            brand = "test brand"

        )
        initial_stock = product.stock
        product.add_stock(20)
        self.assertEqual(product.stock, initial_stock + 20)

    def test_set_price(self):
        product = Product.objects.create(
            name = "Test Product",
            description = "test description",
            brand = "test brand"

        )
        product.set_price(2000)
        self.assertEqual(product.price, 2000)

# Create your tests here.
