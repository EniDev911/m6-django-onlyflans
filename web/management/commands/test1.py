from django.core.management.base import BaseCommand
# from models import Product as p

class Command(BaseCommand):
    help = "Descripción de tu comando y opciones de configuración"


    def add_arguments(self, parser):
        parser.add_argument("create", nargs="+", type=str)
        # Named (optional) arguments
        parser.add_argument(
            "--delete",
            action="store_true",
            help="Delete poll instead of closing it",
        )
    def handle(self, *args, **options):
        print(options)
        # p.objects.create(name="test1", price=12.03, stock=10)
        self.stdout.write("Éxito, corriendo", self.style.SUCCESS)
