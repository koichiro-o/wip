#### EmailStatus

Represents the status of email sent.

##### Supported Calls
```
describeSObjects()

 Special Access Rules

```
Customer Portal users can’t access this object.

##### Fields

```
EmailTemplateName
FirstOpenDate
LastOpenDate
TaskId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the EmailTemplate.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the email was first opened by recipient. Label is Date Opened.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the email was last opened by recipient.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The activity (task or event) associated with the email. Label is Activity ID.


-----

```
 TimesOpened
 WhoId

```
SEE ALSO:

EmailTemplate
