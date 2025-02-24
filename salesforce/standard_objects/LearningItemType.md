#### LearningItemType

Represents a custom exercise type that an Enablement user takes in an Enablement program in the Guidance Center. A custom exercise
type also requires a corresponding LearningItem record for the Guidance Center and corresponding EnblProgramTaskDefinition and
EnblProgramTaskSubCategory records for when admins create a program in Program Builder. This object is available in API version 62.0
and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

Important: Custom exercises aren’t compatible with Partner Enablement programs.

##### Fields

```
ApexEvaluationHandlerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Apex class that specifies how progress and completion of the custom exercise
is assessed when users take the program in the Guidance Center.

This field is a relationship field.

**Relationship Name**
ApexEvaluationHandler


-----

```
ApexSerializerDeserializerId
CustomField
CustomObject

```

**Refers To**
ApexClass

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Apex class that specifies how data related to the custom exercise type is retrieved
and deployed with change sets or managed packages.

This field is a relationship field.

**Relationship Name**
ApexSerializerDeserializer

**Refers To**
ApexClass

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The programmatic name of a custom lookup field on the LearningItem object that references
the custom object used with this custom exercise. Add values to this picklist when you
implement a custom exercise type.

For example, if a custom exercise type shows a screen flow, maybe the custom object’s name
is `ScreenFlow_Object__c` and the custom field on LearningItem is named
```
  ScreenFlow_Field__c. For details, see Implement Custom Exercise Types for

```
[Enablement Programs in the Sales Programs and Partner Tracks with Enablement Developer](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
_Guide._

This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The programmatic name of the custom object used with this custom exercise. Add values
to this picklist when you implement a custom exercise type.

For example, if a custom exercise type shows a Quip document, maybe the custom object’s
name is `ScreenFlow_Object__c. For details, see Implement Custom Exercise Types`


-----

```
DeveloperName
Icon
Language
LightningComponentName

```

[for Enablement Programs in the Sales Programs and Partner Tracks with Enablement Developer](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
_Guide._

This field is unique within your organization.

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
textarea

**Properties**
Create, Update

**Description**
The icon to use for the custom exercise type in the Guidance Center.

Use the format `iconType:iconName, where the values correspond to icon categories`
[and names from the Salesforce Lightning Design System.](https://www.lightningdesignsystem.com/icons/)

**•** `iconType` is the type of icon, such as `standard` or `doctype.`

**•** `iconName` is the icon name, such as `flow` or `slide.`

For example, to use the Standard type Flow icon, this value is `standard:flow.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string


-----

```
MasterLabel
NamespacePrefix

```

**Properties**
Filter, Nillable, Sort

**Description**
The name, including the namespace, of the Lightning Web Component (LWC) used to show
the custom exercise’s content when a user opens the exercise in the Guidance Center. For
example, if the LWC for a screen flow custom exercise is named `screenFlowViewer,`
this value is `c:screenFlowViewer.`

This field can only be accessed from Metadata API and its value is derived from the
`lightningComponentDefinition` [field on the LearningItemType metadata type.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_learningitemtype.htm)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this LearningItemType value. This display value is the internal label that doesn't get
translated.

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


-----
