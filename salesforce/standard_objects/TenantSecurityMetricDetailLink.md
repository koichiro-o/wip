#### TenantSecurityMetricDetailLink

Represents the link between the metric count and metric drill down. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read-only.

##### Fields

```
DetailIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
MetricIdentifier
Name
Tenant

```

**Description**
The unique identifier for this detail record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the type of metric counted. This field is unique within your organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for the data collected.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the tenant that was targeted in the event.

