import csv
import xml.dom.minidom
import random
import os


def process_books_csv():
    print("=== ОБРАБОТКА books.csv ===\n")

    with open("books.csv", "r", encoding="windows-1251") as books_file:
        reader = csv.DictReader(books_file, delimiter=";")
        # 1. Количество записей с названием длиннее 30 символов
        long_titles_count = 0
        all_books = []

        for row in reader:
            all_books.append(row)
            title = row.get("Название", "")
            if len(title) > 30:
                long_titles_count += 1

        print(
            f"1. Количество записей с названием длиннее 30 символов: {long_titles_count}"
        )

        # 2. Поиск книги по автору (до 150 рублей)
        def search_by_author(author_name, max_price=150):
            books_file.seek(0)
            reader = csv.DictReader(books_file, delimiter=";")
            results = []
            for row in reader:
                book_author = row.get("Автор", "")
                price_str = row.get("Цена поступления", "0").replace(",", ".")
                try:
                    price = float(price_str)
                except ValueError:
                    price = 0

                if author_name.lower() in book_author.lower() and price <= max_price:
                    results.append(row)
            return results

        author_to_search = input("\nВведите автора для поиска (до 150 руб): ")
        found_books = search_by_author(author_to_search)

        print(
            f"\n2. Найдено книг автора '{author_to_search}' до 150 руб: {len(found_books)}"
        )
        for i, book in enumerate(found_books, 1):
            title = book.get("Название", "")
            price = book.get("Цена поступления", "0")
            print(f"   {i}. {title} - {price} руб")

        # 3. Генератор библиографических ссылок
        def generate_references(books, count=20):
            selected = random.sample(books, min(count, len(books)))
            references = []
            for book in selected:
                author = book.get("Автор", "Неизвестный автор")
                title = book.get("Название", "Без названия")
                date_str = book.get("Дата поступления", "")
                if date_str and "." in date_str:
                    year = date_str.split(".")[-1].split()[0]
                else:
                    year = "нет года"

                references.append(f"{author}. {title} - {year}")
            return references

        print("\n3. Генерация библиографических ссылок...")
        references = generate_references(all_books)

        with open("bibliographic_references.txt", "w", encoding="utf-8") as f:
            for i, ref in enumerate(references, 1):
                f.write(f"{i}. {ref}\n")

        print("Библиографические ссылки сохранены в 'bibliographic_references.txt'")

        return all_books


def process_currency_xml():
    print("\n=== ОБРАБОТКА currency.xml ===\n")

    # 4. Парсинг XML 
    dom_tree = xml.dom.minidom.parse("currency.xml")
    root = dom_tree.documentElement

    currency_dict = {}

    valutes = root.getElementsByTagName("Valute")

    for valute in valutes:
        name_elements = valute.getElementsByTagName("Name")
        if name_elements:
            name = name_elements[0].firstChild.data

        value_elements = valute.getElementsByTagName("Value")
        if value_elements:
            value_text = value_elements[0].firstChild.data
            value_float = float(value_text.replace(",", "."))
            currency_dict[name] = value_float

    print("4. Словарь 'Name - Value':")
    for i, (name, value) in enumerate(list(currency_dict.items()), 1):
        print(f"   {i}. {name}: {value}")

    print(f"\nВсего валют в словаре: {len(currency_dict)}")

    return currency_dict


def extract_unique_tags(books):
    print("\n5. Перечень всех тегов без повторений:")

    all_tags = set()

    for book in books:
        genre_field = book.get("Жанр книги", "")
        if genre_field:
            tags = [tag.strip() for tag in genre_field.split("#") if tag.strip()]
            all_tags.update(tags)

    print(f"Всего уникальных тегов: {len(all_tags)}")

    sorted_tags = sorted(list(all_tags))

    for i, tag in enumerate(sorted_tags, 1):
        print(f"   {i:3}. {tag}")

    return sorted_tags


def additional_tasks(books):

    # 5. Перечень всех тегов без повторений
    unique_tags = extract_unique_tags(books)

    # 6. 20 самых популярных книг (по количеству выдач)
    print("\n6. 20 самых популярных книг (по количеству выдач):")

    books_with_issues = []
    for book in books:
        issues_str = book.get("Кол-во выдач", "0")
        try:
            issues = int(issues_str)
        except ValueError:
            issues = 0
        books_with_issues.append((issues, book))

    def get_issues_count(book_tuple):
        return book_tuple[0]
    books_with_issues.sort(key=get_issues_count, reverse=True)

    for i, (issues, book) in enumerate(books_with_issues[:20], 1):
        title = book.get("Название", "")
         
        author = book.get("Автор", "")
        print(f"\t{i}. {title}")
        print(f"      Автор: {author}, Выдач: {issues}")


if __name__ == "__main__":
    os.system("cls")
    books_data = process_books_csv()
    currency_data = process_currency_xml()
    additional_tasks(books_data)
