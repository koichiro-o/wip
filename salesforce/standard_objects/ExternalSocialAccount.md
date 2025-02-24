#### ExternalSocialAccount

Represents a managed social media account on a social network such as Facebook or Twitter. This object is available in API version 29.0
and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
AuthorizedBy
DataSourceId
DefaultResponseAccountId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the Radian6 user who added the social account to Radian6.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Radian6 data source for the social account.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the managed social account to use by default when responding.

This is a relationship field.

**Relationship Name**
DefaultResponseAccount


-----

```
DeveloperName
ExternalAccountId
ExternalPictureURL
IsActive

```

**Relationship Type**
Lookup

**Refers To**
ExternalSocialAccount

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the record in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is automatically generated but you can supply
your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no DeveloperName is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
ID of the social account on the social network.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL to the picture of the social account on the social network.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social account is active or not.


-----

```
IsAuthenticated
IsCaseCreationEnabled
IsDataSourceActive
Language
MasterLabel
ProfileUrl

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the social account is authenticated or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether case creation for the social account is enabled or not.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the data source is active or not.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the language of the social account.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Master label for the social account. This display value is the internal label and
does not get translated.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort


-----

```
Provider
ProviderUserId
RuleId
SocialPropertyId
TopicId
UniqueName

```

**Description**
URL for the profile.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Social network, such as Facebook or Twitter, of the social account.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
User ID for the social network of the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Radian6 rule for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Radian6 social property for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the topic for the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
Username

##### Usage

```

**Description**
Unique name for the social account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Username for the social account.


[Although available, many of the Radian6-related fields are no longer accurate or used. We recommend using Social Engagement](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_social_engagement_list.htm)
[Resources in Connect REST API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_resources_social_engagement_list.htm)
