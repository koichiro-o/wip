#### OpportunityStage

```


**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

This field can’t be accessed unless the logged-in user has the Customize
Application permission.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The containing record type, such as an opportunity. Available in API version 30
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates which currency field of the opportunity object is split. Available in API
version 30 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable,Restricted picklist, Sort,Update

**Description**
Indicates the status of the split type. Available in API version 30 and later.


Represents the stage of an Opportunity in the sales pipeline, such as New Lead, Negotiating, Pending, Closed, and so on.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field**
```
 ApiName
 DefaultProbability
 Description
 ForecastCategory
 ForecastCategoryName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or master label.

**Type**
percent

**Properties**
Filter, Nillable, Sort,

**Description**
The default percentage estimate of the confidence in closing a specific opportunity for this
opportunity stage value. Label is Probability (%).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of this opportunity stage value. Limit: 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The default forecast category for this opportunity stage value. The forecast category
automatically determines how opportunities are tracked and totaled in a forecast.

Possible values are:

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

**Type**
picklist


-----

```
IsActive
IsClosed
IsWon
MasterLabel

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Available in API version 12.0 and later. The default forecast category value for this opportunity
stage value.

Possible values are:

**•** `Best Case`

**•** `Closed`

**•** `Commit`

**•** `Most Likely`

**•** `Omitted`

**•** `Pipeline`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value is active (true) or not (false). Inactive
opportunity stage values are not available in the picklist and are retained for historical
purposes only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value represents a closed opportunity (true) or
not (false). Multiple opportunity stage values can represent a closed opportunity. Label
is Closed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value represents a won opportunity (true) or not
(false). Multiple opportunity stage values can represent a won opportunity. Label is Won.

**Type**
string


-----

```
 SortOrder

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this opportunity stage value. This display value is the internal label that does
not get translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the opportunity stage picklist. These numbers are not
guaranteed to be sequential, as some previous opportunity stage values might have been
deleted.


This object represents a value in the opportunity stage picklist, which provides additional information about the stage of an Opportunity,
such as its probability or forecast category. Query this object to retrieve the set of values in the opportunity stage picklist, and then use
that information while processing Opportunity records to determine more information about a given opportunity. For example, the
application could test whether a given opportunity is won or not based on its StageName value and the value of the IsWon property
in the associated OpportunityStage object.

This object is read-only via the API.

SEE ALSO:

Overview of Salesforce Objects and Fields
