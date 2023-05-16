import random
import django


from datacenter.models import Schoolkid
from datacenter.models import Teacher
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation
from datacenter.models import Mark
from datacenter.models import Chastisement


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=["2", "3"])
    for mark in marks:
        mark.points = "5"
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(name, subject):

    commendations = ['Молодец!', 'Отлично!', 'Хорошо!', 'Великолепно!',
                     'Прекрасно!', 'Талантливо!', 'Потрясающе!']
    try:
        child = Schoolkid.objects.get(full_name__contains=name).first()
    except django.core.exceptions.MultipleObjectsReturned:
        print(f"Several child with the name {name} have been found!\n"
              f"Please specify who you mean.")
    except django.core.exceptions.ObjectDoesNotExist:
        print(f"A child named {name} was not found!")
    except Exception as exp:
        print(f"Error: {exp}")
    else:
        subject = Subject.objects.filter(
            title=subject,
            year_of_study=child.year_of_study
        ).first()

        lesson = Lesson.objects.filter(
            group_letter=child.group_letter,
            subject=subject
        ).order_by('?').first()

        teacher = Teacher.objects.all().order_by('?').first()

        Commendation.objects.create(
            text=random.choice(commendations),
            created=lesson.date,
            schoolkid=child,
            subject=subject,
            teacher=teacher
        )
