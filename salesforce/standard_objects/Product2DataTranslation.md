#### Product2DataTranslation

Represents the translated values of the data stored within a Product2 record’s fields. This object is available in API version 45.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** Translation Workbench and data translation must be enabled in your org.

**•** To view this object, you must have the “View Setup and Configuration” permission

##### Fields

```
Description
IsOutOfDate
Language
Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The translated value for the Product2 description.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the translation is out-of-date (true) or current (false). A translation
is out-of-date if the parent Product2 record is updated after the last translation was filed.

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
The translated value for the Product2 record name. This field is required to translate the text
in other fields.


-----

```
ParentId

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record ID of the Product2 associated with the data that is being translated.


Use this object to translate the data stored in a Product2 record into the different languages supported by Salesforce. If data translation
is enabled for custom fields on the Product2 object, additional Product2DataTranslation fields exist for translating the data contained
within those fields.

You can’t use a custom external id field in an upsert call for a Product2DataTranslation object.
