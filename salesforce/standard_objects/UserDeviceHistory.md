#### UserDeviceHistory

Represents tracking information on the UserDevice sObject. This object is available in API version 50.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Fields

```
DataType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data that has changed.

Possible values are:

**•** `Address`

**•** `AnyType`

**•** `AutoNumber`

**•** `Base64`

**•** `BitVector`

**•** `Boolean`

**•** `Content`

**•** `Currency`

**•** `DataCategoryGroupReference`

**•** `DateOnly`

**•** `DateTime`

**•** `Division`

**•** `Double`


-----

```
Field

```


**•** `DynamicEnum`

**•** `Email`

**•** `EncryptedBase64`

**•** `EncryptedText`

**•** `EntityId`

**•** `EnumOrId`

**•** `ExternalId`

**•** `Fax`

**•** `File`

**•** `HtmlMultiLineText`

**•** `HtmlStringPlusClob`

**•** `InetAddress`

**•** `Json`

**•** `Location`

**•** `MultiEnum`

**•** `MultiLineText`

**•** `Namespace`

**•** `Percent`

**•** `PersonName`

**•** `Phone`

**•** `Raw`

**•** `RecordType`

**•** `SfdcEncryptedText`

**•** `SimpleNamespace`

**•** `StringPlusClob`

**•** `Switchable_PersonName`

**•** `Text`

**•** `TimeOnly`

**•** `Url`

**•** `YearQuarter`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The field that has changed.

Possible values are:


-----

```
NewValue
OldValue
UserDeviceId

```


**•** `BrowserType—Browser`

**•** `DeviceNativeUid—Device Native ID`

**•** `DeviceType—Device Type`

**•** `HashedBrowserFingerPrint—Hashed Browser Fingerprint`

**•** `IsVerified—Is Device Verified`

**•** `LastLoginHistory—Login History`

**•** `Name`

**•** `PlatformType—Platform or OS Type`

**•** `PlatformVersion—Platform or OS Version`

**•** `RawBrowserFingerPrint—Raw Browser Fingerprint Data`

**•** `Status—Device Status`

**•** `User`

**•** `UserLastSeen—Last time user was seen`

**•** `UserProvidedDeviceIdentifier—User provided device identifier`

**•** `created—Created.`

**•** `feedEvent—Feed event`

**•** `individualMerged—Individual Merged`

**•** `locked—Record locked.`

**•** `ownerAccepted—Owner (Accepted)`

**•** `ownerAssignment—Owner (Assignment)`

**•** `unlocked—Record unlocked.`

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value after a change has occurred.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value before a change has occurred.

**Type**
reference

**Properties**
Filter, Group, Sort


-----

**Description**
The ID of the UserDevice object.
