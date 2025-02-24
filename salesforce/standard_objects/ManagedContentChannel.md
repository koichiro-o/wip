#### ManagedContentChannel

Represents the details of a CMS channel. CMS channels correspond to managed content publishing endpoints. They deliver published
content from your Salesforce CMS workspaces to an audience. This object is available in API version 55.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
`ManagedContentChannel` is available when the Digital Experiences app is enabled.

##### Fields

```
CacheControlMaxAge
Domain

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time, in seconds, it takes for a requested CMS content resource in the CMS
channel to expire before a new request for the resource must be made.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The domain for a public channel. Only public channels can have an assigned domain.


-----

```
DomainHostName
MediaCacheControlMaxAge
Name
OptionsIsCacheControlPublic
OptionsIsDomainLocked

```

Possible value is:

**•** mydomain.cdn.salesforce-experience.com

Note: The `mydomain` value is specific to the domain of the channel.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The hostname of the domain assigned to the CMS channel. Only public channels can have
an assigned domain.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The amount of time, in seconds, it takes for a requested CMS image or document content
resource in the CMS channel to expire before a new request for the resource must be made.
This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the CMS channel.

**Type**
boolean

**Properties**
Filter

**Description**
When `true, the CMS channel connection type is public. When` `false, the cache control`
is private. The default value is `false.`

**Type**
boolean

**Properties**
Filter


-----

```
OptionsIsSearchable
Type

##### Usage

```

**Description**
When `true, the domain set to the channel can’t be changed. Only public channels can`
have this field set to `true. If the channel type is` `COMMUNITY, the default value is` `true.`
For all other channel types, the default value is `false.`

**Type**
boolean

**Properties**
Filter

**Description**
When `true, users can search for all published CMS content types within the channel. The`
default value is `false.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The connection type of the CMS channel. The connection type determines which audience
can access the CMS content delivered in the channel.

Possible values are:

**•** `COMMUNITY: User access is controlled by the settings of the Experience Cloud site.`

**•** `CloudToCloud: Connects Salesforce CMS to the B2C Commerce Page Designer.`

**•** `ConnectedApp: User access to the channel is controlled by the connected application`
associated with the channel.

**•** `PublicUnauthenticated: No user authentication required, content can be cached`
on public CDNs.

**•** `Record: User access to the content is controlled by the user access to the associated`
record. Content is only accessible to users with access to the record.

**•** `UserPermission: This value is reserved for future use.`


`ManagedContentChannel` can be queried through the public sObject API. Use this object to retrieve information for a specific
CMS channel.
