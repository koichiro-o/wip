#### ExternalAccountHierarchyHistory

Represents the history of changes to values in the fields of an external account hierarchy. This object is available in API version 50.0 and
later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

You must have a Partner or Customer Community Plus license.

##### Fields

```
DataType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Possible values are:

**•** Address

**•** AnyType

**•** AutoNumber

**•** Base64

**•** BitVector

**•** Boolean

**•** Content

**•** Currency

**•** DataCategoryGroupReference

**•** DateOnly

**•** DateTime

**•** Division

**•** Double

**•** DynamicEnum

**•** Email

**•** EncryptedBase64

**•** EncryptedText


-----

```
ExternalAccountHierarchyId
Field

```


**•** EntityId

**•** EnumOrId

**•** ExternalId

**•** Fax

**•** File

**•** HtmlMultiLineText

**•** HtmlStringPlusClob

**•** InetAddress

**•** Json

**•** Location

**•** MultiEnum

**•** MultiLineText

**•** Namespace

**•** Percent

**•** PersonName

**•** Phone

**•** Raw

**•** RecordType

**•** SfdcEncryptedText

**•** SimpleNamespace

**•** StringPlusClob

**•** Switchable_PersonName

**•** Text

**•** TimeOnly

**•** Url

**•** YearQuarter

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the external account hierarchy.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


-----

```
NewValue
OldValue

```

**Description**
Possible values are:

**•** Account

**•** HierarchyType - Hierarchy Type

**•** IsAccessibleToParent - Is Accessible to Parent

**•** IsActive - Is Hierarchy Active

**•** Name

**•** Owner

**•** Parent

**•** Created - Created.

**•** FeedEvent - Feed Event

**•** IndividualMerged - Individual Merged

**•** Locked - Record Locked

**•** OwnerAccepted - Owner (Accepted)

**•** OwnerAssignment - Owner (Assignment)

**•** Unlocked - Record unlocked

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The updated value of the changed field.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The previous value of the changed field.

