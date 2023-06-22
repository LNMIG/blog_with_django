import csv

from django.core.management import BaseCommand

from users.models import User, Rol


class Command(BaseCommand):
    """Command for importing a properly-formatted CSV file with
    customer data into the database.

    # Notes
    - Handles both creating and updating customer records.
    - Uses the file's `id` column as the `id` primary key for our database row.
    - Log messages uses stdout.

    # Expected format:
    ```csv
    id,first_name,last_name,email,gender,company,city,title
    1,Laura,Richards,lrichards0@reverbnation.com,Female,Meezzy,"Warner, NH",Biostatistician I
    ```
    """

    help = "Import customers from CSV into database. Expects one argument containing the file path."

    def add_arguments(self, parser):
        parser.add_argument('filepath', type=str, help='file path for CSV',)
        parser.add_argument('-c', '--create', action='store_true', help='create user',)
        parser.add_argument('-u', '--update', action='store_true', help='update user',)
        parser.add_argument('-s', '--show', action='store_true', help='show users ID',)
        parser.add_argument('-g', '--get', action='store_true', help='get user',)

    def handle(self, *args, **options):
        create = options['create']
        update = options['update']
        show = options['show']
        
        with open(options["filepath"], 'r', encoding="utf-8") as file:
            registry = csv.reader(file)
            data = [[c.replace('\ufeff','') for c in row] for row in registry]
            for row in data:
                row = row[0].split(';')
                print(row, '\n')
                if create:
                    # self.stdout.write(f'id={row[0]}, first_name={row[1]}, last_name={row[2]}, email={row[3]}, gender={row[4]}, company={row[5]}, city={row[6]}, title={row[7]}\n', ending='')
                    user = User.objects.create(
                              first_name=row[0],
                              last_name=row[1],
                              phone=row[2],
                              username=row[3],
                              email=row[4],
                              password=row[5],
                              rol=Rol.objects.get(pk=3)
                             )
                    user.save()

                elif update:
                    # self.stdout.write(f'id={row[0][0]}, first_name={row[0][1]}, last_name={row[0][2]}, email={row[0][3]}, gender={row[0][4]}, company={row[0][5]}, city={row[0][6]}, title={row[0][7]}', ending='')
                    user = User.objects.get(username=row[3])
                    attr = ['first_name', 'last_name', 'phone', 'username', 'email','password']
                    for index, each in enumerate(attr):
                        user.__setattr__(attr[index], row[index])
                    user.save()

                else:
                    self.stdout.write('Nothing to do or show\n', ending='')

                if create:
                    print('El usuario fue creadocon éxito:\n')
                    print(User.objects.get(pk=user.id))
                if update:
                    print('Los datos del usuario fueron actualizados con éxito:\n')
                    print(User.objects.get(pk=user.id))
            if show:
                users = User.objects.all()
                for each in users:
                    n = 'id'
                    print(f'{each} tiene ID = {each.__getattribute__(n)}')
