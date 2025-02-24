#### UserLicense

Represents a user license in your organization. A user license entitles a user to specific functionality and determines the profiles and
permission sets available to the user.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
LicenseDefinitionKey

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
A string that uniquely identifies a particular user license. Label is `License Def. ID.`
Values are:

**AUL: corresponds to the Salesforce Platform user license**

**AUL1: corresponds to the Salesforce Platform One user license**

**AUL_LIGHT corresponds to the Salesforce Platform Light user license**

**FDC_ONE corresponds to the Lightning Platform - One App user license**

**FDC_SUB corresponds to the Lightning Platform App Subscription user license**

**Overage_Platform_Portal_User corresponds to the Overage Authenticated Website user**
license

**PID_STRATEGIC_PRM: corresponds to the Gold Partner user license**

**PID_CHATTER corresponds to the Chatter Only user license**

**PID_CONTENT corresponds to the Content Only user license**

**PID_Customer_Portal_Basic: corresponds to the Customer Portal Manager Standard user**
license and the Customer Portal User license

**PID_Customer_Portal_Standard: corresponds to the Customer Portal Manager Custom**
user license

**PID_FDC_FREE corresponds to the Lightning Platform Free user license**

**PID_IDEAS corresponds to the Ideas Only user license**

**PID_Ideas_Only_Portal corresponds to the Ideas Only Portal user license**

**PID_Ideas_Only_Site corresponds to the Ideas Only Site user license**

**PID_KNOWLEDGE corresponds to the Knowledge Only user license**

**PID_Customer_Community corresponds to the Customer Community license.**


-----

```
MasterLabel
MonthlyLoginsEntitlement

```

**PID_Customer_Community_Login corresponds to the Customer Community Login**
license.

**PID_Partner_Community corresponds to the Partner Community license.**

**PID_Partner_Community_Login corresponds to the Partner Community Login license.**

**PID_Limited_Customer_Portal_Basic: corresponds to the Limited Customer Portal**
Manager Standard user license

**PID_Limited_Customer_Portal_Standard: corresponds to the Limited Customer Portal**
Manager Custom user license

**PID_Overage_Customer_Portal_Basic: corresponds to the Overage Customer Portal**
Manager Standard user license

**PID_Overage_High Volume Customer Portal corresponds to the Overage High Volume**
Customer Portal user license

**Platform_Portal_User: corresponds to the Authenticated Website user license**

**POWER_PRM: corresponds to the Partner user license**

**POWER_SSP: corresponds to the Customer Portal Manager user license**

**SFDC: corresponds to the Full CRM user license**

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The user license label.

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The maximum number of customer or partner portal logins allowed per month. A `null`
value in this field means the user license is charged according to the number of users rather
than the number of logins.

This field is available in API version 20.0 and later.

Note: To be visible and queryable, this field requires:

**•** Digital Experiences enabled

**•** the View Setup and Configuration user permission


-----

```
MonthlyLoginsUsed
Name
Status
TotalLicenses
UsedLicenses

```

**Type**
int

**Properties**
Group, Nillable, Sort

**Description**
The number of successful logins for all users associated with a customer or partner portal
user license. This field has a non-null value if `MonthlyLoginsEntitlement` has
a non-null value.

This field is available in API version 20.0 and later.

Note: To be visible and queryable, this field requires:

**•** Digital Experiences enabled

**•** the View Setup and Configuration user permission

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The internal name of the user license.

Note: Your organization may also include custom user licenses.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The current status of the user license. Valid values for this field are Active and Disabled.

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of user licenses in the organization.

This field is available in API version 32.0 and later.

**Type**
int


-----

UsedLicensesLastUpdated

##### Usage


**Properties**
Filter, Group, Sort

**Description**
The number of user licenses that are assigned to active users in the organization.

This field is available in API version 32.0 and later.

**Type**
dateTime

**Properties**
aggregate, Filter, Sort

**Description**
The timestamp of the query. If your license count exceeds your org’s allotted threshold, the
count timestamp reflects the previous day, otherwise the timestamp reflects the current day
and time.

This field is available in API version 41.0 and later.


Users with the “View Setup and Configuration” permission can use the UserLicense object to view the set of currently defined user
licenses in your organization.

The UserLicense object is currently used by bulk user creation to determine the user license to which each profile and permission set
belongs. For example, if you use the API to create portal users and you want to know which profile belongs to each portal user license,
you can query this object for each profile and check the `LicenseDefinitionKey` to identify the associated user license.

SEE ALSO:

Profile
