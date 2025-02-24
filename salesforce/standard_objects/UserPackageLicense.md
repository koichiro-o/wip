#### UserPackageLicense

Represents a license for an installed managed package, assigned to a specific user. This object is available in API version 31.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve() update()

 Fields

```

`IsRevoked` (Beta)
```
LastCreatedByChangeId

```
(Beta)


**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the managed package license assignment was revoked (true) or not (false).
Defaults to `false. This field is available in API version 58.0 and later.`

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole
discretion. Any use of the Beta Service is subject to the applicable Beta Services Terms
[provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

**Type**
reference


-----

```
LastDeletedByChangeId

```
(Beta)
```
PackageLicenseId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user access change record related to this managed package license assignment. This
field is available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole
discretion. Any use of the Beta Service is subject to the applicable Beta Services Terms
[provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user access change record related to this managed package license assignment being
revoked. This field is available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
LastCreatedByChange

**Relationship Type**
Lookup

**Refers To**
UserAccessChange

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole
discretion. Any use of the Beta Service is subject to the applicable Beta Services Terms
[provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The 18-character Globally Unique ID (GUID) that identifies the package license


-----

```
UserId

##### Usage

```

This is a relationship field.

**Relationship Name**
PackageLicense

**Relationship Type**
Lookup

**Refers To**
PackageLicense

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The User ID of the user licensed to use this package


Use this object, in conjunction with PackageLicense, to provide users access to a managed package installed in your organization.
