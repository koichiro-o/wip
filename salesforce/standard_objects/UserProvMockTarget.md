#### UserProvMockTarget

Represents an entity for testing user data before committing the data to a third-party system for user provisioning.

During the user provisioning process, user account information is sent to a third-party system to create, update or delete a user account
on that system. While configuring user provisioning for your organization using a flow or Apex action, you can use this object to confirm
the associated flow or Apex code is sending the desired data. After confirming the correct fields and values, you can update the flow or
Apex action to send the data to the target system.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ExternalEmail
ExternalFirstName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The first name as stored in the target system for the associated user account.


-----

```
ExternalLastName
ExternalUserId
ExternalUsername
Name
OwnerId
