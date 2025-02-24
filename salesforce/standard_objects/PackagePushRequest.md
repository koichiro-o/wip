#### PackagePushRequest

```
Represents the push request for upgrading a package in one or many orgs from one version to another version.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To initiate a push upgrade for a first-generation managed package, the Upload AppExchange Packages user permission is required.

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

The push upgrade feature is only available to first- and second-generation managed packages that have passed AppExchange security
[review, and unlocked packages. To enable push upgrades for your managed package, log a support case in the Salesforce Partner](https://partners.salesforce.com/)
[Community.](https://partners.salesforce.com/)

For unlocked packages, push upgrades are enabled by default.


-----

##### Fields

**Field Name**
```
DurationSeconds
EndTime
PackageVersionId
ScheduledStartTime

```

**Type**
int

**Properties**
Group, Nillable

**Description**
The length of time in seconds, that the push upgrade took to complete. This field
is new in API version 51.0.

**Type**
dateTime

**Properties**
Create, Nillable, Update

**Description**
The date and time (UTC) at which the push upgrade ended, in ISO 8601 format.
This field is new in API version 51.0.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The non-beta, non-deprecated package version that the package is
being upgraded to.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (UTC) at which the push request is processed, in ISO 8601
format. Set this value to the earliest time that you want Salesforce to attempt to
start the push. As a best practice, schedule pushes at off-peak hours like 1:00 AM
Saturday. If you don’t specify a value, the push starts when the package push
request’s Status is set to `Pending.`

Note: Scheduled push upgrades begin as soon as resources are available
on the Salesforce instance, which is either at or after the start time you
specify. In certain scenarios, the push upgrade could start a few hours
after the scheduled start time.


-----

```
StartTime
Status

##### Usage

```

**Type**
dateTime

**Properties**
Create, Nillable, Update

**Description**
The date and time (UTC) at which the push upgrade actually started, in ISO 8601
format. This field is new in API version 51.0.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the push. Valid values are:

**•** Canceled

**•** Created (default)

**•** Failed

**•** In Progress

**•** Pending

**•** Succeeded

Don’t specify this value when you create the push request. The default value of
Created is used. Later, change the status to Pending to schedule the push upgrade.


Suppose that you want to push version 3.4.6 of your package to all orgs. You’ve already identified the orgs eligible for the upgrade by
using MetadataPackageVersion. Now let’s write some code to create a push request, which holds a push job for each eligible org.

This code sample uses the Web Services Connector (WSC).


-----

Or, if you’re using REST API, submit a POST request to the PackagePushRequest sObject endpoint, as in the following example. SOAP API
is also supported.

This example returns the push request ID (starting with 0DV) that’s required to create push jobs.
```
POST
/services/data/v38.0/sobjects/packagepushrequest/
{
  "PackageVersionId" : "04t...",
  "ScheduledStartTime" : "2016-08-24T21:00:00"
}

```
As your next step, create a push job for each eligible subscriber you want to upgrade using PackagePushJob.

**Scheduling the Push Upgrade**

To signal that the push upgrade is ready to be processed, change the status of the push request to Pending. If you didn’t set a
```
ScheduledStartTime, the push upgrade starts immediately after you change the status.

```
See the following Java example.
```
// ppr is the PackagePushRequest instance
ppr.setStatus("Pending");
conn.update(new SObject[] { ppr });

```
If you’re using REST API, submit a PATCH request to the PackagePushRequest sObject endpoint, as in the following example. SOAP API
is also supported.
```
PATCH
/services/data/v38.0/sobjects/packagepushrequest/0DV...
{
  "Status" : "Pending"
}

```
**Checking the Status of a Push Request**

The PackagePushRequest status is `Succeeded` if all its associated jobs are successful; it’s `Failed` if at least one job failed.


-----

You can also check the status of a job by querying the PackagePushJob’s Status field.

**Aborting a Push Request**

You can abort a package push request by changing its status to Canceled.

For example, if you’re using the REST API, submit a PATCH request to the PackagePushRequest sObject endpoint.
```
PATCH
/services/data/v38.0/sobjects/packagepushrequest/0DV...
{
  "Status" : "Canceled"
}

```
The following example is for Java.
```
// ppr is the PackagePushRequest instance
ppr.setStatus("Canceled");

```
You can abort a package push request only if its status is Created or Pending. If the abort succeeds, all associated push jobs are also
canceled. If you try to abort when the current PackagePushRequest status is Canceled, Succeeded, Failed, or In Progress, the abort doesn’t
occur, and an error message is returned.
