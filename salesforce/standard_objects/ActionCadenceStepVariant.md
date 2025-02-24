#### ActionCadenceStepVariant

Represents an email template or call script variant associated with an action cadence step. Email and call steps can have up to 3 variants
associated so sales teams can compare the engagement results. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
Sales Engagement and Allow Email Template and Call Script Variant Testing must be enabled.

##### Fields

```
ActionCadenceStepId
SplitPercentage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related action cadence step.

This is a relationship field.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStep

**Type**
percent


-----

```
TemplateId
Type

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage of emails to send or calls to make using this email template or call script
variant. The total for all variants must be 100%.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the associated email template or call script.

This is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated action cadence step.

Possible values are:

**•** `AutoSendAnEmail`

**•** `Branch`

**•** `CreateTask`

**•** `DaisyChain`

**•** `LinkedInConnection`

**•** `LinkedInMail`

**•** `ListenerBranch`

**•** `MakeACall`

**•** `PlatformScreenFlow—Available in version 55.0 and later.`

**•** `Root`

**•** `SendAnEmail`

**•** `Wait`

Only email and call steps can have an associated action cadence step variant.


-----

##### Usage

Use ActionCadenceStepVariant to retrieve the email template or call script for an action cadence step:
```
SELECT SplitPercentage, TemplateId FROM ActionCadenceStepVariant WHERE
ActionCadenceStepId=:[idValue]

```
Use ActionCadenceStepVariant to retrieve the call scripts from all call steps:
```
SELECT SplitPercentage, TemplateId, ActionCadenceStepId FROM ActionCadenceStepVariant WHERE
 Type='MakeACall'
