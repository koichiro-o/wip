#### RecordActionHistory

Represents the lifecycle of a RecordAction as it goes through different states. Available in API version 44.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

This object is always read-only.

##### Fields

```
ActionDefinitionApiName
ActionDefinitionLabel
ActionType
IsMandatory

```

**Type**
string

**Description**
Required. The API name of the action associated with the record. To distinguish a quick action
from a flow with the same API name, we prepend "QuickAction" to the API name of every
quick action.

**Type**
string

**Description**
Required. The label of the action that took place.

**Type**
picklist

**Properties**
Defaulted on create, Restricted picklist

**Description**
Required. The type of action associated with the record. Possible values are:

**•** `Flow` (default)

**•** `QuickAction`

**Type**
boolean


-----

```
LoggedTime
ParentRecordId
Pinned

```

**Properties**
Defaulted on create

**Description**
Optional. Specifies whether the action is mandatory. The default value is false.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Required. The timestamp when the state change occurred.

**Type**
reference

**Properties**
Filter, Sort

**Description**
Required. The parent record for the associated action.

This is a relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssetRelationship, AssociatedLocation, Case, ChangeRequest,
CollaborationGroup, Contact, ContactRequest, Contract, EnhancedLetterhead, Incident, Lead,
Location, OperatingHours, Opportunity, Order, Pricebook2, PricebookEntry, Problem, Product2,
ProductItem, ProductItemTransaction, ProductRequest, ProductRequestLineItem,
ProductRequired, ProductTransfer, RebateMemberAggregateItem, ResourceAbsence,
Scorecard, ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, Shipment, SkillRequirement, SocialPersona, SocialPost, TimeSlot,
User, Visit, VoiceCall, WorkType

ChangeRequest, Incident, Problem are available in API version 53.0 and later.

RebateMemberAggregateItem is available in API version 54.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Nillable, Restricted picklist

**Description**
Optional. Specifies whether the action is pinned to the top or bottom, or unpinned. Possible
values are:


-----

```
RecordActionId
State
UserId

##### Usage

```


**•** None

**•** Top

**•** Bottom

**Type**
string

**Properties**
Filter, Sort

**Description**
Required. The ID of the RecordAction.

**Type**
picklist

**Properties**
Defaulted on create, Restricted picklist

**Description**
Required. The state of the action. A state change triggers the logging of a history event.
Possible values are:

**•** `Started` (default)

**•** `Paused`

**•** `Resumed`

**•** `Completed`

**•** `Unlinked—The action was unlinked because the flow was paused and the current`
record for the flow interview changed.

**Type**
reference

**Description**
Required. The user that conducted the action.

This is a polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


The RecordActionHistory object represents the lifecycle of an action on a record as it goes through different states.


-----

The RecordActionHistory object is a big object. For this reason, when you use synchronous SOQL, SOAP, REST, Bulk, or Apex APIs to read
this object, queries must follow a specific pattern or they fail. Queries must match one of these patterns and use fields in this precise
order when more than one field is used.

**•** ParentRecordId

**•** ParentRecordId, LoggedTime (DESC)

**•** ParentRecordId, LoggedTime (DESC), RecordActionId

For example, this SOQL query follows the ParentRecordId, LoggedTime (DESC) pattern.
```
SELECT ActionDefinitionApiName, User, State FROM RecordActionHistory WHERE
      ParentRecordId = {CaseId} ORDER BY ParentRecordId, LoggedTime DESC

```
Asynchronous SOQL queries do not need to follow a pattern, and can query any field.

Apex triggers cannot reference big object records. Use SOQL queries if you want to query RecordActionHistory records in Apex.

[For more information about the Actions & Recommendations component and how it works with RecordActions, see the Lightning Flow](https://developer.salesforce.com/docs/atlas.en-us.254.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)
[for Service Developer Guide. Learn more about big objects and how to query them in the Query Big Objects module on Trailhead.](https://developer.salesforce.com/docs/atlas.en-us.254.0.salesforce_guided_engagement.meta/salesforce_guided_engagement/salesforce_guided_engagement.htm)

##### Java Example

Here’s a Java example of how to query a RecordActionHistory object.
```
public void queryHBPOs(String parentRecordId) {
  try {
   SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd");
     // query for the RecordActionHistory associated with ParentRecord
     QueryResult queryResults = connection.query("SELECT ActionDefinitionApiName,
LoggedTime, State " +
      "FROM RecordActionHistory WHERE ParentRecordId = '" + parentRecordId + "' LIMIT
50");
     if (queryResults.getSize() > 0) {
      for (int i=0;i<queryResults.getRecords().length;i++) {
       // cast the SObject to a strongly-typed RecordActionHistory
       RecordActionHistory raa = (RecordActionHistory)queryResults.getRecords()[i];
      System.out.println("ActionDefinitionApiName: " + raa.getActionDefinitionApiName()
 + " - LoggedTime: "+ format.format(raa.getLoggedTime().getTime()) + " - State: " +
         raa.getState());
      }
     }
  } catch (Exception e) {
     e.printStackTrace();
  }
  }
