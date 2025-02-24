#### FieldHistoryArchive

Represents field history values for all objects that retain field history. FieldHistoryArchive is a big object, available only to users
with the “Retain Field History” permission. This object is available in API version 29.0 and later.

Each instance of the FieldHistoryArchive object represents a single change in the value of a field. FieldHistoryArchive
stores history for both standard and custom fields.

The `Field` field returns the name of the field unless the parent field or object is deleted, in which case it returns the field ID. You can
use the ID to retrieve the old field and object name from the FieldNameAfterArchival and ParentNameAfterArchival
fields, respectively.


-----

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
**Field Name**
```
ArchiveFieldName
ArchiveParentName
ArchiveParentType
ArchiveTimestamp
CreatedById

```

**Type**
string

**Properties**
Nillable

**Description**
The name of the field at the time the data was archived. If the field name changed,
the name is sometimes not the same for all records related to a single field.

**Type**
string

**Properties**
Nillable

**Description**
The name of the parent object at the time the data was archived. If the object
name changed, the name is sometimes not the same for all records related to a
single field.

**Type**
string

**Properties**
Nillable

**Description**
The type of the field at the time the data was archived. If the field type changed,
the type is sometimes not the same for all records related to a single field.

**Type**
dateTime

**Properties**
Nillable

**Description**
The date and time at which the data was archived.

**Type**
reference

**Properties**
Nillable


-----

```
CreatedDate
Field
FieldHistoryType

```

**Description**
The user ID of the user who created the original record.

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**
The date and time at which the original record was created.

**Type**
picklist

**Properties**
Restricted picklist

**Description**
The name of the field that was changed. If the field is deleted from the parent
object, the `Field` field contains the field ID instead.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist, Sort

**Description**
The name of the object that contains the field history. Possible values are:

**•** `Account`

**•** `Article`

**•** `Asset`

**•** `AuthorizationFormConsent` – Available in version 58.0 and later.

**•** `Case`

**•** `CommSubscriptionConsent` – Available in version 58.0 and later.

**•** `Contact`

**•** `ContactPointConsent` – Available in version 58.0 and later.

**•** `ContactPointTypeConsent` – Available in version 58.0 and later.

**•** `Contract`

**•** `ContractLineItem`

**•** `Crisis`

**•** `Employee`

**•** `EmployeeCrisisAssessment`

**•** `Entitlement`

**•** `Individual`


-----

```
HistoryId
Id
NewValue

```


**•** `InternalOrganizationUnit`

**•** `Knowledge`

**•** `Lead`

**•** `Opportunity`

**•** `Order`

**•** `OrderItem`

**•** `PartyConsent` – Available in version 58.0 and later.

**•** `Pricebook2`

**•** `PricebookEntry`

**•** `Product2`

**•** `ServiceAppointment`

**•** `ServiceContract`

**•** `Solution`

**•** `WorkOrder`

**•** `WorkOrderLineItem`

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the relevant history object (for example, AccountHistory). This field is
available in versions 42.0 and later.

**Type**
ID

**Properties**
Defaulted on create, Filter, idLookup

**Description**
The ID of the archived record. It’s useful to have a field’s ID for fields that you’ve
deleted. (Field names aren’t retained in history when you delete fields from
Salesforce.)

**Type**
anyType

**Properties**
Nillable

**Description**
The new value of the modified field.


-----

```
OldValue
ParentId

##### Usage

```
When sorting fields, order them as follows:

**1. FieldHistoryType ASC**

**2. ParentID ASC**

**3. CreatedDate DESC**

SEE ALSO:


**Type**
anyType

**Properties**
Nillable

**Description**
The previous value of the modified field.

**Type**
reference

**Properties**
Filter, Sort

**Description**
The ID of the object that contains the field (the parent object).


_[Developer Guide:Big Objects Implementation Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.bigobjects.meta/bigobjects/big_object.htm)_
