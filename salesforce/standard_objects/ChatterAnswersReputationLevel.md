#### ChatterAnswersReputationLevel

Represents a reputation level within a Chatter Answers zone. This object is available in API version 26.0 and later.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

##### Supported Calls
```
create(), delete(), query(), retrieve(), update()

```

-----

##### Fields

**Field**
```
CommunityID
Name
Value

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the zone for which you’re creating the reputation level.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Name of the reputation level.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Minimum number of points for this level.


Use to create or edit reputation levels for the zone.
