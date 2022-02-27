from faker import Faker

fake = Faker("Ru-ru")


class LoginData:
    def __init__(self, email=None, password=None, lorem_ipsum=None, recipient=None):
        self.email = email
        self.password = password
        self.lorem_ipsum = lorem_ipsum
        self.recipient = recipient

    @staticmethod
    def random_text():
        recipient = fake.email()
        lorem_ipsum = fake.paragraph(nb_sentences=5)
        return LoginData(recipient=recipient, lorem_ipsum=lorem_ipsum)
