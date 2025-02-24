#### PackagePushError

Represents an error encountered during a push request. The number of PackagePushError records created depends on the number of
push jobs in the request that result in an error.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
To initiate a push upgrade for a first-generation managed package, the Upload AppExchange Packages user permission is required.


-----

To initiate a push upgrade for an unlocked or second-generation managed package, the Create and Update Second-Generation Packages
user permission is required.

The push upgrade feature is only available to first- and second-generation managed packages that have passed AppExchange security
[review. To enable push upgrades for your managed package, log a support case in the Salesforce Partner Community.](https://partners.salesforce.com/)

For unlocked packages, push upgrades are enabled by default.

##### Fields

```
ErrorDetails
ErrorMessage
ErrorSeverity
ErrorTitle
ErrorType

```

**Type**
string

**Properties**
Nillable, Sort

**Description**
Explanation of the error.

**Type**
string

**Properties**
Nillable, Sort

**Description**
The error code that appears in the API.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Valid values are:

**•** Error

**•** Warning

**Type**
string

**Properties**
Nillable, Sort

**Description**
The error message title that appears in the API.

**Type**
picklist


-----

```
PackagePushJobId

##### Usage

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Valid values are:

**•** ApexTestFailure

**•** DeployError

**•** FeatureMissing

**•** IneligibleUpgrade

**•** LimitExceeded

**•** LockingFailure

**•** PACError

**•** UnclassifiedError

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. The parent push job record ID.


Suppose that your push upgrade request wasn’t successful due to some of its jobs failing. Let’s write some code to find out what those
errors were.

This code sample uses the Web Services Connector (WSC).


-----
