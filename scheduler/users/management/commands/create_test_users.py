from django.core.management.base import BaseCommand

from users.models import SchedulerUser
import names
import string
from random import choice


class Command(BaseCommand):
    help = "Create superuser and some random users."

    def handle(self, *args, **options):
        if options["amount"]:
            self.create_users(amount=options["amount"],
                              super_name=options["name"] if options["name"] else options["default_name"])
        else:
            self.create_users(options["default_amount"],
                              super_name=options["name"] if options["name"] else options["default_name"])

    def add_arguments(self, parser):
        parser.add_argument(
            "-a",
            "--amount",
            action="store",
            type=int,
            help="Amount of random users"
        )

        parser.add_argument(
            "-n",
            "--name",
            action="store",
            help="Name of your superuser.",
        )

        parser.add_argument(
            "default_name",
            action="store_const",
            const="superuser"
        )

        parser.add_argument(
            "default_amount",
            action="store_const",
            const=3
        )

    def create_users(self, amount, super_name="superuser"):
        old_users = SchedulerUser.objects.filter(test_user=True)
        old_users.delete()
        users = dict()
        super_first = names.get_first_name()
        super_last = names.get_last_name()
        passwd = self.random_password()
        SchedulerUser.objects.create_superuser(
            username=super_name,
            first_name=super_first,
            last_name=super_last,
            password=passwd,
            email="super@mail.ru",
            test_user=True
        )

        users["super_mail"] = "super@mail.ru"
        users["super_passwd"] = passwd

        for user in range(1, amount + 1):
            name = f"user_{user}"
            f_name = names.get_first_name()
            l_name = names.get_last_name()
            mail = self.random_mail()
            passwd = self.random_password()
            SchedulerUser.objects.create_user(
                username=name,
                first_name=f_name,
                last_name=l_name,
                email=mail,
                password=passwd,
                test_user=True
            )

            users[mail] = passwd

        with open("test_users.txt", "w") as f:
            for mail, password in users.items():
                f.write(f"\n{mail}: {password}\n")

    @staticmethod
    def random_password():
        abc = string.ascii_letters + string.digits
        passwd = "".join([choice(abc) for _ in range(20)])
        return passwd

    @staticmethod
    def random_mail():
        abc = string.ascii_letters + string.digits
        mails = ["mail.ru", "gmail.com", "yandex.ru"]
        mail = "@" + "".join([choice(abc) for _ in range(10)]) + choice(mails)
        return mail
