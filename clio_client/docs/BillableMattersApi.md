# clio_sdk.BillableMattersApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billable_matter_ids**](BillableMattersApi.md#billable_matter_ids) | **GET** /billable_matters/ids | Returns the unique identifiers of all BillableMatter
[**billable_matter_index**](BillableMattersApi.md#billable_matter_index) | **GET** /billable_matters | Return the data for all BillableMatters


# **billable_matter_ids**
> BillableMatterShow billable_matter_ids(x_api_version=x_api_version, client_id=client_id, custom_field_values=custom_field_values, end_date=end_date, fields=fields, limit=limit, matter_id=matter_id, originating_attorney_id=originating_attorney_id, page_token=page_token, query=query, responsible_attorney_id=responsible_attorney_id, start_date=start_date)

Returns the unique identifiers of all BillableMatter

This data is retrieved asynchronously

### Example


```python
import clio_sdk
from clio_sdk.models.billable_matter_show import BillableMatterShow
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
    api_instance = clio_sdk.BillableMattersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    client_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property. (optional)
    custom_field_values = 'custom_field_values_example' # str | Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]`  (optional)
    end_date = '2013-10-20' # date | Filter BillableMatter records to those that have matters with unbilled activities on or before this date (Expects an ISO-8601 date). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    limit = 56 # int | A limit on the number of BillableMatter records to be returned. Limit can range between 1 and 1000. Default: `1000`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property. (optional)
    originating_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `display_number` or `number` or `description` matching a given string. (optional)
    responsible_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property. (optional)
    start_date = '2013-10-20' # date | Filter BillableMatter records to those that have matters with unbilled activities on or after this date (Expects an ISO-8601 date). (optional)

    try:
        # Returns the unique identifiers of all BillableMatter
        api_response = api_instance.billable_matter_ids(x_api_version=x_api_version, client_id=client_id, custom_field_values=custom_field_values, end_date=end_date, fields=fields, limit=limit, matter_id=matter_id, originating_attorney_id=originating_attorney_id, page_token=page_token, query=query, responsible_attorney_id=responsible_attorney_id, start_date=start_date)
        print("The response of BillableMattersApi->billable_matter_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableMattersApi->billable_matter_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **client_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property. | [optional] 
 **custom_field_values** | **str**| Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60;  | [optional] 
 **end_date** | **date**| Filter BillableMatter records to those that have matters with unbilled activities on or before this date (Expects an ISO-8601 date). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **limit** | **int**| A limit on the number of BillableMatter records to be returned. Limit can range between 1 and 1000. Default: &#x60;1000&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property. | [optional] 
 **originating_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;display_number&#x60; or &#x60;number&#x60; or &#x60;description&#x60; matching a given string. | [optional] 
 **responsible_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property. | [optional] 
 **start_date** | **date**| Filter BillableMatter records to those that have matters with unbilled activities on or after this date (Expects an ISO-8601 date). | [optional] 

### Return type

[**BillableMatterShow**](BillableMatterShow.md)

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

# **billable_matter_index**
> BillableMatterList billable_matter_index(x_api_version=x_api_version, client_id=client_id, custom_field_values=custom_field_values, end_date=end_date, fields=fields, limit=limit, matter_id=matter_id, originating_attorney_id=originating_attorney_id, page_token=page_token, query=query, responsible_attorney_id=responsible_attorney_id, start_date=start_date)

Return the data for all BillableMatters

Outlines the parameters, optional and required, used when requesting the data for all BillableMatters

### Example


```python
import clio_sdk
from clio_sdk.models.billable_matter_list import BillableMatterList
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
    api_instance = clio_sdk.BillableMattersApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    client_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property. (optional)
    custom_field_values = 'custom_field_values_example' # str | Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]`  (optional)
    end_date = '2013-10-20' # date | Filter BillableMatter records to those that have matters with unbilled activities on or before this date (Expects an ISO-8601 date). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    limit = 56 # int | A limit on the number of BillableMatter records to be returned. Limit can range between 1 and 1000. Default: `1000`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property. (optional)
    originating_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    query = 'query_example' # str | Wildcard search for `display_number` or `number` or `description` matching a given string. (optional)
    responsible_attorney_id = 56 # int | The unique identifier for a single User. Use the keyword `null` to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property. (optional)
    start_date = '2013-10-20' # date | Filter BillableMatter records to those that have matters with unbilled activities on or after this date (Expects an ISO-8601 date). (optional)

    try:
        # Return the data for all BillableMatters
        api_response = api_instance.billable_matter_index(x_api_version=x_api_version, client_id=client_id, custom_field_values=custom_field_values, end_date=end_date, fields=fields, limit=limit, matter_id=matter_id, originating_attorney_id=originating_attorney_id, page_token=page_token, query=query, responsible_attorney_id=responsible_attorney_id, start_date=start_date)
        print("The response of BillableMattersApi->billable_matter_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillableMattersApi->billable_matter_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **client_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property. | [optional] 
 **custom_field_values** | **str**| Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60;  | [optional] 
 **end_date** | **date**| Filter BillableMatter records to those that have matters with unbilled activities on or before this date (Expects an ISO-8601 date). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **limit** | **int**| A limit on the number of BillableMatter records to be returned. Limit can range between 1 and 1000. Default: &#x60;1000&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property. | [optional] 
 **originating_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **query** | **str**| Wildcard search for &#x60;display_number&#x60; or &#x60;number&#x60; or &#x60;description&#x60; matching a given string. | [optional] 
 **responsible_attorney_id** | **int**| The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property. | [optional] 
 **start_date** | **date**| Filter BillableMatter records to those that have matters with unbilled activities on or after this date (Expects an ISO-8601 date). | [optional] 

### Return type

[**BillableMatterList**](BillableMatterList.md)

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

