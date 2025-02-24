#### LegalEntity

```

**Refers To**
Survey

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of feedback used with this exercise. Possible values are:

**•** `AIFeedback—Users submit a video call, and Einstein Coach generates feedback from`
the call’s transcription. With this type, `PromptTemplate` is required.

**•** `PeerFeedback—Users submit a URL to a sample of their work, and select peers and`
managers to review their work. Selected peers and managers complete an assessment
survey. With this type, `SurveyId` is required.

Available in API version 61.0 and later.


Represents the way an organization is structured. An organization can be a single legal entity or it can comprise more than one legal
entity. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with Salesforce Billing.

##### Fields

```
CompanyName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the company that this legal entity represents.


-----

```
Description
LastReferencedDate
LastViewedDate
LegalEntityAddress
Name
OwnerId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the legal entity.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address of the company that this legal entity represents. This field is a compound field
of type Address and combines these fields: LegalEntityCity, LegalEntityCountry,
LegalEntityGeocodeAccuracy, LegalEntityLatitude, LegalEntityLongitude,
LegalEntityPostalCode, LegalEntityState, and LegalEntityStreet. For more information, see
[Address Compound Fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/compound_fields_address.htm)

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the legal entity.

**Type**
reference


-----

```
 Status

##### Associated Objects

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the legal entity.

Possible values are:

**•** `Active`

**•** `Inactive`


This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**LegalEntityFeed**

Feed tracking is available for the object.

**LegalEntityHistory**

History is available for tracked fields of the object.

**LegalEntityOwnerSharingRule**

Sharing rules are available for the object.

**LegalEntityShare**

Sharing is available for the object.
