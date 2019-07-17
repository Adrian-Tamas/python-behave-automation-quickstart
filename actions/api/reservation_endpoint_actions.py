import logging
import requests
import json

from configuration.configuration import reservations_url

logger = logging.getLogger('python-behave-automation-quickstart')


# POST
def do_post_request_to_create_reservation(data):
    """
    Do a post request to create a reservation
    :param data: the details of the new reservation
    :return: the full response object
    """
    url = reservations_url
    logger.debug(f'Doing a POST request to the endpoint: {url}')
    response = requests.post(url=url, data=json.dumps(data))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


# GET
def do_get_request_for_all_reservations():
    """
    Do a get request for all existing reservations
    :return: the full response object
    """
    url = reservations_url
    logger.debug(f'Doing a GET request to the endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


def do_get_reservation_by_book_id_or_user_id(param, param_id):
    """
    Do a get request to obtain reservation using book_id OR user_id
    :param param: book or user
    :param param_id: book_id or user_id
    :return: the reservation details
    """
    url = f'{reservations_url}/{param}/{param_id}'
    logger.debug(f'Doing a GET request to the endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


def do_get_reservation_by_book_id_and_user_id(user_id, book_id):
    """
    Do a get request to obtain reservation using book_id AND user_id
    :param user_id: ID of the user
    :param book_id: ID of the book
    :return: the reservation details
    """
    url = f'{reservations_url}/user/{user_id}/book/{book_id}'
    logger.debug(f'Doing a GET request to the endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


# DELETE
def do_delete_reservation_by_book_id_or_user_id(param, param_id):
    """
    Do a delete request to remove reservation using book_id OR user_id
    :param param: book or user
    :param param_id: book_id or user_id
    :return: the message after reservation is deleted
    """
    url = f'{reservations_url}/{param}/{param_id}'
    logger.debug(f'Doing a DELETE request to the endpoint: {url}')
    response = requests.delete(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


def do_delete_reservation_by_book_id_and_user_id(user_id, book_id):
    """
    Do a delete request to remove reservation using book_id AND user_id
    :param user_id: ID of the user
    :param book_id: ID of the book
    :return: the message after reservation is deleted
    """
    url = f'{reservations_url}/user/{user_id}/book/{book_id}'
    logger.debug(f'Doing a DELETE request to the endpoint: {url}')
    response = requests.delete(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


# PUT
def do_put_request_to_update_reservation(user_id, book_id, data):
    """
    Do a put request to update a reservation
    :param user_id: the id of the user
    :param book_id: the id of the book
    :param data: the updated details of the reservation
    :return: the updated reservation
    """
    url = f'{reservations_url}/user/{user_id}/book/{book_id}'
    logger.debug(f'Doing a PUT request to the endpoint: {url}')
    response = requests.put(url=url, data=json.dumps(data))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response
