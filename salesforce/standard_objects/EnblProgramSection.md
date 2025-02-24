#### EnblProgramSection

Represents an optional section in an Enablement program. A section can include other program items, such as milestones and exercises.
This object is available in API version 60.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=sf.prm_support_license_template.htm&language=en_US)


-----

##### Fields

**Field**
```
DeveloperName
EnablementProgramId
Name
SequenceNumber

```

**Type**
string

**Properties**
Filter, Group, Sort

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

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The Enablement program that contains the section. This field is a relationship field.

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the section that’s visible to users when they take the program.

**Type**
int


-----

**Properties**
Filter, Group, Sort

**Description**
A number that specifies the order of the section, relative to other sections, starting at 0.
