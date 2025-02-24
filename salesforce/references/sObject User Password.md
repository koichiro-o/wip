### sObject User Password

```
Accesses user passwords based on the specified user ID. Sets, resets, or gets the expiration status of a user password based on the HTTP
method. Use the GET method to retrieve a password’s expiration status, the POST method to set a password, or the DELETE method to
initiate a password reset.

IN THIS SECTION:

Get User Password Expiration Status
Gets a user’s password expiration status based on the specified user ID. A True or False value is returned in the response body. This
resource is available in REST API version 24.0 and later.

Set User Password
Sets a user’s password based on the specified user ID. The password provided in the request body replaces the user’s existing
password. This resource is available in REST API version 24.0 and later.

Reset User Password
Initiates a password reset for a user based on the specified user ID. The user’s current password becomes invalid and the user receives
an email with a password reset link. To log in again, the user must finish resetting their password. This resource is available in REST
API version 24.0 and later.


-----

Return Headers Using sObject User Password
Returns only the headers that are returned by sending a GET request to the sObject User Password resource. This operation allows
you to see returned header values of the GET request before retrieving the content itself. This resource is available in REST API version
24.0 and later.

#### Get User Password Expiration Status

Gets a user’s password expiration status based on the specified user ID. A True or False value is returned in the response body. This
resource is available in REST API version 24.0 and later.

If the session doesn’t have permission to access the user information, an INSUFFICIENT_ACCESS error is returned.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/User/userId/password

```
**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

##### Example

For examples of getting password information, setting a password, and resetting a password, see Manage User Passwords on page 83.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Set User Password

Sets a user’s password based on the specified user ID. The password provided in the request body replaces the user’s existing password.
This resource is available in REST API version 24.0 and later.

You can only set one password per request. The new password must conform to the password policies for the organization, otherwise
an INVALID_NEW_PASSWORD error is returned.

If the session doesn’t have permission to access the user information, an INSUFFICIENT_ACCESS error is returned.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/User/userId/password

```
**Formats**
JSON, XML


-----

**HTTP Method**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

##### Example

For examples of getting password information, setting a password, and resetting a password, see Manage User Passwords on page 83.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)

#### Reset User Password

Initiates a password reset for a user based on the specified user ID. The user’s current password becomes invalid and the user receives
an email with a password reset link. To log in again, the user must finish resetting their password. This resource is available in REST API
version 24.0 and later.

Salesforce auto-generates a temporary password for the user and returns it in the response body. If the user can’t access the email link,
they can finish resetting their password by logging in with the temporary password.

If the session doesn’t have permission to access the user information, an INSUFFICIENT_ACCESS error is returned.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/User/userId/password

```
**Formats**
JSON, XML

**HTTP Method**
DELETE

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

##### Example

For examples of getting password information, setting a password, and resetting a password, see Manage User Passwords on page 83.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)


-----

#### Return Headers Using sObject User Password

Returns only the headers that are returned by sending a GET request to the sObject User Password resource. This operation allows you
to see returned header values of the GET request before retrieving the content itself. This resource is available in REST API version 24.0
and later.

If the session doesn’t have permission to access the user information, an INSUFFICIENT_ACCESS error is returned.

##### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/User/userId/password

```
**Formats**
JSON, XML

**HTTP Method**
HEAD

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
None required

##### Example

For examples of getting password information, setting a password, and resetting a password, see Manage User Passwords on page 83.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)
