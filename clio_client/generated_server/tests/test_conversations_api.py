# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.conversation_list import ConversationList  # noqa: F401
from openapi_server.models.conversation_show import ConversationShow  # noqa: F401
from openapi_server.models.conversation_update_request import ConversationUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_conversation_index(client: TestClient):
    """Test case for conversation_index

    Return the data for all Conversations
    """
    params = [("archived", True),     ("contact_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("var_date", '2013-10-20'),     ("fields", 'fields_example'),     ("for_user", True),     ("ids", 56),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("read_status", True),     ("time_entries", True),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/conversations.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_conversation_show(client: TestClient):
    """Test case for conversation_show

    Return the data for a single Conversation
    """
    params = [("fields", 'fields_example')]
    headers = {
        "if_modified_since": '2013-10-20',
        "if_none_match": 'if_none_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/conversations/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_conversation_update(client: TestClient):
    """Test case for conversation_update

    Update a single Conversation
    """
    conversation_update_request = openapi_server.ConversationUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/conversations/{id}.json".format(id=56),
    #    headers=headers,
    #    json=conversation_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

