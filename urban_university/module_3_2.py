# coding: cp1251

def EmailValidate(email):
    return (("@" in str(email))and(str(email).endswith(".com",".ru",".net")))

def SendEmail(message, recipient, *,sender = "university.help@gmail.com"):
    global defaultSender
    if (not EmailValidate(recipient))or(not EmailValidate(sender)):
        print(f"���������� ��������� ������ � ������ <{sender}> �� ����� <{recipient}>")
        return
    if str(sender)==str(recipient):
        print("������ ��������� ������ ������ ����!")
        return
    if not str(sender)== defaultSender:
        print(f"������������� �����������! ������ ���������� � ������ <{sender}> �� ����� <{recipient}>.")
    else:
        print(f"������ ������� ���������� � ������ <{sender}> �� ����� <{recipient}>.")

defaultSender="university.help@gmail.com"
SendEmail('��� ��������� ��� �������� �����', 'vasyok1337@gmail.com')
SendEmail('�� ������ ��� ��������� ��� ������ ������� �����!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
SendEmail('����������, ��������� �������', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
SendEmail('��������� ������ ���� � ��������', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')