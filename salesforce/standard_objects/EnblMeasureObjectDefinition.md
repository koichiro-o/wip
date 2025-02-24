#### EnblMeasureObjectDefinition

Represents the criteria for an object that tracks the job-related activity for an Enablement measure in an Enablement program. A separate
EnblMeasureObjectDefinition is used for a measure's source object and each optional related object. This object is available in API version
56.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

##### Fields

```
DeveloperName
EnablementMeasureDefinitionId
FilterLogic

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The measure that the EnblMeasureObjectDefinition applies to. This field is a relationship
field.

**Relationship Name**
EnablementMeasureDefinition

**Relationship Type**
Lookup

**Refers To**
EnablementMeasureDefinition

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Language
MasterLabel
NamespacePrefix
ObjectApiName

```

**Description**
An expression that determines how to evaluate the optional field filters for the object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the EnblMeasureObjectDefinition value. This display value is the internal label that
doesn't get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
SequenceNumber

##### Usage

```

**Description**
The unique name in the API for the measure's source object or optional related object that
the EnblMeasureObjectDefinition describes.

For example, if you're measuring the number of deals won for a specific product, this field
on one EnblMeasureObjectDefinition references the API name of the Opportunity source
object and this field on another EnblMeasureObjectDefinition references the API name of
the Opportunity Product related object.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A number that specifies the order of the EnblMeasureObjectDefinition, relative to other
EnblMeasureObjectDefinition records under the same EnablementMeasureDefinition, starting
at 1.


An EnablementMeasureDefinition can have multiple EnblMeasureObjectDefinition references, depending on the number of related
objects in the measure. Consider an example measure that tracks activity on the Opportunity source object and the Account related
object.

**•** The EnablementMeasureDefinition identifies the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Account related object.
