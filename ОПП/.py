class MyName:
    """Опис класу / Документація
    """
    total_names = 0  # Class variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        # 1. Перевірка None → Anonymous
        name = name if name is not None else self.anonymous_user().name

        # 2. Перевірка на літери
        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        # 3. Завжди з великої літери
        self.name = name.capitalize()

        # 4. Лічильник об’єктів
        MyName.total_names += 1
        self.my_id = self.total_names

    @property
    def whoami(self) -> str:
        """Class property"""
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property"""
        return self.create_email()

    @property
    def full_name(self) -> str:
        """Властивість повного опису"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def create_email(self, domain="itcollege.lviv.ua") -> str:
        """Instance method — генерує email з кастомним доменом"""
        return f"{self.name}@{domain}"

    def count_letters(self) -> int:
        """Порахувати кількість букв імені"""
        return len(self.name)

    @classmethod
    def anonymous_user(cls):
        """Class method"""
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method — можна змінювати текст"""
        return f"You say: {message}"

    def save_to_file(self, filename="users.txt"):
        """Записує інформацію про користувача у файл"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", None, "Максим")  # ← твоє ім'я добавив сюди
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me}
This is object attribute: {me.name} / {me.my_id}
Who am I: {me.whoami} | Email: {me.my_email}
create_email(): {me.create_email()}
Static method: {me.say_hello("Hi, teacher!")}
Letters count: {me.count_letters()}
Full name: {me.full_name}
Class variable: from class {MyName.total_names} — from object {me.total_names}
{"<*>"*20}""")

print(f"We are done. Created: {MyName.total_names} names!")
 