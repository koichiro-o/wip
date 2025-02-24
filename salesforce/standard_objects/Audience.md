#### Audience

```

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
```
  00530000009M943.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license. Possible values are:

**•** CsnOnly—Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** CspLitePortal—CSP Lite Portal license. Users whose access is limited because they’re
organization customers and access the application through a customer portal or an
Experience Cloud site.

**•** CustomerSuccess—Customer Success license. Users whose access is limited because
they’re organization customers and access the application through a customer portal

**•** Guest—Users whose access is limited so that your customers can view and interact with
your site without logging in.

**•** PowerCustomerSuccess—Power Customer Success license. Users whose access is limited
because they’re organization customers and access the application through a customer
portal. Users with this license type can view and edit data they directly own or data
owned by or shared with users below them in the customer portal role hierarchy.

**•** PowerPartner—Power Partner license. Users whose access is limited because they’re
partners and typically access the application through a partner portal or site.

**•** SelfService—Users whose access is limited because they’re organization customers and
access the application through a self-service portal.

**•** Standard—Standard user license. This user type also includes Salesforce Platform and
Salesforce Platform One user licenses, and admins for this org.


Represents an audience that is defined by criteria and can be assigned and used for targeting in an Experience Cloud site. This object is
available in API version 44.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve(), update()

```

-----

##### Fields

**Field**
```
AudienceName
ContainerId
Description
DeveloperName
FormulaFilterType

```

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Name of the audience.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the site or org that contains the audience. ContainerId is nillable in API versions 47.0
and earlier.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the audience.

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
The unique name of the audience in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
This field is automatically generated, but you can supply your own value if you create the
record using the API.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist


-----

```
Language
MasterLabel

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Formula filter for the criteria used to define the audience. Valid values are:

**•** `AllCriteriaMatch—Matching all the conditions (AND).`

**•** `AnyCriterionMatches—Matching at least one condition (OR).`

**•** `CustomLogicMatches—Matching condition logic (AND and OR) and numbered`
criteria groups. This value is available in API version 45.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the audience. Valid values are:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined
translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in English.

**Type**
string

**Properties**
Filter, Group, Sort, Update


-----

**Description**
Master label for the audience. This internal name doesn’t get translated.
