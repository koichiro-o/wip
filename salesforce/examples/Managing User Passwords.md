### Managing User Passwords

The examples in this section use REST API resources to manage user passwords, such as setting or resetting passwords.

IN THIS SECTION:

Manage User Passwords
Use the sObject User Password resource to set, reset, or get information about a user password. Use the HTTP GET method to get
password expiration status, the HTTP POST method to set the password, and the HTTP DELETE method to reset the password.

#### Manage User Passwords

Use the sObject User Password resource to set, reset, or get information about a user password. Use the HTTP GET method to get password
expiration status, the HTTP POST method to set the password, and the HTTP DELETE method to reset the password.

The associated session must have permission to access the given user password information. If the session does not have proper
permissions, an HTTP error 403 response is returned from these methods.

These methods are available for both users and self-service users. For managing self-service user passwords, use SelfServiceUser
instead of `User` in the REST API URL.

Here is an example of retrieving the current password expiration status for a user:

**Example usage for getting current password expiration status**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/User/005D0000001KyEIIA0/password
   -H "Authorization: Bearer token"

```
**Example request body for getting current password expiration status**
None required

**JSON example response body for getting current password expiration status**
```
  {
    "isExpired" : false
  }

```
**XML example response body for getting current password expiration status**


-----

**Example error response if session has insufficient privileges**
```
  {
    "message" : "You do not have permission to view this record.",
    "errorCode" : "INSUFFICIENT_ACCESS"
  }

```
Here is an example of changing the password for a given user:

**Example usage for changing a user password**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/User/005D0000001KyEIIA0/password
   -H "Authorization: Bearer token" —H "Content-Type: application/json" —d @newpwd.json
  —X POST

```
**Contents for file newpwd.json**
```
  {
    "NewPassword" : "myNewPassword1234"
  }

```
**Example response for changing a user password**
No response body on successful password change, HTTP status code 204 returned.

**Example error response if new password does not meet organization password requirements**
```
  {
    "message" : "Your password must have a mix of letters and numbers.",
    "errorCode" : "INVALID_NEW_PASSWORD"
  }

```
And finally, here is an example of resetting a user password:

**Example usage for resetting a user password**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/User/005D0000001KyEIIA0/password
   -H "Authorization: Bearer token" —X DELETE

```
**Example request body for resetting a user password**
None required

**JSON example response body for resetting a user password**
```
  {
    "NewPassword" : "2sv0xHAuM"
  }

```
**XML example response body for resetting a user password**
```
  <Result>
    <NewPassword>2sv0xHAuM</NewPassword>
  </Result>

```
SEE ALSO:

sObject User Password


-----
