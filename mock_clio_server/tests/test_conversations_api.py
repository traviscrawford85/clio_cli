# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.conversation_update_request import ConversationUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_conversation_index(client: TestClient):
    """Test case for conversation_index

    Return the data for all Conversations
    """
    params = [("archivedquery", True),     ("contact_idquery", 56),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("datequery", '2013-10-20'),     ("fieldsquery", 'fieldsquery_example'),     ("for_userquery", True),     ("idsquery", 56),     ("limitquery", 56),     ("matter_idquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("read_statusquery", True),     ("time_entriesquery", True),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/conversations/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_conversation_update(client: TestClient):
    """Test case for conversation_update

    Update a single Conversation
    """
    conversation_update_request = clio_mock.ConversationUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/conversations/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=conversation_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

