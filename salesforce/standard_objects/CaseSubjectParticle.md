#### CaseSubjectParticle

Represents the Social Business Rules custom format for the Case Subject field on cases created from inbound social posts. This object
is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
DeveloperName
Index

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for the CaseSubjectParticle object.

This name can contain only underscores and alphanumeric characters, and must be unique
in your org. It must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. This field is automatically generated, but you can
supply your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
Language
MasterLabel

```

**Description**
Required. The order in which the custom Case Subject is generated, meaning if the social
network is 0 and the social message is 1, then the subject generates as `Twitter |`
```
  Tweet.

```
**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the case subject field.

Possible values are:

**•** `ar—Arabic`

**•** `da—Danish`

**•** `de—German`

**•** `en_US—English`

**•** `es—Spanish`

**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`

**•** `iw—Hebrew`

**•** `ja—Japanese`

**•** `ko—Korean`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the case subject field.


-----

```
TextField
Type

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies inbound social content added to Case Subject in case records.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Specifies the custom Case Subject format from which inbound social content
appears in case records.

Possible values are:

**•** `ColonSeparator`

**•** `Content—Message`

**•** `HyphenSeparator`

**•** `MessageType`

**•** `PipeSeparator`

**•** `ProvidedString`

**•** `RealName`

**•** `Sentiment`

**•** `SocialHandle`

**•** `SocialNetwork`

**•** `Source`


In the Salesforce UI, case subjects are brief descriptions of cases. They are what agents see on cases first. Social Business Rules specify
the brief descriptions of cases created from social posts. Using CaseSubjectParticle objects you can build your own case subject format,
where each object represents a social post's component. For example, combining CaseSubjectParticle objects with components for
types `MessageType,` `RealName, and` `SocialNetwork` results in "Tweet Customer123 Twitter".
