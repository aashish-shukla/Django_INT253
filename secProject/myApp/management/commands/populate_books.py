from django.core.management.base import BaseCommand
from myApp.models import Book
from datetime import date

class Command(BaseCommand):
    help = 'Populate database with sample books'

    def handle(self, *args, **options):
        # Clear existing books
        Book.objects.all().delete()
        
        # Sample books data
        books_data = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'description': 'A classic American novel set in the Jazz Age, exploring themes of wealth, love, and the American Dream through the eyes of narrator Nick Carraway and his mysterious neighbor Jay Gatsby.',
                'publication_date': date(1925, 4, 10),
                'isbn': '9780743273565',
                'price': 12.99
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'description': 'A gripping tale of racial injustice and childhood innocence in the American South during the 1930s, told through the perspective of young Scout Finch.',
                'publication_date': date(1960, 7, 11),
                'isbn': '9780446310789',
                'price': 14.99
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'description': 'A dystopian social science fiction novel that explores the dangers of totalitarianism, surveillance, and thought control in a society ruled by Big Brother.',
                'publication_date': date(1949, 6, 8),
                'isbn': '9780451524935',
                'price': 13.99
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'description': 'A romantic novel that deals with issues of manners, upbringing, morality, education, and marriage in the society of the landed gentry of early 19th-century England.',
                'publication_date': date(1813, 1, 28),
                'isbn': '9780141439518',
                'price': 11.99
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'description': 'A coming-of-age story that follows teenager Holden Caulfield as he navigates the complexities of adolescence and society in 1950s New York.',
                'publication_date': date(1951, 7, 16),
                'isbn': '9780316769174',
                'price': 15.99
            },
            {
                'title': 'Harry Potter and the Philosopher\'s Stone',
                'author': 'J.K. Rowling',
                'description': 'The first book in the magical Harry Potter series, following young Harry as he discovers he\'s a wizard and begins his education at Hogwarts School of Witchcraft and Wizardry.',
                'publication_date': date(1997, 6, 26),
                'isbn': '9780747532699',
                'price': 18.99
            },
            {
                'title': 'The Lord of the Rings: The Fellowship of the Ring',
                'author': 'J.R.R. Tolkien',
                'description': 'An epic fantasy adventure following hobbit Frodo Baggins as he begins his quest to destroy the One Ring and save Middle-earth from the Dark Lord Sauron.',
                'publication_date': date(1954, 7, 29),
                'isbn': '9780547928210',
                'price': 16.99
            },
            {
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'description': 'A philosophical novel about a young shepherd\'s journey to find treasure, teaching readers about following their dreams and listening to their hearts.',
                'publication_date': date(1988, 1, 1),
                'isbn': '9780062315007',
                'price': 14.50
            }
        ]

        # Create books
        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                isbn=book_data['isbn'],
                defaults=book_data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created book: {book.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Book already exists: {book.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully populated database with {len(books_data)} books!')
        )