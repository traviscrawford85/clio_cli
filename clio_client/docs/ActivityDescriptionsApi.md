# clio_sdk.ActivityDescriptionsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activity_description_create**](ActivityDescriptionsApi.md#activity_description_create) | **POST** /activity_descriptions | Create a new ActivityDescription
[**activity_description_destroy**](ActivityDescriptionsApi.md#activity_description_destroy) | **DELETE** /activity_descriptions/{id} | Delete a single ActivityDescription
[**activity_description_index**](ActivityDescriptionsApi.md#activity_description_index) | **GET** /activity_descriptions | Return the data for all ActivityDescriptions
[**activity_description_show**](ActivityDescriptionsApi.md#activity_description_show) | **GET** /activity_descriptions/{id} | Return the data for a single ActivityDescription
[**activity_description_update**](ActivityDescriptionsApi.md#activity_description_update) | **PATCH** /activity_descriptions/{id} | Update a single ActivityDescription


# **activity_description_create**
> ActivityDescriptionShow activity_description_create(x_api_version=x_api_version, fields=fields, activity_description_create_request=activity_description_create_request)

Create a new ActivityDescription

Outlines the parameters and data fields used when creating a new ActivityDescription

### Example


```python
import clio_sdk
from clio_sdk.models.activity_description_create_request import ActivityDescriptionCreateRequest
from clio_sdk.models.activity_description_show import ActivityDescriptionShow
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
    api_instance = clio_sdk.ActivityDescriptionsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    activity_description_create_request = clio_sdk.ActivityDescriptionCreateRequest() # ActivityDescriptionCreateRequest | Request Body for Activity Descriptions (optional)

    try:
        # Create a new ActivityDescription
        api_response = api_instance.activity_description_create(x_api_version=x_api_version, fields=fields, activity_description_create_request=activity_description_create_request)
        print("The response of ActivityDescriptionsApi->activity_description_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityDescriptionsApi->activity_description_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **activity_description_create_request** | [**ActivityDescriptionCreateRequest**](ActivityDescriptionCreateRequest.md)| Request Body for Activity Descriptions | [optional] 

### Return type

[**ActivityDescriptionShow**](ActivityDescriptionShow.md)

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

# **activity_description_destroy**
> activity_description_destroy(id, x_api_version=x_api_version)

Delete a single ActivityDescription

Outlines the parameters, optional and required, used when deleting the record for a single ActivityDescription

### Example


```python
import clio_sdk
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
    api_instance = clio_sdk.ActivityDescriptionsApi(api_client)
    id = 56 # int | The unique identifier for the ActivityDescription.
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)

    try:
        # Delete a single ActivityDescription
        api_instance.activity_description_destroy(id, x_api_version=x_api_version)
    except Exception as e:
        print("Exception when calling ActivityDescriptionsApi->activity_description_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ActivityDescription. | 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_description_index**
> ActivityDescriptionList activity_description_index(x_api_version=x_api_version, created_since=created_since, fields=fields, flat_rate=flat_rate, ids=ids, limit=limit, page_token=page_token, rate_for_matter_id=rate_for_matter_id, rate_for_user_id=rate_for_user_id, type=type, updated_since=updated_since, user_id=user_id)

Return the data for all ActivityDescriptions

Outlines the parameters, optional and required, used when requesting the data for all ActivityDescriptions

### Example


```python
import clio_sdk
from clio_sdk.models.activity_description_list import ActivityDescriptionList
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
    api_instance = clio_sdk.ActivityDescriptionsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ActivityDescription records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    flat_rate = True # bool | Filter ActivityDescription records to those that have a flat rate, or not. (optional)
    ids = 56 # int | Filter ActivityDescription records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of ActivityDescription records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    rate_for_matter_id = 56 # int | Matter id for rate calculation. (optional)
    rate_for_user_id = 56 # int | User id for rate calculation. If not provided, the user associated to the API request is assumed. (optional)
    type = 'type_example' # str | Filter ActivityDescription records to those of a specific type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter ActivityDescription records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    user_id = 56 # int | The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityDescription records with the matching property. (optional)

    try:
        # Return the data for all ActivityDescriptions
        api_response = api_instance.activity_description_index(x_api_version=x_api_version, created_since=created_since, fields=fields, flat_rate=flat_rate, ids=ids, limit=limit, page_token=page_token, rate_for_matter_id=rate_for_matter_id, rate_for_user_id=rate_for_user_id, type=type, updated_since=updated_since, user_id=user_id)
        print("The response of ActivityDescriptionsApi->activity_description_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityDescriptionsApi->activity_description_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter ActivityDescription records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **flat_rate** | **bool**| Filter ActivityDescription records to those that have a flat rate, or not. | [optional] 
 **ids** | **int**| Filter ActivityDescription records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of ActivityDescription records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **rate_for_matter_id** | **int**| Matter id for rate calculation. | [optional] 
 **rate_for_user_id** | **int**| User id for rate calculation. If not provided, the user associated to the API request is assumed. | [optional] 
 **type** | **str**| Filter ActivityDescription records to those of a specific type. | [optional] 
 **updated_since** | **datetime**| Filter ActivityDescription records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **user_id** | **int**| The unique identifier for a single User. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityDescription records with the matching property. | [optional] 

### Return type

[**ActivityDescriptionList**](ActivityDescriptionList.md)

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

# **activity_description_show**
> ActivityDescriptionShow activity_description_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single ActivityDescription

Outlines the parameters, optional and required, used when requesting the data for a single ActivityDescription

### Example


```python
import clio_sdk
from clio_sdk.models.activity_description_show import ActivityDescriptionShow
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
    api_instance = clio_sdk.ActivityDescriptionsApi(api_client)
    id = 56 # int | The unique identifier for the ActivityDescription.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single ActivityDescription
        api_response = api_instance.activity_description_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of ActivityDescriptionsApi->activity_description_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityDescriptionsApi->activity_description_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ActivityDescription. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**ActivityDescriptionShow**](ActivityDescriptionShow.md)

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

# **activity_description_update**
> ActivityDescriptionShow activity_description_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, activity_description_update_request=activity_description_update_request)

Update a single ActivityDescription

Outlines the parameters and data fields used when updating a single ActivityDescription

### Example


```python
import clio_sdk
from clio_sdk.models.activity_description_show import ActivityDescriptionShow
from clio_sdk.models.activity_description_update_request import ActivityDescriptionUpdateRequest
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
    api_instance = clio_sdk.ActivityDescriptionsApi(api_client)
    id = 56 # int | The unique identifier for the ActivityDescription.
    if_match = 'if_match_example' # str | The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags). (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    activity_description_update_request = clio_sdk.ActivityDescriptionUpdateRequest() # ActivityDescriptionUpdateRequest | Request Body for Activity Descriptions (optional)

    try:
        # Update a single ActivityDescription
        api_response = api_instance.activity_description_update(id, if_match=if_match, x_api_version=x_api_version, fields=fields, activity_description_update_request=activity_description_update_request)
        print("The response of ActivityDescriptionsApi->activity_description_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityDescriptionsApi->activity_description_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the ActivityDescription. | 
 **if_match** | **str**| The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags). | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **activity_description_update_request** | [**ActivityDescriptionUpdateRequest**](ActivityDescriptionUpdateRequest.md)| Request Body for Activity Descriptions | [optional] 

### Return type

[**ActivityDescriptionShow**](ActivityDescriptionShow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

