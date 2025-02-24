#### SurveyEmailBranding

Represents the configuration settings for invitation emails sent to survey participants for a particular survey.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object.

Note: You can’t define custom fields for the SurveyEmailBranding object using the Object Manager.

##### Fields

```
Body
DeveloperName
FooterImageId

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The body text of the invitation email.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique API name of the email branding configuration.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
FromEmailAddress
HeaderImageId
Language

```

**Description**
The ID of the content asset that appears in the footer of the invitation email.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The email address that appears in the “From” field when the invitation is sent to
participants.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the content asset that appears in the header of the invitation email.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the emails. Available languages include:

**•** Chinese (Simplified)

**•** Chinese (Traditional)

**•** Danish

**•** Dutch

**•** English

**•** Finnish

**•** French

**•** German

**•** Italian

**•** Japanese

**•** Korean

**•** Norwegian

**•** Portuguese (Brazilian)

**•** Russian

**•** Spanish

**•** Spanish (Mexican)


-----

```
MasterLabel
Subject

```


**•** Swedish

**•** Thai

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for these email configuration settings.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The subject of the invitation email.

