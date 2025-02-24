#### FileSearchActivity

```

**Description**
Specifies if primary members only are included in work capacity availability calculations. If
the value is `false` both primary and secondary members of the service territory are
included. Available in API version 59.0 and later.

The default value is `false.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the field service org settings.

The format for the values is a two-letter language code in small letters, for example, `fr` for
French. If the language has regional dialects, add the two-letter country code in capital
letters, for example, use `fr_BE` for Belgian French.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the field service org settings.


Represents search activity on a file. This object is available in API version 38.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
AvgNumResults

```

**Type**
double

**Properties**
Filter, Sort


-----

```
ClickRank
CountQueries
CountUsers
Name
Period

```

**Description**
The number of search results returned for the search term. If Period is also included, this
value is aggregated based on the time period specified.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The order that the file appeared in the search results when users clicked it from the list of
results.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of searches for the period (day, month, or year).

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of individual users who clicked the file.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of search activity.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The time period that the search count is applied to. For example, a record where the Count
is 70 and the Period is Monthly indicates that 70 searches took place over the past month.
Totals are aggregated daily for the current month, monthly from the past full month through
the past full year, and yearly beyond that.


-----

```
QueryDate
QueryLanguage
SearchTerm
