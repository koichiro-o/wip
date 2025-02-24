#### PermissionSetLicense

Represents a license that’s used to enable one or more users to receive a specified permission without changing their profile or reassigning
profiles. You can use permission set licenses to grant access, but not to deny access. This object is available in API version 29.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is


-----

```
ExpirationDate
IsAvailableForIntegrations

```
`IsSupplementLicense` (Developer
Preview)


specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date at which the permission set license expires.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the permission set license is enabled for integrations (true)
or not (false). When this field is set to `true, Salesforce integration features`
can access data. The default value is `false. This field is read-only in the API`
and can be edited only in Setup.

If integrations are required for feature functionality and the license isn't enabled
for integrations, you receive an error when setting up the session-based
permission set or executing the feature. Only enable integrations if necessary for
the feature.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a custom permission set license is a supplement license (true)
or a foundation license (false). The default value is `false.`

This field is only available if the Partner Licensing Platform developer preview is
enabled. This field is available in API version 55.0 and later.

Note: The Partner Licensing Platform is available as a developer preview.
The Partner Licensing Platform isn’t generally available unless or until
Salesforce announces its general availability in documentation or in press
releases or public statements. All commands, parameters, and other
features are subject to change or deprecation at any time, with or without
notice. Don't implement functionality developed with these commands
or tools in your production package.


-----

```
Language
MasterLabel
MaximumPermissionsPermissionName
PermissionSetLicenseKey
Status

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The language of the permission set license.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the permission set license. Label is Permission Set License Label.

**Type**
boolean

**Properties**
Filter

**Description**
One field for each permission. For example,
`MaximumPermissionsIdentityConnect` corresponds to the “Use
Identity Connect” permission.

If true, this PermissionSetLicense grants the specified permission. The number
of fields varies depending on the permissions available for the organization.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A string that uniquely identifies a particular permission set license.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of a permission set license. If `Active, the permission set license is`
available. If `Disabled, the permission set license has expired.`


-----

```
TotalLicenses
UsedLicenses

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The total number of this permission set license that are available to your
organization.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of this permission set license that are currently assigned to users.


Users with the “View Setup and Configuration” permission can use the PermissionSetLicense object to view the set of currently defined
permission set licenses in your organization.

Use the PermissionSetLicense object to query existing permission licenses.

For example, to return a list of all active permission set licenses:
```
SELECT MasterLabel
FROM PermissionSetLicense
WHERE Status = 'Active'

```
When combined with the PermissionSetLicenseAssign object, you can create a nested query that returns all users assigned to a particular
permission set license like “Identity Connect”:
```
SELECT MasterLabel, (SELECT AssigneeId FROM PermissionSetLicenseAssign)
FROM PermissionSetLicense
WHERE MaximumPermissionsIdentityConnect=true

```
SEE ALSO:

PermissionSetLicenseAssign
