import csv

from assertpy import assert_that
from behave import given, when, then

from actions.api.book_endpoint_actions import do_get_request_for_all_books


@given(u'I get all books info')
def given_i_get_all_books_info(context):
    context.all_books_response = do_get_request_for_all_books()


@when(u'I save it to a csv')
def when_i_save_to_csv(context):
    with open("test.csv", "w") as f:
        fieldnames = ['id', 'name', 'author', 'description', 'cover']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for book in context.all_books_response.json():
            writer.writerow(book)


@when(u'read the content back')
def when_you_read_the_content_back(context):
    with open("test.csv", "r") as f:
        context.read_books = []
        csv_reader = csv.DictReader(f)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            row = {k: v if v else None for k, v in row.items()}
            context.read_books.append(row)


@then(u'I can ensure all data was written correctly')
def then_i_can_ensure_all_data_was_written_correctly(context):
    for book in context.all_books_response.json():
        book = {k: v if v else None for k, v in book.items()}
        assert_that(book in context.read_books).is_true()
