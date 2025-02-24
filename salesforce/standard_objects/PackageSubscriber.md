#### PackageSubscriber

Represents an installation of a package in an org. This object contains installation information for managed or unlocked packages
developed in the org you’re logged in to.

One record is created per installation. For example, if 5 orgs installed 2 packages, 10 records are created.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
To initiate a push upgrade for a first-generation managed package, the Upload AppExchange Packages user permission is required.

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

The push upgrade feature is only available to first- and second-generation managed packages that have passed AppExchange security
[review. To enable push upgrades for your managed package, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/)

For unlocked packages, push upgrades are enabled by default.

##### Fields

```
InstalledStatus

```

**Type**
picklist


-----

```
InstanceName
MetadataPackageId
MetadataPackageVersionId
OrgKey
OrgName

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the package is installed in the org, the value is i.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The instance that hosts the subscriber org.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The package ID. Package Ids have a prefix of `033. This field is available in API`
version 49.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character package version ID starting with 04t.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The 15-character ID that represents the Salesforce org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The name of the org where the package is installed.


-----

```
OrgStatus
OrgType
ParentOrg

##### Usage

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Valid values are:

**•** `Active`

**•** `Demo`

**•** `Free`

**•** `Inactive`

**•** `Trial`

Orgs with an `OrgStatus` of Inactive can’t receive push upgrades.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Valid values are:

**•** `Production`

**•** `Sandbox`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The production org from which a sandbox was created.


Here are examples of the types of API queries you can perform.

**Query**

Get all package subscriber orgs with a specific package ID

```
SELECT Id, OrgKey, OrgStatus, OrgName,
OrgType FROM PackageSubscriber WHERE
MetadataPackageVersionId = '04t...'

```

-----

Get all package subscriber orgs that have an installed package
created by the org you’re logged in to

**Filter PackageSubscriber Objects by Instance**

```
SELECT Id, OrgKey, OrgStatus, OrgName,
OrgType FROM PackageSubscriber WHERE
InstalledStatus = 'i'

```

If you have packages with many subscribers, querying PackageSubscriber objects can take a while. To improve query performance, add
filters to your PackageSubscriber queries, such as an `InstanceName` filter. InstanceName is a field that represents the instance
that the subscriber org is hosted on.

**1. Get the org’s package and the latest released version of the package.**
```
  /**
  * Get the MetadataPackage object corresponding to this org's managed package
  */
  public MetadataPackage getMetadataPackage() throws ConnectionException {
   // retrieve the managed package, which won’t have an empty namespace
  QueryResult result = conn.query("select id from MetadataPackage where namespaceprefix
   <> ''");
   return (MetadataPackage) result.getRecords()[0];
  }
  /**
  * Get the latest MetadataPackageVersion object of the given MetadataPackage
  */
  public MetadataPackageVersion getLatestMetadataPackageVersion(MetadataPackage
  metadataPackage)
  throws ConnectionException {
   // get the latest released version of the given package
   String query = "Select id, ReleaseState, MajorVersion, MinorVersion, PatchVersion,
  MetadataPackageId"
   + " From MetadataPackageVersion"
   + " Where MetadataPackageId = '%s' and ReleaseState = 'Released'"
   + " Order by majorversion desc, minorversion desc, patchversion desc";
   QueryResult result = conn.query(String.format(query, metadataPackage.getId()));
   return (MetadataPackageVersion) result.getRecords()[0];
  }

```
**2. Get eligible subscribers. The following query strings and methods are modified to allow querying for PackageSubscribers filtered by**
an instance.


-----

**3. Put it all together. The following code sample shows how to use the previous methods to modify the workflow to perform package**
pushes by instance.
```
  String[] instances = { "NA4" }; // Here we list the instances we would like to push to
  MetadataPackage metadataPackage = api.getMetadataPackage();
  MetadataPackageVersion version = api.getLatestMetadataPackageVersion(metadataPackage);
  // do pushes by instance to avoid API timeouts retrieving PackageSubscribers
  for (String instanceName : instances) {
  PackageSubscriber[] eligibleSubscribers = api.getEligibleSubscriberIds(version,
  instanceName);
  // ... proceed with creating PushRequests and PushJobs as before
