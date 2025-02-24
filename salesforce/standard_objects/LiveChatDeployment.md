#### LiveChatDeployment

```
Represents the general settings for deploying Live Agent on a website. This object is available in API version 24.0 and later.

##### Supported Calls
```
create(), query(), update(), retrieve()

 Fields

```
```
BrandingId
ConnectionTimeoutDuration

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the static image resource that’s displayed in the chat window.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the amount of time before the chat times out, in seconds.


-----

```
ConnectionWarningDuration
DeveloperName
Domains
HasTranscriptSave

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the amount of time before a time-out warning is displayed to the agent,
in seconds.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
textarea

**Properties**
Create, Filter (unavailable in API version 25.0 and later), Nillable, Sort (unavailable
in API version 25.0 and later)

**Description**
A comma-separated list of domains the deployment is allowlisted for. Leave this
blank to allow the deployment to be used on any domain.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


-----

```
Language
MasterLabel
MobileBrandingId
OptionsHasPrechatApi
SiteId
WindowTitle

```

**Description**
Determines whether visitors can download and save transcripts from the chat
window.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the deployment.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the deployment

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the static image resource displayed in the mobile version of the
chat window.

**Type**
boolean

**Properties**
Create, Filter

**Description**
Determines whether developers can access the Pre-Chat API.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The record ID of the site used for loading static resources.

**Type**
string


-----

**Properties**
Create, Filter, Group, Sort

**Description**
The text displayed in the title bar of the browser window used to launch the chat
window.

##### Usage

Use this object to query and manage live chat deployments.
