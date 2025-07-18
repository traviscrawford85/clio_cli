# clio_sdk.ConversationMessagesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversation_message_create**](ConversationMessagesApi.md#conversation_message_create) | **POST** /conversation_messages | Create a new ConversationMessage
[**conversation_message_index**](ConversationMessagesApi.md#conversation_message_index) | **GET** /conversation_messages | Return the data for all ConversationMessages
[**conversation_message_show**](ConversationMessagesApi.md#conversation_message_show) | **GET** /conversation_messages/{id} | Return the data for a single ConversationMessage


# **conversation_message_create**
> ConversationMessageShow conversation_message_create(x_api_version=x_api_version, fields=fields, conversation_message_create_request=conversation_message_create_request)

Create a new ConversationMessage

Outlines the parameters and data fields used when creating a new ConversationMessage

### Example


```python
import clio_sdk
from clio_sdk.models.conversation_message_create_request import ConversationMessageCreateRequest
from clio_sdk.models.conversation_message_show import ConversationMessageShow
from clio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.clio.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = clio_sdk.Configuration(
    host = "https://app.clio.com/api/v4"
)


# Enter a context with an instance of the API client
with clio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clio_sdk.ConversationMessagesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    conversation_message_create_request = clio_sdk.ConversationMessageCreateRequest() # ConversationMessageCreateRequest | Request Body for Conversation Messages (optional)

    try:
        # Create a new ConversationMessage
        api_response = api_instance.conversation_message_create(x_api_version=x_api_version, fields=fields, conversation_message_create_request=conversation_message_create_request)
        print("The response of ConversationMessagesApi->conversation_message_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationMessagesApi->conversation_message_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **conversation_message_create_request** | [**ConversationMessageCreateRequest**](ConversationMessageCreateRequest.md)| Request Body for Conversation Messages | [optional] 

### Return type

[**ConversationMessageShow**](ConversationMessageShow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversation_message_index**
> ConversationMessageList conversation_message_index(conversation_id, x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)

Return the data for all ConversationMessages

Outlines the parameters, optional and required, used when requesting the data for all ConversationMessages

### Example


```python
import clio_sdk
from clio_sdk.models.conversation_message_list import ConversationMessageList
from clio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.clio.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = clio_sdk.Configuration(
    host = "https://app.clio.com/api/v4"
)


# Enter a context with an instance of the API client
with clio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clio_sdk.ConversationMessagesApi(api_client)
    conversation_id = 56 # int | The unique identifier for a single Conversation. Use the keyword `null` to match those without a ConversationMessage. The list will be filtered to include only the ConversationMessage records with the matching property.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ConversationMessage records to those having the `created_at` field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter ConversationMessage records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of ConversationMessage records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the ConversationMessage records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `body` matching a given string. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ConversationMessage records to those having the `updated_at` field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all ConversationMessages
        api_response = api_instance.conversation_message_index(conversation_id, x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, query=query, updated_since=updated_since)
        print("The response of ConversationMessagesApi->conversation_message_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationMessagesApi->conversation_message_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **int**| The unique identifier for a single Conversation. Use the keyword &#x60;null&#x60; to match those without a ConversationMessage. The list will be filtered to include only the ConversationMessage records with the matching property. | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter ConversationMessage records to those having the &#x60;created_at&#x60; field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter ConversationMessage records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of ConversationMessage records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the ConversationMessage records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;body&#x60; matching a given string. | [optional] 
 **updated_since** | **datetime**| Filter ConversationMessage records to those having the &#x60;updated_at&#x60; field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**ConversationMessageList**](ConversationMessageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conversation_message_show**
> ConversationMessageShow conversation_message_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single ConversationMessage

Outlines the parameters, optional and required, used when requesting the data for a single ConversationMessage

### Example


```python
import clio_sdk
from clio_sdk.models.conversation_message_show import ConversationMessageShow
from clio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.clio.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = clio_sdk.Configuration(
    host = "https://app.clio.com/api/v4"
)


# Enter a context with an instance of the API client
with clio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clio_sdk.ConversationMessagesApi(api_client)
    id = 56 # int | The unique identifier for the ConversationMessage.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single ConversationMessage
        api_response = api_instance.conversation_message_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ConversationMessagesApi->conversation_message_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConversationMessagesApi->conversation_message_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ConversationMessage. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ConversationMessageShow**](ConversationMessageShow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**304** | Not Modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

