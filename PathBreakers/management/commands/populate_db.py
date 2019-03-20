from django.core.management.base import BaseCommand
from PathBreakers.Models import Profession, PathBreaker

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--name',
            nargs='?',
            help='pathbreaker name',
        )

        parser.add_argument(
            '--blurb',
            nargs='?',
            help='pathbreaker blurb',
        )

        parser.add_argument(
            '--link',
            nargs='?',
            help='pathbreaker link',
        )

        parser.add_argument(
            '--profilepic',
            nargs='?',
            help='pathbreaker profile pic',
        )

        parser.add_argument(
            '--yog',
            nargs='?',
            type=int,
            help='pathbreaker year of graduation',
        )

        parser.add_argument(
            '--degree',
            nargs='?',
            help='pathbreaker degree',
        )

        parser.add_argument(
            '--profession',
            nargs='?',
            help='pathbreaker profession',
        )

        parser.add_argument(
            '--tag',
            nargs='?',
            help='pathbreaker tag',
        )

    def getProfessionTag(self, profession, tag):
        professionTag=None
        if profession and tag:
            try:
                self.stdout.write(profession+" "+tag)
                professionTag = Profession.ProfessionTag.objects.get(profession__name=profession, tag__tag=tag)
            except Profession.ProfessionTag.DoesNotExist:
                try:
                    profession = Profession.Profession.objects.get(name=profession)
                except Profession.Profession.DoesNotExist:
                    profession = Profession.Profession.objects.create(name=profession)
                try:
                    tag = Profession.Tag.objects.get(tag=tag)
                except Profession.Tag.DoesNotExist:
                    tag = Profession.Tag.objects.create(tag=tag)

                professionTag = Profession.ProfessionTag.objects.create(tag=tag, profession=profession)
            except Profession.MultipleObjectsReturned:
                self.stdout.write("multiple objects returned");
        return professionTag

    def handle(self, *args, **options):
        professionTag = self.getProfessionTag(options['profession'], options['tag'])
        name=options['name']
        blurb=options['blurb']
        yog=options['yog']
        link=options['link']
        pic=options['profilepic']
        degree=options['degree']

        try:
            pb = PathBreaker.PathBreaker.objects.get(link=link)
        except PathBreaker.PathBreaker.DoesNotExist:
            pb = PathBreaker.PathBreaker.objects.create(name=name, blurb=blurb, yog=yog, link=link, profilePic='PathBreakers/'+pic, degree=degree)
            pb.professionTag.add(professionTag)
        except PathBreaker.PathBreaker.MultipleObjectsReturned:
            print(name+" "+blurb+"  "+link+"  already exist")


