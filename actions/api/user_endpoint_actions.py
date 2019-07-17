import json
import logging
import requests

from configuration.configuration import users_url

logger = logging.getLogger('python-behave-automation-quickstart')


# POST
def do_post_request_to_create_user(data):
    """
    Do a post request to add an user
    :param data: the new user details
    :return: the full response object
    """
    url = users_url
    logger.debug(f'Doing a POST request to the endpoint: {url}')
    response = requests.post(url=url, data=json.dumps(data))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response


# GET
def do_get_request_for_all_users():
    """
    Do a get request for all existing users
    :return: the full response object
    """
    url = users_url
    logger.debug(f'Doing a GET ALL request to the USERS endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response


def do_get_request_for_user(user_id):
    """
    Do a get request for one user
    :param user_id: the ID of the user
    :return: the user details
    """
    url = f'{users_url}/{user_id}'
    logger.debug(f'Doing a GET one user request to the USERS endpoint: {url}')
    response = requests.get(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response


# DELETE
def do_delete_request_for_user(user_id):
    """
    Do a delete request for one user
    :param user_id: the ID of the user
    :return: message after delete action
    """
    url = f'{users_url}/{user_id}'
    logger.debug(f'Doing a DELETE one user request to the USERS endpoint: {url}')
    response = requests.delete(url=url)
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response


# PUT
def do_put_request_to_update_user(user_id, data):
    """
    Do a update request for one user
    :param user_id: the ID of the user
    :param data: the updated user details
    :return: the user object with updated details
    """
    url = f'{users_url}/{user_id}'
    logger.debug(f'Doing a PUT request to the USERS endpoint: {url}')
    response = requests.put(url=url, data=json.dumps(data))
    logger.debug(f'Got response: {response.json()}' if response.ok
                 else f'Status code was {response.status_code} because: {response.reason}')
    return response
