import requests
import json

from actions.api import logger
from configuration.configuration import reservations_url


# POST
def do_post_request_to_create_reservation(reservation):
    """
    Do a post request to create a reservation
    :param reservation: the details of the new reservations
    :return: the full response object
    """
    url = reservations_url
    logger.debug(f'Doing a POST request to the endpoint: {url}')
    response = requests.post(url=url, data=json.dumps(reservation))
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


def do_get_reservation_by_entity_id(**kwargs):
    """
    Do a get request to obtain reservation using book_id OR user_id
    **kwargs: receive user_id or book_id as parameter
    :return: the reservations details
    """
    if "book_id" in kwargs:
        url = f'{reservations_url}/book/{kwargs.get("book_id")}'
    elif "user_id" in kwargs:
        url = f'{reservations_url}/user/{kwargs.get("user_id")}'
    else:
        raise NotImplementedError
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
    :return: the reservations details
    """
    url = f'{reservations_url}/user/{user_id}/book/{book_id}'
    logger.debug(f'Doing a GET request to the endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


# DELETE
def do_delete_reservation_by_book_id_or_user_id(**kwargs):
    """
    Do a delete request to remove reservation using book_id OR user_id
    **kwargs: receive user_id or book_id as parameter
    :return: the message after reservations is deleted
    """
    if "book_id" in kwargs:
        url = f'{reservations_url}/book/{kwargs.get("book_id")}'
    elif "user_id" in kwargs:
        url = f'{reservations_url}/user/{kwargs.get("user_id")}'
    else:
        raise NotImplementedError
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
    :return: the message after reservations is deleted
    """
    url = f'{reservations_url}/user/{user_id}/book/{book_id}'
    logger.debug(f'Doing a DELETE request to the endpoint: {url}')
    response = requests.delete(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response


# PUT
def do_put_request_to_update_reservation(user_id, book_id, reservation):
    """
    Do a put request to update a reservations
    :param user_id: the id of the user
    :param book_id: the id of the book
    :param reservation: the updated details of the reservations
    :return: the updated reservations
    """
    url = f'{reservations_url}/user/{user_id}/book/{book_id}'
    logger.debug(f'Doing a PUT request to the endpoint: {url}')
    response = requests.put(url=url, data=json.dumps(reservation))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because {response.reason}')
    return response
