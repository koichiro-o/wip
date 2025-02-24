#### ConvAnalysisTopicEntry

Represents a single entry under the ConvAnalysisTopic object. An entry represents a segment of a video or voice call that is associated
with a conversation analysis topic. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), undelete(), update(), upsert()

 Special Access Rules

```
Users need the Sales Signals permission set and the Sales Signals feature must be enabled.

##### Fields

```
BulletGenerationsIdentifier
CallId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The generation ID used to track the LLM-generated response for feedback purposes.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier of the voice or video call that corresponds to the entry.

This field is a polymorphic relationship field.

**Relationship Name**
Call

**Refers To**
VideoCall, VoiceCall


-----

```
ConvAnalysisTopicId
SnippetStartTime
Summary
