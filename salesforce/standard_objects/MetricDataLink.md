#### MetricDataLink

The link between the metric and the data source, such as a report.

Note: The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information,
[see Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
DatasourceFieldName
DataSourceId
LastSynchronizationTime
Name
TargetId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The field name of the data source, such as a report summary field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the data source.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last time the data was synchronized.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name given to the data link record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the metric that the data is linked to.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**MetricDataLinkHistory**

History is available for tracked fields of the object.

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)
