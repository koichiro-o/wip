#### CustomBrand

Represents a custom branding and color scheme. This object is available in API version 28.0 and later.


-----

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
This object is available only when your org has digital experiences enabled.

##### Fields

```
ParentId

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the parent entity that this branding applies to. The parent entity can
be an Experience Cloud site, organization, topic, or reputation level.

The branding applies to the entity that the ParentId references. For example,
if the `ParentId` references a network ID, the branding applies to that
Experience Cloud site only, and if the `ParentId` references an organization
ID, the branding applies to the organization that it is accessed through, and so
on. Label is `Branded Entity ID.`


Use this object along with CustomBrandAsset to apply a custom branding scheme to your Experience Cloud site. The branding scheme
for the site shows in both the user interface and in the Salesforce mobile app. You must have Create and Manage Experiences to customize
site branding.

You can also use this object to apply a custom branding scheme to your org when it is accessed through the Salesforce mobile app.

SEE ALSO:

Network
