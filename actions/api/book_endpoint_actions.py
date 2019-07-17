import json
import logging
import requests

from configuration.configuration import books_url

logger = logging.getLogger('python-behave-automation-quickstart')


# POST
def do_post_request_to_create_book(data):
    """
    Do a post request to create a book
    :param data: the details of the new book
    :return: the full response object
    """
    url = books_url
    logger.debug(f'Doing a POST request to the endpoint: {url}')
    response = requests.post(url=url, data=json.dumps(data))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


# GET
def do_get_request_for_all_books():
    """
    Do a get request for all existing books
    :return: the full response object
    """
    url = books_url
    logger.debug(f'Doing a GET request to the endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


def do_get_request_for_book(book_id):
    """
    Do a get request for one book
    :param book_id: the ID of the book
    :return: the book details
    """
    url = f'{books_url}/{book_id}'
    logger.debug(f'Doing a GET request to the endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


# DELETE
def do_delete_request_for_book(book_id):
    """
    Do a delete request for one book
    :param book_id: the ID of the book
    :return: the message after delete action
    """
    url = f'{books_url}/{book_id}'
    logger.debug(f'Doing a DELETE request to the endpoint: {url}')
    response = requests.delete(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


# PUT
def do_put_request_to_update_book(book_id, data):
    """
    Do a put request to update details for a book
    :param book_id: the ID of the book
    :param data: the details to update
    :return: the book object with updated details
    """
    url = f'{books_url}/{book_id}'
    logger.debug(f'Doing a PUT request to the endpoint: {url}')
    response = requests.put(url=url, data=json.dumps(data))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response
