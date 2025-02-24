#### UnifiedActivityRelation

Represents a relationship between an activity and a related record that’s a target or topic of the activity. For example, a related record
can be an opportunity, account, and so on. This object is available for reports and dashboards in the Winter ’24 release and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```
Note: This object is available only for reporting. It isn’t supported for SOQL queries and APIs.

##### Special Access Rules

Einstein Activity Capture and Activity 360 Reporting must be enabled.

##### Fields

```
ActivityId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the activity. This field is a polymorphic relationship field.


-----

```
RelatedId

```

**Relationship Name**
Activity

**Relationship Type**
Lookup

**Refers To**
UnifiedActivity, UnifiedVideoCall, UnifiedVoiceCall

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the related record. This field is a polymorphic relationship field.

**Relationship Name**
Related

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Contract, Lead, Opportunity, User

