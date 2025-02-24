#### ConvAnalysisTopic

Represents a topic generated from the Sales Signals refresh or run. For example, a product experiencing issues due to high pricing could
be a topic identified through the analysis of multiple calls. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), undelete(), update(), upsert()

 Special Access Rules

```
Users need the Sales Signals permission set and the Sales Signals feature must be enabled.

##### Fields

```
CallPercentage
Category
ConvAnalysisSummaryId

```

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
Required. The percentage of calls that apply to a topic, out of the total number of calls that
were analyzed.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. A classification or grouping used to filter topics. This field is used in conjunction
with `Keyword.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The conversation analysis summary associated with the topic.

This field is a relationship field.

**Relationship Name**
ConvAnalysisSummary


-----

```
GenerationsIdentifier
Keyword
MentionCount
Order
Summary

```

**Relationship Type**
Master-detail

**Refers To**
ConvAnalysisSummary (the parent object)

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID used to track the LLM-generated response for feedback purposes.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. A specific word used in conjunction with Category to filter topics. For example,
```
  Product:Salesforce, where the keyword is Salesforce.

```
**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The number of call insights associated with the topic.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
Required. A numerical value used to sort topics in a sequence.

**Type**
textarea

**Properties**
Create, Update

**Description**
Required. A detailed explanation of the topic.


-----

```
Title
TopicSentiment
TotalCalls
TotalCallsForCategoryKeyword
TotalMentionsForCategoryKeyword
TurnIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The title of the topic that describes it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The sentiment of the topic, whether it’s negative, neutral, or positive.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total number of calls analyzed for the topic.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The total number of calls analyzed for category:keyword. Multiple topics can be under
a single `category:keyword.`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total number of mentions analyzed for `category:keyword.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort


-----

**Description**
UUID that is generated and used to track a group of LLM-generated content.
