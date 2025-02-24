#### ContentHubRepository

Represents a Files Connect external data source such as Microsoft SharePoint or OneDrive for Business. This object is available in API
version 33.0 and later.

##### Special Access Rules

Chatter and Files Connect must be enabled for the organization.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

 Fields

```
```
DeveloperName
MasterLabel
Type

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the record in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is automatically generated but you can supply
your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no DeveloperName is specified,
performance may slow while Salesforce generates one for each record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for the external data source. This display value is the internal label
and does not get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
The data source type. Possible values are:

**•** `contenthubGoogleDrive`

**•** `contenthubOffice365`

**•** `contenthubOneDrive`

**•** `contenthubSharepoint`

**•** `contenthubBox`

**•** `contenthubQuip`
