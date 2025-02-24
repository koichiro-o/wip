#### NetworkDiscoverableLogin

Represents the Login Discoverable page from where customers and partners log in to an Experience Cloud site. Customers and partners
are users with an External Identity license or any communities license for Experience Cloud. This object is available in API version 44.0
and later.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(), upsert()

 Fields

```
```
ApexHandlerId
ExecuteApexHandlerAsId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the Apex handler created by the Login Discovery page type.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the user who is executing the handler.


-----

```
NetworkId
UsernameLabel

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

Unique

**Description**

The ID of `NetworkId` is unique within your org.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Log in prompt on login page when the login page type is Login Discovery.


Use this object to access the Login Discovery Page, which is a login page type that prompts users to identify themselves with an email
address, phone number, or custom identifier. DiscoverableLogin performs an interview-based login process, where users are first prompted
to provide identity and then authenticated. For example, users receive a verification code that they enter to complete the login process.

Note: The NetworkDiscoverableLogin object is created when Login Discovery Page is selected as the login page type on the
Login & Registration (L&R) page. If you later switch to another login page type, such as a Visualforce Page or Experience Builder
Page, the object isn’t deleted. The object persistence means you can’t delete the Apex class associated with the
NetworkDiscoverableLogin object. To delete the Apex class, return to the L&R page and change the login page type back to Login
**Discovery page. Select another Apex class, and then you can delete the first one.**
