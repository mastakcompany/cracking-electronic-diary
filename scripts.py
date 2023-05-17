import random


from datacenter.models import Schoolkid
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation
from datacenter.models import Mark
from datacenter.models import Chastisement

COMMENDATIONS = ['Молодец!', 'Отлично!', 'Хорошо!', 'Великолепно!',
                 'Прекрасно!', 'Талантливо!', 'Потрясающе!']


def fix_marks(schoolkid):
    schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid).first()
    Mark.objects.filter(schoolkid=schoolkid, points__in=["2", "3"]).update(points="5")


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(name, subject):

    try:
        child = Schoolkid.objects.get(full_name__contains=name).first()
    except Schoolkid.DoesNotExist:
        print(f"Several child with the name {name} have been found!\n"
              f"Please specify who you mean.")
    except Schoolkid.MultipleObjectsReturned:
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

        Commendation.objects.create(
            text=random.choice(COMMENDATIONS),
            created=lesson.date,
            schoolkid=child,
            subject=subject,
            teacher=lesson.teacher
        )
