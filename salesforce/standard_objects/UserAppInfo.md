#### UserAppInfo

Stores the last Lightning app logged in to. If the user hasn’t logged into Salesforce or if the user lost access to the last accessed app, the
UserAppInfo object stores a Null value. This object is available in API version 38.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
AppDefinitionId
FormFactor

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the last Lightning app that the user logged in to. This field is available
in API version 43.0 and later.

This is a relationship field.

**Relationship Name**
AppDefinition

**Relationship Type**
Lookup

**Refers To**
AppDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The relative size of the app as displayed. Values are:

**•** Small—suitable for a small device like a mobile phone

**•** Medium—suitable for a tablet

**•** Large—suitable for a large display device, like a monitor

It’s possible to have three versions of the app as the one last logged in to, where
each version has a different form factor.


-----

```
UserId

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user that used this app.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserAppInfoChangeEvent (API version 62.0)**
Change events are available for the object.
