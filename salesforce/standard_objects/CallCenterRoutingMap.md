#### CallCenterRoutingMap

Stores a mapping between a user or queue in a Salesforce org to a user or queue in an external system’s call center. This object is available
in API version 53.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
CallCenterId
DeveloperName
ExternalId
Language

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to a call center.

This is a relationship field.

**Relationship Name**
CallCenter

**Relationship Type**
Lookup

**Refers To**
CallCenter

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name is a combination of the Salesforce user ID or queue name, and the call
center ID, with an underscore between these two values.

**•** `[SALESFORCE_USER_ID]_[CALL_CENTER_ID]`

**•** `[SALESFORCE_QUEUE_NAME]_[CALL_CENTER_ID]`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique identifier for the external system’s user or queue.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
MasterLabel
QuickConnect
ReferenceRecordId

```

**Description**
The language of the MasterLabel.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the CallCenterRoutingMap.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Amazon Connect QuickConnectId ARN used to determine agent availability for
Omni-Channel call transfers. Available in API version 56.0 and later.

This is a polymorphic relationship field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Lookup field to a Salesforce user or queue.

This is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Group, User

