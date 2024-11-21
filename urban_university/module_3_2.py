def EmailValidate(email):
    return (("@" in str(email))and(str(email).endswith(".com",".ru",".net")))

def SendEmail(message, recipient, *,sender = "university.help@gmail.com"):
    global defaultSender
    if (not EmailValidate(recipient))or(not EmailValidate(sender)):
        print(f"Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>")
        return
    if str(sender)==str(recipient):
        print("Нельзя отправить письмо самому себе!")
        return
    if not str(sender)== defaultSender:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.")
    else:
        print(f"Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.")

defaultSender="university.help@gmail.com"
SendEmail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
SendEmail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
SendEmail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
SendEmail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')