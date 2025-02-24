#### ExtKnowledgeConnector

Represents a connector to a third-party knowledge source for Unified Knowledge. This object is available in API version 60.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Knowledge must be enabled in your org. Salesforce Knowledge users, unlike customer and partner users, must also be granted
the Knowledge User feature license.

##### Fields

```
IsLocked

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated action condition record is locked or not.

The default value is `false.`


-----

```
LastSyncDate
LastSyncStatus
MayEdit
Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the connector last synced with the third-party knowledge source to import
articles into Salesforce.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the connector’s last sync of articles from the third-party knowledge
source into Salesforce.

Possible values are:

**•** `articleLimitExceeded—Exceeded Article or Version Limits`

**•** `completed—Completed`

**•** `completedWithErrors—Completed With Errors`

**•** `ended—Ended`

**•** `failed—Failed`

**•** `initiating—Started`

**•** `invalidCredentials—Invalid Credentials`

**•** `queued—Queued`

**•** `syncing—Syncing`

**•** `timedOut—Timed Out`

**•** `unavailable—Zoomin Unavailable`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the automated import article condition record can be edited or not.

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


-----

```
NamedCredentialId
OwnerId
PartnerConnectorIdentifier
ShouldOpenInSource

```

**Description**
The connector’s label in Unified Knowledge setup.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salesforce ID of the named credential that’s used for a request. The named credential identifies
the third-party system and the third-party authentication settings.

This field is a relationship field.

**Relationship Name**
NamedCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The user ID of the owner of the connector.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
boolean


-----

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether articles imported into Salesforce open in the third-party source from links
in Salesforce.

The default value is `false.`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ExtKnowledgeConnectorOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ExtKnowledgeConnectorShare on page 66**
Sharing is available for the object.
