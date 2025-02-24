#### EnablementMeasureDefinition

Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome
in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter logic,
for tracking the activity. This object also represents Enablement measure information in Metadata API. This object is available in API
version 56.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

##### Fields

```
AggregateFieldApiName
AggregateFunction
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique name in the API for the field that the `AggregateFunction` uses for
calculating.

For example, if you’re measuring how much revenue a sales rep has won, the value of
`aggregateFunction` is `Sum` and the value of `aggregateFieldApiName` is
```
  Amount, which is the API name of the Amount field on the Opportunity object.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The method for calculating progress towards the milestone or outcome from records that
qualify for the measure’s criteria.

Possible values are:

**•** `Average`

**•** `Count`

**•** `Sum`

For example, if you’re measuring the number of deals won, the function is `Count.`

If the function is `Average` or `Sum, then` `AggregateFieldApiName` specifies the
API name of the field to use for calculating progress.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
An internal description for the measure to help Enablement admins understand the activity
that’s tracked.


-----

```
DeveloperName
DisplayFieldApiName
IsValid

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
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name in the API for the field that primarily identifies records that qualify for the
activity you’re measuring. For example, if you’re measuring the number of deals won, you’re
tracking the Opportunity object, and maybe you want to identify opportunities by their
name. In this case, this field can be `Name, the API name of the Opportunity Name field on`
the Opportunity object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the measure is valid. A measure becomes invalid and stops tracking
progress under these circumstances:

**•** An object or field is removed.

**•** An object label or API name is renamed.

**•** A field’s API name is renamed.

Default is `false. A measure only becomes invalid after a breaking change is saved the`
[corresponding outcome or milestone progress is calculated. See Considerations for Creating](https://help.salesforce.com/s/articleView?id=sf.enablement_measures_considerations.htm&language=en_US)
[and Editing Measures.](https://help.salesforce.com/s/articleView?id=sf.enablement_measures_considerations.htm&language=en_US)


-----

```
Language
MasterLabel
NamespacePrefix
PublishedDateTime

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label for this EnablementMeasureDefinition value. This display value is the internal label that
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
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the measure was activated for use in Enablement programs.


-----

```
SourceMeasureObjectId
SourceObjectApiName
Status

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the EnblMeasureObjectDefinition that specifies the criteria for the source object
that tracks the activity you're measuring. This field is a relationship field.

**Relationship Name**
SourceMeasureObject

**Relationship Type**
Lookup

**Refers To**
EnblMeasureObjectDefinition

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unique name in the API for the source object that tracks the activity you're measuring.
This value is a derived value. For example, if you're measuring the number of deals won, this
value is `Opportunity, the API name for the Opportunity object.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The availability of the measure for use in Enablement programs.

Possible values are:

**•** `Archived—Available in API versions 56.0 to 60.0.`

**•** `Draft—The measure is saved, but not activated for use in programs.`

**•** `Published—The measure is activated for use in programs. In Lightning Experience,`
this value is Active.


An EnablementMeasureDefinition can have multiple EnblMeasureObjectDefinition references, depending on the number of related
objects in the measure. Consider an example measure that tracks activity on the Opportunity source object and the Account related
object.

**•** The EnablementMeasureDefinition identifies the Opportunity source object.


-----

**•** An EnblMeasureObjectDefinition specifies the criteria on the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Account related object.
