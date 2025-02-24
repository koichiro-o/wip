#### OperatingHours

Represents the hours in which a service territory, service resource, or account is available for work. OperatingHours is used by Field
Service, Salesforce Scheduler, Salesforce Meetings, Sales Engagement, and Workforce Engagement. This object is available in API version
38.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Description
LastReferencedDate
LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the operating hours. Add any details that aren’t included in
the name.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the operating hours record was last modified. Its label in the user
interface is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId
TimeZone

##### Usage

```

**Description**
The date when the operating hours record was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the operating hours. For example, Summer Hours, Winter
```
  Hours, or Peak Season Hours.

```
**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the operating hours record.

This field is available in API version 59.0.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The time zone that the operating hours fall within.


By default, only System Administrators can view, create, and assign operating hours.

Service territory members—which are service resources who can work in the territory—automatically use their service territory’s operating
hours. If a resource needs different operating hours than their territory, create separate operating hours for them from the Operating
Hours tab. Then, select the desired hours in the `Operating Hours` lookup field on the service territory member detail page.


-----

To view a service resource’s operating hours for a particular territory, navigate to their Service Territories related list and click the Member
Number for the territory. You reach the service territory member detail page, which lists the member’s operating hours and dates during
which they belong to the territory.

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**[OperatingHoursChangeEvent (API version 54.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[OperatingHoursHistory (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/sforce_api_associated_objects_history.htm;)**
History is available for tracked fields of the object.
