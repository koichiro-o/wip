#### ServiceTerritoryDataTranslation

Represents the translated values of the data stored within a ServiceTerritory record’s fields. This object is available in API version 54.0
and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.


-----

**•** Translation Workbench and data translation must be enabled in your org.

**•** To view this object, you must have the “View Setup and Configuration” permission

##### Fields

```
Description
IsOutOfDate
Language
Name
ParentId

```

**Type**
textarea

**Properties**
Create, Nillable,Update

**Description**
The translated value for the ServiceTerritory description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date (true) or current (false). A translation
is out-of-date if the parent ServiceTerritory record is updated after the last translation was
filed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language for these translated values.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The translated value for the ServiceTerritory record name. This field is required to translate
the text in other fields.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID of the ServiceTerritory associated with the data that is being translated.


-----

##### Usage

Use this object to translate the data stored in a ServiceTerritory record into the different languages supported by Salesforce. If data
translation is enabled for custom fields on the ServiceTerritory object, additional ServiceTerritoryDataTranslation fields exist for translating
the data contained within those fields.

You can’t use a custom external id field in an upsert call for a ServiceTerritoryDataTranslation object.
