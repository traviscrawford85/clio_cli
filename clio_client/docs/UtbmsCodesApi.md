# clio_sdk.UtbmsCodesApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**utbms_code_index**](UtbmsCodesApi.md#utbms_code_index) | **GET** /utbms/codes | Return the data for all UtbmsCodes
[**utbms_code_show**](UtbmsCodesApi.md#utbms_code_show) | **GET** /utbms/codes/{id} | Return the data for a single UtbmsCode


# **utbms_code_index**
> UtbmsCodeList utbms_code_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, type=type, updated_since=updated_since, utbms_set_id=utbms_set_id)

Return the data for all UtbmsCodes

Outlines the parameters, optional and required, used when requesting the data for all UtbmsCodes

### Example


```python
import clio_sdk
from clio_sdk.models.utbms_code_list import UtbmsCodeList
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
    api_instance = clio_sdk.UtbmsCodesApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter UtbmsCode records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter UtbmsCode records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of UtbmsCode records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    order = 'order_example' # str | Orders the UtbmsCode records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    type = 'type_example' # str | Filter UtbmsCode records to those of a given type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter UtbmsCode records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    utbms_set_id = 56 # int | The unique identifier for a single UtbmsSet. Use the keyword `null` to match those without a UtbmsCode. The list will be filtered to include only the UtbmsCode records with the matching property. (optional)

    try:
        # Return the data for all UtbmsCodes
        api_response = api_instance.utbms_code_index(x_api_version=x_api_version, created_since=created_since, fields=fields, ids=ids, limit=limit, order=order, page_token=page_token, type=type, updated_since=updated_since, utbms_set_id=utbms_set_id)
        print("The response of UtbmsCodesApi->utbms_code_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtbmsCodesApi->utbms_code_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **created_since** | **datetime**| Filter UtbmsCode records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter UtbmsCode records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of UtbmsCode records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **order** | **str**| Orders the UtbmsCode records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **type** | **str**| Filter UtbmsCode records to those of a given type. | [optional] 
 **updated_since** | **datetime**| Filter UtbmsCode records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **utbms_set_id** | **int**| The unique identifier for a single UtbmsSet. Use the keyword &#x60;null&#x60; to match those without a UtbmsCode. The list will be filtered to include only the UtbmsCode records with the matching property. | [optional] 

### Return type

[**UtbmsCodeList**](UtbmsCodeList.md)

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

# **utbms_code_show**
> UtbmsCodeShow utbms_code_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single UtbmsCode

Outlines the parameters, optional and required, used when requesting the data for a single UtbmsCode

### Example


```python
import clio_sdk
from clio_sdk.models.utbms_code_show import UtbmsCodeShow
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
    api_instance = clio_sdk.UtbmsCodesApi(api_client)
    id = 56 # int | The unique identifier for the UtbmsCode.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single UtbmsCode
        api_response = api_instance.utbms_code_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of UtbmsCodesApi->utbms_code_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtbmsCodesApi->utbms_code_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the UtbmsCode. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**UtbmsCodeShow**](UtbmsCodeShow.md)

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

