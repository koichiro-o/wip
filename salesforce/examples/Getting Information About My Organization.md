### Getting Information About My Organization

The examples in this section use REST API resources to retrieve organization-level information, such as a list of all objects available in
your organization.

IN THIS SECTION:

List Available REST API Versions
Use the Versions resource to list summary information about each REST API version currently available, including the version, label,
and a link to each version's root. You don’t need authentication to retrieve the list of versions.

List Org Limits
Use the Limits resource to list your org limits.

List Available REST Resources
Use the Resources by Version resource to list the resources available for the specified API version. This provides the name and URI
of each additional resource.

Get a List of Objects
Use the Describe Global resource to list the objects available in your org and available to the logged-in user. This resource also returns
the org encoding, as well as maximum batch size permitted in queries.

Get a List of Objects If Metadata Has Changed
Use the Describe Global resource and the If-Modified-Since HTTP header to determine if an object’s metadata has changed.

#### List Available REST API Versions

Use the Versions resource to list summary information about each REST API version currently available, including the version, label, and
a link to each version's root. You don’t need authentication to retrieve the list of versions.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/ -H "Authorization: Bearer
  token"

```
Note: When using a self-signed SSL certificate, the -k flag can be used to skip certificate validation.

**Example request body**
none required

**Example JSON response body**


-----

-----

-----

SEE ALSO:

Versions

#### List Org Limits

Use the Limits resource to list your org limits.

**•** `Max` is the limit for the org.

**•** `Remaining` is the number of calls or events left for the org.

**Example usage**


-----

**Example request body**
none required

**Example response body**


-----

-----

-----

-----

#### List Available REST Resources

Use the Resources by Version resource to list the resources available for the specified API version. This provides the name and URI of
each additional resource.

**Example**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/ -H "Authorization:
  Bearer token"

```
**Example request body**
none required

**Example JSON response body**


-----

**Example XML response body**


-----

##### Further Information

[For information about the identity resource, see Identity URLs.](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_using_openid.htm&type=5&language=en_US)

For the other resources, see Reference .

#### Get a List of Objects

Use the Describe Global resource to list the objects available in your org and available to the logged-in user. This resource also returns
the org encoding, as well as maximum batch size permitted in queries.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/ -H
  "Authorization: Bearer token"

```
**Example request body**
none required

**Example response body**


-----

#### Get a List of Objects If Metadata Has Changed

Use the Describe Global resource and the `If-Modified-Since` HTTP header to determine if an object’s metadata has changed.

You can include the `If-Modified-Since` header with a date in `EEE, dd MMM yyyy HH:mm:ss z` format when you use
the Describe Global resource. If you do, response metadata is returned only if an available object’s metadata has changed since the
provided date. If no metadata has been modified since the provided date, a `304 Not Modified` status code is returned with no
response body.

The following example assumes that no changes have been made to objects after March 23, 2015.

**Example Describe Global request**
```
  /services/data/v62.0/sobjects

```
**Example** `If-Modified-Since` **header used with request**
```
  If-Modified-Since: Tue, 23 Mar 2015 00:00:00 GMT

```
**Example response body**
No response body returned

**Example response status code**
```
  HTTP/1.1 304 Not Modified
  Date: Wed, 25 Jul 2015 00:05:46 GMT

```
If changes to an object were made after March 23, 2015, the response body contains metadata for all available objects. For an example,
see Get a List of Objects.
