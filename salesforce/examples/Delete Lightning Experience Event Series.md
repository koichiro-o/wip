### Delete Lightning Experience Event Series

```
Use the HTTP DELETE method to remove one or more IsRecurrence2 events in a series. You can remove a single event, all events following
and including a specific event, or an entire event series.

#### Delete a Single Event in a Series

Use the sObject Rows on page 149 resource to delete event records. To delete a single occurrence in a series, specify the event ID and
use the DELETE method on page 47 of the resource to delete a record.

#### Delete Multiple Events or All Events from a Series

To delete all events in a series from a specific occurrence and onwards, specify the event ID and use the DELETE method of the resource
to delete a record. When calling this method, IsRecurrence2 must be true and IsRecurrence2Exclusion must be false.

To delete an entire event series, specify the event ID of the first occurrence in the series and use the DELETE method of the resource to
delete a record.

**Example for deleting multiple events or all events from a series**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Event/00Uxx0000000000/fromThisEventOnwards
   -H "Authorization: Bearer token" -X DELETE

```
**Example request body**
```
  None needed

```
**Example response body after successfully deleting events**


-----

#### Considerations

Deleting from an event onwards doesn’t support calls from events that:

**•** Occurred before the original value of Recurrence2PatternStartDate.

**•** Are defined as child events.

If the event series originated outside of Salesforce and the event ID of the first occurrence is unavailable, you can’t delete all events in a
series. Instead, delete events from a specific occurrence onwards.
