#### ScratchOrgInfo

```

**Description**
The ID of the report that is run and summarized to return a single value.

This is a relationship field.

**Relationship Name**
Report

**Relationship Type**
Lookup

**Refers To**
Report

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the scorecard that the metric is related to. Several metrics can be tied to a single
scorecard.

This is a relationship field.

**Relationship Name**
Scorecard

**Relationship Type**
Lookup

**Refers To**
Scorecard


Represents a scratch org and its audit log. Use this object to create a scratch org and keep a log of its creation and deletion. This object
is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
AdminEmail
AuthCode
ConnectedAppCallbackUrl
ConnectedAppConsumerKey
Country

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The email address of the scratch org’s Administration user. The read only
```
  SignupEmail field is populated with this value. If you don't provide a value

```
for `AdminEmail, the field is left blank and the` `SignupEmail is populated`
with the email address of the org user who is creating this object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A one-time authorization code that can be exchanged for an OAuth access token
and refresh token using standard Salesforce APIs. It’s used with
`ConnectedAppCallbackUrl` and ConnectedAppConsumerKey,
when the specified connected app hasn't been configured with an X.509
certificate. This field is read only.

**Type**
textarea

**Properties**
Create

**Description**
Required. When used with ConnectedAppConsumerKey, it specifies the
callback URL used for OAuth. If using Salesforce CLI, the default is
```
  http://localhost:1717/OauthRedirect.

```
**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. When used with ConnectedAppCallbackUrl, it specifies the
connected app that is approved automatically during scratch org creation. If
using Salesforce CLI and the default connected app, indicate PlatformCLI.

**Type**
string


-----

```
DeletedBy
DeletedDate
Description
DurationDays
Edition

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The two-character, upper-case ISO-3166 country code. You can find a full list of
these codes at several sites, such as:
[www.iso.ch/iso/en/prods-services/iso3166ma/02iso-3166-code-lists/list-en1.html.](http://www.iso.ch/iso/en/prods-services/iso3166ma/02iso-3166-code-lists/list-en1.html)
The language of the scratch org is auto-determined based on the value of this
field. If you don’t specify a value, this field defaults to the Dev Hub’s country code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user who requested that the scratch org be deleted. This field is read only.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the DeletedBy user requested that the scratch org be deleted.
This field is read only.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A free-form text field for you to enter a description of this scratch org.

**Type**
int

**Properties**
Create, Filter, Nillable, Group, Sort

**Description**
Number of days after which the scratch org expires. Valid values are 1–30. The
default is 7.

**Type**
picklist


-----

```
ErrorCode
ExpirationDate
Features
HasSampleData
Language

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Required if you don’t provide Snapshot or SourceOrg. The org edition of this
scratch org. Valid values are Group, Developer, Enterprise, and
```
  Professional.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error code if the scratch org creation isn’t successful. This field is read only.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the scratch org expires. This field is read only.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
A semi-colon delimited list of the features enabled in this scratch org, such as
MultiCurrency. See the Salesforce DX Developer Guide for the full list of valid
features.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the scratch org contains sample data. If set to `true, the`
sample data is similar to the data in a Salesforce free trial org.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


-----

```
LastLoginDate
LastReferencedDate
LastViewedDate
LoginUrl
Name

```

**Description**
The language of the scratch org being created. Specify the language using a
language code listed under "Supported Languages" in Salesforce Help. For
example, use `zh_CN` for simplified Chinese. The value you select overrides the
language set by locale.

If you don’t specify a value, the language is based on the Country used during
scratch org creation. If you don’t specify a value for Country, the value defaults
to the Dev Hub’s country.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date of the last user login to the scratch org. This field is read only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record. This field is read only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, and LastReferenceDate isn’t null, the user accessed this
record or list view indirectly. This field is read only.

**Type**
textarea

**Properties**
Nillable

**Description**
A URL that logs you in to the scratch org. This field is read only.

**Type**
string


-----

```
Namespace
OrgName
OwnerId
Release

```

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The auto-generated ID of this scratch org. This field is read only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The namespace you want to associate with this scratch org. The value of this field
corresponds to the NamespacePrefix field of the NamespaceRegistry
object that describes your namespace.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The name of the scratch org. This name appears as the Organization
Name in the Company Information Setup page.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created this scratch org.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The release of the scratch org. During Salesforce's major release transitions, this
field allows you to select the Salesforce release version, based on the version of
your Dev Hub. This field is available in API version 46.0 and later. Valid values are:

**•** Current

**•** Preview

**•** Previous

[See Select the Salesforce Release for a Scratch Org for more information.](https://developer.salesforce.com/docs/atlas.en-us.254.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_scratch_orgs_version_selection.htm)


-----

```
ScratchOrg
SignupCountry
SignupEmail
SignupInstance
SignupLanguage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The org ID of the scratch org. This field is read only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The country code of the scratch org. This field is populated with the value of the
`Country` field. If you didn’t provide a value for `Country, it’s the country`
code of the Dev Hub. This field is read only.

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
The email address of the scratch org’s Administration user. This field is populated
with the value of the AdminEmail field. If you didn't provide a value for
```
  AdminEmail, it's the email address of your user in the Dev Hub. This field is

```
read only.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce instance on which this scratch org resides. This field is read only.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the scratch org. This field is populated with the value of the
```
  Language field. If you didn’t provide a value for Language, it’s the language

```
of the Dev Hub. This field is read only.


-----

```
SignupTrialDays
SignupUsername
Snapshot
SourceOrg
Status

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of days between the scratch org's creation and expiration. This field
is read only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The username of the Administration user of this scratch org. This field is populated
with the value of the Username field. If you didn’t provide a value for
```
  Username, the value of this field is auto-generated. This field is read only.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
If this scratch org was created from a scratch org snapshot, then this field contains
either the name or ID of the snapshot. Specifically, the name corresponds to the
`Name` field of the snapshot’s record in the OrgSnapshot standard object; the ID
corresponds to the record ID.

If this scratch org wasn’t created from a snapshot, this field is empty.

If you specify `Snapshot, you can’t specify` `Edition` or SourceOrg.

This field is available in API version 61.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the org whose shape (features, settings, limits, and licenses) information
is used for creating scratch orgs. If you specify SourceOrg, you can’t specify
`Edition` or Snapshot.

**Type**
picklist


-----

```
Username

##### Associated Objects

```

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the scratch org, such as active, expired, or deleted. This field is read
only.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The username of the Administration user of this scratch org.


This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**ScratchOrgInfoFeed**

Feed tracking is available for the object.

**ScratchOrgInfoHistory**

History is available for tracked fields of the object.

**ScratchOrgInfoShare**

Sharing is available for the object.

SEE ALSO:

ActiveScratchOrg

NamespaceRegistry

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.sfdx_dev.meta/sfdx_dev)_
