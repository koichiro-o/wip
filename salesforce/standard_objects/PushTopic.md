#### PushTopic

Represents a query that is the basis for notifying Streaming API clients of changes to records in an org. This object is available in API
version 21.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
**•** This object is available only if Streaming API is enabled for your org.

**•** Users with the Create permission can create this record.

**•** To receive notifications, users must have read access on both the object in the PushTopic query and the PushTopic itself.

##### Fields

```
ApiVersion
Description
IsActive

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Required. API version to use for executing the query specified in `Query. It must be an API`
version greater than 20.0. If your query applies to a custom object from a package, this value
must match the package's `ApiVersion.`

Example value:

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the PushTopic. Limit: 400 characters

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the record currently counts towards the organization's allocation.


-----

```
Name
NotifyForFields
NotifyForOperationCreate
NotifyForOperationDelete
NotifyForOperationUndelete

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Descriptive name of the PushTopic, such as `MyNewCases` or
```
  TeamUpdatedContacts. Limit: 25 characters. This value identifies the channel and

```
must be unique.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies which fields are evaluated to generate a notification.

Possible values are:

**•** `All`

**•** `Referenced` (default)

**•** `Select`

**•** `Where`

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if a create operation should generate a notification, otherwise, `false. Defaults to`
```
  true. This field is available in API version 29.0 and later.

```
**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if a delete operation should generate a notification, otherwise, `false. Defaults to`
`true. Clients must connect using the` `cometd/29.0` (or later) Streaming API endpoint
to receive delete and undelete event notifications. This field is available in API version 29.0
and later.

**Type**
boolean


-----

```
NotifyForOperationUpdate
NotifyForOperations
Query

```

**Properties**
Create, Filter, Update

**Description**
`true` if an undelete operation should generate a notification, otherwise, `false. Defaults`
to true. Clients must connect using the cometd/29.0 (or later) Streaming API endpoint
to receive delete and undelete event notifications. This field is available in API version 29.0
and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
`true` if an update operation should generate a notification, otherwise, `false. Defaults`
to `true. This field is available in API version 29.0 and later.`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies which record events may generate a notification.

In API version 29.0 and later, this field is read-only, and doesn’t contain information about
delete and undelete events. Use `NotifyForOperationCreate,`
`NotifyForOperationDelete,` `NotifyForOperationUndelete` and
`NotifyForOperationUpdate` to specify which record events should generate a
notification.

Possible values are:

**•** `All` (default)

**•** `Create`

**•** `Extended`

**•** `Update`

A value of `Extended` means that neither create or update operations are set to generate
events.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The SOQL query statement that determines which record changes trigger events
to be sent to the channel.


-----

Limit: 1,300 characters

##### Usage

The PushTopic defines when notifications are generated in the channel. Determine which fields to configure by checking out these links
in the Streaming API Developer Guide.

**•** [PushTopic Queries](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_streaming.meta/api_streaming/pushtopic_queries.htm)

**•** [Events](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_streaming.meta/api_streaming/events.htm)

**•** [Notifications](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_streaming.meta/api_streaming/notifications.htm)

SEE ALSO:

_[Streaming API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_streaming.meta/api_streaming/intro_stream.htm)_
