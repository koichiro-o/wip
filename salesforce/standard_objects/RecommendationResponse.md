#### RecommendationResponse

Represents the user responses to a presented offer or recommendation for Einstein Next Best Action. This object is available in API version
51.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated() query(), retrieve(),

 Special Access Rules

```
You must have one of these user permissions to read, delete, or update recommendation responses:

**•** Modify All Data

**•** Manage Next Best Action Recommendations

**•** Manage Next Best Action Strategies

##### Fields

```
ActionReference

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The full name of an action flow at the time of the response. The full name includes the action’s
namespace.


-----

```
ContextRecord
ContextRecordName
ContextRecordType
NetworkId
OnBehalfOf

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of context record that contains the Einstein Next Best Action component. For example,
if the Einstein Next Best Action component is on a case record the ContextRecord is the ID
of the case record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the context record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that’s associated with the value stored in the ContextRecord field.
For example, Account, Case, or Contact.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site associated with the recommendation (if applicable). This is
a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort


-----

```
OnBehalfOfName
OnBehalfOfType
RecommendationKey
RecommendationName
RecommendationType

```

**Description**
The user ID or record that is indirectly reacting to the recommendation.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the value stored for `OnBehalfOf` at time of response.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that’s associated with the value stored in the OnBehalfOf field. For
example, Account, Case, or Contact.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
RecommendationId if available, otherwise a generated string that represents the
recommendation name.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Name of the recommendation returned from the recommendation strategy.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Object type of the recommendation. It can be Recommendation or any object type mapped
to the Recommendation object. For example, if you map Product to Recommendation, the
RecommendationType is Product.


-----

```
Response
StrategyReference
StrategyVersion

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The user’s response to the recommendation.

Possible values are:

**•** `Accepted`

**•** `Rejected`

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The full name of a recommendation strategy flow at the time of the response. The response
is formatted as namespace underscore prefix double underscore flowname, such
as `namespace_prefix__flowname.`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The recommendation strategy version that’s active at the time of the response.


The RecommendationResponse object can’t be customized with additional fields.
