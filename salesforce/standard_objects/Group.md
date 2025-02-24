#### Group

```
A set of User records.


**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The ID of the user who currently owns this Google Document. Default value is the
user logged in to the API to perform the create.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the attachment's parent object. The following objects are supported
as parents of Google documents: Account, Asset, Campaign, Case, Contact, Contract,
Custom Object Behavior, Lead, Opportunity, Product2, and Solution.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The URL of the Google document.


Groups are sets of users. They can contain individual users, other groups, the users in a particular role or territory, or the users in a particular
role or territory plus all the users below that role or territory in the hierarchy.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), search(), retrieve(),
update(), upsert()

 Special Access Rules

```
Authenticated internal and external users can access this object.


-----

##### Fields

**Field**
```
Description
DefaultDivision
DeveloperName
 DoesIncludeBosses

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the group. This field is available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
This record’s default division. Only applicable if divisions are enabled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores. In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a managed
package and the changes are reflected in a subscriber’s organization. This name is unique
by group type and corresponds to Group Name in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Only your Salesforce org’s internal users can access this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether records shared with users in this group are also shared with users
higher in the role hierarchy (true) or not (false). This field is only available for public


-----

```
DoesSendEmailToMembers
Email
Name
OwnerId
QueueRoutingConfigId

```

groups. This field corresponds to the Grant Access Using Hierarchies checkbox in Setup.
This field is available in API version 18.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email is sent (true) or not sent (false) to the group members.
The email is sent to queue members as well.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address for a group of type Case. Applies only for a case queue.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the group. Corresponds to Label on the user interface.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns the group.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Organization, User

**Type**
reference


-----

```
RelatedId
Type

```

**Properties**
Create, Delete, Query, Retrieve, Update

**Description**
The ID of the queue routing configuration associated with the queue.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of the associated groups. For groups of type “Role,” the ID of the
associated UserRole. The `RelatedId` field is polymorphic.

This is a polymorphic relationship field.

**Relationship Name**
Related

**Relationship Type**
Lookup

**Refers To**
User, UserRole

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. Type of the group. One of the following values:

**•** `AllCustomerPortal—Public group that includes all Customer Portal or`
Customer Community Plus users. This type is only available when a Customer Portal
or a Customer Site is enabled for your org.

**•** `ChannelProgramGroup—Public group for partners in a channel program.`

**•** `CollaborationGroup—Chatter group.`

**•** `Manager—Public group that includes a user’s direct and indirect managers. This`
group is read-only.

**•** `ManagerAndSubordinatesInternal—Public group that includes a user`
and the user’s direct and indirect reports. This group is read-only.

**•** `Organization—Public group that includes all the User records in the`
organization. This group is read-only.

**•** `Participant—Compliant Data Sharing group that includes internal users who`
have the Use Compliant Data Sharing permission. A group can contain other
participant groups only, or a group can contain both internal users with the Use


-----

Compliant Data Sharing permission and other participant groups. This value is only
available when Compliant Data Sharing is enabled for your org.

**•** `PRMOrganization—Public group that includes all the partners in an organization`
that has the partner site or portal feature enabled.

**•** `Queue—Public group that includes all the User records that are members of a`
queue.

**•** `Regular—Standard public group. When you create()` a group, its type must
be Regular, unless a partner site or portal is enabled for the organization, in which
case the type can be `Regular` or `PRMOrganization.`

**•** `Role—Public group that includes all the User records in a particular UserRole.`

**•** `RoleAndSubordinates—Public group that includes all the User records in a`
particular UserRole and all the User records in any subordinate UserRole. The
availability of this value depends on the type of org, org creation date, release update
enforcement status, and whether digital experiences is enabled. For more information,
[see this knowledge article.](https://help.salesforce.com/s/articleView?language=en_US&id=002628970&type=1)

**•** `RoleAndSubordinatesInternal—Public group that includes all the User`
records in an internal UserRole, excluding customer and partner roles, and all the
User records in any subordinate internal UserRole. The availability of this value depends
on the type of org, org creation date, release update enforcement status, and whether
[digital experiences is enabled. For more information, see this knowledge article.](https://help.salesforce.com/s/articleView?language=en_US&id=002628970&type=1)

**•** `Territory—Public group that includes all the User records in an organization`
that has the territory feature enabled.

**•** `TerritoryAndSubordinates—Public group that includes all the User records`
in a particular UserRole and all the User records in any subordinateUserRole in an
organization that has the territory feature enabled.

Only `Personal,` `Regular, and` `Queue` can be used when creating a group. The
other values are reserved.

##### Usage

Unlike users, this object can be deleted.

Only public groups are accessible via the API. Personal groups are not available.

In API version 34.0 and later, you can query a group using `Related.Name` to retrieve the group’s name. `Related.Name` is
supported for public groups, user roles, territories, manager groups, and user names.

In API version 13.0 and later, if you delete a public group, it is deleted even if it has been used in sharing, consistent with the behavior
for UserRole. In versions before 13.0, such sharing prevents the record from being deleted.

SEE ALSO:

GroupMember

Overview of Salesforce Objects and Fields


-----
