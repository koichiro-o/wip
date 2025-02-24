#### AuthorizationForm

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID for this configuration.

This is a relationship field.

**Relationship Name**
AuthConfig

**Relationship Type**
Lookup

**Refers To**
AuthConfig

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the Auth. Provider or SAML configuration.

This is a polymorphic relationship field.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider, SamlSsoConfig


Represents the specific version and effective dates of a form that is associated with consent, such as a privacy policy or terms and
conditions. This object is available in API version 46.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is available if Data Protection and Privacy is enabled.

##### Fields

```
DefaultAuthFormTextId
EffectiveFromDate
EffectiveToDate
IsSignatureRequired

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the default authorization form text to use if text isn’t available
for a specific language.

This is a relationship field.

**Relationship Name**
DefaultAuthFormText

**Relationship Type**
Lookup

**Refers To**
AuthorizationFormText

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the authorization form takes effect.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the authorization form is no longer in effect.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the authorization form requires a signature.


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
RevisionNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced (LastReferencedDate)
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the authorization form.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The revision number of the authorization form. For example, "rev1.21."

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormChangeEvent (API version 61.0)**
Change events are available for the object.

**AuthorizationFormHistory**

History is available for tracked fields of the object.

**AuthorizationFormOwnerSharingRule**

Sharing rules are available for the object.

**AuthorizationFormShare**

Sharing is available for the object.
