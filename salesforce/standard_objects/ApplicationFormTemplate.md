#### ApplicationFormTemplate

Represents the fields to capture application metadata as a template which is used in application tracking and processing. This object is
available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only with the EAndU Cloud Program Access permission set.

##### Fields

```
ApprovalFlowName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ApplicationType
ApprovalLimitAmount
ApprovalFlowName
ApproverId

```

**Description**
The name of the flow that must be launched to approve the applications associated with
the application form template.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of application or template.

Possible values are:

**•** `Contractor`

**•** `EVCharger—EV Charger`

**•** `EnergyEfficiency—Energy Efficiency`

**•** `NewConnection—New Connection`

The default value is `NewConnection.`

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Amount up to which the approver has the authority to approve applications.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the flow that must be launched to approve the applications associated with
the application form template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user who must approve the application payout.

This field is a relationship field.

**Relationship Name**
Approver


-----

```
Description
Name

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the application form template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the application form template.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[ApplicationFormTemplateChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ApplicationFormTemplateFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[ApplicationFormTemplateHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ApplicationFormTemplateOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ApplicationFormTemplateShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
