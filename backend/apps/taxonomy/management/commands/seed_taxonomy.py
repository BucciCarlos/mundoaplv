from django.core.management.base import BaseCommand
from apps.taxonomy.models import Allergen, Allergy

class Command(BaseCommand):
    help = 'Pobla la base de datos con alérgenos y alergias iniciales según el Código Alimentario Argentino (Art. 156 tris)'

    def handle(self, *args, **options):
        # 1. Alérgeno: Leche de Vaca y Alergia: APLV
        leche_allergen, created_leche = Allergen.objects.update_or_create(
            name='Leche de Vaca',
            defaults={
                'description': 'Proteínas de la leche de vaca (caseína, suero, etc.). Principal alérgeno infantil.',
                'caa_hidden_names': 'Caseína, Caseinato de calcio, Caseinato de sodio, Suero de leche, Lactosuero, Sólidos lácteos, Grasa butírica, Lactoalbúmina, Fosfato de lactoalbúmina, Cuajo, Shrikhand'
            }
        )
        if created_leche:
            self.stdout.write(self.style.SUCCESS('Creado alérgeno: Leche de Vaca'))
        else:
            self.stdout.write(self.style.WARNING('Actualizado alérgeno: Leche de Vaca'))

        aplv_allergy, created_aplv = Allergy.objects.update_or_create(
            name='APLV (Alergia a la Proteína de la Leche de Vaca)',
            defaults={
                'description': 'Alergia alimentaria común en la infancia mediada o no por anticuerpos IgE.',
                'is_ige_mediated': False
            }
        )
        aplv_allergy.allergens.add(leche_allergen)
        if created_aplv:
            self.stdout.write(self.style.SUCCESS('Creada alergia: APLV y vinculada a Leche de Vaca'))

        # 2. Alérgeno: Huevo y Alergia: Alergia al Huevo
        huevo_allergen, created_huevo = Allergen.objects.update_or_create(
            name='Huevo',
            defaults={
                'description': 'Proteínas de clara (ovoalbúmina) y yema.',
                'caa_hidden_names': 'Albúmina, Ovalbúmina, Yema, Clara, Lisozima, Globulina, Conalbúmina, Avidina, Lecitina de huevo'
            }
        )
        if created_huevo:
            self.stdout.write(self.style.SUCCESS('Creado alérgeno: Huevo'))

        huevo_allergy, created_huevo_al = Allergy.objects.update_or_create(
            name='Alergia al Huevo',
            defaults={
                'description': 'Alergia a proteínas de la clara o yema del huevo.',
                'is_ige_mediated': True
            }
        )
        huevo_allergy.allergens.add(huevo_allergen)

        # 3. Alérgeno: Soja y Alergia: Alergia a la Soja
        soja_allergen, created_soja = Allergen.objects.update_or_create(
            name='Soja',
            defaults={
                'description': 'Proteínas derivadas de la leguminosa de soja.',
                'caa_hidden_names': 'Lecitina de soja, Proteína vegetal hidrolizada, Tofu, Miso, Tempeh, Edamame, Salsa de soja, Kinnako'
            }
        )
        if created_soja:
            self.stdout.write(self.style.SUCCESS('Creado alérgeno: Soja'))

        soja_allergy, created_soja_al = Allergy.objects.update_or_create(
            name='Alergia a la Soja',
            defaults={
                'description': 'Reacción inmunológica a las proteínas de la soja.',
                'is_ige_mediated': True
            }
        )
        soja_allergy.allergens.add(soja_allergen)

        # 4. Alérgeno: Trigo y Alergia: Alergia al Trigo
        trigo_allergen, created_trigo = Allergen.objects.update_or_create(
            name='Trigo',
            defaults={
                'description': 'Cereal que contiene gluten y otras proteínas alérgenas.',
                'caa_hidden_names': 'Gluten, Sémola, Espelta, Kamut, Salvado, Harina de trigo, Almidón de trigo, Germen de trigo'
            }
        )
        if created_trigo:
            self.stdout.write(self.style.SUCCESS('Creado alérgeno: Trigo'))

        trigo_allergy, created_trigo_al = Allergy.objects.update_or_create(
            name='Alergia al Trigo',
            defaults={
                'description': 'Reacción inmunológica a las proteínas del trigo (diferente de la enfermedad celíaca).',
                'is_ige_mediated': True
            }
        )
        trigo_allergy.allergens.add(trigo_allergen)

        self.stdout.write(self.style.SUCCESS('¡Carga de taxonomía inicial del CAA completada con éxito!'))
