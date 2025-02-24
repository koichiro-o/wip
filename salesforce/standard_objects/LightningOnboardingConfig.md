#### LightningOnboardingConfig

Represents the feedback provided when users switch from Lightning Experience to Salesforce Classic. Admins can customize the question,
how frequently the form appears, and where the feedback is stored in Chatter from the Adoption Assistance page in Lightning Experience
Setup. Available in API version 47.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

[See Switch to Salesforce Classic Feedback Form in Salesforce Help for more details.](https://help.salesforce.com/articleView?id=lex_encourage_work_feedback.htm&language=en_US)

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
CollaborationGroupId
CustomQuestion

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Chatter Group where the user feedback is posted.

This is a relationship field.

**Relationship Name**
CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
CollaborationGroup

**Type**
textarea


-----

```
DeveloperName
FeedbackFormDaysFrequency
IsCustom
Language

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text of the custom question added by the admin. Maximum of 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of days between showing the feedback form when a user switches. A value of
```
  0 indicates that the form is shown for every switch. Maximum of 30.

```
**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if a feedback form includes a custom question `yes` or not `no.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
MasterLabel
PromptDelayTime
SendFeedbackToSalesforce

```

**Description**
Indicates the language used in the org where the feedback form was created.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the prompt. Maximum of 80 characters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the amount of time in seconds to delay between instances of all prompts, both
org- and Salesforce-created. Minimum of 0 hours and 0 minutes. Maximum of 99 hours and
59 minutes.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the user feedback can be shared with Salesforce. If yes, share the feedback with
Salesforce. If no, the feedback is only shared in the Chatter Group chosen when customizing
the form. The default value is `false.`

