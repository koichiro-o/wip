#### AiModelLanguage

An object that stores language related information that is generated for each AI model. This object is available in API version 55.0 and
later.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Special Access Rules

```
For Einstein Reply Recommendations:

Requires the Einstein Reply Recommendations org permissions, Einstein Reply Recommendations org pref, and Admin user or user with
Einstein Reply Manager permissions.

##### Fields

```
ApplicationType
ExternalAiModelId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of application using the AI model.

Possible values are:

**•** `ARTICLE_RECOMMENDATION`

**•** `EAR_FOR_CONVERSATION`

**•** `EAR_FOR_VOICE`

**•** `FAQ`

**•** `REPLY_RECOMMENDATION`

**•** `USE_CASE_EXPLORER`

**•** `UTTERANCE_RECOMMENDATION`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the AI model used to generate predictions.

This field is a relationship field.

**Relationship Name**
ExternalAiModel

**Relationship Type**
Lookup

**Refers To**
ExternalAIModel


-----

```
Language
Name
ServingStatus
TranscriptCount

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Languages supported by this AI model.

Possible values are:

**•** `Arabic`

**•** `Chinese-simplified`

**•** `Chinese-traditional`

**•** `Dutch`

**•** `English`

**•** `French`

**•** `German`

**•** `Italian`

**•** `Japanese`

**•** `Korean`

**•** `Polish`

**•** `Portuguese`

**•** `Russian`

**•** `Spanish`

**•** `Thai`

**•** `Turkish`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
AI model name.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines if the language is enabled or disabled for this AI model.

**Type**
int


-----

**Properties**
Filter, Group, Sort

**Description**
Transcript count detected for each language.
