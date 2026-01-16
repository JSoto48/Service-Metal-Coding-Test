from django.core.management.base import BaseCommand
from products.models import Product, ProductImage, ProductSpecs


class Command(BaseCommand):
    help = 'Seed database with sample products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding products...')
        
        # Clear existing data
        Product.objects.all().delete()
        
        # Example product 1: Gate Valve (from the example URL)
        gate_valve = Product.objects.create(
            name='2" PVC Socket Gate Valve - Spears 2022-020',
            sku='2022-020',
            description='Made off heavy bodied PVC & CPVC Construction. EPDM Gate Valves NSF certified for potable water use. Suitable for Vacuum Service. Assembled with silicone-free, water soluble lubricants.',
            main_category='Valves',
            subcategory='Gate Valves',
            price=153.04,
            stock_quantity=25,
        )
        
        # Add images for gate valve
        ProductImage.objects.create(
            product=gate_valve,
            image_url='https://www.pvcfittingsonline.com/cdn/shop/files/spearsthreadedvalve_5.jpg?v=1747959277&width=1500',
            alt_text='2 inch PVC gate valve front view',
            is_primary=True,
            display_order=0
        )
        
        # Add specifications for gate valve
        specs_gate = [
            ('Material', 'PVC'),
            ('O-rings', 'EPDM'),
            ('End Type', 'Socket'),
            ('Max Pressure', '200 PSI @ 73°F'),
            ('Standards', 'NSF certified for potable water use'),
        ]
        for spec_name, spec_value in specs_gate:
            ProductSpecs.objects.create(
                product=gate_valve,
                spec_name=spec_name,
                spec_value=spec_value
            )
        
        # Example product 2: Ball Valve
        # ball_valve = Product.objects.create(
        #     name='1-1/2" PVC True Union Ball Valve',
        #     sku='BV-150-TU',
        #     brand='GF Piping Systems',
        #     main_category='Valves',
        #     subcategory='Ball Valves',
        #     price=67.89,
        #     stock_quantity=15,
        #     description='True union ball valve with full port design for maximum flow.'
        # )
        
        # ProductImage.objects.create(
        #     product=ball_valve,
        #     image_url='https://example.com/ball-valve.jpg',
        #     alt_text='1.5 inch ball valve',
        #     is_primary=True,
        #     display_order=0
        # )
        
        # specs_ball = [
        #     ('Size', '1-1/2 inch'),
        #     ('Material', 'PVC'),
        #     ('Port Type', 'Full Port'),
        #     ('Max Pressure', '150 PSI'),
        #     ('Handle Type', 'Lever'),
        # ]
        # for spec_name, spec_value in specs_ball:
        #     ProductSpecs.objects.create(
        #         product=ball_valve,
        #         spec_name=spec_name,
        #         spec_value=spec_value
        #     )
        
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {Product.objects.count()} products'))

