def remove_chastisements(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains = schoolkid_name)
    except ObjectDoesNotExist:
        print("Извините, ученик не найден.")
        return
    except MultipleObjectsReturned:
        print("Извините, найдено несколько учеников.")
        return
    remarks = Chastisement.objects.filter(schoolkid=schoolkid)
    remarks.delete()


def fix_marks(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains = schoolkid_name)
    except ObjectDoesNotExist:
        print("Извините, ученик не найден.")
        return
    except MultipleObjectsReturned:
        print("Извините, найдено несколько учеников.")
        return
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()

def create_commendation(schoolkid_name, subject):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains = schoolkid_name)
    except ObjectDoesNotExist:
        print("Извините, ученик не найден.")
        return
    except MultipleObjectsReturned:
        print("Извините, найдено несколько учеников.")
        return
    try:
        lessons = Lesson.objects.filter(year_of_study=6, group_letter='А', subject__title=subject)
        lesson = lessons[0]
    except IndexError:
        print("Извините, предмет не найден. Проверьте вписанный вами предмет.")
        return
    praises = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший  ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!']
    praise = random.choice(praises)
    Commendation.objects.create(text = praise, created = lesson.date, schoolkid = schoolkid, subject = lesson.subject, teacher = lesson.teacher)
