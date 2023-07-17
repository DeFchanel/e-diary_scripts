PRAISES = [
    'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший  ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!'
]


def get_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains = schoolkid_name)
    except Schoolkid.DoesNotExist:
        print("Извините, ученик не найден.")
        return
    except Schoolkid.MultipleObjectsReturned:
        print("Извините, найдено несколько учеников.")
        return
    return schoolkid


def remove_chastisements(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    remarks = Chastisement.objects.filter(schoolkid=schoolkid)
    remarks.delete()


def fix_marks(schoolkid_name):
    schoolkid = get_schoolkid(schoolkid_name)
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def create_commendation(schoolkid_name, subject):
    schoolkid = get_schoolkid(schoolkid_name)
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=subject).order_by('?').first()
    if not lesson:
        print("Извините, предмет не найден. Проверьте вписанный вами предмет.")
        return
    praise = random.choice(PRAISES)
    Commendation.objects.create(text = praise, created = lesson.date, schoolkid = schoolkid, subject = lesson.subject, teacher = lesson.teacher)
