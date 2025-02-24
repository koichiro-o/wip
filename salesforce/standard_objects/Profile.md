#### Profile

Represents a profile, which defines a set of permissions to perform different operations. Operations can include creating a custom profile
or querying, adding, updating, or deleting information.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

 Special Access Rules

```
As of Summer ’20 and later, Customer Portal and Partner Portal users can’t access this object.

To view the following settings, assignments, and permissions for standard and custom objects in a specified profile, the View Setup and
Configuration permission is required.

**•** Client settings

**•** Field permissions

**•** Layout assignments

**•** Object permissions

**•** Permission dependencies

**•** Permission set tab settings

**•** Permission set group components

**•** Record types

Starting in Winter ’21, only users with correct permissions can view profile names other than their own if the Profile Filtering setting is
enabled.


-----

Important: Profile names are also exposed when users with permissions to perform the following tasks take these actions:

**•** Create a tab or record type with a wizard step that includes the assignment of tabs and record types to profiles.

**•** Configure a login flow where viewing profile lists is required to make flow associations.

**•** Set up delegated admins where looking up profiles is needed to identify assignable profiles.

**•** Administer an org as a delegated customer admin.

**•** Administer an org as a delegated admin to view and assign profiles of the delegated group.

##### Fields

```
Description
IsSsoEnabled
LastReferencedDate
LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the profile.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, users assigned to this profile can delegate username and password authentication`
to a corporate database instead of the user database.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this profile. Available
in API version 29.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this profile. Available in API version 29.0
and later.


-----

```
Name
PermissionsPermissionName
UserLicenseId
UserType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the profile.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
One field for each permission. If `true, users assigned to this profile have the named`
permission. The number of fields varies depending on the permissions for the org and license
type.

Tip: To get a list of available permissions in SOAP API, use describeSObjects().

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the UserLicense associated with this profile.

This is a relationship field.

**Relationship Name**
UserLicense

**Relationship Type**
Lookup

**Refers To**
UserLicense

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The category of user license. Each `UserType` is associated with one or more UserLicense
records. Each UserLicense is associated with one or more profiles. In API version 10.0 and later,
valid values include:


-----

**•** Standard: user license. This user type also includes Salesforce Platform and Salesforce
Platform One user licenses. Label is Standard.

**•** PowerPartner: User whose access is limited because they’re a partner and typically access
the application through a partner portal or Experience Cloud site. Label is Partner.

**•** CspLitePortal: user whose access is limited because they’re an org's customer and access
the application through a Customer Portal or Experience Cloud site. Label is High Volume
**Portal.**

**•** CustomerSuccess: user whose access is limited because they’re an org's customer and
access the application through a Customer Portal. Label is Customer Portal User.

**•** PowerCustomerSuccess: user whose access is limited because they’re an org's customer
and access the application through a Customer Portal. Label is Customer Portal Manager.

Users with this license type can view and edit data they directly own or data owned by or
shared with users below them in the Customer Portal role hierarchy.

**•** CsnOnly: user whose access to the application is limited to Chatter. This user type includes
Chatter Free and Chatter moderator users. Label is Chatter Free.

**•** Guest: user whose access is limited because they’re an unauthenticated user without login
credentials. Label is Guest.

`UserType` replaces `LicenseType, which is unavailable as of API version 10.0. In API`
versions 8.0 and 9.0 `LicenseType` is still available with the following valid values:

**•** AUL: Lightning Platform user license. Label is Apex Platform.

**•** AUL1: Lightning Platform user license with only one user. Label is Apex Platform One.

**•** Salesforce: Salesforce user license. Label is Salesforce.

**•** PackageManager: user who can create and work with managed packages for AppExchange.
Label is Package Manager.

**•** PRM: user whose access is limited because they’re a partner and typically accesses the
application through a partner portal. Label is Partner.

**•** CustomerUser: user whose access is limited because they’re an org's customer and accesses
the application through a Customer Portal. Label is Customer Portal User.

**•** CustomerManager: user whose access is limited because they’re an org's customer and
accesses the application through a Customer Portal. Label is Customer Portal Manager.

Users with this license type can view and edit data they directly own or data owned by or
shared with users below them in the Customer Portal role hierarchy.

In API version 53.0 and later, you can’t set the value of `UserType` using Apex.

##### Usage

Use the Profile object to create custom profiles that start without any permissions enabled except for required permissions for the profile’s
user license. While you can use the Profile Metadata type to deploy profiles, we recommend that you use the Profile SOAP API object
because it allows you to create empty profiles.

You can also query the set of currently configured user profiles in your org. Your client application can use Profile objects to obtain valid
profile IDs for use when querying or modifying users through the API.


-----

In the user interface, profiles can be used to assign user licenses from specific pools (Lightning Platform user license or Salesforce user
license, for example). When users are reassigned to profiles with different license types, the number of available licenses in the old license
type pool increases, one per user assignment updated. Also, the number of available licenses decreases by the same amount in the new
license type pool.

SEE ALSO:

Overview of Salesforce Objects and Fields

PermissionSet
